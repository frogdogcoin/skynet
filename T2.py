import requests
import os

base_url = "https://meta.makotodigital.art/image/{}.png"
save_folder = "../imagesoppepe/"

# Create the save folder if it doesn't exist
os.makedirs(save_folder, exist_ok=True)

# Download and save the images
for number in range(1, 1001):  # Update the range from 1 to 1000
    url = base_url.format(number)
    filename = f"{number}.png"
    save_path = os.path.join(save_folder, filename)
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, "wb") as f:
            f.write(response.content)
        print(f"Image {filename} downloaded and saved successfully.")
    else:
        print(f"Failed to download image {filename}.")
