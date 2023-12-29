for i in (0, 1, 2, 3, 4, 5):
    if i == 2 or i == 4:
        continue
    print(i)


"""A continue statement will skip to the next iteration of the loop
bypassing the rest of the current block continuing the loop.
Note: 2 & 4 are not printed, since continue goes to the next iteration instead of continuing on
print(i) when i== 2 or i == 4"""