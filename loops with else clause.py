"""for & while loops can optionally have an else clause.
    Else clause executes after a for loop terminates by iterating to completion,
    or after  a while loop terminates by its conditional expression becoming false"""


for i in range(3):
    print(i)
else:
    print('done')

i = 0

while i < 3:
    print(i)
    i += 1
else:
    print('done')


"""The else clause does not execute if the loop terminats through a break statement
    or by raising an exception."""

for i in range(2):
    print(i)
    if i == 1:
        break

else:
    print('done')


"""MAIN USE CASE FOR THE for... else clause CONSTRUCT"""

a = [1, 2, 3, 4]
for i in a:
    if type(i) is not int:
        print(i)
        break
else:
    print('NO EXCEPTION')

