from todo.models import TodoList
from todo.storage import Storage
from todo.cli import setup_cli

def main():
    todo_list = TodoList()
    storage = Storage()
    
    # Load existing tasks from storage
    storage.load_tasks(todo_list)
    
    # Run the CLI
    setup_cli(todo_list, storage)

if __name__ == "__main__":
    main()
