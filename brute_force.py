def menu():
    print("\n=== TOOLS BRUTE FORCE ===")
    print("1. Brute Force Login File Sederhana")
    print("2. Brute Force PIN File Terkunci")
    print("0. Keluar")

def file_login_bruteforce():
    print("\n--- Brute Force Login File Sederhana ---")
    target_user = input("Username target: ")
    wordlist_path = input("Masukkan path ke wordlist password: ")
    database_file = input("Masukkan path ke file login.txt (username:password): ")

    try:
        # Ambil data username:password dari file login.txt
        credentials = {}
        with open(database_file, "r") as f:
            for line in f:
                user, pw = line.strip().split(":")
                credentials[user] = pw

        # Buka wordlist dan brute force
        with open(wordlist_path, "r") as f:
            for line in f:
                password = line.strip()
                print(f"[!] Mencoba: {target_user}:{password}")
                if target_user in credentials and credentials[target_user] == password:
                    print(f"[+] Password ditemukan: {password}")
                    return
        print("[-] Password tidak ditemukan.")
    except Exception as e:
        print(f"[ERROR] {e}")

def pin_file_bruteforce():
    print("\n--- Brute Force PIN File Terkunci ---")
    file_path = input("Masukkan path ke file pinlock.txt: ")
    wordlist_path = input("Masukkan path ke wordlist PIN: ")

    try:
        with open(file_path, "r") as f:
            encrypted = f.read().strip()

        with open(wordlist_path, "r") as f:
            for pin in f:
                pin = pin.strip()
                if pin == encrypted:
                    print(f"[+] PIN ditemukan: {pin}")
                    return
                else:
                    print(f"[!] Mencoba PIN: {pin}")
        print("[-] PIN tidak ditemukan.")
    except Exception as e:
        print(f"[ERROR] {e}")

# Main loop
while True:
    menu()
    pilihan = input("Pilih fitur (0-2): ")

    if pilihan == "1":
        file_login_bruteforce()
    elif pilihan == "2":
        pin_file_bruteforce()
    elif pilihan == "0":
        print("Keluar dari tools.")
        break
    else:
        print("Pilihan tidak valid.")
