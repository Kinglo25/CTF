import subprocess

# Define the path to the bcrypt binary and the words.txt file
bcrypt_path = './bcrypt-1.1/bcrypt'
input_file = 'password_dictionary.txt'

# Read the encryption keys from words.txt
with open(input_file, 'r') as file:
    keys = file.readlines()

# Loop through each key and run the bcrypt command
for key in keys:
    key = key.strip()  # Remove any extra spaces or newline characters
    if key:  # Skip empty lines
        print(f'Testing key: {key}')
        # Run the bcrypt command with the current encryption key
        result = subprocess.run([bcrypt_path, 'pipex.bfe'], input=key, text=True, capture_output=True)

        # Check the output to determine if this key is correct
        # If the output contains a success message or matches the hash, break the loop
        if result.returncode == 0:  # Check if the command executed successfully
            # If bcrypt's output indicates success, you can stop the script
            print(f'Key found: {key}')
            break
        else:
            # You can add any specific checks to see if the output matches your expected result
            # For example, checking result.stdout for certain strings
            pass

