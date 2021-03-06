import numpy as np
import matplotlib.pyplot as plt

class Bandit:
    #K臂老虎机
    #属性 probs, bext_index
    #method : play(k) 
    def __init__(self, K):
        #K problities
        self.k = K;
        self.probs = np.random.uniform(size = K);
        self.best_prob = self.probs.max();
        self.best_index = self.probs.argmax();
    
    def play(self, k):
        #when choose the k ,what happened
        if(np.random.rand() < self.probs[k]):
            return 1;
        else:
            return 0;


class Solver():
    def __init__(self, bandit):
        self.bandit = bandit;
        #进行记录, 每次的行动, 以及遗憾.
        self.count = np.zeros(self.bandit.k);
        self.regret = 0;
        self.actions = [];
        self.regrets = [];
    
    def update_regrets_actions(self, k):
        # update the regrets, and reurn if win
        self.regret += (self.bandit.best_prob - self.bandit.probs[k]);
        self.regrets.append(self.regret);
        self.actions.append(k);
        self.count[k] +=1 ;
        #return self.bandit.step(k);

    
    def run_one_step():
        #choose a bandit k
        return -1;
    
    def run(self, num_steps):
        for i in range(0, num_steps):
            action = self.run_one_step();
            self.update_regrets_actions(action);
            #self.count[action] += 1;


class EGreedy(Solver):
    #某个算法具体的实现,
    def __init__(self, bandit, epsilon = 0.01, init_prob= 1.0):
        super().__init__(bandit);
        self.epsilon = epsilon;
        self.estimates = np.array([init_prob] * self.bandit.k);
        self.name = "EGreedy";
    
    def run_one_step(self):
        #choose a k ,and updata the estimates
        #随机 or 经验
        if(np.random.random() < self.epsilon):
            #随机
            k = np.random.randint(0, self.bandit.k);
        else:
            #经验
            k = np.argmax(self.estimates);
        
        r = self.bandit.play(k);
        #self.count[k] += 1;
        self.estimates[k] += 1. / (self.count[k]+1) * (r - self.estimates[k]);
        #print(self.estimates)

        return k;
        

def picshow(solvers):
    for solver in solvers :
        time = len(solver.regrets)
        #print(time)
        time_list = range(time);
        plt.plot(time_list, solver.regrets, label = solver.name);
    
    plt.xlabel("time steps");
    plt.ylabel('regrets')
    
    #show the label
    plt.legend();
    plt.show()






if __name__ == '__main__':
    np.random.seed(2);
    K = 10;
    bandit = Bandit(10);

    egreedy = EGreedy(bandit)
    egreedy.run(5000);

    picshow([egreedy]);
    #print(bandit.best_prob);
    #print(egreedy.actions)
    print(egreedy.estimates)
    print(egreedy.regret)

    #print(np.random.random(50))
