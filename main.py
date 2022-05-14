#!/usr/bin/env python
# -*- coding: utf-8 -*-
from utils.visualize import visualizeChamberHum, visualizeChamberOxi, visualizeChamberTemp
from utils.clean import clean_data
import dataset_review # all functions
import pandas as pd
import os
import argparse

# TODO argparse
parser = argparse.ArgumentParser()
parser.add_argument("--input_csv", type=str, required=True, help="path to csv")
parser.add_argument("--metodo", type=str, required=True, help='Metodo empleado en la compostera (string).')
args = parser.parse_args()

def main(input_csv, metodo):
    
    print('1. Running main \n')
    print('\t This will clean and visualize data.')
    
    print('2. Cleaning data \n')
    input_csv_path = os.path.join(f'{os.getcwd()}\\Data\\{args.input_csv}')
    clean_data(input_csv, metodo)
    # cleaned_data = pd.read_csv('C:\\Users\\L.MONGEBOLANOS\\OneDrive - Gruppo HERA\\Desktop\\Compost\\Data\\cleaned_data_abril.csv', sep=',', index_col=0)

    print('3. Reading cleaned_data')
    file_noext = input_csv.split('.')[0]
    cleaned_data = pd.read_csv(f'./Data/{file_noext}_cleaned.csv', sep=',', index_col=0)
    # cleaned_data = pd.read_csv(input_csv_path, sep=',', index_col=0)
    cleaned_data['Datetime'] = pd.to_datetime(cleaned_data['Datetime'])
    print(cleaned_data.head())

    # Separating chambers
    print('4. Separating Chambers \n')
    chamber0 = cleaned_data[cleaned_data['Chamber'] == 0] # Muestra
    chamber1 = cleaned_data[cleaned_data['Chamber'] == 1]
    chamber2 = cleaned_data[cleaned_data['Chamber'] == 2]
    print(f'Muestra: \n {chamber0.head(2)} \n \n Chamber 1: \n {chamber1.head(2)} \n \n Chamber 2: \n {chamber2.head(2)} \n \n')

    graph_path = os.path.join(f'{os.getcwd()}\\Graphs')
    review_path = os.path.join(f'{os.getcwd()}\\ComposteraReviewed')

    # TODO CALL DATASET_REVIEW
    print('5. Reviewing dataset.')
    # run.main()

    print('6. Saving Temp/Oxy/Hum Plots \n')
    for idx, chamber in enumerate([chamber0,chamber1,chamber2]):
        visualizeChamberTemp(chamber=chamber, chamber_id=idx,  output_folder=graph_path, title=f'Chamber {idx}: Temperature')
        visualizeChamberHum(chamber, idx, graph_path, title=f'Chamber {idx}: Humidity')
        visualizeChamberOxi(chamber, idx, graph_path, f'Chamber {idx}: Oxygen')
        
    # visualizeChamberTemp(chamber=chamber2, chamber_id=2,  output_folder=graph_path, title='Chamber 2: Temperature')        
    # visualizeChamberHum(chamber2, 2, './Graphs', title='Chamber 2: Humidity')
    # visualizeChamberOxi(chamber2, 2, './Graphs', 'Chamber 2: Oxygen')
    print('Completed.')

    return

if __name__ == "__main__":
    main(args.input_csv, args.metodo)