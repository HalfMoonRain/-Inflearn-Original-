# Chapter04-03
# 파이썬 심화
# 시퀀스형 
# 해시테이블(hashtable) -> 적은 리소스로 많은 데이터를 효율적으로 관리
# Dict -> Key 중복허용 X, Set -> 중복허용 X
# Dict 및 Set 심화

# immutable Dict

# 읽기 전용 Dict 사용할 수 있음
from types import MappingProxyType

d = {'key1':'value1'}

# Read Only
d_frozen = MappingProxyType(d)

print(d, id(d)) # hash(d) 는 출력되지 않음 
print(d_frozen, id(d_frozen)) # hash(d_frozen) 또한 출력 되지 않음 하지만 수정은 안됨

# 수정 불가
# d_frozen['key2'] = 'value2'

# 수정 가능
d['key2'] = 'value2'

print(d)

print()
print()

s1 = {'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'}
s2 = set(['Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'])
s3 = {3}
s4 = set() # Not {}
s5 = frozenset({'Apple', 'Orange', 'Apple', 'Orange', 'Kiwi'})

s1.add('Melon')

# 추가 불가
# s5.add('Melon')


# 선언 최적화
# 바이트 코드 -> 파이썬 인터프리터 실행
from dis import dis


print('-------')
print(dis('{10}'))
print('-------')
print(dis('set([10])'))

