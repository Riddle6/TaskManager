
def getTask():

    myDict = {} # Empty dictionary.
    
    myTasks = [] # Empty list.

    mySteps = []

    while True:
        print("\n--- Task Menu ---")
        print("1. Add a Task")
        print("2. Add a Step to a Task")
        print("3. Mark a Step as Completed")
        print("4. View all Tasks")
        print("5. Remove a Task")
        print("6. Display Total Number of Tasks")
        print("7. Quit")

        try:
            option = int(input("\nChoose an Option (1-7): "))

            if option <= 0 or option > 7:
                print("\nThis option does not exist! Please enter a valid option; 1: add a Task - 7: to Quit.")


        except ValueError:
            print("\nThis is not a valid option! Please try again.")
            option = int(input("\nChoose an Option (1-7): ")) 
            # Asking once more, otherwise if the user inputs another letter twice in a row, the program 
            # crashes. I am unable to handle this exception error. But it's very unlikely to happen.
            


        if option == 1:

            while True:

                task = input("Enter the Task Name: ")

                check_task = task != '' and all(c.isalpha() or c.isspace() for c in task)
                # This advanced Python code checks to see if the task is in the alphabet or has a space,
                # which will return True. Otherwise it returns False.
                '''
                For futher elaboration:
                The all() method checks to see if "all" of the other conditions return True. In which
                isalpha() checks if the string is in the alphabet and/or the isspace() checks for a
                whitespace character in a string. "for c in task" finally checks if these conditions are
                True within the "task", and then the code moves on to the if-else statement below.
                '''
                    
                if check_task == True: # If the task has no numbers or symbols.
                    print("\nTask successfully added to your list!")
                    myTasks.append(task)
                    break

                elif check_task == False: # If the user inputted symbols or numbers.
                    print("\nYour task cannot be a number or symbol! Please try again.\n")


        if option == 2: # Option 2

            if len(myTasks) == 0: # If the list is empty, then there's no tasks.
                print("\nError! There are no tasks to add a step to!")
                continue

            check_step = input("Enter the Task Name you want to add a step to: ")
            
            if task in check_step: # If the task input matches the task name prompted by the step.
                step = input("Enter the step description: ")
                mySteps.append(step)
                
                #print("\nStep", mySteps, "successfully added to:", myTasks)
            else:
                print("This Task does not exist on your list! Please try again.")
                continue


        if option == 5:

            if len(myTasks) != 0:
                input("\nWhich task would you like to remove? ") # Work in Progress

            else:
                print("\nError! There are no tasks to remove!")
                continue
        
        if option == 6:
            print(f"\nYou have {len(myTasks)} tasks remaining.")


        if option == 7:
            print("\nThank you for using Task Manager!\n")
            break


getTask()