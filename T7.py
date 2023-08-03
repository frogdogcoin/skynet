import os
import time
import json
import sys
import T1

print(str(len(sys.argv)))

directory_path = "../bnetly"

if os.getenv("OPENAI_API_KEY"):
    if len(sys.argv) < 2:
        print("T7 Please provide the DIRECTORY_PATH, file_path, human input, and OpenAI key as command line arguments.")
        sys.exit(1)
    DIRECTORY_PATH_MEDIA = sys.argv[1]
    file_path_credentials = sys.argv[2]
    api_key = os.getenv("OPENAI_API_KEY")
    human_input = sys.argv[3]

else:
    if len(sys.argv) < 3:
        print("T7 Please provide the DIRECTORY_PATH, file_path, and human input as command line arguments.")
        sys.exit(1)
    DIRECTORY_PATH_MEDIA = sys.argv[1]
    file_path_credentials = sys.argv[2]
    api_key = sys.argv[3]
    human_input = sys.argv[4]

print(api_key)



while True:
    try:

        T1.t_send_message(file_path_credentials, DIRECTORY_PATH_MEDIA, human_input, api_key)

        time.sleep(0.5)

    except Exception as e:
        print(e)
