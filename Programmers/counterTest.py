import collections
def solution(participant, completion):
    a = collections.Counter(participant)
    b = collections.Counter(completion)
    answer = a - b
    return list(answer)[0]

solution(["marina", "josipa", "nikola", "vinko", "filipa"], ["josipa", "filipa", "marina", "nikola"])
