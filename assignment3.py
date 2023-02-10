#Write a Python program that accepts a word from the user and reverse it.(input is taken from user)
nums = []
even = 0
odd = 0

print("Enter 10 Numbers: ")
for i in range(9):
  nums.insert(i, int(input()))

for i in range(9):
  if nums[i]%2==0:
    even = even+1
  else:
    odd = odd+1

print("\nEven Number: ")
print(even)
print("Odd Number: ")
print(odd)