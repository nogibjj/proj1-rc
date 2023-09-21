# IDS 706 Individual Project 1

This repository is for IDS706 individual project 1. 



## Brief description 

This repository employs Pandas to perform statistical analysis and generate visualizations for the "Cars.csv" dataset. The dataset "Cars.csv" comprises various variables, including mpg, weight, year, origin, acceleration, and more.

Additionally, the visualizations produced allow for an in-depth analysis of the correlation between weight and mpg, as well as weight and acceleration, concerning their respective origins or years. Both scatter plots and fitted plots, which incorporate the line of best fit, are included to provide a more comprehensive understanding of the data.

## Files 


- .devcontainer for a Python environment includes a Dockerfile and devcontainer.json.

- workflows are the configuration files for setting up automated build, test, and deployment pipelines

- .gitignore is for specify which files or directories should be excluded from version control when using Git.

- Makefile is a configuration file for commands for setup, testing, and linting

- README.md is the instruction file for the readers.

- requirements.txt is to specify the dependencies (libraries and packages) required to run the project.

- desc_stats.ipynb is a jupyter notebook that includes the scratch notes for creating the functions. It also displays the plots created.
        
- main.py is a Python file. This specific main.py includes features of importing the pandas package and utilizing pandas to visualize the dataset Cars.csv.
        
- test_main.py is a test file for main.py.

- lib.py includes all the written functions for describing statistics and visualizing data in Cars.csv
        
- test_lib.py is a test file for lib.py.
        
- Cars.csv is the dataset includes variables such as mpg, acceleration, weight, and year etc. 

- scatter_mpg.png, scatter_acc.png, fitted_acc.png are the automatically saved plots generated by the functions. They are saved in png format.



## Github Actions

Status badges for each makefile commands are displayed below. CI.yml includes all commands. 

`install.yml`
[![Install](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/install.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/install.yml)

`test.yml`
[![Test](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/test.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/test.yml)

`format.yml`
[![Format](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/format.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/format.yml)

`lint.yml`
[![Lint](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/lint.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/lint.yml)

`deploy.yml`
[![Deploy](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/deploy.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/deploy.yml)

`generate_and_push.yml`
[![Generate_and_Push](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/generate_and_push.yml/badge.svg)](https://github.com/nogibjj/Kelly_Tong_Individual_Project1/actions/workflows/generate_and_push.yml)




## Visualizations

#### Relation between car weight and mpg with 
![image](https://github.com/nogibjj/proj1-rc/assets/123079408/d236458b-8c93-4c6a-bf97-d700c71607a9)



#### Relation between car weight and acceleraton 

![image](https://github.com/nogibjj/proj1-rc/assets/123079408/ad97e915-2ffe-4057-b4be-50e755b45ab6)



#### Fitted relation between car weight and acceleraton 
![image](https://github.com/nogibjj/proj1-rc/assets/123079408/e1fa1b6e-1a52-48c4-a396-013e79454967)




## Conclusion

We encourage and appreciate contributions! If you have any suggestions, improvements, or notice any issues or inconsistencies, please feel free to contribute by submitting a pull request or opening an issue. Your input is valuable and helps enhance the project.
