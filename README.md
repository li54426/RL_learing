##强化学习路径 笔记 代码

#### 简介

强化学习有两大类基于 值 和基于 策略 , 在强化学习里面，优化的目标是**策略**（Policy）

- 首先介绍基于值的强化学习，基于值的强化学习的典型代表为**Q-learning**和**SARSA**，前者是异策略（Off-Policy），后者是同策略（On-Policy）的
- 若 P, R 已知则为基于模型的强化学习, 否则是无模型的强化学习
- 智能体-----进行学习和实施决策的机器
- 环境-----除了智能体之外所有与之相互作用的事物
- 如果我们需要智能体为我们做某件事, 我们提供收益的方式必须要使智能体在最大化收益的同时也实现我们的目标. 收益信号只能用来传达**什么是**你想实现的目标, 而不是**如何实现**这个目标



###第二章 老虎机(已完成)

Notes : 

- 可以先写一个虚类算法, 比如老虎机中所有的算法只有一个run_one_step不同, 其他相同,可以先写一个虚类来完成整体框架
- 为什么是概率是小于 eg. p =0.6, random() < p的解释是从0到p 的概率刚好为p

###第三章 马尔科夫决策过程(未完待续)
Q: 马尔科夫过程和隐含马尔科夫过程有什么不同. 建议看一下机器学习的视频

- 马尔可夫性 : 某时刻的状态只取决于上一时刻的状态时,, t时刻的状态包含了 t-1 时刻的状态信息.

- 马尔可夫过程: 状态S , 状态转移矩阵P
    状态转移矩阵 : a_ij 从 i -> j 状态转移, 也就是每一行和为1,

- 马尔可夫奖励过程: S P r(奖励函数) gamme(折扣因子)

    回报 (G_t): 从 t 开始, 到终止状态时, 所有奖励衰减的和.

    价值 : 一个状态的期望回报

    贝尔曼方程 :　V = R + gamma* P V　

- 马尔可夫决策过程(MDP) : S, A, gamma, r(s, a)  P(s | s,a)

- $$
    Q(s, a)=E\left[\sum_{t} \gamma^{t} r_{t} \mid (s, a)\right]
    $$

- $$
    Q(s, a)=\sum_{s^{\prime}} p\left(s^{\prime} \mid s, a\right)\left(R(s, a)+V\left(s^{\prime}\right)\right)
    $$

- $$
    V(s)=\sum_{a} \pi(a \mid s) Q(s, a)
    $$

- 

- $$
    \begin{aligned}
    V^{\pi}(s) &=\mathbb{E}_{\pi}\left[R_{t}+\gamma V^{\pi}\left(S_{t+1}\right) \mid S_{t}=s\right] \\
    &=\sum_{a \in A} \pi(a \mid s)\left(r(s, a)+\gamma \sum_{s^{\prime} \in S} p\left(s^{\prime} \mid s, a\right) V^{\pi}\left(s^{\prime}\right)\right)
    \end{aligned}
    $$

#### 蒙特卡洛方法

每个实例中进行更新
$$
\begin{aligned}
&N(s) \leftarrow N(s)+1 \\
&V(s) \leftarrow V(s)+\frac{1}{N(s)}(G-V(S))
\end{aligned}
$$

###第四章 动态规划算法

核心

- 贝尔曼期望方程
- $\begin{aligned}
    V^{\pi}(s) =\sum_{a \in A} \pi(a \mid s)\left(r(s, a)+\gamma \sum_{s^{\prime} \in S} p\left(s^{\prime} \mid s, a\right) V^{\pi}\left(s^{\prime}\right)\right)
    \end{aligned}$

- 动态规划方式求解
- $V^{k+1}(s)=\sum_{a \in A} \pi(a \mid s)\left(r(s, a)+\gamma \sum_{s^{\prime} \in S} P\left(s^{\prime} \mid s, a\right) V^{k}\left(s^{\prime}\right)\right)$



### 第五章 时序差分算法

- 定义: 大部分强化学习的场景中, 状态转移概率是无法写出来的, 因此, 只能通过智能体和环境交互进行采样来学习, 

- 两大经典算法 : Sarsa    Q-learning

- 时序差分的思想: 

- $$
    V\left(S_{t}\right) \leftarrow V\left(S_{t}\right)+\alpha\left(R_{t+1}+\gamma V\left(S_{t+1}\right)-V\left(S_{t}\right)\right)
    $$

####  Sarsa

$$
Q\left(s_{t}, a_{t}\right) \leftarrow Q\left(s_{t}, a_{t}\right)+\alpha\left[r_{t}+\gamma Q\left(s_{t+1}, a_{t+1}\right)-Q\left(s_{t}, a_{t}\right)\right]
$$

根据s0, 选出回报最大的a0, 得到r, 然后根据a得到下一个状态s1, 再选出最大的a1, 根据  这五个参数更新Q-table

#### Q-learning

$$
Q\left(s_{t}, a_{t}\right) \leftarrow Q\left(s_{t}, a_{t}\right)+\alpha\left[R_{t}+\gamma \max _{a} Q\left(s_{t+1}, a\right)-Q\left(s_{t}, a_{t}\right)\right]
$$

Sarsa 必须使用当前-贪婪策略采样得到的数据, 而Q-learning则可以不用

#### question

需要注意的是，打印出来的回报是行为策略在环境中交互得到的，而不是 Q-learning 算法在学习的目标策略的真实回报。我们把目标策略的行为打印出来后，发现其更偏向于走在悬崖边上，这与 Sarsa 算法得到的比较保守的策略相比是更优的。 但是仔细观察 Sarsa 和 Q-learning 在训练过程中的回报曲线图，我们可以发现，在一个序列中 Sarsa 获得的期望回报是高于 Q-learning 的。这是因为在训练过程中智能体采取基于当前函数的-贪婪策略来平衡探索与利用，Q-learning 算法由于沿着悬崖边走，会以一定概率探索“掉入悬崖”这一动作，而 Sarsa 相对保守的路线使智能体几乎不可能掉入悬崖。



### 第六章 Dyna -Q

- 环境的模型---- 智能体可以用来预测环境对其动作的反应的实物

- 基于模型的强化学习 : 环境模型是通过采样数据获得的

- 

- ```
    Initialize Q(s,a)and Model(s,a)
    Loop forever:
        (a)S  <-   current(nonterminal)state
        (b)A←e-greedy(S,Q)
        (c)Take action A;observe resultant reward,R,and state,S'
        (d)Q(S,A)   Q(S,A)+a[R+ymaxa Q(S',a)-Q(S,A)]    Direct RL
        (e)Model(S,A)  <-   R,S'(assuming deterministic environment)   model learning
        (f)Loop repeat n times:    planning 
            S   random previously observed state 
            A   random action previously taken in S 
            R,S←Model(S,A)
            Q(S,A)Q(S,A)+a R+ymaxa Q(S',a)-Q(S,A)
    ```

- 



### DQN

用神经网络来表示 Q 函数,

- 若动作是连续的, 输入是状态 s 和动作 a , 输出是标量
- 若动作是离散的, 输入为 s , 输出是每个动作 a 的值
- 

### 拓展1 : 隐马尔可夫模型

一个HMM由(π, A, B)组成

- π是状态先验概率,
- A 是状态转移矩阵, a_ij 是 从状态 si 到 sj
- B = $ b_{ij }$ 是指 状态si 时,  观测值为 $O_j$ 的概率 

经典的隐含马尔可夫模型的案例
	一共有N个袋子, 每个袋子里面有M种不同的球, 先选袋子再选球, 得到球的颜色. 

三种问题:

一旦一个系统可以作为 HMM 被描述，就可以用来解决三个基本问题。

- 评估（Evaluation)

    给定 HMM, 求某个观察序列的概率。

- 解码

    求隐含状态的概率

- 学习

    给定观察序列, 得到一个隐含马尔可夫模型.

两种方法:

- 前向计算 : 评估问题 
    	定义 : α_t(i) = P(O, Si)   到 t 时刻, 观测为O, 状态为 Si, 每列的和为P(O)
    	初始化 : π(i) * b io
    	前向计算 $α _t (j) = ( \sum α_i(i) a_{ij}) *b_{jo} $

- P(O) = \sum α t (i)

- ![img](https://pic3.zhimg.com/v2-c7bd94a7917e521f28fa08418e481f32_r.jpg)

- 维特比算法: 解码问题 使P(S | O) 最大 

    P(S | O) = P(O , S) / P( O ) = P(O, S) 

定义β t (i) 是 t 时刻状态为 Si ,并且观测为 Ot, O t+1,,,OT的概率 



















