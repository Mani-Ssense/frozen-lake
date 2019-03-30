import gym

env = gym.make('FrozenLake-v0')

print('reseting the env...')
observation = env.reset()
print('observation:', observation)
print('initial state is:')
env.render()
print('---------------------start moving-------------------------------')
'''
LEFT = 0
DOWN = 1
RIGHT = 2
UP = 3
'''
# do:
# DOWN, DOWN, RIGHT, RIGHT, DOWN, RIGHT
steps = [1, 1, 2, 2, 1, 2]
number_of_reaching_goal = 0
for i_episode in range(1000):
    observation = env.reset()

    for step in steps:
        print('step:' , step)
        observation, reward, done, info = env.step(step)
        print('observation', observation)
        print('reward', reward)
        print('done', done)
        print('info', info)
        #env.render()
        print('---------------------------------------')
        if done:
            if reward:
                print('success')
                number_of_reaching_goal = number_of_reaching_goal + 1
            break

env.close()
print(number_of_reaching_goal)
print('success rate %:', (number_of_reaching_goal / 1000)* 100) 