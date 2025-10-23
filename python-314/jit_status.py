try:
    from sys import _jit
except ImportError:
    print("Module sys._jit unavailable")
else:
    print("Python compiled with JIT support:", _jit.is_available())
    print("JIT enabled for this process:", _jit.is_enabled())
    print("JIT currently running:", _jit.is_active())
