import numpy as np
from regex import R

def compute(chain, rewards, gamma):
    G = 0
    for i in range(len(chain)):
        cur = chain[i] -1
        G += gamma ** i * rewards[cur]
    return G 


def compbel(rewards, P, gamma):
    #V = R + g P V
    rewards = np.array(rewards).reshape(-1, 1)

    len = rewards.shape[0]
    A = np.eye(len) - gamma * P
    V = np.linalg.solve(A, rewards)
    return V


if __name__ == '__main__':
    np.random.seed(5)

    S_1 = [0.9, 0.1, 0, 0, 0, 0]
    S_2 = [0.5, 0, 0.5, 0, 0, 0]
    S_3 = [0, 0, 0, 0.6, 0, 0.4]
    S_4 = [0, 0, 0, 0, 0.3, 0.7]
    S_5 = [0, 0.2, 0.3, 0.5, 0, 0]
    S_6 = [0, 0, 0, 0, 0, 1]
    P = [S_1, S_2, S_3, S_4, S_5, S_6]
    P = np.array(P)

    rewards = [-1, -2, -2, 10, 1, 0]
    gamma = 0.5

    chain = [1, 2, 3, 6]
    #list 不能进行减法操作
    #chain_ = chain -1
    
    G = compute(chain, rewards, gamma)
    print(G)
    #-2.5
    V = compbel(rewards, P,gamma)
    print(V)


    P_from_mdp_to_mrp = [
    [0.5, 0.5, 0.0, 0.0, 0.0],
    [0.5, 0.0, 0.5, 0.0, 0.0],
    [0.0, 0.0, 0.0, 0.5, 0.5],
    [0.0, 0.1, 0.2, 0.2, 0.5],
    [0.0, 0.0, 0.0, 0.0, 1.0],
]
    