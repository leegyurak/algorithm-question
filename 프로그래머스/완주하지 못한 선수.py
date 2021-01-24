import collections

def solution (participant, completion) :
    participant.sort()
    completion.sort()

    result = collections.Counter(participant) - collections.Counter(completion)
    return list(result)[0]