# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 14:09:10 2020

@author: JEMIMA
"""

def responseYes():
    global time_task_continue, time_minute_continue
    global time_hour_continue, hour_used_before_break, minute_used_before_break
    tell_time()
    now_continue = datetime.datetime.now()
    date_task_continue = now_continue.strftime('%Y-%m-%d')
    time_task_continue = current_time
    time_hour_continue = int(time.strftime("%I", time_n))
    time_minute_continue = int(time.strftime("%M", time_n))
    print(f"You are continuing at {date_task_continue} on {time_task_continue}")
    print("Type Done if you are Done with the task completely or Break if you want to go on a break.")
def whenDone():
    global time_task_continue, time_minute_continue, money_to_be_paid, date_task_completed
    global time_hour_continue, hour_used_before_break, minute_used_before_break, time_task_completed
    tell_time()
    if response.strip().capitalize() == "Done":
        now_done_break = datetime.datetime.now()
        date_task_completed = now_done_break.strftime('%Y-%m-%d')
        time_task_completed = current_time
        time_hour_done = int(time.strftime("%I", time_n))
        time_minute_done = int(time.strftime("%M", time_n))
        print(f"You completed the task {task} on {date_task_completed} at {time_task_completed}")
        hour_used_after_break = abs(time_hour_done - time_hour_continue)
        minute_used_after_break = abs(time_minute_done - time_minute_continue)
        total_hours_used_for_task = abs(hour_used_before_break + hour_used_after_break)
        total_minutes_used_for_task = abs(minute_used_before_break + minute_used_after_break)
        total_time_spent_on_task = (total_minutes_used_for_task / 60) + total_hours_used_for_task
        money_to_be_paid = 5 * total_time_spent_on_task
        print(f"You are to be paid $%.2f" %money_to_be_paid)
def taskInput():
    #Function to take the name of the task and if the user is ready to start the task
    global task, date_task_started, date_task_completed, time_task_started, response
    task = input("Type the description(name) of the task you want to track: ").strip()
    print("Ready to get started with the task? Yes or No?")
    response = input("Answer: ")
    if response.strip().capitalize() == "Yes":
        responseYes_1()
    while response.strip().capitalize() == "No":
        noResponse()
def completed_Task():
    print("Type Break if you want to go on a break or Done when you are completely done with the task.")
    global date_task_completed, time_task_completed, response
    response = input("Your response: ")
    if response.strip().capitalize() == "Done":
        done()
    elif response.capitalize().strip() == "Break":
        breakTask()
        csvCreation()