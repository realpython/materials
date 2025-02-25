from pytest import StashKey, TestReport

STASH_REPORT_KEY = StashKey[TestReport]()
CACHE_TASKS_KEY = "realpython/tasks"
COMMAND_TASK = "--task"
MIN_FAILURES_BEFORE_HINT = 3
TEST_TIMEOUT_SECONDS = 1.5
