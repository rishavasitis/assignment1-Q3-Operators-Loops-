numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even = 0
odd = 0
for i in numbers:
    if(i % 2 == 0):
        even += 1
    else:
        odd += 1
print("total Even numbers available in the list: ", even)
print("total Odd numbers available in the list: ", odd)