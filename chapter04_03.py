# Chapter04-03
# 파이썬 심화
# 시퀀스형 
# 컨테이너(Container : 서로다른 자료형[list, tuple, collections.deque], Flat : 한 개의 자료형[str,bytes,bytearray,array.array, memoryview])
# 플랫(Flat: 한개의 자료형[str, bytes, bytearray, array.array, memoryview])
# 가변(list, bytearray, array.array, memoryview, deque) vs 불변(tuple, str, bytes)
# 불변(tuple, str, bytes)
# 해시테이블
# key에 Value를 저장하는 구조
# 파이썬 dict 해쉬 테이블 예
# key 값의 연산 결과에 따라 직접 접근이 가능한 구조
# key값을 해싱 함수 -> 해쉬 주소 -> key 에 대한 value를 구할 수 있다.

# Dict 구조
# print(__builtins__.__dict__)

# Hash 값 확인 --> 고유하다

t1 = (10, 20, (30, 40, 50))
t2 = (10, 20, [30, 40, 50])

print(hash(t1))
# print(hash(t2)) --> mutable 한 리스트가 안에 있어서 예외발생

print()
print()

# Dict Setdefault 예제
# tuple을 dict으로 만들자
source = (('k1', 'val1'),
          ('k1', 'val2'),
          ('k2', 'val3'),
          ('k2', 'val4'),
          ('k3', 'val5'))

new_dict1 = {}
new_dict2 = {}

# No use Setdefault
for k, v in source:
    if k in new_dict1:
        new_dict1[k].append(v)
    else:
        new_dict1[k] = [v]

print(new_dict1)

# Use Setdefault
for k, v in source:
    new_dict2.setdefault(k, []).append(v)
    
print(new_dict2)


# 주의
new_dict3 = {k: v for k, v in source}
# 나중값을 덮어 써지게 되므로 이렇게 만들면 안됨
print(new_dict3)
