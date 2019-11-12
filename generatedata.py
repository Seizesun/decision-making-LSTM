# -*- coding: utf-8 -*-

"""
2019.11 -- WAN_lab

 1. Here, it is to generate specific distribution data that meets the simulation
    requirements of our experiment.
 2. There are three important parameters: variance, sample length(n_runs) and hr(hazard rste).
 3. you can adjust them at will to meet your analysis requirements .
    (other distributed data can also be used for this model simulation)
                                                                      from XY_fu 
"""

import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
import scipy


def generate_data(hr,datastd,n_runs):
    
    values = np.linspace(0,1,101)
    mean_pool = np.linspace(0.2,0.8,601)
    mean_vector_0 = np.random.random(size=n_runs)
    mean_vector_1 = np.amax(mean_pool)-np.amin(mean_pool)
    mean_vector = mean_vector_0*mean_vector_1 + np.amin(mean_pool)
    runlength_vector=np.random.geometric(p=hr,size=[n_runs,1])

    
    print("Hr,datastd,n_runs:",hr,datastd,n_runs)
    
    dataset =[]
    for i in range (len(runlength_vector)):
        b = np.random.normal(loc=0,scale=1.0,size=runlength_vector[i])
        c= mean_vector[i]+datastd*b
        dataset.append(c)
    return (dataset)


def reshapedata(dataset):
    data=[0]
    for j in range(len(dataset)):
        data = np.concatenate((data,dataset[j]),axis = 0)
    return (data.astype("float32"))  
    plt.plot(data)
    
    
            



    
           


    
