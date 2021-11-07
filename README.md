# OpenAI Gym Environments: gym_DFA

## Description:
Each environment contain a set of reads to be assembled. 
```bash
#dataset_1 example
reads = [TAA,AAC,ACG] 
Your task is to implement an agent that can assemble these reads into "TAACG"
```
## Observation:
will be added once the final design is finalized		


## Actions:

Type: *Discrete( number of reads )*
```bash
reads = ["TAA","AAC","ACG"]
"TAA" correspond to action 0
"ACG" correspond to action 2
```

## Reward:

Rewards is 0 for all non terminal step (no immediate reward, what matter is the final DNA only)

At the end of episode (terminal state), the score is given base on the length of the assembled DNA.

```bash
reads = ["TAA","AAC","ACG"]
action = 0,1,2    ----> TAA AAC ACG ----> "TAACG" ---> score=5
action = 1,2      ----> AAC ACG ----> "AACG" ---> score=4
```
Your task is to implement an agent that choose a sequeunce of optimal action that receive the highest score (best DNA sequence) 
## Episode Termination:

Episodes terminate when 

1. agent perform invalid action (repeat the same read/pick read that does not overlap correctly)
2. agent exhausts all available option (use all reads)

## List of environments:

more dataset will be add in later version


Genome size | Number of reads | Read length | Env. name (v1) | 
------------ | ------------- | ------------- | ------------- | 
8 | 6 | 3 | dataset_1| 


## Get started

### Installation

```bash
$ pip install gym
$ git clone https://github.com/taroandmulan/gym_DFA
$ cd gym_DFA
$ pip install -e .
```


### how to use
for someone who are new to openAI gym, read this first https://gym.openai.com/docs/
```python
import gym

env = gym.make("gym_DFA:dataset_1-v1")
# implement your agent here
```
### manual agent support 
use user input (keyboard) to manually choose action
```bash
python manual_agent_test.py
# use keyboard to select action at each time step 
```

