import os
import re
import requests
from urllib.parse import urlparse, parse_qs
import time

url = "http://net.bnetly.com/read.jsp"
save_directory = "../bnetly"

# Create the save directory if it doesn't exist
os.makedirs(save_directory, exist_ok=True)

while True:
    try:
        # Download the webpage content
        response = requests.get(url)
        content = response.text

        # Find all .txt file references
        txt_files = re.findall(r'href=["\'](.*?\.txt)["\']', content)

        # Download and save the .txt files
        for txt_file in txt_files:
            file_url = "http://net.bnetly.com/" + txt_file
            parsed_url = urlparse(file_url)
            filename = parse_qs(parsed_url.query).get('filename')
            if filename:
                sanitized_filename = filename[0]  # Extract the filename from the query parameter
                file_path = os.path.join(save_directory, sanitized_filename)
                if not os.path.exists(file_path):  # Check if the file already exists
                    response = requests.get(file_url)
                    with open(file_path, "wb") as file:
                        file.write(response.content)
                    print(f"Downloaded: {file_path}")
                else:
                    print(f"Skipped - File already exists: {file_path}")

        time.sleep(2)  # Wait for 1 second before the next iteration
    except Exception as e:
        print(f"An error occurred: {e}")
        print("Retrying...")
        time.sleep(5)
        continue  # Retry the loop if an exception occurs
