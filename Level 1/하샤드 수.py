def solution(x):
    a = []
    for i in str(x):
        int_i = int(i)
        a.append(int_i)
    plus = sum(a)
    
    if x%plus == 0:
        answer = True
    else:
        answer = False
        
    return answer