# sets for list
# A set is a data type for 변경 가능하고(mutable) 순서가 없는(unordered) 데이터임
# 즉, 중복 요소가 있으면 하나로 합쳐짐
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)
print("\n")

# sets for tuple
numbers = (1, 2, 6, 3, 1, 1, 6)
unique_nums = set(numbers)
print(unique_nums)
print("\n")

# in, add, pop for sets
fruit = {"apple", "banana", "orange", "grapefruit"}  # define a set
print("watermelon" in fruit)  # check for element
fruit.add("watermelon")  # add an element
print(fruit)
print(fruit.pop())  # remove a random element
print(fruit)
