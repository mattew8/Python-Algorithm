def solution(arr):
    answer_num = 0
    answer = [arr[0]] 
    for i in range(len(arr)):
        if arr[i] != answer[answer_num]:
            answer.append(arr[i])
            answer_num += 1
    return answer

print(solution([1,1,2,3,4,4]))
# [1,2,3,4]

