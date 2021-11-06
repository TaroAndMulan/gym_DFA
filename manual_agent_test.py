import gym

env = gym.make('gym_DFA:dataset_1-v1')
obs = env.reset()
info ={"DNA":""}
print ("--------------- manual AGENT mode ---------------")
print ("reads :"+str(env.reads))
print (r"solution sequence=[0,1,2,3,4,5] --> TAATGCCA")
print ("-------------------------------------------------")
i = 0
seq = ""
while True:
    i+=1
    print ("step {}".format(i)) 
    print ("list of action:{}".format(env.reads_p))
    print ("action(select which base append)",end=":")
    action = int(input())
        
    obs, reward, done, info = env.step(action)
    print ("Dna sequence -> {}".format(info["DNA"]))
    # Render the game
    if done == True:
        print ("")
        print ("**************************************")
        print ("FINAL_Dna_sequence = {}".format(info["DNA"]))
        print ("score = {}".format(reward))

        break

env.close()