#! python3
"""
###### Task 2
Ask the user to enter in the prices of 5 items in dollars.cents (eg 10.34).  Find the total value of all items and then calculate the total price including 5% GST and 7% PST

Sample:
Enter in price of item #1: 10.25
Enter in price of item #2: 11.45
Enter in price of item #3: 13.85
Enter in price of item #4: 9.25
Enter in price of item #5: 10.25
Your subtotal is 55.05
Your GST is 2.75
Your PST is 3.85
Your total is 61.65
"""

one = float(input("Enter in prce of item #1:" ))
two = float(input("Enter in prce of item #2:" ))
three = float(input("Enter in prce of item #3:" ))
four = float(input("Enter in prce of item #4:" ))
five = float(input("Enter in prce of item #5:" ))

total = one + two + three + four + five
print(f"your subtotal is {total}")
Gst = 5 * total / 100
print(f"GST is {Gst}")
pst = 7 * total / 100
print(f"PST is {pst}")