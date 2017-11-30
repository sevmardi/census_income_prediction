import os
import sys 
import numpy as np

import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from matplotlib import rcParams

from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn import svm

# import sklearn.cross_validation
from sklearn.ensemble import RandomForestClassifier
from sklearn import linear_model

CENSUS_DATASET = (
    "../data/census-income.data",
)

# read in data
data = pd.read_csv('../data/census-income.data', names=None)

data.columns = ['AAGE', 'ACLSWKR', 'ADTIND', 'ADTOCC', 'AHGA', 'AHRSPAY',
                'AHSCOL', 'AMARITL', 'AMJIND', 'AMJOCC', 'ARACE', 'AREORGN',
                'ASEX', 'AUNMEM', 'AUNTYPE', 'AWKSTAT', 'CAPGAIN', 'CAPLOSS',
                'DIVVAL', 'FILESTAT', 'GRINREG', 'GRINST', 'HHDFMX', 'HHDREL',
                'MARSUPWT', 'MIGMTR1', 'MIGMTR3', 'MIGMTR4', 'MIGSAME', 'MIGSUN',
                'NOEMP', 'PARENT', 'PEFNTVTY', 'PEMNTVTY', 'PENATVTY', 'PRCITSHP',
				'SEOTR', 'VETQVA', 'VETYN', 'WKSWORK', 'YEAR', 'TARGET']

# this create histograms of values in each column
for index in range(len(data.columns)):
 	# print counter (data.ix[:, i].values)
 	rcParams.update({'figure.autolayout': True})	

 	lables, values = zip(*Counter(data.ix[:, index].values).items())
 	idexes = np.arange(len(lables))

 	width = 1

 	plt.yticks(idexes + width * 0.5, lables)
 	plt.savefig('hist_column' + str(index) + '.pdf', format="pdf")

 	plt.clf()


