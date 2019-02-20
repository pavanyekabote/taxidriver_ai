import numpy as np
import gym
import sys
from collections import deque,defaultdict
import math
class Agent:
  
  def __init__(self, nA, nS, alpha=0.7, gamma= 0.6):
    self.nA = nA
    self.nS = nS
    self.Q =  defaultdict(lambda: np.zeros(self.nA))
    self.n_iteration = 1
    #learning_rate
    self.alpha = alpha
    self.gamma = gamma
    self.action_iteration = 1
    pass
  
  def update_iteration(self):
    self.n_iteration += 1
    pass
  
  def choose_action(self, state):
    policy = self.get_epsilon_greedy_policy(state)
    action = np.random.choice(np.arange(self.nA), p=policy)
    self.action_iteration+=0.01
    return action
  
  def update_Q(self,state, action, next_state, reward):
    alpha = self.alpha
    gamma = self.gamma
    policy = self.get_epsilon_greedy_policy(next_state)
    self.Q[state][action] += alpha * ( reward + gamma * np.dot(self.Q[next_state], policy) - self.Q[state][action])
    pass
  
  def get_epsilon_greedy_policy(self,state, epsilon=None):
    eps = 1/(self.n_iteration + self.action_iteration)
    if epsilon is not None:
      eps = epsilon
    
    policy = np.ones(self.nA) * eps / self.nA
    policy[np.argmax(self.Q[state])] = 1 - eps + ( eps / self.nA )
    return policy
    
