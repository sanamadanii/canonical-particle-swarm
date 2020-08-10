
# coding: utf-8

# In[28]:


import random
import math
import numpy as np
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

np.random.seed(123)
np.random.rand()


# In[29]:


def individual(x1_max,x1_min,x2_max,x2_min):
    indv=[]
    x=random.uniform(x1_min,x1_max)
    indv.append(x)
    y=random.uniform(x2_min,x2_max)
    indv.append(y)
    return indv

print(individual(3,-2,1,-2))


# In[30]:


def init_pop(popSize,x1_max,x1_min,x2_max,x2_min):
    return [individual(x1_max,x1_min,x2_max,x2_min) for x in range(popSize)]



# In[31]:


pop=init_pop(50,3,-2,1,-2)
print(pop)


# In[32]:


def fitness(particle):
    
    fit = math.sin(2*particle[0]-0.5*math.pi)+3*math.cos(particle[1])+0.5*particle[0]
    
    return fit



# In[33]:


print(fitness(pop[0]))


# In[34]:


def updateVelocity(particle,pbest,pg,vMax,c1,c2):
    Nv=[]
    for j in range(len(particle)):
        randVar1= np.random.rand()
        randVar2= np.random.rand()
        newv=vMax[j]+randVar1*c1*(pbest-particle[j])+randVar2*c2*(pg-particle[j])
        if newv>=1 :
            newv=1
        elif newv< -0.1 :
            newv=-0.1
        particle[j]=particle[j]+newv
        Nv.append(newv)
    return particle,Nv
print(updateVelocity([-1.7304230354706378, 0.3577235274424897],2.8943475073639684, 4.589116383082064,[-0.1,1],2,2)[0])


# In[35]:


def PSO(popSize,x1_min,x1_max,x2_min,x2_max,numofiteration,c1=2,c2=2):
    pop=init_pop(popSize,x1_max,x1_min,x2_max,x2_min)
    Fitness=[]
    for i in range(len(pop)):
        fit=fitness(pop[i])
        Fitness.append(fit)
    pbest=Fitness
    final_particles=[]
    vMax=[]
    final_particles.append(pop)
    for i in range(len(pop)):
        temp=[]
        v1=random.uniform(-0.1,1)
        v2=random.uniform(-0.1,1)
        temp.append(v1)
        temp.append(v2)
        vMax.append(temp)
    for i in range(numofiteration):
        newpop=[]
        for j in range(len(pop)-1):
            particle=pop[j]
            pg=max(Fitness)
            v=vMax[j]
            updated=updateVelocity(particle,pbest[j],pg,v,c1,c2)
            
            Fitness[j] = fitness(updated[0])
            vMax[j]=updated[1]
            newpop.append(updated[0])
            for h in range(len(Fitness)):
                if(Fitness[h]>pbest[h]):
                    pbest[h]=Fitness[h]
        final_particles.append(newpop)
        
           
        
    return final_particles,pg



# In[36]:



pso=PSO(50,-2,3,-2,1,500)
print(pso[1])


# In[38]:


plt.plot(pso[0][0],'.',pso[0][1],'*')   


# In[42]:


plt.plot(pso[0][0])   


# In[43]:


plt.plot(pso[0][1])   

