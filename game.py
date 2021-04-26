# num_check 함수 사용
def num_check(number):
    dict_namber1 = {"1": "오른쪽으로 이동"}
    dict_namber2 = {"2": "왼쪽으로 이동"}
    dict_namber3 = {"3": "블록 바꾸기"}
    if number == 1:
        return print(dict_namber1["1"])
    elif number == 2:
        return print(dict_namber2["2"])
    elif number == 3:
        return print(dict_namber3["3"])
    else:
        return print("잘못 눌렀움 ㅡ3ㅡ")


print("게임을 시작합니다")
print("테트리스 시작")
print("1. 오른쪽 2. 왼쪽 3. 블록 바꾸기")

number = int(input("숫자를 입력하세요 : "))

print("당신이 입력한 숫자는 ? ", number)

num_check(number)


# ㄹ 블록 ,ㄱ 블록, ㄴ 블록, ㅁ 블록, ㅣ 블록, ㅜ 블록
list_block = ["ㄹ", "ㄱ", "ㄴ", "ㅁ", "ㅣ", "ㅜ"]
print("블록의 종류 :", list_block)
print("블록 갯수:", len(list_block))
for i in range(len(list_block)):
    print(list_block[i])
