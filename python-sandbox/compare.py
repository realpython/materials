import warnings

from RestrictedPython import compile_restricted

from sandbox import run_untrusted

# RestrictedPython warns about print() calls, which don't matter here.
warnings.filterwarnings("ignore", category=SyntaxWarning)

HOSTILE = (
    "os = [c for c in ().__class__.__base__.__subclasses__()"
    " if c.__name__ == '_wrap_close'][0].__init__.__globals__\n"
    "print(os['listdir']('/home'))\n"
)

print("1. exec() with only print() in builtins:")
exec(HOSTILE, {"__builtins__": {"print": print}})

print("2. RestrictedPython refused to compile:")
try:
    compile_restricted(HOSTILE, "<untrusted>", "exec")
except SyntaxError as error:
    print(error.args[0][0])

print("3. Locked-down container:")
result = run_untrusted(HOSTILE)
exit_code, stdout, stderr = result.values()
if exit_code == 0:
    print(stdout.strip())
else:
    print(f"Sandbox failed ({exit_code}): {stderr}")
