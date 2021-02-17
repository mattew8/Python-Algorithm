def solution(N, stages):
    all_stage = list(range(1,N+1))
   # all_stage = [1, 2, 3, 4, 5]
    all_user = len(stages)
    
    fail = []
    
    for i in all_stage:
        if i in stages:
            how_many = stages.count(i)/all_user
            fail.append(how_many)
        else:
            fail.append(0)

        all_user = all_user - stages.count(i)
    
    fail_dict = dict(zip(all_stage, fail))
#     zip 을 이용해 zip(key[], value[])로 dict을 만들 수 있다

    fail_dict = sorted(fail_dict, key=lambda x: fail_dict[x], reverse=True)
        
    answer = fail_dict
    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
# [3, 4, 2, 1, 5]