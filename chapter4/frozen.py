import gym
from cliffwalkenv import PolicyIteration


if __name__ =='__main__':
    env = gym.make('FrozenLake-v1')
    env = env.unwrapped
    #环境渲染, 4 * 4
    env.render()
    holes = set()
    ends = set()
    for s in env.P:
        for a in env.P[s]:
            for s_ in env.P[s][a]:
                if s_[2] == 1.0:  # 获得奖励为1,代表是目标
                    ends.add(s_[1])
                if s_[3] == True:
                    holes.add(s_[1])
    holes = holes - ends
    print("冰洞的索引:", holes)
    print("目标的索引:", ends)

    for a in env.P[14]:  # 查看目标左边一格的状态转移信息
        print(env.P[14][a])

    action_meaning = ['<', 'v', '>', '^']
    theta = 1e-5
    gamma = 0.9
    agent = PolicyIteration(env, theta, gamma)
    agent.policy_iteration()
    agent.print_agent(agent, action_meaning, [5, 7, 11, 12], [15])