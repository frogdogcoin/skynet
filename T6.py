import os
import time
import json
import sys
import T1

print(str(len(sys.argv)))

directory_path = "../bnetly"

if os.getenv("OPENAI_API_KEY"):
    if len(sys.argv) < 2:
        print("T6 Please provide the DIRECTORY_PATH, file_path, human input, and OpenAI key as command line arguments.")
        sys.exit(1)
    DIRECTORY_PATH_MEDIA = sys.argv[1]
    file_path_credentials = sys.argv[2]
    api_key = os.getenv("OPENAI_API_KEY")

else:
    if len(sys.argv) < 3:
        print("T6 Please provide the DIRECTORY_PATH, file_path, and human input as command line arguments.")
        sys.exit(1)
    DIRECTORY_PATH_MEDIA = sys.argv[1]
    file_path_credentials = sys.argv[2]
    api_key = sys.argv[3]


print(api_key)


def parse_json_file(file_path, file_path_credentials, DIRECTORY_PATH_MEDIA, api_key):
    try:
        with open(file_path, 'r') as file:
            json_data = json.load(file)

            file = json_data.get("File", "")
            key = json_data.get("Key", "")
            value = json_data.get("Value", "")
            account_address = json_data.get("Account Address", "")
            signature = json_data.get("Signature", "")
            signature_verification_result = json_data.get("Signature Verification Result", False)
            balance_of = json_data.get("Total Supply", 0)

            print("File:", file)
            print("Key:", key)
            print("Value:", value)
            print("Account Address:", account_address)
            print("Signature:", signature)
            print("Signature Verification Result:", signature_verification_result)
            print()

            # Create a new file path with ".done" extension
            new_file_name = os.path.splitext(os.path.basename(file_path))[0] + ".done"
            new_file_path = os.path.join(os.path.dirname(file_path), new_file_name)

            # Write the parsed information into the new file
            file_content = f"File: {file}\nKey: {key}\nValue: {value}\nAccount Address: {account_address}\nSignature: {signature}\nSignature Verification Result: {signature_verification_result}\n"
            array = [value, str(signature_verification_result), str(balance_of)]
            human_input = value
            T1.t_send_message(file_path_credentials, DIRECTORY_PATH_MEDIA, human_input, api_key)

            with open(new_file_path, 'w') as new_file:
                new_file.write(file_content)

    except Exception as e:
        print(e)

while True:
    try:
        for json_file in os.listdir(directory_path):
            if json_file.endswith(".json") and os.path.isfile(os.path.join(directory_path, json_file)):
                file_path = os.path.join(directory_path, json_file)
                base_name = os.path.splitext(json_file)[0]
                other_extension = ".done"
                other_file = os.path.join(directory_path, base_name + other_extension)

                if not os.path.exists(other_file):
                    parse_json_file(file_path, file_path_credentials, DIRECTORY_PATH_MEDIA, api_key)

        time.sleep(0.5)

    except Exception as e:
        print(e)
