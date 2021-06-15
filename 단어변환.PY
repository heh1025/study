def solution(begin, target, words):
    answer = 0
    queue = [begin]
    while True:
        tmp_q = []
        for a in queue:
            if a == target:
                return answer
            for b_idx in range(len(words)-1, -1, -1):
                b = words[b_idx]
                difference = sum([x != y for x, y in zip(a, b)])
                if difference == 1:
                    tmp_q.append(words.pop(b_idx))
        if not tmp_q:
            return 0
        queue = tmp_q
        answer += 1