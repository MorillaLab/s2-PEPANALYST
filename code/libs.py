from sklearn import preprocessing
#ESM embedding
import torch
import esm
import matplotlib.pyplot as plt 
import os 
from scipy.stats import norm
import scipy.stats as sps
import cv2
from scipy.ndimage import convolve
import skimage
from scipy import ndimage
from scipy.spatial.distance import cdist
from nibabel.testing import data_path
import nibabel as nib
from sklearn.mixture import GaussianMixture
import os
import pandas as pd
import skimage.measure
import seaborn as sns
import scipy as sp
import gudhi as gd
import random
import sys
sys.path.append('../') 
from Code.function_geometry import * 
from Code.codegeometry import * 
from PIL import Image
from sklearn.utils import shuffle
import random
from sklearn.model_selection import train_test_split


import sklearn.preprocessing   as skp
import sklearn.neighbors       as skn
import sklearn.model_selection as skm
import sklearn.decomposition   as skd
import sklearn.manifold        as skf
import sklearn.pipeline        as skl
import sklearn.svm             as sks
import sklearn.ensemble        as ske
import itertools
import tensorflow as tf

import gudhi.clustering.tomato as gdt
import gudhi.representations   as gdr

import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
import torch
#tokenizer
from tape import ProteinBertModel, TAPETokenizer
# from tape import UniRepModel, UniRepTokenizer
# from tape import ProteinBertModel, ProteinBertTokenizer
from transformers import AutoTokenizer
from transformers import BertModel, BertTokenizer
# ProtGPT2
# from transformers import pipeline

from keras.models import Sequential
from keras.layers import Conv1D,Conv2D, Dense, Flatten, Dropout,MaxPooling2D
from keras import layers
from keras.layers import MaxPooling1D,MaxPooling2D
from keras.optimizers import SGD, RMSprop
from keras import regularizers
from sklearn.metrics import f1_score, precision_score, recall_score, accuracy_score,confusion_matrix,matthews_corrcoef