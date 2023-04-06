
word='naver daum'

word_list=['pizza','hamburger','']

print(word.split(' '))
print(word.split(' ')[0])

print(word[::-1])

# append = 리스트 끝
# insert = 원하는 위치에 삽입

food=['juice','icecream']

# index 1의 위치에 아이템들 모두 추가
food[1:1] = ['grape','부대찌개']
print(food)

# 2부터 3까지 아이템 교체
food[2:4] = ['cu','gs25']
print(food)

food = ['pizza', 'sandwich', 'donuts', 'muffin', 'hamburger']
food[2:4] = ['apple', 'kiwi', 'cookie']
print(food)
# output: ['pizza', 'sandwich', 'apple', 'kiwi', 'cookie', 'hamburger']

food = ['pizza', 'hamburger', 'sandwich', 'donuts']
food.remove('sandwich')
print(food)
# output: ['pizza', 'hamburger', 'donuts']

# 리스트 요소 삭제
del food[1:3]
print(food)
# output: ['pizza', 'donuts']

# 리스트 모든 아이템 삭제
del food[:]
print(food)
# output: []


# extend 
food = ['pizza', 'hamburger']
food2 = ['apple', 'banana', 'kiwi']
all_food = food + food2
print(all_food)
# output: ['pizza', 'hamburger', 'apple', 'banana', 'kiwi']

# 모든 아이템 리스트에 추가하기
food = ['pizza', 'hamburger']
food2 = ['apple', 'banana', 'kiwi']
food.extend(food2)
print(food)
# output: ['pizza', 'hamburger', 'apple', 'banana', 'kiwi']

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(alphabet[0:-2])

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
print(alphabet[:6])
print(alphabet[6:])
print(alphabet[:])
print(len(alphabet))
# output:
# ['a', 'b', 'c', 'd', 'e', 'f']
# ['g', 'h']
# ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
# 8

number = [10, 100, 54, 72, 61]
number.sort()
print(number)
# output: [10, 54, 61, 72, 100]


number = [10, 100, 54, 72, 61]
# @@@@@@@ sort()를 사용하면 List를 정렬할 수 있습니다. 인자로 reverse=True를 전달하면 반대 방향으로 정렬을 할 수 있습니다.
number.sort(reverse=True)
print(number)
# output: [100, 72, 61, 54, 10]

food = ['pizza', 'hamburger', 'sandwich', 'donuts']
print(len(food))
# food.sort(key=len)
print(food)
# output: ['pizza', 'donuts', 'sandwich', 'hamburger']

''' 
3-2. key

정렬을 목적으로 하는 함수를 값으로 넣는다. lambda를 이용할 수 있다.

key 값을 기준으로 정렬되고 기본값은 오름차순이다. 

>>> str_list = ['좋은하루','good_morning','굿모닝','niceday']
>>> print(sorted(str_list, key=len))  # 함수
['굿모닝', '좋은하루', 'niceday', 'good_morning']

>>> print(sorted(str_list, key=lambda x : x[1]))  # 람다
['niceday', 'good_morning', '굿모닝', '좋은하루']
'''

