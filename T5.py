import os
import json
from eth_account.messages import encode_defunct
from eth_account import Account
import time
from web3 import Web3
import eth_keys.exceptions


YOUR_CONTRACT_ABI = '[{"constant":true,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_tokenId","type":"uint256"}],"name":"ownerOf","outputs":[{"name":"","type":"address"}],"payable":false,"stateMutability":"view","type":"function"},{"constant":true,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":false,"stateMutability":"view","type":"function"}]'
provider = Web3.HTTPProvider('https://mainnet.infura.io/v3/6de1bfac1d654305b4ac7eeb6ab89b08')
web3 = Web3(provider)

def verify_signed_message(message, signature, public_address):
    # Skip signature verification if signature, account address, or message is empty
    if not signature or not public_address or not message:
        return False

    message = encode_defunct(text=message)

    # Verify the signature
    try:
        signer = Account.recover_message(message, signature=signature)
    except:
        # Signature verification failed
        return False

    # Verify if the signer's address matches the provided public address
    return signer == public_address

save_directory = "../bnetly"  # Update the save directory name

while True:
    # Get the list of files in the directory
    files = os.listdir(save_directory)

    # Filter and process the text files
    txt_files = [file for file in files if file.endswith('.txt')]
    for txt_file in txt_files:
        file_path = os.path.join(save_directory, txt_file)

        # Read the content of the text file
        with open(file_path, "r", encoding="utf-8", errors="ignore") as file:
            content = file.read()

        # Remove the first part of the string
        delimiter = "Data Request"
        if content.startswith(delimiter):
            content = content[len(delimiter):]

        try:
            # Parse the content as JSON
            data = json.loads(content)

            # Access the values in the parsed JSON
            key = data.get("key")
            value = data.get("value")
            account_address = data.get("accountAddress")
            signature = data.get("signature")

            # Print the parsed values
            print("File:", txt_file)
            print("Key:", key)
            print("Value:", value)
            print("Account Address:", account_address)
            print("Signature:", signature)

            is_valid = verify_signed_message(value, signature, account_address)
            print("Signature verification result:", is_valid)

            # Create a new file for the verification result in JSON format
            result_file_path = os.path.join(save_directory, f"{txt_file}.bnetly.json")
            
            # Check if the file already exists
            if os.path.exists(result_file_path):
                print("Verification result file already exists:", result_file_path)
                continue

            total_supply =  0

            if account_address:
                contract_address = "0x81c08F832Fbc5716Bb3fA551D4Ee265C12bF6921"
                contract = web3.eth.contract(address=contract_address, abi=YOUR_CONTRACT_ABI)
                total_supply = contract.functions.balanceOf(account_address).call()
            else:
                print("Invalid account address.")

            result_data = {
                "File": txt_file,
                "Key": key,
                "Value": value,
                "Account Address": account_address,
                "Signature": signature,
                "Signature Verification Result": is_valid,
                "Total Supply": total_supply
            }

            with open(result_file_path, "w") as result_file:
                json.dump(result_data, result_file)

            print("Verification result saved to:", result_file_path)

        except json.JSONDecodeError:
            print("Error parsing JSON in file:", txt_file)
            print()
        except eth_keys.exceptions.BadSignature as e:
            print("Invalid signature format in file:", txt_file)
            print("Error:", str(e))
            print()
    
    time.sleep(2)