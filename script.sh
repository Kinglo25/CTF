#!/bin/bash
# Usage: ./bcrypt_bruteforce.sh file.bfe wordlist.txt

ENCRYPTED_FILE="$1"
WORDLIST="$2"
BCRYPT_PATH="bcrypt-1.1/bcrypt"

if [[ ! -f "$ENCRYPTED_FILE" || ! -f "$WORDLIST" ]]; then
  echo "Usage: $0 <encrypted_file> <wordlist>"
  exit 1
fi

while read -r KEY; do
  KEY=$(echo -n "$KEY" | tr -d '\n')
  echo "Trying key: $KEY"
  
  # Use expect to automate the interaction with bcrypt
  DECRYPTED_OUTPUT=$(expect -c "
    spawn $BCRYPT_PATH -o $ENCRYPTED_FILE
    expect \"Enter passphrase:\"
    send \"$KEY\r\"
    expect \"Enter passphrase:\"
    send \"$KEY\r\"
    expect eof
  " 2>&1)
  
  if [[ $? -eq 0 ]]; then
    echo "Success! Key found: $KEY"
    echo "Decrypted output: $DECRYPTED_OUTPUT"
    exit 0
  else
    echo "Failed with key: $KEY"
    echo "Output: $DECRYPTED_OUTPUT"
  fi
done < "$WORDLIST"

echo "Key not found in wordlist."
exit 1