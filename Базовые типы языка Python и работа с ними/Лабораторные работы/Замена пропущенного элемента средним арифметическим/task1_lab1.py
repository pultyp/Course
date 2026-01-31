numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]


# TODO заменить значение пропущенного элемента средним арифметическим

none_index = numbers.index(None)

sum_numbers = 0
for num in numbers:
    if num is not None:
        sum_numbers += num

count_elements = len(numbers)

average = sum_numbers / count_elements

numbers[none_index] = average

print("Измененный список:", numbers)
