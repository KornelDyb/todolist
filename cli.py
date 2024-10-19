from functions import get_todos,write_todos
import time   

now = time.strftime("%b %d, %Y %H:%M:%S") 

print("It is", now)

while True:
    user_action = input("Type add, show, complete edit or exit: ").strip()
    if user_action.startswith("add"):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo+ "\n")

        write_todos(todos)
        
    elif user_action.startswith("show"):

        todos = get_todos()
    
        for index, item in enumerate(todos):
            item = item.strip("\n")
            print(f"{index + 1}-{item}")
    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()
                
            todos[number] = input("Enter new todo: ") + "\n"

            write_todos(todos)

        except ValueError:
            print("this command is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])
            
            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)

            write_todos(todos)
            
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("there is no item with that number")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("this command is not valid")
        

print("bye!")

    