import numpy as np
import uproot
import pandas as pd
import csv
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import math


# For reference this is the header
# country  net_approval  Approve  Disapprove  DK/Refused (percentual)

# https://www.kaggle.com/yamqwe/trump-world-truste
list_of_datasets = []
list_of_datasets.append("/afs/cern.ch/user/o/orlando/reach_examples/fivethirtyeight-trump-world-trust/TRUMPWORLD-issue-1.csv" )
list_of_datasets.append("/afs/cern.ch/user/o/orlando/reach_examples/fivethirtyeight-trump-world-trust/TRUMPWORLD-issue-2.csv" )
list_of_datasets.append("/afs/cern.ch/user/o/orlando/reach_examples/fivethirtyeight-trump-world-trust/TRUMPWORLD-issue-3.csv" )
list_of_datasets.append("/afs/cern.ch/user/o/orlando/reach_examples/fivethirtyeight-trump-world-trust/TRUMPWORLD-issue-4.csv" )
list_of_datasets.append("/afs/cern.ch/user/o/orlando/reach_examples/fivethirtyeight-trump-world-trust/TRUMPWORLD-issue-5.csv" )

policies_map = []
policies_map.append( [1,'Withdraw support for international climate change agreements'] )
policies_map.append( [2,'Build a wall on the border between the U. S. and Mexico'] )
policies_map.append( [3,'Withdraw U.S. support from the Iran nuclear weapons agreement'] )
policies_map.append( [4,'Withdraw U.S. support for major trade agreements'] )
policies_map.append( [5,'Introduce tighter restrictions on those entering the U.S. from some majority-Muslim countries'] )

# utility functions for simple analysis and plots

# From this example https://github.com/nicola-orlando/uncover-covid-19-challenge/blob/master/q1/covid_q1.py
# and https://stackoverflow.com/questions/46828689/adding-avg-line-to-bar-plot-using-read-excel-pandas-matplotlib
def make_text_freq_plot(color,indexes,keys_counts,plot_title,is_log_y,y_axis_name,is_grid,width,legend,tick_size=0):
    plt.bar(indexes, keys_counts, width, color=color, linewidth=0.5,edgecolor='black',label=legend)
    ax=plt.axes()
    if is_log_y:
        plt.yscale('log')        
    plt.ylabel(y_axis_name)
    if tick_size != 0: 
        for tick in ax.xaxis.get_major_ticks():
            tick.label.set_fontsize(tick_size) 
        for tick in ax.yaxis.get_major_ticks():
            tick.label.set_fontsize(tick_size) 
    if is_grid: 
        plt.grid(True,axis='y')
    plt.legend()
    mean = keys_counts.mean()
    ax.axhline(mean)
    plt.xticks(rotation=90)
    plt.tight_layout()
    plt.show()
    plt.savefig(plot_title)
    plt.close()

# For datasets TRUMPWORLD-issue-* showing the approval of individual countries for a number of Trump's policies we want to show 1D data vs country
dataset_index = 0
for dataset in list_of_datasets:
    df = pd.read_csv(dataset)

    df = df.rename(columns={'DK/Refused':'DKRefused'})

    # print("Prining head of the file to see how it looks")
    print(df.head())
    print("Prining data types")
    print(df.dtypes)

    title_base = policies_map[dataset_index][1]
    print('Processing the data for: '+title_base)
    
    make_text_freq_plot('lavender',df.country,df.net_approval,'net_approval_'+str(dataset_index)+'.png',False,'Net Approval [%]',False,0.8,title_base,5.0)
    make_text_freq_plot('lavender',df.country,df.Approve,'Approve_'+str(dataset_index)+'.png',False,'Approve [%]',False,0.8,title_base,5.0)
    make_text_freq_plot('lavender',df.country,df.Disapprove,'Disapprove_'+str(dataset_index)+'.png',False,'Disapprove [%]',False,0.8,title_base,5.0)
    make_text_freq_plot('lavender',df.country,df.DKRefused,'DK-Refused_'+str(dataset_index)+'.png',False,'DK/Refused',False,0.8,title_base,5.0)
    
    dataset_index = dataset_index + 1

