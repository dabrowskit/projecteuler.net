'''

ID_013
Large sum
Difficulty level: 5%

Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.

'''


with open("numbers.txt","r") as file:
    number_list = []
    for line in file:
        number_list.append(line.rstrip('\n'))
    sum = 0
    for num in number_list:
        num = int(num)
        sum += num
    first_10_digits_sum = str(sum)

print(first_10_digits_sum[:10])
