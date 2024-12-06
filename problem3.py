#! python3

"""
##### Problem 3
Have the user enter an integer that is smaller than 10
Find the sum of the series:
1 + 11 + 111 + 1111 + ....
for the n terms, where the nth term has n number of 1's

input:
int number that is smaller than 10

output:
the sum of the series is xxxx

example:
enter a number: 4
the sum of the series is 1234
"""
n = 1.111111111111111111111111111111111111111
x = int(input("enter a number less than 10: "))
sum = 0

if x>10:
    print("enter an integer less than 10")

for i in range(x):
   y = round(n*(10**i))
   sum = sum + y
print(f"The sum of the series is {sum}")

