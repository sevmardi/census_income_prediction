import numpy as np
import pandas as pd
import json
import matplotlib.pyplot as plt
from math import floor
import time
import os
from sklearn.datasets.base import Bunch
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn import preprocessing
from sklearn.preprocessing import Imputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import pickle


CENSUS_DATASET = (
    "data/census-income.data",
)

# read in data
data = pd.read_csv('data/census-incokme.data', names=None)

data.columns = ['AAGE', 'ACLSWKR', 'ADTIND', 'ADTOCC', 'AHGA', 'AHRSPAY',
                'AHSCOL', 'AMARITL', 'AMJIND', 'AMJOCC', 'ARACE', 'AREORGN',
                'ASEX', 'AUNMEM', 'AUNTYPE', 'AWKSTAT', 'CAPGAIN', 'CAPLOSS',
                'DIVVAL', 'FILESTAT', 'GRINREG', 'GRINST', 'HHDFMX', 'HHDREL',
                'MARSUPWT', 'MIGMTR1', 'MIGMTR3', 'MIGMTR4', 'MIGSAME', 'MIGSUN',
                'NOEMP', 'PARENT', 'PEFNTVTY', 'PEMNTVTY', 'PENATVTY', 'PRCITSHP',
				'SEOTR', 'VETQVA', 'VETYN', 'WKSWORK', 'YEAR', 'TARGET']



def load_data(root='data'):
	""" Load the meta data from the file """
	pass   


def normalize(params):
    pass


def sigmoid(s):
    pass


def sigmoid_gradient(s):
    pass


def predict():
    pass
