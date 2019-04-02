import gym
import numpy

env = gym.make('FrozenLake-v0')

def f(position):
    dic = {
        0: 1,
        1: 2,
        2: 1,
        3: 0,
        4: 1,
        5: 1,
        6: 1,
        7: 0,
        8: 2,
        9: 2,
        10: 1,
        11: 0,
        12: 2,
        13: 2,
        14: 2, 
    }

    return dic[position]
""" 
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3

SFFF
FHFH
FFFH
HFFG

"""
def h(position):
    dic = {
        0: [1, 1, 2, 2, 1, 2],
        1: [2, 1, 1, 1, 2],
        2: [1, 1, 1, 2],
        3: [0, 1, 1, 1, 2],
        4: [1, 2, 2, 1, 2],
        5: [2, 1, 1, 2],
        6: [1, 1, 2],
        7: [0, 1, 1, 2],
        8: [2, 2, 1, 2],
        9: [2, 1, 2],
        10:[1, 2],
        11:[0, 1, 2],
        12:[2, 2, 2],
        13:[2, 2],
        14:[2], 
    }

    return dic[position]

def k(position, a):
    if a >= 0.5:
        return f(position)
    else:
        return h(position)

r = {}
for a in numpy.arange(0, 1.1, 0.1):
    a = round(a, 2)
    number_of_success = 0
    for i in range(1000):
        observation = env.reset()
        action_to_do = k(observation, a)
        
        if type(action_to_do) == list:
            for step in action_to_do:
                observation, reward, done, info = env.step(step)
                if done:
                    if reward:
                        number_of_success = number_of_success + 1
                    break
        else:
            done = False
            while done == False: 
                observation, reward, done, info = env.step(action_to_do)
                if reward:
                    number_of_success = number_of_success + 1
    r[a] = number_of_success

for key, value in r.items():
    print(key, value)
