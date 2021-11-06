import gym
from gym import spaces
import numpy as np

class BaseEnv(gym.Env):
    """Custom Environment that follows gym interface"""
    def __init__(self,reads,genome):
        super(BaseEnv, self).__init__()

        self.reads = reads
        self.reads_p = [str(index)+":"+read for index,read in enumerate(self.reads)]
        self.genes = "TAATGCCA"
        self.kmers = len(self.reads[0])
        self.overlap_length = self.kmers-1
        N_DISCRETE_ACTIONS = len(self.reads)
        self.action_space = spaces.Discrete(N_DISCRETE_ACTIONS)
        self.observation_space = spaces.Box(low=0, high=1,
                                            shape=(N_DISCRETE_ACTIONS+1,), dtype=np.uint8)

        self.last_mer = ""
        self.constructed_string = ""
        self.state = []
        self.map = {'A':0,'T':1,'C':2,'G':3}
        self.inverse_map = {0:'A',1:'T',2:'C',3:'G'}
        self.max = len(self.reads)
        self.count = 0

    def step(self, action):
        
        if action>=len(self.reads) or action<0:
            reward = len(self.state)
            done = True
            return self.state,reward,done,{"DNA":self.constructed_string}

        self.count += 1

        if not len(self.state):
            self.last_mer=self.reads[action]
            self.constructed_string = self.last_mer
            self.state = np.zeros(len(self.reads)+1)
            self.state[0]=action
            self.state[action+1]=0
            info = {"DNA":self.constructed_string}
            return self.state,0,False,info  

        s = self.last_mer

        if not self.overlap(s,self.reads[action]):
            reward = len(self.constructed_string)
            done = True
        else:
            self.state[0] = action
            self.state[action+1] = 0
            self.last_mer = self.reads[action]
            self.constructed_string = self.constructed_string+self.reads[action][-1]
            reward = 0
            done = False

        info = {"DNA":self.constructed_string}
        observation = self.state
        if self.count == self.max:
            done = True
            reward = len(self.constructed_string)

        return observation, reward, done, info

    def overlap(self,first,second):
        if first[1:]==second[:-1]:
            return True
        return False

    def reset(self):
        self.last_mer = ""
        self.state = []
        self.count = 0
        return self.state # reward, done, info can't be included

    def render(self, mode='human'):
        pass

    def close(self):
        return 0

class dataset_1(BaseEnv):
    def __init__(self):
        reads = ["TAA","AAT","ATG","TGC","GCC","CCA"]
        genome = "TAATGCCA"
        super().__init__(reads,genome)
    

