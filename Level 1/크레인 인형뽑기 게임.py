def solution(board, moves):
    answer = 0
    result = ["a"]
    # out of range로 인해 임의의 원소 추가

    for j in moves:
        go = True
        for i in board:
#         [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
            if go == True:
                if i[j-1] != 0:
                    if i[j-1] == result[-1]:
                        answer += 2
                        del result[-1]
#                         index를 기준으로 원소 삭제시 del을 사용
                    else :
                        result.append(i[j-1])

                    i[j-1] = 0
                    # 인형이 뽑힌 자리는 0으로
                                         
                    go = False
                    # 이중 for문 탈출. 바깥쪽 for문 실행하도록
                    continue
    return answer

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))
# 4