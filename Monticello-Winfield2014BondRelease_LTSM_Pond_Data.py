
# coding: utf-8

# In[1]:

from odo import odo


# In[2]:

import pandas as pd


# In[3]:

data=odo('MW2014LTSMPondsBR.csv', pd.DataFrame)


# In[5]:

print data


# In[6]:

import scipy.stats


# In[7]:

data.dtypes


# In[8]:

ponds=list(pd.unique(data.POND.ravel()))


# In[9]:

print ponds


# In[23]:

import numpy as np


# In[24]:

import matplotlib.cbook
import matplotlib.pyplot as plt


# In[25]:

print len(ponds)


# In[ ]:

p=0
while p <= len(ponds)-2:
    output=data[data['POND'].isin([ponds[p]])]
    del output['Flow _GPM']
    del output['FDP_Flow_GPM']
    #print output
    #median_flow=numpy.median(output['Flow_CFS'])
    #mean_flow=numpy.mean(output['Flow_CFS'])
    #max_flow=numpy.amax(output['Flow_CFS'])
    #median_conductivity=numpy.median(output['Conductivity umho/cm'])
    #mean_conductivity=numpy.mean(output['Conductivity umho/cm'])
    #max_conductivity=numpy.amax(output['Conductivity umho/cm'])
    stats=matplotlib.cbook.boxplot_stats(list(output['Conductivity umho/cm']), whis=1.5, bootstrap=None, labels=None)
    print stats
    """for n in range(len(stats)):
        stats[n]['med'] = np.median(data)
        stats[n]['mean'] *= 2"""

    print(stats[0].keys())
    fs = 10 # fontsize
    fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(6,6))
    axes[0, 0].bxp(stats)
    axes[0, 0].set_title('Default', fontsize=fs)
    
    axes[0, 1].bxp(stats, showmeans=True)
    axes[0, 1].set_title('showmeans=True', fontsize=fs)

    axes[1, 1].bxp(stats, showmeans=True, meanline=True)
    axes[1, 1].set_title('showmeans=True,\nmeanline=True', fontsize=fs)

    axes[1, 0].bxp(stats, shownotches=True)
    axes[1, 0].set_title('notch=True', fontsize=fs)

    
    plt.show()
    
    #print str(ponds[p])+' median flow='+ str(median_flow)+' median conductivity='+ str(median_conductivity)
    #print str(ponds[p])+' mean flow='+ str(mean_flow)+' mean conductivity='+ str(mean_conductivity) 
    #print str(ponds[p])+' max flow='+ str(max_flow)+' max conductivity='+ str(max_conductivity)
    p+=1



