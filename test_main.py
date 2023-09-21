#Check if the images and output markdown is generated
import os
import main

def test_data():
  dataset = "IDS706-PROJ1/Cars.csv"
  result = main.data(dataset)
  assert result is not None

def test_save_plot():
  assert os.path.exists("scatter_mpg.png")

def test_save_plot2():
  assert os.path.exists("fitted_mpg.png")

def test_save_plot3():
  assert os.path.exists("scatter_acc.png")

def test_save_plot4():
  assert os.path.exists("fitted_mpg.png")

def test_save_markdown():
  assert os.path.exists("desc_stats.md")
