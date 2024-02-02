def solution(s, t):
    if len(s) != len(t):
        return False
    
    for s_, t_ in zip(sorted(s), sorted(t)):
        if s_ != t_:
            return False
    return True

