def solution(n, lost, reserve):
    answer = n - len(lost)
    # 우선 전체 학생 수 n에서 체육복이 없는 사람 수인 len(lost)를 빼준다

    no_overlap_lost = list(set(lost)-set(reserve))
    no_overlap_reserve = list(set(reserve)-set(lost))
    temp_ans = len(lost+reserve) - len(set(lost + reserve))
    # 이 문제의 첫번째 핵심. 가장 먼저 lost와 reserve에 중복해서 있는 학생들을 빼줘야만 한다! 이게 가장 우선
    # set함수를 써 리스트 간 중복되는 녀석을 빼준다
    # 덤으로 len(lost+reserve)-len(set(lost + reserve)) 이 녀석을 통해 중복되는 인자들의 개수를 알 수도 있다
    
    answer = answer + temp_ans
    # 중복된다 = 체육복이 있다 이므로 answer에다가 더해준다.

    for steel in no_overlap_lost:
        if steel - 1 in no_overlap_reserve :
            answer = answer + 1
            no_overlap_reserve.remove(steel - 1)

        elif steel + 1 in no_overlap_reserve :
            answer = answer + 1
            no_overlap_reserve.remove(steel + 1)

        # 이제 lost와 reserve간에 중복되는 인자가 없으므로 각 번호 양 옆에 여분이 있으면 빌려준다
        # 여기서 두번째 핵심. 학생2의 경우 1에게도 3에게도 빌릴 수 있는데, 학생4도 도난당했으면 2는 1에, 4는 3에 빌려야만 한다.
        # 그러므로 steel - 1부터 if문으로 돌려 자기보다 작은 번호 사람에게 우선적으로 빌리도록 만들어야 한다

    return answer


