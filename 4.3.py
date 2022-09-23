# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
numbers = [1,1,1,2,2,2,3,3,3,4,5,6]
list = []
for i in numbers:
    if numbers.count(i) == 1:
        list.append(i)
print(list)        

# def elements(nums):
#     nums = [int(i) for i in nums.split()]
#     return(list(set(nums)))

# numbers = "1 4 7 234 234 7 2 9"
# print(elements(numbers))
