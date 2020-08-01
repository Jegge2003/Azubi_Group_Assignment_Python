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
1. taskInput() – This function takes the name of the task entered by the user and the response entered by the user to start the task or not.
2. completed_Task() – This function enables the user to input ‘Break’ to take a break from the task or input ‘Done’ when completely done with the task.
3. time_task_lasted_calculator() – This function picks minutes and hours separately and converts minutes to hours to tell the total number of hours spent on the task.
4. tell_time() – This function tells the total amount of time spent on the task before a break or at the end of the task.
5. breakTask() – This function enables the user to take a break so he/she can resume the task at a later time.
6. breakFunction() – This function ends a current loop to enable the user make another input for execution.
7. responseYes() – Enables the user to enter ‘Yes’ to continue with the task till it’s completed.
8. whenDone() – This function enables the user to see the total time spent on the task and the amount he/she deserves.
9. whenBreakAgain() – Should the user take further breaks, this function keeps records of break time and time of resumption of the project.


Contributors/Team Members
1. James Owusu-Appiah
2. Joseph Segbefia
3. Jemima Denteh

