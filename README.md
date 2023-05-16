# The taxi problem

**authors**: Swan Sauvegrain and Astrid Djouhassi

**license**: Free to use, copy, modify and distribute

**version**: 1.0

## Introduction

This project aims to modelize the taxi problem and solve it using renforcement learning.
Current implementation only allows for one passenger.

## How to use

Configure the problem in the config.json file.
The passenger and the walls are configured with index.
The indexes start at 0 in the top right corner and follows the english reading , incrementing from left to right and top to bottom.
For example, a 3x2 grid will have these indexes:
|   |   |   |
|---|---|---|
| 1 \|| 2 \|| 3 |
| 4 \|| 5 \|| 6 |

To configure vertical walls, indicate the index of the case at the right of the wall with the value "right". Similarly, to configure horizontal walls, indicate the index of the case above the wall with the value "down".