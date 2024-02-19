import csv
import os
import requests
from io import StringIO
from datetime import datetime
from weasyprint import HTML
from multiprocessing import Pool

# Define a function to validate and handle potential errors
def validate_url(url):
    if not url.startswith("http"):
        print(f"Invalid URL: {url}. Skipping...")
        return

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if request fails
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {url} ({e}). Skipping...")
        return None

def download_and_save_pdf(url):
    response = validate_url(url)
    if not response:
        return

    # Create a unique filename using the URL and timestamp
    now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    unique_filename = os.path.splitext(url.split('/')[-1])[0] + "_" + now + ".pdf"

    # Create the "pdf_files" directory if it doesn't exist
    output_dir = os.path.join(os.path.dirname(__file__), "pdf_files")
    os.makedirs(output_dir, exist_ok=True)

    try:
        html = HTML(string=response.content)
        html.write_pdf(os.path.join(output_dir, unique_filename))
        print(f"Downloaded webpage for URL: {url} and saved as: {unique_filename}")
    except Exception as e:
        print(f"Error saving PDF for URL: {url} ({e}).")

# Get the path to the script, assuming the CSV file is in the same directory
script_path = os.path.dirname(os.path.abspath(__file__))
csv_file = os.path.join(script_path, "docs-mule-urls-11k.csv")

# Open the CSV file and iterate over each row
with open(csv_file, newline='') as csvfile:
    reader = csv.reader(csvfile)
    next(reader, None)  # Skip the header row

    # Extract URLs from the CSV
    urls = [row[0] for row in reader]

# Use multiprocessing for parallel processing
if __name__ == "__main__":
    # Adjust the number of processes based on your system performance
    num_processes = 6
    with Pool(processes=num_processes) as pool:
        pool.map(download_and_save_pdf, urls)

print("PDF downloads complete!")
