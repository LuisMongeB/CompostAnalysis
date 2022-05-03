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

In order to run main.py, an argument called **input_csv** has to be added that points to the name of the csv INSIDE of the **Data** folder. 
