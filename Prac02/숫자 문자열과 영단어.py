

# 1. 한 char씩 추가하면서 대상되는 스트링 정릴 (변수 활용) - 반복문
# 2. 확인되는 스트링으로 변환이 가능한 숫자가 있는지 점검
# 3. 일치하는 스트링이 있으면 대상되는 내용을 answer 변수로 누적
#
def solution(s) :

    voca = {
        'zero': 0, 'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9
    }

    answer = ''
    word = ''


    for c in s:

        try:
            i = int(c)
            answer += c

        except:
            word += c

            try:
                if len(word) >= 3:
                    answer += str(voca[word])
                    word = ''
            except:
                continue

    return int(answer)


