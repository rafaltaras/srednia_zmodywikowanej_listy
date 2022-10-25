from ast import Del, Delete
from unicodedata import numeric


numbers = [5,32,56,2,2,16,7,10,23,100]
mean_number = 0


for seq, number in enumerate(numbers):
    x = number % 10
    if x >= 5:
        y = 10 - x
        number = number + y
        numbers[seq] = number 
    else:
        number = number - x
        numbers[seq] = number

#print(numbers)
numbers.remove(min(numbers))
numbers.remove(max(numbers))
print(numbers)

mean_number = sum(numbers) / len(numbers)
print(mean_number)




   


