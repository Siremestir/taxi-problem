import random    

# The value iteration algorithm to calulate the value function for each state
def valueIteration(states, actions, transitions, rewards, epsilon, gamma):
    # delta to mesure the difference between state values in precedent and current function
    delta=1
    # initialise the value function to 0 for all states
    V= { s:0.0 for s in states}
    i= 1
    # value iteration loop with stop condition  delta < epsilon
    while delta >= epsilon:
        temp_delta = 0
        previous_iteration = V.copy()
        for state in states:
            previous_value = previous_iteration[state]
            best_action, best_value = pi(state, actions, transitions, rewards, gamma, previous_iteration)
            V[state] = best_value

            new_delta = abs(previous_value - best_value)
            if temp_delta < new_delta:
                temp_delta = new_delta


        delta = temp_delta
        print("Values (it_%i) %s ; delta : %s" % (i, str(V), str(delta)))
        i += 1
    
    return V


def pi(state, actions, transitions, rewards, gamma, previous_iteration):
    action_values = dict()
    for action in actions:
        reward = rewards(state, action)
        transition_dict = transitions(state, action)
        t_sum = 0
        for transition in transition_dict:
            probability = transition_dict[transition]
            s_prime = previous_iteration[transition]
            t_sum += probability * s_prime
        
        value = reward + gamma * t_sum
        action_values[action] = value
        
    best_action = max(action_values, key=action_values.get)
    best_value = action_values[best_action]
    return best_action, best_value


def random_pick(states):
    organized_states = dict()
    n = 0
    for key in states:
        n += states[key]
        organized_states[key] = n

    r = random.random()
    res = None
    for key in organized_states:
        if r < organized_states[key]:
            if res is None or organized_states[key] < organized_states[res]:
                res = key

    return res


def playEpisode(state, is_end, vi, actions, transitions, rewards, gamma):
    while not is_end(state):
        best_action, best_value = pi(state, actions, transitions, rewards, gamma, vi)
        next_state = random_pick(transitions(state, best_action))
        print("state = %s, action = %s, next_state = %s" % (state, best_action, next_state))
        state = next_state