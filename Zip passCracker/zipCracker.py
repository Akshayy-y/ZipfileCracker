import zipfile

def brute_force_zip(zip_path, wordlist_path):
    zip_file = zipfile.ZipFile(zip_path)

    with open(wordlist_path, 'r') as f:
        for line in f:
            password = line.strip()
            try:
                zip_file.extractall(pwd=bytes(password, 'utf-8'))
                print(f"[+] Password found: {password}")
                return
            except:
                print(f"[-] Tried: {password}")
    
    print("[!] Password not found in wordlist.")

# Replace with your file paths
zip_path = 'Zip passCracker/test.zip'
wordlist_path = 'Zip passCracker/wordlist.txt'
brute_force_zip(zip_path, wordlist_path)
