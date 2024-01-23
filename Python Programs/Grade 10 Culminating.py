"""
Schedule (Culminating project)
June 1st, 2020
"""

#DEFINITIONS

password, pass_ans, options, description, answer = "password123", "", "\n\t\t\tMenu\na)Read Description\nb)View Schedule\nc)Make New Password\nd)Exit Program", "description", ""

#This description is for the user to understand the program 
description = "\nHello user! This program has been designed as a private schedule. You may choose to add\nyour own events and meetings to this schedule. You will be prompted to enter the time of these in a 24-hour\ncycle, which will then be displayed in an A.M. / P.M. cycle for your convinience. Changing the set password\nis also an option! Once you are finished with your schedule, you are welcome to choose to exit the program."

space = "               " #Makes space between the A.M. and P.M. columns
day_am=[space,space,space,space,space,space,space,space,space,space,space,space] #These two list are empty so that the program can easly replace events 
day_pm=["","","","","","","","","","","",""]

#FUNCTIONS

def display_schedule(space,day_pm,day_am):  #This function displays the schedule with each event at the time it happens.
    print("\nAM                  PM\n")
    for i in range(12):
        if (i+1)<10:
            print("0"+str(i+1)+" : "+day_am[i]+"0"+str(i+1)+" : "+day_pm[i])
        else:
            print((i+1),": "+day_am[i]+str(i+1)+" : "+day_pm[i])

def new_password(answer): #This function prompts for the new password then makes sure it is between 4 to 10 characters. 
    while True:
        new_pc = input("Enter new password (Must be 4 - 10 characters): ")
        if 3<len(new_pc)<11:
            break
        else:
            print ("Invalid Answer")  
    while new_pc!=answer: #This loop re-asks for the new password until it is correct.  
        answer = input("Enter password: ")
        if new_pc!=answer:
            print("Invalid Answer\n")

def valid_ans_option(): #This function asks the user for the option they would like to do, makes sure it is a valid answer. 
    while True: 
        option = input("\nEnter option letter: ")
        option = option.lower()
        if option!="a" and option!="b" and option!="c" and option!="d":
            print("\nInvalid Answer")
        else:
            break
    return option

def valid_ans_event(): #This function asks the user if they would like to add an event, makes sure it is a valid answer. 
    while True:
        new_event = input("\nMake new event? ")
        new_event = new_event.lower()
        if new_event!="yes" and new_event!="no":
            print("Invalid Answer")
        else:
            break
    return (new_event)

def valid_ans_title(): #Asks for title, makes sure it is no more than 10 characters.
    while True:
        title = input("Enter title (no more than 10 characters): ")
        if len(title)>10:
            print ("Invalid Title")
        else:
            space = 15 - len(title)
            for i in range(space):
                title = title + " "
            break
    return (title)

def valid_ans_hour(): #Asks for hour, makes sure it is in a 24-hour cycle.
    while True:
        hour = input("Enter hour (out of 24 hour cycle): ")
        try:
            hour = int(hour)
            if 0<hour<25:
                break
            else:
                print("Invalid Answer")
        except ValueError:
            print("Invalid Answer")
    return (hour)

#ENTER PASSCODE

print("\n\t\t\tLog In\n") #Adds title 

while pass_ans!=password: #Has the user input the set password "password123", they can change this later
    pass_ans = input("Enter password: ")
    if pass_ans!=password:
        print("Invalid Answer\n") 

#MENU
        
while True:    
     while True:
        print (options) #Prints the option 
        option = valid_ans_option() #Gets the valid answer for the option
        if option == "a": #Option A
            print (description) #Prints the description already defined 
            break
        elif option == "b": #Option B
            while True:
                print("\n\t\t\tPlanner\n") #Prints a title at the center of the screen
                display_schedule(space,day_pm,day_am) #Displays the schedule
                if valid_ans_event()=="yes":
                    title = valid_ans_title() #Gets title
                    hour = valid_ans_hour() #Gets hour
                    if hour>12: #If hour is from 12 to 24..
                        hour = hour - 12  #Subtracts 12 in order to add to P.M cycle
                        day_pm.pop(hour-1) #These commands replace the empty space with the new event
                        day_pm.insert((hour-1),title) 
                    else:
                        day_am.pop(hour-1) #If not, adds to A.M. cycle
                        day_am.insert((hour-1),title)
                else:
                    break
        elif option == "c": #Option C
            new_password(answer)
        else:
            break
     if option == "d": #Option D 
        break #Stops the program
    
