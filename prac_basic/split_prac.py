

'''
* 문자열 나눌 때 사용
아무것도 안넣으면 공백(띄어쓰기,탭) 기준으로 문자열을 나눠 리스트의 요소로 저장
분할된 문자 개수만큼 각각을 변수로 지정하는 것도 가능
'''

'''
@ PARAMETER
sep - 문자열을 나누는 기호를 값으로 입력, 기본값은 공백을 기준으로 함
maxsplit - 문자를 나눌 최대 분할 수, 기본값은 -1(제한 없음), 아무 값도 안 넣으면 문자 전체를 나눔

'''

test='today is not monday, it\'s thursday'
# 기본값(공백)으로 분할
print()
print(test.split())
print()
print(test.split(sep=','))
print() 
#공백기준 1번 분할
print(test.split(maxsplit=1))
print()
#공백기준 2번 분할
print(test.split(maxsplit=2))
print()
#공백기준 3번 분할
print(test.split(maxsplit=3))
print()

print('---------------------------------')

test = 'Hello world : 안녕하세요?'
a,b = test.split(':')
print(a)
print(b)


