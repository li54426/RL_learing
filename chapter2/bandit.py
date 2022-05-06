import numpy as np
import matplotlib.pyplot as plt

class Bandit:
    #K臂老虎机
    #属性 probs, bext_index
    #method : choose(k) 
    def __init__(self, K):
        #K problities
        self.probs = np.random.uniform(size = K);
        self.best_prob = probs.max();
        self.best_index = probs.argmax();
    
    def steps(self, k):
        #when choose the k ,what happened
        if(np.random.rand() < self.probs[k-1]):
            return 0;
        else:
            return 1;

np.random.seed(1);
K = 10;
bandit = Bandit(10);



#print(type(bandit))
print("the bandit probs is");
print(bandit.probs);

print("the best index is");
print(bandit.best_index);

print("the best prob is");
print(bandit.best_prob);
