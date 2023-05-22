import qLearning
import gameGrid as game

epsilon = 0.4
gamma = 0.99
alpha = 0.1

print("\n----------------------------")
print("Simple MDP")
print("----------------------------\n")

# print the MDP model éléments S,A,T,R
print("\n----------------------------")
print("START MDP model")
print("----------------------------\n")

# print model set of states S
print("STATES S : \n" + str(game.states))
# print model set of actions A
print("\nACTIONS A : \n" + str(game.actions))
# print model transition function T(s,a,s')
print("\nTRANSITION FUNCTION :")
for s in game.states:
    for a in game.actions:
        print("start state = " + s + ", action = " + a + ", next_states = " + str(game.transitions(s,a)))
# print model reward function R(s,a)
print("\nREWARD FUNCTION :")
for s in game.states:
    for a in game.actions:
        print("start state = " + s + ", action = " + a + ", reward = " + str(game.rewards(s,a)))
        
print("\n----------------------------")
print("END MDP model")
print("----------------------------\n")

# Run Q-Learning
print("\n----------------------------")
print("LEARNING THE Q TABLE")
print("----------------------------\n")
q_table, epochs, penalties = qLearning.q_train(game.states, game.actions, game.transitions, game.rewards, game.isEnd, epsilon, gamma, alpha, "s0")

# Run a complete episode from initial state to end state
print("\n----------------------------")
print("POLICY À PARTIR DE S0")
print("----------------------------\n")
qLearning.play_episode("s0", game.isEnd, q_table, game.transitions, game.rewards, gamma, alpha)
print("\n----------------------------")
print("POLICY À PARTIR DE S20")
print("----------------------------\n")
qLearning.play_episode("s20", game.isEnd, q_table, game.transitions, game.rewards, gamma, alpha)