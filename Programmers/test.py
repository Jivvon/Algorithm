def solution(answers):
    sol1 = list(i%5+1 for i in range(10000))
    sol2 = list(2 for _ in range(10000))
    for i in range(1, 10000, 8):
        sol2[i] = 1
    for i in range(3, 10000, 8):
        sol2[i] = 3
    for i in range(5, 10000, 8):
        sol2[i] = 4
    for i in range(7, 10000, 8):
        sol2[i] = 5
    els = [3,3,1,1,2,2,4,4,5,5]
    sol3 = []
    for _ in range(1000):
        sol3.extend(els)
    
    counts = [0, 0, 0]
    for i, ans in enumerate(answers):
        if ans == sol1[i]:
            counts[0]+=1
        if ans == sol2[i]:
            counts[1]+=1
        if ans == sol3[i]:
            counts[2]+=1
    
    answer = []
    maxcount = max(counts)
    for i, el in enumerate(answers):
        if el == maxcount:
            answer.append(i+1)
    
    answer.sort()
    return answer

if __name__ == "__main__":
    ret = solution([1,2,3,4,5])
    print(ret)
