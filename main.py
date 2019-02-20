import numpy as np
import gym
import sys
from collections import deque,defaultdict
import math
from agent import Agent
from tasks import train_agent, render
import os
import time
taxi_env = gym.make("Taxi-v2")
taxi_env.render()

# Action space
nA = taxi_env.action_space.n
nS = taxi_env.observation_space.n
#nA,nS
taxi_env.reset()
    
# Create an agent 
taxi_agent = Agent(nA, nS)

x=train_agent(taxi_agent, taxi_env, n_episodes=1000)
      
#x=train_agent(taxi_agent, taxi_env, n_episodes=100)
#render(taxi_env, taxi_agent)
#time.sleep(3)
#x=train_agent(taxi_agent, taxi_env, n_episodes=300)
#render(taxi_env, taxi_agent)
#time.sleep(3)
#x=train_agent(taxi_agent, taxi_env, n_episodes=400)
#render(taxi_env, taxi_agent)
print("\n--Developed by Pavan Yekabote :)\n\n")

