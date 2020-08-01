#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  1 01:57:35 2020

@author: Joseph Segbefia
"""

def responseYes_1(): # Function to start keeping track of the time user started work 
    global time_task_started, time_task_completed, time_hour_completed, time_task_completed, date_task_started
    global time_minute_completed, time_minute_started, time_hour_started, money_to_be_paid, date_task_completed
    now_start = datetime.datetime.now()
    date_task_started = now_start.strftime('%Y-%m-%d')
    tell_time()
    time_task_started = current_time
    time_hour_started = int(time.strftime("%I", time_n))
    time_minute_started = int(time.strftime("%M", time_n))
    print(f"You are beginning this task on {date_task_started} at {current_time}")
    completed_Task()
    
def noResponse(): #Function which describes what happens when user is not ready to start the project
    global time_task_started, time_task_completed, time_hour_completed, time_task_completed, date_task_started, response
    global time_minute_completed, time_minute_started, time_hour_started, money_to_be_paid, date_task_completed
    print("Come back when you are ready to start the task")
    print("Ready to get started with the task? Yes or No?")
    response = input("Answer: ")
    if response.strip().capitalize() == "Yes":
        now_start = datetime.datetime.now()
        date_task_started = now_start.strftime('%Y-%m-%d')
        tell_time()
        time_task_started = current_time
        time_hour_started = int(time.strftime("%I", time_n))
        time_minute_started = int(time.strftime("%M", time_n))
        print(f"You are beginning your task named {task} on {date_task_started} at {current_time}")
        completed_Task()
        
def invalidInput(): #Function to take care of invalid input from the user
    global time_task_started, time_task_completed, time_hour_completed, time_task_completed, date_task_started, response
    global time_minute_completed, time_minute_started, time_hour_started, money_to_be_paid, date_task_completed
    print("Invalid Input.")
    print("Make sure to type Yes or No to be validated")
    response = input("Answer: ")
    if response.strip().capitalize() == "Yes":
        responseYes_1()
    if response.strip().capitalize() == "No":
        noResponse()
        
def done(): #Function that returns a summary of the project with the payment due 
    global time_task_started, time_task_completed, time_hour_completed, time_task_completed, date_task_started, response
    global time_minute_completed, time_minute_started, time_hour_started, money_to_be_paid, date_task_completed
    now_done = datetime.datetime.now()
    global date_time_task_completed
    date_task_completed = now_done.strftime('%Y-%m-%d')
    tell_time()
    time_task_completed = current_time
    global time_hour_completed, time_minute_completed
    time_hour_completed = int(time.strftime("%I", time_n))
    time_minute_completed = int(time.strftime("%M", time_n))
    print(f"You completed the task on {date_task_completed} at {current_time}")
    time_task_lasted_calculator()
    csvCreation()
    
def responseYes(): # Function to take care of a user resuming after taking a break from the project
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
    
    
      
  
  
