import copy
from distutils.util import change_root
from sqlite3 import Row

class CliffWalkEnv:
    def __init__(self, ncol =12, nrow =4) -> None:
        #初始化为四行, 十二列的表格
        self.nrow = nrow
        self.ncol = ncol
        #状态, 动作转移矩阵, 也就是P(a, s)
        #p[a][s] = [(p, nexts, r, done)]
        self.P = self.creatp()

    def creatp(self):
        P =  [[[] for i in range(4)] for j in range(4 *12)]
        change = [[0, -1], [0, 1], [-1, 0], [1, 0]]
        for i in range(self.nrow):
            for j in range(self.ncol):
                for a in range(4):
                    if i== self.nrow - 1 and j > 0:
                        cur = i *self.ncol + j
                        P[cur][a] = [(1, cur, 0, True)]
                        continue
                    next_x = min(self.nrow-1, max(0, j+change[a][0]))
                    next_y = min(self.nrow - 1, max(0, i + change[a][1]))
                    next_state = next_y * self.ncol + next_x
                    reward = -1
                    done = False
                    # 下一个位置在悬崖或者终点
                    if next_y == self.nrow - 1 and next_x > 0:
                        done = True
                        if next_x != self.ncol - 1:  # 下一个位置在悬崖
                            reward = -100
                    P[i * self.ncol + j][a] = [(1, next_state, reward, done)]
        return P

class PolicyIteration:
    def __init__(self,env, theta, gamma):
        self.env = env
        self.ns = self.env.nrow * self.env.ncol
        self.v = [0] * self.env.nrow * self.env.ncol
        self.pi = [[ 0.25 ] * 4 for i in range(self.ns)]
        self.theta = theta
        self.gamma = gamma

    def policy_evaluation(self):
        cnt = 1
        while 1:
            max_diff = 0
            v_new = [0] * self.env.nrow * self.env.ncol
            for s in range(self.ns):
                qsa_list = []
                for a in range(4):
                    qsa = 0
                    for res in self.env.P[s][a]:
                        p, s_next, r ,done = res
                        qsa += p * (r +self.gamma * self.v[s_next]) * (1-done)
                    qsa_list.append(self.pi[s][a] * qsa)
                v_new[s] = sum(qsa_list)  # 状态价值函数和动作价值函数之间的关系
                max_diff = max(max_diff, abs(v_new[s] - self.v[s]))
            self.v = v_new
            if max_diff < self.theta: break  # 满足收敛条件,退出评估迭代
            cnt += 1
        print("策略评估进行%d轮后完成" % cnt)


    def policy_improvement(self):
        for s in range(self.ns):
            qsa_list = []
            for a in range(4):
                qsa = 0
                for res in self.env.P[s][a]:
                    p, next_state ,r ,done = res
                    qsa += p * (r * self.gamma * self.v[next_state] * (1-done) )
                qsa_list.append(qsa)
            maxq = max(qsa_list)
            cntq = qsa_list.count(maxq)
            self.pi[s] = [1 / cntq if q == maxq else 0 for q in qsa_list]
        print('策略提升完成')
        return self.pi

    def policy_iteration(self):
        while 1 :
            self.policy_evaluation()
            old_pi = copy.deepcopy(self.pi)
            new_pi = self.policy_improvement()
            if old_pi == new_pi :
                break


    def print_agent(self):
        action_meaning = ['^', 'v', '<', '>']
        disaster = list(range(37, 47))
        end =[47]

        print('状态价值')
        for i in range(self.env.nrow):
            for j in range(self.env.ncol):
                str = '.3f{}'.format(self.v[i * self.env.ncol + j])
                print(str ,end = ' ')
        print()

        print('策略')
        for i in range(self.env.nrow):
            for j in range(self.env.ncol):
                if(i * self.env.ncol + j)  in disaster:
                    print("****", end = ' ')
                elif(i * self.env.ncol + j) in end:
                    print('EEEE', end = ' ')
                else:
                    a = self.pi[i * self.env.ncol + j]
                    pi_str = ''
                    for k in range(4):
                        pi_str += action_meaning[k] if a[k] > 0 else 'o'
                    print(pi_str, end =' ')
            print()


if __name__ =='__main__':
    env = CliffWalkEnv()
    agent = PolicyIteration(env, 0.001, 0.9)
    agent.policy_iteration()
    agent.print_agent()
