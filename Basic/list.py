# using list index
list_of_random_things = [1, 3.4, "a string", True]

print(list_of_random_things[1:2])  # 왼쪽(포함) ~ 오른쪽(미 포함)
print(list_of_random_things[:2])  # 시작 ~ 2(미 포함)
print(list_of_random_things[1:])  # 1(포함) ~ 마지막
print("\n")
print("\n")

# using in
print("this" in "this is a string")
print(5 not in [1, 2, 3, 4, 6])

# Mutability
my_lst = [1, 2, 3, 4, 5]
my_lst[0] = "one"
print(my_lst)  # lists are mutable
greeting = "Hello there"
# greeting[0] = "M"  # TypeError occurred : string are immutable
print("\n")
print("\n")

# usefull Functions
list_temp = [1, 7, 3, 9, 11, 15, 20, -3, -5, -11]
print(len(list_temp))
print(max(list_temp))
print(min(list_temp))
print(sorted(list_temp))
print("\n")
print("\n")

# join/append method
separator1 = "\n".join(["fore", "aft", "starboard", "port"])
print(separator1)
separator2 = "-".join(["fore", "aft", "starboard", "port"])
print(separator2)
letters = ["a", "b", "c", "d"]
print(letters)
letters.append("e")
print(letters)
letters.pop()
print(letters)
letters.remove("b")
print(letters)
letters.insert(1, "b")
print(letters)
letters.extend(["e", "f", "g"])
print(letters)
