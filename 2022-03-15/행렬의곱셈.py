def solution(arr1, arr2):
    answer = []
    for i in range(0, len(arr1)):
        temp_row = []
        for j in range(0, len(arr2[0])):
            value = 0
            for k in range(0, len(arr1[0])):
                value += arr1[i][k] * arr2[k][j]
            temp_row.append(value)
        answer.append(temp_row)
    return answer
