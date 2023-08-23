# ET3_Answers_2023 Problem 1 & 2

# Image Dataset Management Script (Problem 1)

This script is designed to organize image files, gather their information, and create a CSV dataset containing relevant details about each image. It can be particularly useful for managing image datasets used in various projects.

## Features

- Copies images from a source directory to a designated dataset folder.
- Extracts information like image name, size, and modification date for analysis.
- Creates a CSV dataset to store the extracted image details.

## Prerequisites

- Python 3.x
- Required Python packages:
  - `pathlib`
  - `shutil`
  - `datetime`
  - `os`
  - `pandas`
  - `re`

## Usage

1. Place the script (`manage_images.py`) in the directory containing the images you want to manage.
2. Open a terminal or command prompt and navigate to the directory with the script.
3. Run the script using the command: `python manage_images.py`
4. The script will organize the images into a folder named `DairyImages` and gather their information.
5. The gathered information will be saved in a CSV file named `image_data.csv`.

## Code Explanation

The script follows these steps:

1. Get the current working directory and define folder names.
2. Locate all `.jpg` images within the current directory and its subdirectories.
3. Create a destination folder (`DairyImages`) if it doesn't exist.
4. Loop through the images, extract relevant information, and copy each image to the destination folder.
5. Build a DataFrame using `pandas` to store image details.
6. Save the DataFrame as a CSV file (`image_data2.csv`).

---

# JSON Data Transformation Script (Problem 2)

This script is designed to transform JSON data based on calculated scaling factors and create a new JSON output. It's particularly useful when working with coordinate data that needs to be scaled and transformed.

## Features

- Calculates scaling factors for transforming coordinate data.
- Reads input data from a text file.
- Creates a new JSON structure based on the transformed coordinates.

## Prerequisites

- Python 3.x
- Required Python libraries:
  - `json`

## Usage

1. Place the script (`transform_json.py`) in the directory containing the text file with coordinate data (`image1.txt`).
2. Open a terminal or command prompt and navigate to the directory with the script.
3. Run the script using the command: `python transform_json.py`
4. The script will calculate scaling factors, read coordinate data from `image1.txt`, transform the data, and create a new JSON output (`output.json`).

## Code Explanation

The script follows these steps:

1. Calculate scaling factors based on the provided `old_data` and `new_data`.
2. Create a JSON template structure for annotations.
3. Read coordinate data from `image1.txt`, transform the data using scaling factors, and add to the JSON structure.
4. Write the transformed JSON structure to an output file (`output.json`).



