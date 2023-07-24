from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
import random
import os
import sys
import openai


# Specify the path to your web driver executable
# Download the appropriate web driver for your browser and OS
# Create a new instance of the browser driver
def get_tweet(human_input):
    human = human_input

    response = openai.Completion.create(
    model="text-davinci-003",
    prompt="The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: "+ human +" \nAI:",
    temperature=0.9,
    max_tokens=2000,
    top_p=1,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=[" Human:", " AI:"]
    )
    titles = response.choices[0].text 
    return titles

def read_credentials(file_path):
    credentials = []
    with open(file_path, 'r') as file:
        for line in file:
            username, password = line.strip().split(',')
            credentials.append((username, password))
    return credentials

def get_video_files(directory):
    video_files = []
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            video_files.append(filename)
    return video_files

def t_send_message(file_path, DIRECTORY_PATH, human_input, api_key): 
    credentials = read_credentials(file_path)    
    openai.api_key = api_key
    try:
        for username, password in credentials:
            # Your code logic goes here
            # You can perform any operations using the username and password variables
            print(f"Username: {username} - Password: {password}")
            driver = webdriver.Chrome()  # Change to webdriver.Firefox() if using Firefox
            try:
                # Open Twitter
                driver.get("https://twitter.com")

                # Wait until the page is loaded
                wait = WebDriverWait(driver, 10)
                wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "body")))
                time.sleep(2)
                # Find and click the "Sign in" button
                login_element = driver.find_element(By.XPATH, "//span[contains(text(), 'Sign in')]")
                login_element.click()

                # Introduce a random delay between actions (e.g., 2 to 5 seconds)
                delay = random.randint(2000, 5000) / 1000.0
                time.sleep(delay)

                # Find the username input field and enter the username
                username_input = driver.find_element(By.CSS_SELECTOR, "input[name='text'][type='text']")
                username_input.send_keys(username)
                time.sleep(2)
                # Find and click the "Next" button
                next_element = driver.find_element(By.XPATH, "//span[contains(text(), 'Next')]")
                next_element.click()
                time.sleep(2)
                # Find the password input field and enter the password
                password_input = driver.find_element(By.CSS_SELECTOR, "input[name='password'][type='password']")
                password_input.send_keys(password)
                time.sleep(1)    

                for i in range(3):
                    driver.switch_to.active_element.send_keys(Keys.TAB)

                # Simulate pressing Enter key on the active element
                driver.switch_to.active_element.send_keys(Keys.ENTER)
                time.sleep(2)
                tweet_button = driver.find_element(By.CSS_SELECTOR, "a[data-testid='SideNav_NewTweet_Button']")
                tweet_button.click()

                time.sleep(2)  # Wait until the tweet box is shown
                
                tweet_button = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "a[data-testid='SideNav_NewTweet_Button']")))

                video_files = get_video_files(DIRECTORY_PATH)

                if video_files:
                    random_video_file = random.choice(video_files)
                    print("Random video file:", os.path.abspath(os.path.join(DIRECTORY_PATH, random_video_file)))
                    file_input = driver.find_element(By.CSS_SELECTOR, "input[type='file']")
                    file_input.send_keys(os.path.abspath(os.path.join(DIRECTORY_PATH, random_video_file)))
                else:
                    print("No video files found in the directory:", DIRECTORY_PATH)

                time.sleep(19)  # Sleep for 179 seconds

                tweet_box = wait.until(EC.presence_of_element_located((By.XPATH, "//div[@aria-label='Tweet text']")))
                tweet_box.send_keys(get_tweet(human_input))

                # Wait for the tweet to be ready to send
                time.sleep(2)

                # Find the tweet button and click it
                tweet_button = driver.find_element(By.XPATH, "//*[contains(text(),'Tweet')]")
                driver.execute_script("arguments[0].scrollIntoView();", tweet_button)
                driver.execute_script("arguments[0].click();", tweet_button)

                print("---------------------------------------------------------------------------")
                time.sleep(61.1)
                # Close the browser
                driver.quit()
            except Exception as e:
                driver.quit()
                print("An error occurred:", str(e))    

        
        time.sleep(160)        
    except Exception as e:
        print("An error occurred:", str(e))


