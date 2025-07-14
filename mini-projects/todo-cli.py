import os

file_path = "mini-projects/todo.txt"

todoList = []


while True:
    todo = input("What do you need to get done? (q to exit)")

    if todo.lower() == 'q':
        break
    else:
        todoList.append(todo)
        print("Item added to list")


with open(file_path, "a") as file:
    file.write('\n'.join(todoList))