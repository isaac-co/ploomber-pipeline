# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.13.8
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% tags=[]
# Retrieve titanic dataset.
#
# *Note:* You can open this file as a notebook (JupyterLab: right-click on it in the side bar -> Open With -> Notebook)


# %% tags=[]
# Uncomment the next two lines to enable auto reloading for imported modules
# # %load_ext autoreload
# # %autoreload 2
# For more info, see:
# https://docs.ploomber.io/en/latest/user-guide/faq_index.html#auto-reloading-code-in-jupyter

# %% tags=["parameters"]
# If this task has dependencies, list them them here
# (e.g. upstream = ['some_task']), otherwise leave as None.
upstream = None

# This is a placeholder, leave it as None
product = None


# %% tags=["injected-parameters"]
# This cell was injected automatically based on your stated upstream dependencies (cell above) and pipeline.yaml preferences. It is temporary and will be removed when you save this notebook
product = {"data": "C:\\Users\\Isaac\\Desktop\\Folder\\Scripts\\ploomber-pipeline\\Demo-Pipeline\\output\\titanic_raw.csv", 
           "nb": "C:\\Users\\Isaac\\Desktop\\Folder\\Scripts\\ploomber-pipeline\\Demo-Pipeline\\output\\load_titanic.ipynb"}


# %% tags=[]
import seaborn as sns

titanic = sns.load_dataset('titanic')
titanic.to_csv(product['data'], index=False)
