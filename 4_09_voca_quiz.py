with open("vocabulary.txt", "r", encoding="UTF-8") as f:
    for line in f:
        voca = line.strip().split(": ")
        answer = voca[0]
        kor = voca[1]
        guess = input("{}: ".format(kor))

        if answer == guess:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(answer))
