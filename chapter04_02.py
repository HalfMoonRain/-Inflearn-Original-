# Chapter04-02
# 파이썬 심화
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 리스트 및 튜플 고급

# Tuple Advanced
# Unpacking

# b, a = a, b

# *를 붙이면 unpacking 이 일어남
print(divmod(100, 9))
print(divmod(*(100, 9)))
print(*(divmod(100, 9)))

print()
x, y , *rest = range(10)
print(x, y, rest)

x, y , *rest = range(2)
print(x, y, rest)

x, y, *rest = 1,2,3,4,5
print(x, y, rest)

# Mutable(가변) vs Immutable(불변)
l = (15, 20, 25) 
m = [15, 20, 25]

print(l, id(l))
print(m, id(m))

l = l * 2
m = m * 2

print(l, id(l))
print(m, id(m))

l *= 2
m *= 2

print(l, id(l))
print(m, id(m))

print()
print()

# sort vs sorted
# reverse, key=len, key=str.lower, key=func ...

# sorted : 정렬 후 새로운 객체 반환 
f_list = ['orange', 'apple', 'mango', 'papaya', 'lemon', 'strawberry', 'coconut']
print('sorted - ', sorted(f_list))
print('sorted - ', sorted(f_list, reverse=True))
print('sorted - ', sorted(f_list, key=len))
print('sorted - ', sorted(f_list, key=lambda x : x[-1]))
print('sorted - ', sorted(f_list, key=lambda x : x[-1], reverse=True))

print('sorted - ', f_list)

# sort : 정렬 후 객체 직접 변경 (원본이 수정)

# 반환 값 확인(None)
print('sort - ', f_list.sort())
print('sort - ', f_list.sort(reverse=True), f_list)