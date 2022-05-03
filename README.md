# CompostAnalysis
This code is meant to automate the analysis of data coming from compost bins for the Master Thesis of my brother in Biosystems Engineering. 

To avoid tools like Excel, which can do the same operations and plots but are more rigid, we decided to adopt Python. The idea being that the raw data generated by each compost bin can be downloaded as a .csv file and given as input to main.py in order to:

1. Clean data and export the clean csv;
2. Print and save some descriptive statistics about the the compost bin;
3. Visualize and save plots necessary for facilitating the writing of the thesis.

The project structure goes as follows:

**Data folder:** where the initial input_csv will be.

**Graphs:** where the resulting graphs will be stored.


## Running main

From the project directory main.py can run with an argument called **input_csv** that has to be added to point to the name of the csv INSIDE of the **Data** folder. 

![image](https://user-images.githubusercontent.com/65911072/166419261-bfda3203-413b-40a8-9b05-7b40334fa8e0.png)


