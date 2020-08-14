import random
dic = {}

with open("vocabulary.txt", "r", encoding="UTF-8") as f:
    # 단어 추출
    for line in f:
        voca = line.strip().split(": ")
        eng, kor = voca[0], voca[1]
        # dictionary에 추가
        dic[eng] = kor

    # 유저 입력값 받기
    while True:
        # 랜덤으로 단어 받아오기
        keys = list(dic.keys())
        idx = random.randint(0, len(keys) - 1)
        eng = keys[idx]
        kor = dic[eng]

        guess = input("{}: ".format(kor))

        if guess == 'q':
            break

        if guess == eng:
            print("맞았습니다!")
        else:
            print("아쉽습니다. 정답은 {}입니다.".format(eng))

