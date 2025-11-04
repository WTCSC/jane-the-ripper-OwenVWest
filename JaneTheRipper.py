import hashlib, time

def type_out(text, delay=0.01):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)

def PasswordCrack(hash_file, wordlist_file, hashtype): #paths for hash and wordlist files
    with open(hash_file, 'r') as hashF:
        finallist = []
        hashS = set()
        for line in hashF:
            hashS.add(line.strip())
        with open(wordlist_file, 'r') as hashWordlist:
            for line in hashWordlist:
                wordCurrent = line.strip()
                if hashtype == "md5":
                    hashObject = hashlib.md5(wordCurrent.encode())
                elif hashtype == "SHA-1":
                    hashObject = hashlib.sha1(wordCurrent.encode())
                elif hashtype == "SHA-256":
                    hashObject = hashlib.sha256(wordCurrent.encode())
                else:
                    finallist = ["Failed"]
                    return finallist
                hashCurrent = hashObject.hexdigest()
                if hashCurrent in hashS:
                    finallist.append(f"[+] Succeeded, {hashCurrent} --> {wordCurrent}")
                else:
                    finallist.append(f"[-] Failed, {hashCurrent}")
    return finallist
def main():
    
    hash_file = input("Input path to hash list file: ") # jane-the-ripper-OwenVWest/hashes.txt
    word_file = input("Input path to word list file: ") # jane-the-ripper-OwenVWest/wordlist.txt
    typehash = input("What type of hash do you want to use? (md5, SHA-1 and SHA-256 are supported): ")
    type_out("\n-------Hash Cracking Start-------\n\n")
    outputlist = PasswordCrack(hash_file, word_file, typehash)
    for item in outputlist:
        print(item)
    type_out("\n-------Hash Cracking End-------")
    if outputlist == ["Failed"]:
        print("\n\n[/] All hashes failed succsessfully, (Input a valid hash from the list of supported hash types)\n")
    else:
        print("\n\n[!] All hashes cracked successfully!\n")
main()