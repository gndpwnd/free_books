import os
import subprocess
from tqdm import tqdm

# Selecte category of books
folder_name = "medical"

# Get the current directory - call this script to run in the current directory
current_dir = os.getcwd()

# Find all the files in the current directory that end with ".pdf"
pdf_files = [file_name for file_name in os.listdir(current_dir) if file_name.endswith(".pdf")]

# Loop through all the PDF files and run the system command for each file
for pdf_file in tqdm(pdf_files, desc="Running system command", unit="file"):

    # Build the system command using the file name
    command = ("spaces-cli upload " + pdf_file + " -t archive-books/" + folder_name + "/" + pdf_file)

    # Run the system command using subprocess
    subprocess.run(command, shell=True)
