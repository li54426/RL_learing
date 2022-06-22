import numpy as np

def try_list():
    a = [[i for i in range(4)],[j for j in range(4,8)]]

    print(a[0][1])

    P = [[[] for i in range(4)] for j in range(4 *12)]
    print(P)


def sample(MDP, Pi, step_max, times):
    #进行采样
    S, A, P, R, gamma =MDP
    episodes = []
    step = 0
    s = np.random.randint(4)
    while s != 4 and step <= step_max:
        step += 1
        rand = np.random.rand()
        temp = 0
        for a in A:


    


def MC(episodes, V, N, gamma):
    for episode in episodes:
        G = 0
        len = len(episode)
        for i in range(len-1, -1, -1):
            (s, a, r, s_ )= episode[i]
            G = r + gamma * G
            N[s] = N[s] + 1
            V[s] += (G - V[s])/ N[s]



if __name__ == '__main__':
    steps = 20

    episodes = sample(MDP, Pi1, steps, 1000)
    gamma - 0.5
    V = {'s1': 0,
    "s2" : 0,
    's3' : 0,
    's4' : 0,
    's4': 0,
    's5' : 0
    }
    N = {'s1': 0,
    "s2" : 0,
    's3' : 0,
    's4' : 0,
    's4': 0,
    's5' : 0
    }

    MC(episodes, V, N, gamma)
    print('V is', V)