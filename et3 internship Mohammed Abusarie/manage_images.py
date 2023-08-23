import pathlib
import shutil
import datetime
import os
import pandas as pd
import re

currpath = pathlib.Path.cwd()
datasetFolderName="DairyImages"
listOfImages=list(currpath.rglob("*.jpg"))
destination_path = os.path.join( currpath , datasetFolderName ) 

# Create the destination folder if it doesn't exist
if not os.path.exists(destination_path):
    os.makedirs(destination_path)

#for image in listOfImages:
#    shutil.copy(str(image), destination_path) #copy each image to a certain folder

# Create an empty DataFrame with the specified columns
columns = ['Image', 'Image Size', 'Image Modification Date']
dataset = pd.DataFrame(columns=columns)

# Loop through the list of images and add their information to the dataset
for image_path in listOfImages:
    image_name = os.path.basename(image_path)
    image_name_cleaned = re.sub(r'^[^-]*-', '', image_name) #get rid of the prefix
    image_size_kb = round(image_path.stat().st_size / 1024, 2)  # Convert to KB
    image_size_formatted = f'{image_size_kb} KB'  # Format size with units
    image_mod_date = datetime.datetime.fromtimestamp(image_path.stat().st_mtime).strftime('%A %B %d %H:%M:%S %Y')

    dataset = dataset.append({
        'Image': image_name_cleaned,
        'Image Size': image_size_formatted,
        'Image Modification Date': image_mod_date
    }, ignore_index=True)

dataset.to_csv('image_data.csv', index=False)

