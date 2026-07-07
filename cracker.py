import time

# 1. This is the "target" password we want to crack
target_password = "secret123"

print(True)
print(f"[*] Starting brute-force attack against target password...")
time.sleep(1) # Adds a 1-second dramatic pause

# 2. Open our dictionary file and read the passwords
with open("passwords.txt", "r") as file:
    # Loop through each password in the file one by one
    for line in file:
        # Clean up the password (remove hidden spaces or new lines)
        guessed_password = line.strip()
        
        print(f"[~] Trying: {guessed_password}")
        time.sleep(0.5) # Slows it down so we can watch it work
        
        # 3. Check if the guess matches our target
        if guessed_password == target_password:
            print("\n" + "="*30)
            print(f"[+] SUCCESS! Password cracked: {guessed_password}")
            print("="*30)
            break
    else:
        # This runs if the loop finishes and never finds a match
        print("\n[-] Attack finished. Password not found in dictionary.")
