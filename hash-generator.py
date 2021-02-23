import hashlib
import binascii
import time

print(hashlib.algorithms_available)
# Spaces
print("")
print("")

# Banner
print(" ██░ ██  ▄▄▄        ██████  ██░ ██      ▄████ ▓█████  ███▄    █ ▓█████  ██▀███   ▄▄▄     ▄▄▄█████▓ ▒█████   ██▀███")
print("▓██░ ██▒▒████▄    ▒██    ▒ ▓██░ ██▒    ██▒ ▀█▒▓█   ▀  ██ ▀█   █ ▓█   ▀ ▓██ ▒ ██▒▒████▄   ▓  ██▒ ▓▒▒██▒  ██▒▓██ ▒ ██▒")
print("▒██▀▀██░▒██  ▀█▄  ░ ▓██▄   ▒██▀▀██░   ▒██░▄▄▄░▒███   ▓██  ▀█ ██▒▒███   ▓██ ░▄█ ▒▒██  ▀█▄ ▒ ▓██░ ▒░▒██░  ██▒▓██ ░▄█ ▒")
print("░▓█ ░██ ░██▄▄▄▄██   ▒   ██▒░▓█ ░██    ░▓█  ██▓▒▓█  ▄ ▓██▒  ▐▌██▒▒▓█  ▄ ▒██▀▀█▄  ░██▄▄▄▄██░ ▓██▓ ░ ▒██   ██░▒██▀▀█▄")
print("░▓█▒░██▓ ▓█   ▓██▒▒██████▒▒░▓█▒░██▓   ░▒▓███▀▒░▒████▒▒██░   ▓██░░▒████▒░██▓ ▒██▒ ▓█   ▓██▒ ▒██▒ ░ ░ ████▓▒░░██▓ ▒██▒")
print(" ▒ ░░▒░▒ ▒▒   ▓▒█░▒ ▒▓▒ ▒ ░ ▒ ░░▒░▒    ░▒   ▒ ░░ ▒░ ░░ ▒░   ▒ ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░ ▒▒   ▓▒█░ ▒ ░░   ░ ▒░▒░▒░ ░ ▒▓ ░▒▓░")
print("▒ ░▒░ ░  ▒   ▒▒ ░░ ░▒  ░ ░ ▒ ░▒░ ░     ░   ░  ░ ░  ░░ ░░   ░ ▒░ ░ ░  ░  ░▒ ░ ▒░  ▒   ▒▒ ░   ░      ░ ▒ ▒░   ░▒ ░ ▒░")
print("░  ░░ ░  ░   ▒   ░  ░  ░   ░  ░░ ░   ░ ░   ░    ░      ░   ░ ░    ░     ░░   ░   ░   ▒    ░      ░ ░ ░ ▒    ░░   ░")
print(" ░  ░  ░      ░  ░      ░   ░  ░  ░         ░    ░  ░         ░    ░  ░   ░           ░  ░            ░ ░     ░")

# Spaces
print("")
print("")

#Welcome
print("[+]Welcome to hash-generator! coded by c00LAgent")
print("")
print("[+]Github: https://github.com/c00LAgent/")
print("[+]Twitter: https://twitter.com/AgentGeneric")


# Spaces
print("")
print("")
print("")
print("[+]Select from the Hash Menu:")

# Spaces
print("")
print("")

print("0) MD5")
print("1) SHA1")
print("2) SHA256")
print("3) SHA512")
print("4) SHA384")
print("5) SHA224")
print("6) NTLM")

print("")
print("99) exit")

print("")

menuSelect = int(input("hash> "))

# Pick Hash Option From Menu
if menuSelect == 0:
    hashInput = input("Enter string:")

    #Spaces
    print("")

    md5 = hashlib.md5()
    md5.update(hashInput.encode('utf-8'))
    print(md5.hexdigest())

elif menuSelect == 99:
    # Exit

    # Spaces
    print("")
    print("")

    print("[+]Exiting...")
    time.sleep(0.5)
    exit()


elif menuSelect == 1:
    hashInput = input("Enter string:")

    # Spaces
    print("")

    sha1 = hashlib.sha1()
    sha1.update(hashInput.encode('utf-8'))
    print(sha1.hexdigest())




elif menuSelect == 2:
    hashInput = input("Enter string:")

    # Spaces
    print("")

    sha256 = hashlib.sha256()
    sha256.update(hashInput.encode('utf-8'))
    print(sha256.hexdigest())


elif menuSelect == 3:
    hashInput = input("Enter string:")

    # Spaces
    print("")

    sha512 = hashlib.sha512()
    sha512.update(hashInput.encode('utf-8'))
    print(sha512.hexdigest())

elif menuSelect == 4:
    hashInput = input("Enter string:")

    # Spaces
    print("")

    sha384 = hashlib.sha384()
    sha384.update(hashInput.encode('utf-8'))
    print(sha384.hexdigest())

elif menuSelect == 5:
    hashInput = input("Enter string:")

    # Spaces
    print("")

    sha224 = hashlib.sha224()
    sha224.update(hashInput.encode('utf-8'))
    print(sha224.hexdigest())

elif menuSelect == 6:
    hashInput = input("Enter string:")

    # Spaces
    print("")

    ntlm = hashlib.new('md4', hashInput.encode('utf-16le')).digest()
    print(binascii.hexlify(ntlm).decode())






else:
    print("Please Choose a hash from the menu")

    #Space and Time Sleep
    print("")
    print("")
    time.sleep(2)

    # Show Menu again
    print("0) MD5")
    print("1) SHA1")
    print("2) SHA256")
    print("3) SHA512")
    print("4) SHA384")
    print("5) SHA224")
    print("6) NTLM")

    print("")
    print("99) exit")
    print("")

    menuSelect = int(input("hash> "))




# Spaces
print("")
print("")

# Hash Again?
hashAgain = str(input("Hash more strings ?(y/n):"))

 # Spaces
print("")
print("")

while hashAgain == "y":
    time.sleep(2)

    # Show Menu again
    print("0) MD5")
    print("1) SHA1")
    print("2) SHA256")
    print("3) SHA512")
    print("4) SHA384")
    print("5) SHA224")
    print("6) NTLM")

    print("")
    print("99) exit")
    print("")

    menuSelect = int(input("hash> "))

    # Start Hashing Again
    if menuSelect == 0:
        hashInput = input("Enter string:")

        # Spaces
        print("")

        md5 = hashlib.md5()
        md5.update(hashInput.encode('utf-8'))
        print(md5.hexdigest())

        # Spaces
        print("")
        print("")

        hashAgain = str(input("Hash more strings ?(y/n):"))

    elif menuSelect == 99:
        # Exit

        # Spaces
        print("")
        print("")

        print("[+] Exiting...")
        time.sleep(0.5)
        exit()



    elif menuSelect == 1:
        hashInput = input("Enter string:")

        # Spaces
        print("")

        sha1 = hashlib.sha1()
        sha1.update(hashInput.encode('utf-8'))
        print(sha1.hexdigest())

        # Spaces
        print("")
        print("")

        hashAgain = str(input("Hash more strings ?(y/n):"))





    elif menuSelect == 2:
        hashInput = input("Enter string:")

        # Spaces
        print("")

        sha256 = hashlib.sha256()
        sha256.update(hashInput.encode('utf-8'))
        print(sha256.hexdigest())

        # Spaces
        print("")
        print("")

        hashAgain = str(input("Hash more strings ?(y/n):"))


    elif menuSelect == 3:
        hashInput = input("Enter string:")

        # Spaces
        print("")

        sha512 = hashlib.sha512()
        sha512.update(hashInput.encode('utf-8'))
        print(sha512.hexdigest())

        # Spaces
        print("")
        print("")

        hashAgain = str(input("Hash more strings ?(y/n):"))


    elif menuSelect == 4:
        hashInput = input("Enter string:")

        # Spaces
        print("")

        sha384 = hashlib.sha384()
        sha384.update(hashInput.encode('utf-8'))
        print(sha384.hexdigest())

        # Spaces
        print("")
        print("")

        hashAgain = str(input("Hash more strings ?(y/n):"))


    elif menuSelect == 5:
        hashInput = input("Enter string:")

        # Spaces
        print("")

        sha224 = hashlib.sha224()
        sha224.update(hashInput.encode('utf-8'))
        print(sha224.hexdigest())

        # Spaces
        print("")
        print("")

        hashAgain = str(input("Hash more strings ?(y/n):"))


    elif menuSelect == 6:
        hashInput = input("Enter string:")

        # Spaces
        print("")

        ntlm = hashlib.new('md4', hashInput.encode('utf-16le')).digest()
        print(binascii.hexlify(ntlm).decode())

        # Spaces
        print("")
        print("")

        hashAgain = str(input("Hash more strings ?(y/n):"))





    else:
        print("Please Choose a hash from the menu")

        # Space and Time Sleep
        print("")
        print("")
        time.sleep(2)

        # Show Menu again
        print("0) MD5")
        print("1) SHA1")
        print("2) SHA256")
        print("3) SHA512")
        print("4) SHA384")
        print("5) SHA224")
        print("6) NTLM")

        print("")
        print("99) exit")
        print("")

        menuSelect = int(input("hash> "))

if hashAgain == "n":
    # Exit

    #Spaces
    print("")
    print("")

    print("[+] Exiting...")
    time.sleep(0.5)
    exit()

