# Azubi_Group_Assignment_Python
This is an assignment given by Azubi Graduate Training Program on creating a time tracking program.


Implementation Process
1. Nana inputs his task description for the first time.
2. A message appears saying: ‘Ready to get started your task? Yes or No?’
3. If Nana enters ‘No’, a message appears saying: ‘Come back later when you are ready to start the task’.
4. However if Nana enters ‘Yes’, the system automatically generates his PC’s time and date to start recording the time he will spend on the task.
5. Nana may want to take a break from the task or end the task when he is done. To take a break, he must type ‘Break’. Otherwise, he should type ‘Done’. This way, the program can record the time he spent on the task.
6. If he types ‘Break’, the system automatically generates the date and time of break using his PC’s date and time settings.
7. Two messages will show up. One will ask, ‘Are you ready to continue your uncompleted task? Yes or No?’ The second message shows the number of hours Nana spent on the task before taking a break.
8. If Nana enters ‘No’, he will receive a message telling him to come back when he is ready to complete the unfinished task.
9. Otherwise if ‘Yes’, the system starts recording from the time of resumption of the task till Nana is completely done. 
10. If Nana enters ‘Done’, he receives a message indicating the total time spent on the task and the corresponding amount of money he deserves. 
11. However, if Nana takes no break from the project and ends the task, the system records the time spent on the task and displays a message notifying Nana of the time spent and the corresponding amount of money he deserves.
12. If Nana wants to take multiple breaks, he can repeat the process from No. 6 to No. 10.


Program Dependencies
1. DateTime Module – This module generates the system date and time of the user’s PC so the time spent on the project can be tracked.
2. Time Module – This module tracks and generates the total time spent on the task.
3. CSV Module – This module takes the various inputs made by the user to create the CSV file.


Design Process
1. taskInput() – This function takes the name of the task entered by the user and the response entered by the user to start the task or not.Function to take the name of the task and if the user is ready to start the task. If the input is Yes, the responseYes_1 function is called. If the input is No, the noResponseFunctino is called
2. completed_Task() – This function enables the user to input ‘Break’ to take a break from the task or input ‘Done’ when completely done with the task. Function to be called when the user is done or wants to go on a break. If the input is done then the done function is called. Else if the input is break the breakfunction is called
3. time_task_lasted_calculator() – This function picks minutes and hours separately and converts minutes to hours to tell the total number of hours spent on the task. Function to calculate the money to be paid. It works by using the absolute value of the difference of the hour and minute started and the hour and minute completed. It converts the minutes to hours and add it to the hours. It then multiples the sum by $5
4. tell_time() – This function tells the total amount of time spent on the task before a break or at the end of the task. This function tells the current time in hours and minutes. It also gives the hours and minutes separately
5. breakTask() – This function enables the user to take a break so he/she can resume the task at a later time. Function to be called if the user inputs break or wants to go on a break
6. breakFunction() – This function ends a current loop to enable the user make another input for execution. Function to be called when break is type. It shows the time the user is going on the break. It also shows the time the user spent before going on a break. Afterwards it shows if the user is ready to undergo the task. If  the response is Yes, it calls the responseYes function and whenDone function. If the response is No, it tells the user to come back when ready
7. responseYes() – Enables the user to enter ‘Yes’ to continue with the task till it’s completed. This function is shows the time the user will continue the task. It generates the continue time and also prints out a message for the user. The user types done if done and break if wants to go on a break
8. whenDone() – This function enables the user to see the total time spent on the task and the amount he/she deserves. This function gets called when the user types done. It shows the time completed and the date completed too. It shows the money in dollars that the user deserves
9. whenBreakAgain() – Should the user take further breaks, this function keeps records of break time and time of resumption of the project. This function is called when the user breaks multiple times
10. csvCreation() - This is the function for the creation of the csv file that hold the initial record. It gives the user the date started, task name, etc
11. responseYes_1() - This function is called when you type yes to the first statement that appears. It gives the time you started the task and the corresponding day
12. noResponse() - This function is called when you type No instead of yes. It is called by the while loop when response is No
13. invalidInput() - This function is called when the user inputs a wrong value aside the designated ones
14. done() - This function calls teh time task lasted calculator and the csvCreation function. It is called when the user types done for the first time without going on a break

Contributors/Team Members
1. James Owusu-Appiah
2. Joseph Segbefia
3. Jemima Denteh

