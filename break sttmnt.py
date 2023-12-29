i = 0
while 1 < 7:
    print(i)
    if(i == 4):
        print("Breaking the loop")
        break
    i += 1



for i in (0, 1, 2, 3, 4):
    print(i)
    if i == 2:
        break


"""If a loop has an else clause, it does not execute when the loop is terminated through a break statement

When a break statement executes inside a loop control flow breaks out of the loop immediately.

Executing the above prints every digit until number 4 when the break statement is met and the loop stops"""