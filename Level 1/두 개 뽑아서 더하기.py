def solution(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            if i == j+1:
                continue            
            if j+1 == len(numbers):
                break
            result.append(numbers[i] + numbers[j+1])   
    answer = list(set(result))
    return sorted(answer)

print(solution([2,1,3,4,1]))
# [2, 3, 4, 5, 6, 7]