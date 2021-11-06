# OpenAI Gym Environments: gym_DFA

## Description:
Each environment contain a set of reads to be assembled. 
for example
reads = [TAA,AAC,ACG] must be assembled into "TAACG"
## Observation:
will be added once the implementation is finalized

		


## Actions:

Type: *Discrete( number of reads )*

example

reads = ["TAA","AAC","ACG"]

if you wish to append with "TAA" then choose action 0

if you wish to append with "ACG" then choose action 2


## Reward:

Rewards is 0 for all step except the terminal step

At the terminal state, the reward is given base on the length of the constructed DNA

## Episode Termination:

Episodes terminate when 

1. agent perform invalid action (repeat the same read/pick read that does not overlap with the current constructed DNA string)
2. 
3. 

## List of environments:

Genome size | Number of reads | Read length | Env. name (v1) | 
------------ | ------------- | ------------- | ------------- | 
8 | 6 | 3 | dataset_1| 


## Get started

### Installation

```bash
$ pip install gym
$ git clone https://github.com/taroandmulan/gym_DFA.git
$ cd gym_DFA
$ pip install -e .
```


### how to use
for someone who are new to openAI gym, read this first https://gym.openai.com/docs/
```python
import gym

env = gym.make('gym_DFA_v1:dataset_1')
# more dataset will be add in later version) 
# implement your agent here
```

