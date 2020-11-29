%reload_ext autoreload

%autoreload 2

%matplotlib inline

from fastai.vision import *

from fastai.metrics import error_rate

import warnings

warnings.filterwarnings('ignore')

import eazyml


username = 'process.env.username'

password = 'process.env.password'

train_file_path = '/VMS/home/raj/eazyml/train.csv'


# To authenticate and retrieve an authentication token to be used for

# all API calls

resp = eazyml.ez_auth(username, password)

auth_token = resp["token"]


options = {

    "id": "null",

    "impute": "yes",

    "outlier": "no",

    "discard": ["Column_Names"],

    "accelerate": "yes",

    "outcome" : "Outcome_Column"

}


# To upload training data in a file. The accepted file formats are CSV

# and Microsoft Excel.

resp = eazyml.ez_load(auth_token, train_file_path, options)

dataset_id = resp["dataset_id"]


options = {

    "outcome_type" : "categorical"

}


# To specify the outcome variable and optionally it's data type.

outcome_set = eazyml.ez_set_outcome(auth_token, dataset_id,

              "charges", options)


#Resp: {

#'status_code': 200,

#u'message': u'Outcome has been set successfully!',

#u'dataset_id': u'7457',

#u'success': True

#}




