'''Thread-safe version of Tkinter.

Usage:

    import mtTkinter as Tkinter
    # Use "Tkinter." as usual.

or

    from mtTkinter import *
    # Use Tkinter module definitions as usual.

This module modifies the original Tkinter module in memory, making all
functionality thread-safe. It does this by wrapping the Tk class' tk
instance with an object that diverts calls through an event queue when
the call is issued from a thread other than the thread in which the Tk
instance was created. The events are processed in the creation thread
via an 'after' event.

The modified Tk class accepts two additional keyword parameters on its
__init__ method:
    mtDebug:
        0 = No debug output (default)
        1 = Minimal debug output
        ...
        9 = Full debug output
    mtCheckPeriod:
        Amount of time in milliseconds (default 100) between checks for
        out-of-thread events when things are otherwise idle. Decreasing
        this value can improve GUI responsiveness, but at the expense of
        consuming more CPU cycles.

Note that, because it modifies the original Tkinter module (in memory),
other modules that use Tkinter (e.g., Pmw) reap the benefits automagically
as long as mtTkinter is imported at some point before extra threads are
created.

Author: Allen B. Taylor, a.b.taylor@gmail.com
'''

from Tkinter import *
import threading
import Queue

class _Tk(object):
    """
    Wrapper for underlying member tk of class Tk.
    Diverts out-of-thread calls to the 'call' method through the event queue.
    Forwards all other method calls to the underlying tk object.
    """

    def __init__(self, tk, mtDebug = 0, mtCheckPeriod = 10):
        self._tk = tk

        # Create the incoming event queue.
        self._eventQueue = Queue.Queue(1)

        # Identify the thread from which this object is being created so we can
        # tell later whether an event is coming from another thread.
        self._creationThread = threading.currentThread()

        # Store remaining values.
        self._debug = mtDebug
        self._checkPeriod = mtCheckPeriod

    def __getattr__(self, name):
        # Divert missing member accesses to the underlying tk object.
        return getattr(self._tk, name)

    def call(self, *args, **kwargs):
        "Thread-safe call method."

        # Check if we're in the creation thread.
        if threading.currentThread() == self._creationThread:
            # We're in the creation thread; just call the event directly.
            if self._debug >= 8 or args[0] != 'after' and self._debug >= 2:
                print 'Calling event directly:', args, kwargs
            return self._tk.call(*args, **kwargs)
        else:
            # We're in a different thread than the creation thread; enqueue
            # the event, and then wait for the response.
            responseQueue = Queue.Queue(1)
            if self._debug >= 1:
                print 'Marshalling event:', args, kwargs
            self._eventQueue.put((args, kwargs, responseQueue))
            isException, response = responseQueue.get()

            # Handle the response, whether it's a normal return value or
            # an exception.
            if isException:
                exType, exValue, exTb = response
                raise exType, exValue, exTb
            else:
                return response

# Define a hook for class Tk's __init__ method.
def _Tk__init__(self, *args, **kwargs):
    # We support some new keyword arguments that the original __init__ method
    # doesn't expect, so separate those out before doing anything else.
    new_kwnames = ('mtCheckPeriod', 'mtDebug')
    new_kwargs = {}
    for name, value in kwargs.items():
        if name in new_kwnames:
            new_kwargs[name] = value
            del kwargs[name]

    # Call the original __init__ method, creating the internal tk member.
    self.__original__init__(*args, **kwargs)

    # Replace the internal tk member with a wrapper that handles calls from
    # other threads.
    self.tk = _Tk(self.tk, **new_kwargs)

    # Set up the first event to check for out-of-thread events.
    self.after_idle(_CheckEvents, self)

# Replace Tk's original __init__ with the hook.
Tk.__original__init__ = Tk.__init__
Tk.__init__ = _Tk__init__

def _CheckEvents(tk):
    "Event checker event."

    used = False
    try:
        # Process all enqueued events, then exit.
        while True:
            try:
                # Get an event request from the queue.
                args, kwargs, responseQueue = tk.tk._eventQueue.get_nowait()
            except:
                # No more events to process.
                break
            else:
                # Call the event with the given arguments, and then return
                # the result back to the caller via the response queue.
                used = True
                if tk.tk._debug >= 2:
                    print 'Calling event from main thread:', args, kwargs
                try:
                    responseQueue.put((False, tk.tk.call(*args, **kwargs)))
                except SystemExit, ex:
                    raise SystemExit, ex
                except Exception, ex:
                    # Calling the event caused an exception; return the
                    # exception back to the caller so that it can be raised
                    # in the caller's thread.
                    from sys import exc_info
                    exType, exValue, exTb = exc_info()
                    responseQueue.put((True, (exType, exValue, exTb)))
    finally:
        # Schedule to check again. If we just processed an event, check
        # immediately; if we didn't, check later.
        if used:
            tk.after_idle(_CheckEvents, tk)
        else:
            tk.after(tk.tk._checkPeriod, _CheckEvents, tk)

# Test thread entry point.
def _testThread():
    text = "This is Tcl/Tk version %s" % TclVersion
    if TclVersion >= 8.1:
        try:
            text = text + unicode("\nThis should be a cedilla: \347",
                                  "iso-8859-1")
        except NameError:
            pass # no unicode support
    label = Label(root, text=text)
    label.pack()
    test = Button(root, text="Click me!",
              command=lambda root=root: root.test.configure(
                  text="[%s]" % root.test['text']))
    test.pack()
    root.test = test
    quit = Button(root, text="QUIT", command=root.destroy)
    quit.pack()
    # The following three commands are needed so the window pops
    # up on top on Windows...
    root.iconify()
    root.update()
    root.deiconify()

# Test. Mostly borrowed from the Tkinter module, but the important bits moved
# into a separate thread.
if __name__ == '__main__':
    import threading
    root = Tk(mtDebug = 1)
    thread = threading.Thread(target = _testThread)
    thread.start()
    root.mainloop()
    thread.join()