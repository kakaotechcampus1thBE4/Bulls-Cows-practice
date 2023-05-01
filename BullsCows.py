from random import randint

def generate_numbers():
    numbers = []
    i = 0
    new_number = 0
    while i < 3:
        new_number = randint(0, 9)
        if new_number not in numbers:
            numbers.append(new_number)
            i += 1
    print("0과 9사이의 서로 다른 숫자 3개를 랜덤한 순서로 뽑았습니다.\n")

    return numbers
