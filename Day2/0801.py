#문자열 출력
print("naver", "kakao", "samsung", sep="/")
print("first", end=""); print("second")

#문자열
a = 'python'
print(a[0], a[2])

#문자열 슬라이싱
carnum = "11가 0801"
print(carnum[-4:])

#문자열 인덱싱과 슬라이싱
text = "홀짝홀짝홀짝"
print(text[::2])
print(text[::-1])

#치환
myphone = "202-208-01"
solution_myphone = myphone.replace("-", "")
print(solution_myphone)

#문자열 다뤄보기.
url = "heep://book.kr"
url_split = url.split('.')
print(url_split[-1])


#replace
string = 'abcdfe2a354a32a'
new_string = string.replace('a', 'A')
print(new_string)

#간단한 문자열을 출력

people1 = "김재섭"
age1 = 24
people2 = "김제섭"
age2 = 25


#%formatting
print("이름은 %s이고 나이는 %d입니다." % (people1, age1))
print("이름은 %s이고 나이는 %d입니다." % (people2, age2))


#format()
print("이름은 {} 나이는 {}".format(people1, age1))
print("이름은 {} 나이는 {}".format(people2, age2))


#f-string
print(f"이름: {people1}, 나이: {age1}")
print(f"이름: {people2}, 나이: {age2}")


#제거하기/타입 바꿔주기
a = "5,969,782,558"
new_a = a.replace(",", "")
solution_a = int(new_a)
print(solution_a)

#데이터 슬라이싱
text2 = "2022/08 오늘은 날씨가 맑습니다."
print(text2[:7])

#strip 메서드
data ="                    김재섭             "
new_data = data.strip()
print(new_data)