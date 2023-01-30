def solution(n, arr1, arr2):
    answer = ['']*n

    # 10진수 -> 2진수 변환 문자열 생성
    arr1Bin, arr2Bin = [],[]
    for i in range(n):
        arr1Bin.append(format(arr1[i],'b').zfill(n))
        arr2Bin.append(format(arr2[i],'b').zfill(n))

    # 비밀지도 문자열에 ' ', '#' 채우기 설정
    for i in range(n):
        for j in range(n):
            if (arr1Bin[i][j] == '0') and (arr2Bin[i][j] == '0'):
                answer[i] += " "
            else:
                answer[i] += "#"

    return answer


n = 6
arr1 = 	[46, 33, 33 ,22, 31, 50]
arr2 = 	[27 ,56, 19, 14, 14, 10]
print(solution(n, arr1, arr2))