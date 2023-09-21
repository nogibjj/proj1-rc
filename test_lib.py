import lib
#import pandas as pd

data = "project1/Auto.csv"

def test_describe_dataset():
  lib.describe_dataset(data)
  
def test_scatter_mpg():
  lib.scatter_mpg(data)

def test_fitted_mpg():
  lib.fitted_mpg(data)

def test_scatter_acc():
  lib.scatter_acc(data)

def test_fitted_acc():
  lib.fitted_acc(data)

def test_generate_general_markdown():
  lib.generate_general_markdown(data)
