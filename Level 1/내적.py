def solution(a, b):
    ablist = []
    for i in range(len(a)):
        ablist.append(a[i]*b[i])
    
    answer = sum(ablist)
    return answer

print(solution([1,2,3,4], [-3,-1,0,2]))
# 3