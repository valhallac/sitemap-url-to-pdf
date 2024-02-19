# sitemap-url-to-pdf

This Python script downloads webpages from a CSV file and saves them as PDFs. It utilizes multiprocessing for parallel processing for potential speedup.

Disclaimer:

This script is provided for educational purposes only. It is your responsibility to use it ethically and legally. Downloaded content should not violate copyright or other intellectual property rights. Modifying or using this script for any malicious or harmful purposes is strictly prohibited.

Features:

    Downloads webpages from a CSV file containing URLs.
    Ignores the header row in the CSV file.
    Saves each webpage as a separate PDF file with a unique name.
    Creates a "pdf_files" folder within the script's directory to store PDFs.
    Uses multiprocessing for parallel processing.

Requirements:

    Python 3.x
    requests library (pip install requests)
    weasyprint library (pip install weasyprint)

Usage:

    Replace urls.csv with the actual name of your CSV file containing URLs.
    Install the required libraries (see Requirements).
    Run the script: python script.py
    Check the "pdf_files" folder for downloaded PDFs.

Notes:

    This script does not validate the content of downloaded webpages. Use it with caution and awareness of potential copyright and legal implications.
    Adjust the number of processes in the script based on your system's performance and requirements.

Further development:

    Error handling for various potential issues (e.g., invalid URLs, network errors).
    More flexibility in filename generation.
    Downloading specific content from webpages instead of entire pages.

I hope this script serves as a starting point for your learning and exploration. However, remember to use it responsibly and ethically.
