#!/bin/bash

# Usage: ./bcrypt_bruteforce.sh file.bfe wordlist.txt

ENCRYPTED_FILE="$1"
WORDLIST="$2"
BCRYPT_PATH="/home/wiklo/CTF/bcrypt-1.1/bcrypt"

if [[ ! -f "$ENCRYPTED_FILE" || ! -f "$WORDLIST" ]]; then
  echo "Usage: $0 <encrypted_file> <wordlist>"
  exit 1
fi

while IFS= read -r KEY; do
  KEY=$(echo -n "$KEY" | tr -d '\r\n')
  echo "Trying key: $KEY"
  DECRYPTED_OUTPUT=$(echo "$KEY" | "$BCRYPT_PATH" -o "$ENCRYPTED_FILE" 2>&1)
  
  if [[ $? -eq 0 ]]; then
    echo "Success! Key found: $KEY"
    echo "Decrypted output: $DECRYPTED_OUTPUT"
    exit 0
  fi
done < "$WORDLIST"

echo "Key not found in wordlist."
exit 1