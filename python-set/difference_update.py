todo_list = {
    "Implement user login",
    "Fix bug #123",
    "Improve performance",
    "Write unit tests",
}
completed_tasks = {"Fix bug #123", "Improve performance"}
todo_list.difference_update(completed_tasks)
todo_list
