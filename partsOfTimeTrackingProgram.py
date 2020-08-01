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

def time_task_lasted_calculator():
    global time_task_started, time_task_completed, time_hour_completed, time_task_completed
    global time_minute_completed, time_minute_started, time_hour_started, money_to_be_paid, date_task_completed
    now_done = datetime.datetime.now()
    time_task_completed = now_done.strftime('%I:%M')
    tell_time()
    total_hours_for_task = abs(time_hour_completed - time_hour_started)
    total_minutes_for_task = abs(time_minute_completed - time_minute_started)
    total_time_spent_on_task = (total_minutes_for_task/60) + total_hours_for_task
    money_to_be_paid = 5*total_time_spent_on_task
    print(f"Hours taken for completion of the task was {total_hours_for_task}")
    print(f"Minutes taken for completion of the task was {total_minutes_for_task}")
    print("Based on the total time you spent on the task, your pay is $%.2f" %money_to_be_paid)

def breakFunction():
    global time_task_continue, time_minute_continue, time_task_completed, response, time_hour_started, time_minute_started
    global time_hour_continue, hour_used_before_break, minute_used_before_break, time_task_started
    now_break = datetime.datetime.now()
    tell_time()
    while response.capitalize().strip() == "Break":
        break_date = now_break.strftime('%Y-%m-%d')
        break_time = current_time
        time_hour_break = int(time.strftime("%I", time_n))
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

def csvCreation():
    global task, time_task_started, date_task_started, date_task_completed, time_task_completed, money_to_be_paid
    with open('time_tracking_details.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["task", "date_started", "time_started", "date_completed", "time_completed", "amount_to_be_paid_dollars"])
        writer.writerow([task, date_task_started, time_task_started,
                         date_task_completed, time_task_completed, ('%.2f' %money_to_be_paid)])
    file.close()

def breakTask():
    global time_hour_started, time_minute_started, task
    global time_task_continue, time_minute_continue, time_hour_continue
    global hour_used_before_break, minute_used_before_break
    tell_time()
    breakFunction()

def whenBreakAgain():
    global time_task_continue, time_minute_continue, time_task_completed, time_task_started, response
    global time_hour_continue, hour_used_before_break, minute_used_before_break, money_to_be_paid
    tell_time()
    breakFunction()