import pandas as pd 
import os
import matplotlib.pyplot as plt 

def clean_data(input_csv):

    raw_data = pd.read_csv(f'{os.getcwd()}\\Data\\{input_csv}', sep=',')

    # Print the different sensors
    gr = raw_data.groupby('Channel')['Sensor Name']
    print(gr.unique(), '\n')

    # Missing values
    print('Missing values: \n', raw_data.isna().sum())
    raw_data.Unit = raw_data.Unit.fillna(value='muestra')

    # Converting timestamp to Datetime
    raw_data['Datetime'] = pd.to_datetime(raw_data['Timestamp'], infer_datetime_format=True)

    # Rounding the Value column
    raw_data['Value'] = raw_data['Value'].round(3)

    # Add chamber column

    raw_data['Chamber'] = raw_data['Channel'].apply(separate_channels)

    # Column selection
    selected_columns = ['Datetime', 'Channel', 'Chamber','Sensor Name', 'Unit', 'Value']

    cleaned_data = raw_data[selected_columns]
    print('Cleaned data: \n', cleaned_data.head(5))

    # Export to csv
    print('Exporting cleaned data to CSV')
    file_noext = input_csv.split('.')[0]
    cleaned_data.to_csv(f'./Data/{file_noext}_cleaned.csv', )

    

# Helper functions

def separate_channels(sensor_name):

    camara1_channels = [11,12,13,16]
    camara2_channels = [14,17,18,19]

    if (sensor_name in camara1_channels):
        return 1
    elif (sensor_name in camara2_channels):
        return 2
    else:
        return 0