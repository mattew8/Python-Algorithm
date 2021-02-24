def solution(participant, completion):
    run = sorted(participant)
    win = sorted(completion)
    win.append("X")
    for i in range(len(run)):
        # run과 win이 순서대로 배열되어있으니 0번부터 끝까지 순서대로 비교
        if run[i]!=win[i]:
            return run[i]
            # 비교하다가 i번째 원소가 다르면 그 run[i]를 return하면 끝!

print(solution(["a","b","c","b"],["a","b","c"]))