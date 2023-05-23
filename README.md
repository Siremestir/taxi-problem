# The taxi problem

**authors**: Swan Sauvegrain and Astrid Djouhassi

**license**: Free to use, copy, modify and distribute

**version**: 1.1

## Introduction

This project aims to modelize the taxi problem and solve it using reinforcement learning.
Current implementation only allows for one passenger.

## Code structure

All relevant code is contained in the following python files.

 - **gameGrid**: Problem modelization. Contains the state space, the action space, the transition function, the rewards function, and the isEnd function.
 - **qLearning**: Heart of the code, contains all of the utils and main functions for training and solivng the problem.
 - **main-Q**: Main script, with all parameters. Calls the functions in qLearning.py in order.

main-VI.py and valueIteration.py are only here as debug tools, to confirm the modelization is correct and find the optimal policy when a human cannot.

## How to use

Configure the problem in the config.json file.
The passenger and the walls are configured with indexes.
The indexes start at 0 in the top right corner and follows the english reading , incrementing from left to right and top to bottom.
For example, a 3x2 grid will have these indexes:
|   |   |   |
|---|---|---|
| 1 \|| 2 \|| 3 |
| 4 \|| 5 \|| 6 |

To configure vertical walls, indicate the index of the case at the right of the wall with the value "right". Similarly, to configure horizontal walls, indicate the index of the case above the wall with the value "down".

To execute the main program, use the following command:
``python3 main-Q.py``