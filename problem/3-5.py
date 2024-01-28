def solution(reward, health, optional):

    return 

def recursive(idx, attack, reward, health, optional):

    time = health[idx] // attack
    if (health[idx] % attack) != 0:
        time += 1


    total_time = time + recursive(idx + 1, attack + reward[idx],  reward, health, optional)

    if optional[idx] == 1:
        total_time = min(total_time, recursive(idx + 1, attack,  reward, health, optional))

    return total_time