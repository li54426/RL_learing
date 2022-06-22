import matplotlib.pyplot as plt
import numpy as np
from tqdm import tqdm

class CliffWalkingEnv:
    def __init__(self, ncol, nrow) -> None:
        self.nrow = nrow
        self.ncol = ncol
        self.x = 0
        self.y = nrow - 1


    def step(self, action):
        change = [[0, -1], 
        [0, 1], [-1, 0], [1, 0]]
        self.x = min(self.ncol - 1, max(0, self.x + change[action][0]))
        self.y = min(self.nrow-1, max(0, self.y + change[action][1]))
        next_state = self.ncol * self.y + self.x
        reward = -1
        done = False
        if self.y == self.nrow -1 and self.x > 0:
            done = True
            if self.x != self.ncol-1 :
                reward = -100

        return next_state, reward, done

    def reset(self):
        self.x = 0
        self.y = self.nrow -1
        return self.ncol * self.y + self.x


class Sarsa:
    def __init__(self, ncol, nrow, epsilon, alpha, gamma, naction):
        self.Qtable = np.zeros((nrow * ncol, naction))
        self.epsilon = epsilon
        self.alpha = alpha
        self.gamma = gamma
        self.naction = naction

    def take_action(self, state):
        if np.random.random() < self.epsilon :
            return np.random.randint(self.naction)

        else :
            return np.argmax(self.Qtable[state])

    def best_action(self, state):
        qmax = np.max(self.Qtable)
        a = [0 for i in range(self.naction)]
        for i in range(self.naction):
            a[i]=1 if self.Qtable[state, i] == qmax else 0

        return a

    def update(self, s0, a0, r, s1, a1):
        td_errr = r + self.gamma * self.Qtable[s1, a1] - self.Qtable[s0, a0]
        self.Qtable[s0, a0] += self.alpha * td_errr









if __name__ == '__main__':
    env = CliffWalkingEnv(12, 4)
    agent = Sarsa(12, 4, 0.1, 0.1,0.9, 4)
    num_episodes = 500
    return_list = []

    for i in range(10):
        with tqdm(total=int(num_episodes / 10), desc='Iteration %d' % i) as pbar:
            for i_episode in range(int(num_episodes / 10)):  # 每个进度条的序列数
                episode_return = 0
                state = env.reset()
                action = agent.take_action(state)
                done = False
                while not done:
                    next_state, reward, done = env.step(action)
                    next_action = agent.take_action(next_state)
                    episode_return += reward  # 这里回报的计算不进行折扣因子衰减
                    agent.update(state, action, reward, next_state, next_action)
                    state = next_state
                    action = next_action
                return_list.append(episode_return)
                if (i_episode + 1) % 10 == 0:  # 每10条序列打印一下这10条序列的平均回报
                    pbar.set_postfix({
                        'episode':
                        '%d' % (num_episodes / 10 * i + i_episode + 1),
                        'return':
                        '%.3f' % np.mean(return_list[-10:])
                    })
                pbar.update(1)

    episodes_list = list(range(len(return_list)))
    plt.plot(episodes_list, return_list)
    plt.xlabel('Episodes')
    plt.ylabel('Returns')
    plt.title('Sarsa on {}'.format('Cliff Walking'))
    plt.show()

