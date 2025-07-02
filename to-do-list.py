def to_do_list(added_task,):
    while True:
        try:
            num=int(input("""Enter the serial number of the task you want to perform:
                1.Add Task
                2.View Task
                3.Delete a Task by its number 
                4.exit the app
                """))
            if num not in[1,2,3,4]:
                raise ValueError
        except ValueError:
            print("Enter only serial number of the task you want to perform i.e from 1-4")
            continue
        if num ==1:
            print("You can add your task here:")
            new_task=input()
            added_task.append(new_task)
            print("Task added successfully")
        elif num ==2:
            if added_task==[]:
                print("No task added please enter a task")
            else:
                print("Your tasks:-")
                for i,task in enumerate(added_task,1):
                    print(f'{i}.{task}')            
        elif num==3: 
            if added_task==[]:
                print("No task to delete")
            else:
                print('Your tasks:-')
                for i,task in enumerate(added_task,1):
                    print(f'{i}.{task}')
                try:
                    delete= int(input(" Which task do you want to delete.Enter the serial number of it:"))
                    n=added_task.pop(delete-1)
                    print("Task deleated successfully")
                    print(f'''You have these task after deleting task {n}:- ''')
                                     
                    for i,task in enumerate(added_task,1):
                        print( f'''{i}.{task}''') 
                except ValueError:
                    print("enter only number")
                except IndexError:
                    print("cannot delete Numbe does not exist")
                    
        elif num==4:
            break          
    return "exited succesfully" 
added_task=[]
final=to_do_list(added_task)
print(final)


