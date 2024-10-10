import torch
import torch.nn.functional as F
from torch import nn 

import matplotlib.pyplot as plt

import numpy as np

from tqdm import tqdm

import gym


#定义网络
class Net(torch.nn.module):
    def __init__(self, n_state, n_hidden, n_action):
        super().__init__()
        self.line1 = nn.Linear(n_state, n_hidden)
        self.line2 = nn.Linear(n_hidden, n_action)

    def forward(self, x):
        x = self.line1(x)
        x = F.relu(x)

        x = self.line2(x)
        x = F.relu(x)
        return x





if __name__ == '__main__':
    