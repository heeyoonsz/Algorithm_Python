'''
문자열 안에서 찾고 싶은 문자의 개수를 찾고 싶을 때
iterable 자료형에서 사용 가능
변수.count('찾는 요소') 형태로 사용
'''

print('hello'.count('l'))

b='ox o x oxoxoxoxxxo oxoxxox'
print(b.count('ox'))

print('------------------------')

a=[1,1,1,2,3,3,4,4,90,10]
# 1의 개수 3개 반환
print(a.count(1))

'''
@@ 딕셔너리, 셋에서 count 사용 불가 @@
'''

bool = True,False,True  
bool.count(True)
type(bool)