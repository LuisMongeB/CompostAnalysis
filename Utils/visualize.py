import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

# TODO approach it as if it was an import

# TEMP

def visualizeChamberTemp(chamber, chamber_id,  output_folder, title):
  '''
  This function accepts a dataframe of a single chamber, the id of the chamber as an int \
  and the title of the graph as a string.
  Ex: visualizeChamberTemp(chamber1, 1, path_to_folder,'Chamber 1')
  '''


  # Separate channels
  if chamber_id == 1:
    temp_chamber = chamber[(chamber['Channel']==13) | (chamber['Channel']==11)]
  elif chamber_id == 2:
    temp_chamber = chamber[(chamber['Channel']==14) | (chamber['Channel']==17)]
  else:
    temp_chamber = chamber[chamber['Channel'] == 20]
  
  # Title
  plt.figure(figsize=(10,10))
  sns.scatterplot(data=temp_chamber, x='Datetime', y='Value', hue='Channel', palette='coolwarm', )
  plt.title(title)
  # Labels
  plt.xlabel('Datetime')
  plt.ylabel('Temperature Value')
  # Legend
  plt.legend()

  # Save Plot
  plt.savefig(f'{output_folder}/chamber{chamber_id}_temp.png', dpi=300)
  plt.close()
# HUMIDITY

def visualizeChamberHum(chamber, chamber_id, output_folder, title=''):
  '''
  This function accepts a dataframe of a single chamber, the id of the chamber as an int \
  and the title of the graph as a string.
  Ex: visualizeChamberTemp(chamber1, 1, path_to_folder,'Chamber 1')
  '''


  # Separate channels
  if chamber_id == 1:
    hum_chamber = chamber[chamber['Channel'] == 12]
  elif chamber_id == 2:
    hum_chamber = chamber[chamber['Channel'] == 18]
  else:
    hum_chamber = chamber[chamber['Channel'] == 10]
    
  
  plt.figure(figsize=(10,10))
  sns.scatterplot(data=hum_chamber, x='Datetime', y='Value', hue='Channel', palette='coolwarm')
  # Labels
  plt.xlabel('Datetime')
  plt.ylabel('Humidity Value')
  # Title
  plt.title(title)

  plt.legend()
  plt.savefig(f'{output_folder}/chamber{chamber_id}_hum.png', dpi=300)
  plt.close()
  # OXYGEN

def visualizeChamberOxi(chamber, chamber_id , output_folder, title=''):
  '''
  This function accepts a dataframe of a single chamber, the id of the chamber as an int \
  and the title of the graph as a string.
  Ex: visualizeChamberTemp(chamber1, 1, 'Chamber 1')
  '''


  # Separate channels
  if chamber_id == 1:
    oxi_chamber = chamber[chamber['Channel']==16]
  elif chamber_id == 2:
    oxi_chamber = chamber[chamber['Channel']==19]
  else:
    oxi_chamber = chamber[chamber['Channel'] == 20]
  
  plt.figure(figsize=(10,10))

  sns.scatterplot(data=oxi_chamber, x='Datetime', y='Value', hue='Channel', palette='coolwarm')

  plt.title(title)
  plt.xlabel('Datetime')
  plt.ylabel('Oxygen Value')
  plt.legend()

  plt.savefig(f'{output_folder}/chamber{chamber_id}_oxi.png', dpi=300)
  plt.close()