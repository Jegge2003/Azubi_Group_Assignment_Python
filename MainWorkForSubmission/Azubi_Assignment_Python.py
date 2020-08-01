#This file is a combined work by:
 #Jemima Denteh
 #Joseph Segbefia
 #James Owusu-Appiah
#The individual codes that were written were compiled to make this a success.
#PYG - 19

import datetime
import time
import csv
time_task_started = '11:00'
time_task_completed = '12:00'
current_time = '10:00'
date_task_started = date_task_completed  =  '2020-07-04'
time_n = (2020, 7, 30, 23, 30, 4, 3, 212, 0)
time_hour_started = time_minute_started = time_hour_completed = time_minute_completed = 0
time_task_continue = time_hour_continue = time_minute_continue = hour_used_before_break = 0
minute_used_after_break = minute_used_before_break = money_to_be_paid = 0
task = "Waiting"
response = "Yes"

def taskInput():
    #Function to take the name of the task and if the user is ready to start the task
    #If the input is Yes, the responseYes_1 function is called
    #If the input is No, the noResponseFunctino is called
    global task, date_task_started, date_task_completed, time_task_started
    global response
    task = input("Type the description(name) of the task you want to track: ").strip()
    print("Ready to get started with the task? Yes or No?")
    response = input("Answer: ")
    if response.strip().capitalize() == "Yes":
        responseYes_1()
    while response.strip().capitalize() == "No":
        noResponse()

def completed_Task():
    #Function to be called when the user is done or wants to go on a break
    #If the input is done then the done function is called
    #Else if the input is break the breakfunction is called
    print("Type Break if you want to go on a break or Done when you are completely done with the task.")
    global date_task_completed, time_task_completed
    global response
    response = input("Your response: ")
    if response.strip().capitalize() == "Done":
        done()
        csvCreation()
    elif response.capitalize().strip() == "Break":
        breakTask()
        csvCreation()

def time_task_lasted_calculator():
    #Function to calculate the money to be paid
    #It works by using the absolute value of the difference of the hour and minute started and the hour and minute completed
    #It converts the minutes to hours and add it to the hours
    #It then multiples the sum by $5
    global time_task_started, time_task_completed, time_hour_completed, time_task_completed
    global time_minute_completed, time_minute_started, time_hour_started, money_to_be_paid, date_task_completed
    now_done = datetime.datetime.now()
    time_task_completed = now_done.strftime('%H:%M')
    tell_time()
    total_hours_for_task = abs(time_hour_completed - time_hour_started)
    total_minutes_for_task = abs(time_minute_completed - time_minute_started)
    total_time_spent_on_task = (total_minutes_for_task/60) + total_hours_for_task
    money_to_be_paid = 5*total_time_spent_on_task
    print(f"Hours taken for completion of the task was {total_hours_for_task}")
    print(f"Minutes taken for completion of the task was {total_minutes_for_task}")
    print("Based on the total time you spent on the task, your pay is $%.2f" %money_to_be_paid)

def tell_time():
    #This function tells the current time in hours and minutes
    #It also gives the hours and minutes separately
    global current_time, time_n
    time_n = time.gmtime()
    current_time = time.strftime("%H:%M %p", time_n)  # %I= prints the hour, %M= gives the minutes, %P= prints AM or PM
    time_hour = int(time.strftime("%H", time_n))
    time_minute = int(time.strftime("%M", time_n))

def breakTask():
    #Function to be called if the user inputs break or wants to go on a break
    global time_hour_started, time_minute_started, task
    global time_task_continue, time_minute_continue, time_hour_continue
    global hour_used_before_break, minute_used_before_break
    tell_time()
    breakFunction()

def breakFunction():
    #Function to be called when break is type
    #It shows the time the user is going on the break
    #It also shows the time the user spent before going on a break
    #Afterwards it shows if the user is ready to undergo the task
    #If  the response is Yes, it calls the responseYes function and whenDone function
    #If the response is No, it tells the user to come back when ready
    global time_task_continue, time_minute_continue, time_task_completed, response, time_hour_started, time_minute_started
    global time_hour_continue, hour_used_before_break, minute_used_before_break, time_task_started
    global response
    now_break = datetime.datetime.now()
    tell_time()
    while response.capitalize().strip() == "Break":
        break_date = now_break.strftime('%Y-%m-%d')
        break_time = current_time
        time_hour_break = int(time.strftime("%H", time_n))
        time_minute_break = int(time.strftime("%M", time_n))
        print(f"You are going on a break from your ongoing task on {break_date} at {break_time}")
        hour_used_before_break = abs(time_hour_break - time_hour_started)
        minute_used_before_break = abs(time_minute_break - time_minute_started)
        print(
            f"You worked on the project for {hour_used_before_break} hours, {minute_used_before_break} minute before going on a break at {break_time}")
        print("Are you ready to continue with your uncompleted task? Yes? or No?")
        response = input("Your response: ")
        if response.capitalize().strip() == "Yes":
            responseYes()
            response = input("Your response: ")
            whenDone()
        while response.strip().capitalize() == "No":
            print("Come back another time when you are ready to finish your uncompleted task.")
            print("Ready to continue the uncompleted task? Yes or No?")
            response = input("Your response: ")
            if response.capitalize().strip() == "Yes":
                responseYes()
                response = input("Your response: ")
                whenDone()

def responseYes():
    #This function is shows the time the user will continue the task
    #It generates the continue time and also prints out a message for the user
    #The user types done if done and break if wants to go on a break
    global time_task_continue, time_minute_continue
    global time_hour_continue, hour_used_before_break, minute_used_before_break
    tell_time()
    now_continue = datetime.datetime.now()
    date_task_continue = now_continue.strftime('%Y-%m-%d')
    time_task_continue = current_time
    time_hour_continue = int(time.strftime("%H", time_n))
    time_minute_continue = int(time.strftime("%M", time_n))
    print(f"You are continuing at {date_task_continue} on {time_task_continue}")
    print("Type Done if you are Done with the task completely or Break if you want to go on a break.")

def whenDone():
    #This function gets called when the user types done
    #It shows the time completed and the date completed too
    #It shows the money in dollars that the user deserves
    global time_task_continue, time_minute_continue, money_to_be_paid, date_task_completed
    global time_hour_continue, hour_used_before_break, minute_used_before_break, time_task_completed
    tell_time()
    if response.strip().capitalize() == "Done":
        now_done_break = datetime.datetime.now()
        date_task_completed = now_done_break.strftime('%Y-%m-%d')
        time_task_completed = current_time
        time_hour_done = int(time.strftime("%H", time_n))
        time_minute_done = int(time.strftime("%M", time_n))
        print(f"You completed the task {task} on {date_task_completed} at {time_task_completed}")
        hour_used_after_break = abs(time_hour_done - time_hour_continue)
        minute_used_after_break = abs(time_minute_done - time_minute_continue)
        total_hours_used_for_task = abs(hour_used_before_break + hour_used_after_break)
        total_minutes_used_for_task = abs(minute_used_before_break + minute_used_after_break)
        total_time_spent_on_task = (total_minutes_used_for_task / 60) + total_hours_used_for_task
        money_to_be_paid = 5 * total_time_spent_on_task
        print(f"You are to be paid $%.2f" %money_to_be_paid)

def whenBreakAgain():
    #This function is called when the user breaks multiple times
    global time_task_continue, time_minute_continue, time_task_completed, time_task_started, response
    global time_hour_continue, hour_used_before_break, minute_used_before_break, money_to_be_paid
    tell_time()
    breakFunction()

def csvCreation():
    #This is the function for the creation of the csv file that hold the initial record
    #It gives the user the date started, task name, etc
    global task, time_task_started, date_task_started, date_task_completed, time_task_completed, money_to_be_paid
    with open('time_tracking_details.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["task", "date_started", "time_started", "date_completed", "time_completed", "amount_to_be_paid_dollars"])
        writer.writerow([task, date_task_started, time_task_started,
                         date_task_completed, time_task_completed, ('%.2f' %money_to_be_paid)])
    file.close()

def responseYes_1():
    #This function is called when you type yes to the first statement that appears
    #It gives the time you started the task and the corresponding day
    global time_task_started, time_task_completed, time_hour_completed, time_task_completed, date_task_started
    global time_minute_completed, time_minute_started, time_hour_started, money_to_be_paid, date_task_completed
    now_start = datetime.datetime.now()
    date_task_started = now_start.strftime('%Y-%m-%d')
    tell_time()
    time_task_started = current_time
    time_hour_started = int(time.strftime("%H", time_n))
    time_minute_started = int(time.strftime("%M", time_n))
    print(f"You are beginning this task on {date_task_started} at {current_time}")
    completed_Task()

def noResponse():
    #This function is called when you type No instead of yes
    #It is called by the while loop when response is No
    global time_task_started, time_task_completed, time_hour_completed, time_task_completed, date_task_started, response
    global time_minute_completed, time_minute_started, time_hour_started, money_to_be_paid, date_task_completed
    global response
    print("Come back when you are ready to start the task")
    print("Ready to get started with the task? Yes or No?")
    response = input("Answer: ")
    if response.strip().capitalize() == "Yes":
        now_start = datetime.datetime.now()
        date_task_started = now_start.strftime('%Y-%m-%d')
        tell_time()
        time_task_started = current_time
        time_hour_started = int(time.strftime("%H", time_n))
        time_minute_started = int(time.strftime("%M", time_n))
        print(f"You are beginning your task named {task} on {date_task_started} at {current_time}")
        completed_Task()

def invalidInput():
    #This function is called when the user inputs a wrong value aside the designated ones
    global time_task_started, time_task_completed, time_hour_completed, time_task_completed, date_task_started, response
    global time_minute_completed, time_minute_started, time_hour_started, money_to_be_paid, date_task_completed
    print("Invalid Input.")
    print("Make sure to type Yes or No to be validated")

    response = input("Answer: ")
    if response.strip().capitalize() == "Yes":
        responseYes_1()
    if response.strip().capitalize() == "No":
        noResponse()

def done():
    #This function calls teh time task lasted calculator and the csvCreation function
    #It is called when the user types done for the first time without going on a break
    global time_task_started, time_task_completed, time_hour_completed, time_task_completed, date_task_started
    global time_minute_completed, time_minute_started, time_hour_started, money_to_be_paid, date_task_completed
    global response
    now_done = datetime.datetime.now()
    global date_time_task_completed
    date_task_completed = now_done.strftime('%Y-%m-%d')
    tell_time()
    time_task_completed = current_time
    global time_hour_completed, time_minute_completed
    time_hour_completed = int(time.strftime("%H", time_n))
    time_minute_completed = int(time.strftime("%M", time_n))
    print(f"You completed the task on {date_task_completed} at {current_time}")
    time_task_lasted_calculator()
    csvCreation()

if __name__ == '__main__': taskInput()
 
 

