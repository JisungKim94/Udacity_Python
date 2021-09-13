# A tuple is another useful container. It's a data type for immutable ordered sequences of elements
# 튜플은 수정은 불가능하고 ()사용 list는 []사용
location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])
print("\n")

# 일반적인 사용법
length, width, height = 52, 40, 100
print("The dimensions are {} x {} x {}".format(length, width, height))
print("\n")

# 변수를 순서대로 가져오기
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))
