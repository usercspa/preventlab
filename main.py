%reload_ext autoreload
%autoreload 2
%matplotlib inline

from fastai.vision import *
from fastai.metrics import error_rate

import warnings
warnings.filterwarnings('ignore')

help(untar_data)
path = untar_data(URLs.PETS)
print(path)