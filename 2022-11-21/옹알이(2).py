def solution(babbling):
    count = 0
    babble = [ "aya", "ye", "woo", "ma" ]
    for a in babbling:
        for text in babble:
            if text * 2 not in a:
                a = a.replace(text, ' ')
        if a.strip() == '':
            count += 1
    return count
