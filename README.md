# DFS OPTIMIZER

Uses player and team statistics with DraftKings salary information to assist DFS players with lineup construction.

---

## Getting Started

These instructions will get you a copy of the project up and running on your local machine

### Cloning

- Clone this repository to your local machine using https://github.com/fwang084/DFS_Optimizer

### Setup

> Install pip

```shell
$ easy_install pip
```

> Install BeautifulSoup

```shell
$ pip install BeautifulSoup4
```

> Install requests library

```shell
$ pip install requests
```

> Install xlrd module

```shell
$ pip install xlrd
```
---
## Contributing

### Step 1

- **Option 1**
    - 🍴 Fork this repo!

- **Option 2**
    - 👯 Clone this repo to your local machine using `https://github.com/fwang084/DFS_Optimizer.git`

### Step 2

- **HACK AWAY!** 🔨🔨🔨

### Step 3

- 🔃 Create a new pull request using <a href="https://github.com/fwang084/DFS_Optimizer/compare/" target="_blank">`https://github.com/fwang084/DFS_Optimizer/compare/`</a>.

---

## FAQ

- **How should the optimal_lineup function in Calculate be used?**
    - First, decide which players are "locked in", meaning that they must be included. Pass in a player list and a list that represents a lineup, with locked players represented by their name as a string in the appropriate position in the lineup. An example is given in lines 150-152 of Calculate.py .

- **How long does the optimal_lineup function take?**
    - The algorithm takes significantly shorter time if many locked players are provided. Otherwise, there are too many cases, and the program's runtime will be too long. Depending on how big the player pool is on a day, increasing the number of locked players or filtering the player list before passing it into optimal_lineup can reduce runtime to an adequate time.
    
- **What do I do if I want find_best_value() to return more or less than 40 players?**
    - 40 works well for me, but simply change the number after LIMIT within the find_best_value function if you want a different number of players.

---

## Support

- Contact me at frankw084@berkeley.edu
