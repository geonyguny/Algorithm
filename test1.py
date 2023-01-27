def solution(numbers, hand):
    answer = ''
    distance = [[1,3],[0,0],[1,0],[2,0],[0,1],[1,1],[2,1],[0,2],[1,2],[2,2],[0,3],[2,3]]
    L = 10
    R = 11
    

    for i in numbers:
        if i in (1,4,7):
            L =i
            answer += "L"
        elif i in (3,6,9):
            R=i
            answer += "R"
        else:
            Ldist = abs(distance[i][0] - distance[L][0])+abs(distance[i][1] - distance[L][1])
            Rdist = abs(distance[i][0] - distance[R][0])+abs(distance[i][1] - distance[R][1])
            if Ldist > Rdist:
                R = i
                answer += "R"
            elif Ldist < Rdist:
                L = i
                answer += "L"
            else:
                if hand == "right":
                    R = i
                    answer += "R"
                else:
                    L = i
                    answer += "L"
    return answer

numbers = [1, 2, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand = "right"
print(solution(numbers, hand))