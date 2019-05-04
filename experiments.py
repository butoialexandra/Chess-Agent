import numpy as np
import pickle
import matplotlib.pyplot as plt

def show_sarsa(rewards):
    plt.plot(np.arange(rewards.size), rewards)
    plt.title('Rewards per episode')
    plt.ylabel('Reward')
    plt.xlabel('Episode number')


if __name__ == '__main__':
    with open('sarsa_first_try.pickle', 'rb') as file:
        rewards = pickle.load(file)
        show_sarsa(rewards)
