from functools import reduce
from operator import or_

global_settings = frozendict(theme="light", editor="vim", telemetry=True)
user_settings = frozendict(theme="dark")
project_settings = frozendict(editor="code", telemetry=False)

layers = [global_settings, user_settings, project_settings]
print(reduce(or_, layers, frozendict()))
