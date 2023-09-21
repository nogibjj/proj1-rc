import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# This file includes all the functions created. 

def describe_dataset(data):
  df = pd.read_csv(data)
  return df.describe()

def scatter_mpg(data_path):
  Auto = pd.read_csv(data_path)
  
  # Create the scatter plot
  plt.figure(figsize=(10, 6))
  plot = sns.scatterplot(data = Auto, x = 'weight', y = 'mpg', hue = 'origin')
  
  # Set labels for the axes
  plt.xlabel('Vehicle weight (lbs)')
  plt.ylabel('MPG')
  plt.title('Relation between Car Weight and MPG')
  
  plot.legend()
  
  # Show the plot
  plt.show()
  plt.savefig("scatter_mpg.png")


def scatter_acc(data_path):
  Auto = pd.read_csv(data_path)
  
  # Create the scatter plot
  plt.figure(figsize=(5, 5))
  sns.scatterplot(data = Auto, x = 'weight', y = 'acceleration')
  
  # Set labels for the axes
  plt.xlabel('Vehicle weight (lbs)')
  plt.ylabel('Acceleration')
  plt.title('Relation between Car Weight and Acceleration ')

 # Show the plot
  plt.show()
  plt.savefig("scatter_acc.png")
 

def fitted_acc(data_path):
  Cars = pd.read_csv(data_path)
  
  plt.figure(figsize=(5,5))
  sns.lmplot(data=Cars, x='weight', y='acceleration', height=4, aspect=4)
  plt.title('Fitted relation between Car Weight and Acceleration')
  
  # Set labels for the axes
  plt.xlabel('Vehicle weight (lbs)')
  plt.ylabel('Acceleration')
  
  # Show the plot
  plt.show()
  plt.savefig("fitted_acc.png")

def generate_general_markdown(data):
    """generate an md file with outputs"""
    describe = describe_dataset(data)
    markdown_table1 = str(describe)

    # Write the markdown table to a file
    with open("desc_stats.md", "w", encoding="utf-8") as file:
        file.write("Describe:\n")
        file.write(markdown_table1)
        file.write("\n\n")  # Add a new line
        file.write("![weight vs mpg](scatter_mpg.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("\n\n")  # Add a new line
        file.write("![weight vs acceleration](scatter_acc.png)\n")
        file.write("\n\n")  # Add a new line
        file.write("\n\n")  # Add a new line
        file.write("![fitted weight vs acceleration](fitted_acc.png)\n")



