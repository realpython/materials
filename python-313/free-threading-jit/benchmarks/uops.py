import dis

import _opcode
from pyinfo import print_details


def reveal_code(function):
    if uops := "\n".join(_get_micro_ops(function)):
        print(uops)
    else:
        print("Micro-ops unavailable")


def _get_micro_ops(function):
    for executor in _get_executors(function):
        for uop, *_ in executor:
            yield uop


def _get_executors(function):
    bytecode = function.__code__._co_code_adaptive
    for offset in range(0, len(bytecode), 2):
        if dis.opname[bytecode[offset]] == "ENTER_EXECUTOR":
            try:
                yield _opcode.get_executor(function.__code__, offset)
            except ValueError:
                pass


print_details()
