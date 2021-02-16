def solution(s):
    words = s.split(" ")
#     words =   ['try', 'hello', 'world']
    answer = []
    strange = str()
    for i in words:
#         i = 'try' , 'hello' , 'world'
        for w in range(len(i)):
#         w = 1 , 2 ,3 ...
            if w % 2 == 0:
                strange += i[w].upper()

            else:
                strange += i[w].lower()
        answer.append(strange)
        strange = str()
    answer = ' '.join(answer)
    return answer

print(solution("try hello world"))
