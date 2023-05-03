def take_guess():
    print("숫자 3개를 하나씩 차례대로 입력하세요.")
    i = 0
    new_guess = []                             
    while i < 3:
        gue_number = int(input("{}번째 숫자를 입력하세요: ".format(i + 1)))
        if gue_number > 9 and gue_number < 0:    
            print("범위를 벗어나는 숫자입니다. 다시 입력하세요.")
            continue
        if gue_number in new_guess:             
            print("중복되는 숫자입니다. 다시 입력하세요. ")
        else:
            new_guess.append(gue_number)        
            i += 1

    return new_guess
