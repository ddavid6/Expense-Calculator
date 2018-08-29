import math
import sys
import datetime

while True:
 print("Do you wanna open bank calculator?: Y/N")
 now = datetime.datetime.now()
 user_input = input("")
 if user_input == "N":
        break
 elif user_input == "Y":
        print("Welcome to bank calculator")
        print (now)
        checkingAcc = float(input("Enter current checking account balance: "))
        savingAcc = float(input("Enter current savings account balance: "))
        monthRent = float(input("Enter current months rent: "))
        workHours = float(input("Enter hours worked bi-weekly: "))
        largeTrans = float(input("Enter any large amounts spent: "))
        taxCut = float((22/100)*(workHours*11))
        salary = float((workHours*11)-taxCut)
        monthlySalary = float(salary*2)
        excessMoney = float(checkingAcc - 150)
        checkingAcc = float((checkingAcc)- largeTrans)
        newcheckingAcc = float((checkingAcc + salary)-monthRent)


        
        print("Monthly Salary: " , monthlySalary)
        print("Bi-weekly Salary: ", salary)
        print("Current Checking Account is: " , checkingAcc)
        print("New Checking Account is: " , newcheckingAcc)
        print("New Savings Account is: " , savingAcc)

        print("Do you want to add money from savings?: Y/N")
        user_input = input("")
        if user_input == "N":
            print("Do you want to add money TO savings?: Y/N")
            user_input = input("")
            if user_input == "N":
                break
            elif user_input == "Y":
                transferAmt = float(input("Enter amount to be transfered: "))
                newcheckingAcc = newcheckingAcc - transferAmt
                savingAcc = savingAcc + transferAmt
                print("New Checking Account is: " , newcheckingAcc)
                print("New Savings Account is: " , savingAcc)
        elif user_input == "Y":
            transferAmt = float(input("Enter amount to be transfered: "))
            newcheckingAcc = newcheckingAcc + transferAmt
            savingAcc = savingAcc - transferAmt
            print("New Checking Account is: " , newcheckingAcc)
            print("New Savings Account is: " , savingAcc)
            

            
       
                   
        
        
        
    
     
