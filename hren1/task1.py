numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

# TODO заменить значение пропущенного элемента средним арифметическим

len = len(numbers)
sum = 0
i = 0
find_i = 0
while (i < len):
    if (numbers[i] != None):
        sum += numbers[i]
    else:
        find_i = i

    i+=1

average = sum / (i)

numbers[find_i] = average

print("Измененный список:", numbers)
