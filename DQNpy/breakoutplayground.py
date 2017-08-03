import gym
import numpy as np
from matplotlib import pyplot as plt

env = gym.envs.make("Breakout-v0")
#env = gym.envs.make("LunarLander-v2")

print("Action space size: {}".format(env.action_space.n))
#print(env.get_action_meanings())
print(env.unwrapped.get_action_meanings())

env.reset()
#plt.figure()
for ii in range(100):
    env.step(0)
    plt.clf()
#    plt.imshow(env.render(mode='rgb_array'))
    plt.imshow(env.render(mode = 'rgb_array'))
#[env.step(2) for x in range(10000000)]



# observation = env.reset()
# print("Observation space shape: {}".format(observation.shape))

# plt.figure()
# plt.imshow(env.render(mode='rgb_array'))

# [env.step(2) for x in range(1)]
# plt.figure()
# plt.imshow(env.render(mode='rgb_array'))

# env.render(close=True)
# plt.imshow(observation[34:-16,:,:])


