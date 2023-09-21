#This is the python script that describe the statistics
import lib
import pandas as pd

def main():
    """Main function to call data visualization functions"""

    data = "project1/Auto.csv"
    
    summary = lib.describe_dataset(data)
    print(summary)

    lib.scatter_mpg(data)

    lib.fitted_mpg(data)

    lib.scatter_acc(data)

    lib.fitted_acc(data)

    lib.generate_general_markdown(data)

def data(dataset):
    result = pd.read_csv(dataset)
    return result

if __name__ == "__main__":
    main()
