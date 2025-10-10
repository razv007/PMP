import random
import math

def simulate(n: int, seed: int) -> float:
    random.seed(seed)
    red_count=0
    for i in range(n):
        red=3
        die=random.randint(1,6)
        if die==6:
            red=4
        p_red=red/10        
        if random.random()<p_red:
            red_count+=1

    return red_count/n

def theoretical_probability() -> float:
    # (1/2)*(3/10) + (1/6)*(4/10) + (1/3)*(3/10)= 9/60 + 4/60 + 6/60 = 19/60
    return 19/60

N = 1000000
est = simulate(1000000, 10)
theo = theoretical_probability()
print(est)
print(theo)
print(abs(est - theo))
