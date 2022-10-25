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

print(numbers)

   


