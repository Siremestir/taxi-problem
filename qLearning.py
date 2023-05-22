import random

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


def step(state, action, transitions, rewards, is_end):
    next_state = random_pick(transitions(state, action))
    done = is_end(next_state)
    reward = rewards(state, action)
    return next_state, reward, done


def q_train(states, actions, transitions, rewards, is_end, epsilon, gamma, alpha, origin):
    # initialise the value function to 0 for all states and actions
    q_table = {s:{ a:0.0 for a in actions} for s in states}
    # For plotting metrics
    all_epochs = []
    all_penalties = []

    for i in range(1, 201):
        state = origin

        epochs, penalties, reward = 0, 0, 0
        done = False
        
        while not done:
            if random.uniform(0, 1) < epsilon:
                action = random.choice(actions) # Explore action space
            else:
                action = max(q_table[state], key=q_table[state].get) # Exploit learned values

            next_state, reward, done = step(state, action, transitions, rewards, is_end) 
            
            old_value = q_table[state][action]
            next_max = q_table[next_state][max(q_table[next_state], key=q_table[next_state].get)]
            
            new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
            q_table[state][action] = new_value

            if reward == -10:
                penalties += 1

            state = next_state
            epochs += 1
            
        if i % 100 == 0:
            print(f"Episode: {i}")

        all_epochs.append(epochs)
        all_penalties.append(penalties)

    print("Training finished.\n")
    return q_table, all_epochs, all_penalties


def play_episode(origin, is_end, q_table, transitions, rewards, gamma, alpha):
    state = origin

    epochs, penalties = 0, 0
    done = False
    
    while not done:
        action = max(q_table[state], key=q_table[state].get) # Exploit learned values

        next_state, reward, done = step(state, action, transitions, rewards, is_end) 
        
        old_value = q_table[state][action]
        next_max = q_table[next_state][max(q_table[next_state], key=q_table[next_state].get)]
        
        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state][action] = new_value
        # print(old_value, new_value)

        if reward == -10:
            penalties += 1

        print("state = %s, action = %s, next_state = %s" % (state, action, next_state))
        state = next_state
        epochs += 1

    print("Episode end. %i epochs, %i penalties." % (epochs, penalties))