
import numpy as np
import gym
import sys
from collections import deque,defaultdict
import math
import os
import time
def train_agent(agent, env, n_episodes = 1000):
  
  sample_rewards = deque(maxlen=100)
  #avg_rewards = deque(maxlen = n_episodes)
  best_avg_reward = -math.inf
  
  for i_episode in range(n_episodes+1):
    if i_episode % 100 == 0:
      print("\rEpisode {}/{}".format(i_episode, n_episodes), end="")
      sys.stdout.flush()
    
    samp_reward = 0
    # take an initial state
    state = env.reset()
    while True:
      #Choose an action based on state
      action = agent.choose_action(state)
      
      #Perform action on environment
      next_state, reward, done, info = env.step(action)
    
      samp_reward += reward
      
      #Update Q to make agent learn
      agent.update_Q(state, action, next_state, reward)
      
      state = next_state
      
      if done: 
        sample_rewards.append(samp_reward)
        if i_episode%100 == 0:
          print("Episode {} Finished :) ".format(i_episode))
          time.sleep(3)
        break
      if i_episode % 100 ==0:
        render(env)
    
    if(i_episode >= 100):
      avg_reward = np.mean(sample_rewards)
      #avg_rewards.append(avg_reward)
      if avg_reward > best_avg_reward:
        best_avg_reward = avg_reward
      print("\rTraining agent to drive Episode {}/{} || Best average reward {}".format(i_episode, n_episodes, best_avg_reward), end="")
      sys.stdout.flush()
      
    agent.update_iteration()
  return agent, best_avg_reward
  
def test_agent(agent, env, n_episodes=1):
  
  for i_episode in range(n_episodes):
    state = env.reset()
    while True:
      action = agent.choose_action(state)
      next_state, reward, done, info = env.step(action)
      state = next_state
      env.render()
      if done:
        break
      
def play_game_render(env, agent):
    state = env.reset()
    while True:
        a = agent.choose_action(state)
        os.system('clear')
        next_state, reward, done, info = env.step(a)
        state = next_state
        env.render()
        time.sleep(0.5)
        if done:
            break
    
def render(env):
  env.render()
  time.sleep(0.09)
  os.system('clear')