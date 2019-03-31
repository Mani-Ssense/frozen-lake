import gym

env = gym.make('FrozenLake-v0')

def f(pos):
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

    return dic[pos]

number_of_reaching_goal = 0
for i_episode in range(1000):
    observation = env.reset()
    done = False
    while done == False: 
        observation, reward, done, info = env.step(f(observation))
        if reward:
            number_of_reaching_goal = number_of_reaching_goal + 1
        env.render()

print(number_of_reaching_goal)
print('success rate %:', (number_of_reaching_goal / 1000) * 100)
