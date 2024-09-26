#PROG 1700 – Tech Check #1
#Variables, Operators, Input/Output & Casting

# Restaurant Bill 
# You will create a console-based Python program that will calculate the amount of the tip, the tax, and the 
# total amount of a restaurant bill. The program will prompt the user to input the original amount of the bill. 
# The program will then output the amount of the tax (15% of the original amount) and a tip (20% of the original amount). 
# Finally, the program will output the new total of the bill.

"""
Student Name:  Mathew Akunyili  
Program Title: Tech check 1
Description:    Creat a program that calculates the total bil in a resturant 
"""
def main():
    # YOUR CODE STARTS HERE, each line must be indented (one tab)

    # welcome user to program
    print("Hello welcome to our program, we will help you calculate the tax and tip of you bill")

    #prompt user to input bill
    bill = input("Please enter your original bill amount:")

    #Calculate tax of bill
    tax = int(bill) * 0.15

    #calculate tip of bill
    tip = int(bill) * 0.20

    #Print original bill to user
    print("Your original bill amount is: $"+bill)

    #Print tax to user
    print("Your tax is:", tax)

    #print tip to user
    print("Your tip is:", float(tip))

    #print total bil to user
    total = float(bill) + float(tip) + float(tax)
    print("Your total is: $"+str(total))







    # YOUR CODE ENDS HERE

main()