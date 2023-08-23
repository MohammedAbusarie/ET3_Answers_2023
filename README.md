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
3. Run the script using the command:
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
