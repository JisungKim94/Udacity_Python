# dictionaires
# Dictionary keys must be immutable
# 딕셔너리는 문자열뿐만 아니라 정수나 플로트 튜플과 같은 불변 유형의 키를 가질 수 있습니다.
# 모든 키가 같은 유형일 필요는 없습니다! 키를 묶는 대괄호[]를 사용하여 값을 조회하거나 사전에 새 값을 삽입할 수 있습니다.
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
print(elements["lithium"])
# print(elements[3])    # dictionary는 숫자 index로는 안불림 (KeyError)
print("\n")

# in, get for dictionaires
print("carbon" in elements)
print(elements.get("dilithium"))
print("\n")

# Identity Operator
# n = elements["dilithium"] # 없는걸 부르면 KeyError 발생하는디
n = elements.get("dilithium")  # 이렇게 부르면 댐
print(n is None)
print(n is not None)
print("\n")

# is
# is는 동일한 객체인지를 확인하는거임 같은 값을 가지더라도 다른 객체라면 FALSE를 띄움
# b = a 를 통해서 a와 b는 동일한 객체를 가지지만, a와 c는 같은 값을 가지지만 서로 다른 객체이므로
# is를 하면 FALSE가 return 된다.
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b)
print(a is b)
print(a == c)
print(a is c)
print("\n")

# invalid dictionary - this should break
# 딕셔너리의 key는 immutable만 사용할 수 있는데, list는 mutable이라서 unhashable type error 발생
# room_numbers = {
#     ['Freddie', 'Jen']: 403,
#     ['Ned', 'Keith']: 391,
#     ['Kristin', 'Jazzmyne']: 411,
#     ['Eugene', 'Zach']: 395
# }

# valid dictionary - this should work
# immutable한 tuple을 사용하면 error 없음
room_numbers = {
    ("Freddie", "Jen"): 403,
    ("Ned", "Keith"): 391,
    ("Kristin", "Jazzmyne"): 411,
    ("Eugene", "Zach"): 395,
}
print(room_numbers[("Eugene", "Zach")])
