# Day 17 - PassVault: Encrypted Password Manager
# Securely stores and retrieves passwords using AES encryption.

from cryptography.fernet import Fernet
import json
import os
import getpass
import time

DB_FILE = "vault_data.json"
KEY_FILE = "vault.key"


# ------------------------------------------------------
# Encryption / Decryption Handling
# ------------------------------------------------------
def generate_key():
    """Generate and save an encryption key (only once)."""
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)
    print("🔑 New encryption key generated and saved as vault.key.")
    return key


def load_key():
    """Load existing encryption key or create a new one if missing."""
    if not os.path.exists(KEY_FILE):
        return generate_key()
    with open(KEY_FILE, "rb") as key_file:
        return key_file.read()


def encrypt_data(data, key):
    """Encrypts text using the Fernet key."""
    f = Fernet(key)
    return f.encrypt(data.encode()).decode()


def decrypt_data(data, key):
    """Decrypts encrypted text."""
    f = Fernet(key)
    return f.decrypt(data.encode()).decode()


# ------------------------------------------------------
# Database Handling
# ------------------------------------------------------
def load_vault():
    """Load existing password vault."""
    if not os.path.exists(DB_FILE):
        return {}
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def save_vault(vault):
    """Save vault data to file."""
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(vault, f, indent=4)


# ------------------------------------------------------
# Core Vault Operations
# ------------------------------------------------------
def add_entry(vault, key):
    """Add new credential."""
    site = input("Enter site/app name: ").strip()
    username = input("Enter username/email: ").strip()
    password = getpass.getpass("Enter password (hidden): ").strip()
    encrypted_pass = encrypt_data(password, key)
    vault[site] = {"username": username, "password": encrypted_pass}
    save_vault(vault)
    print(f"✅ Saved credentials for {site}.")


def view_entry(vault, key):
    """View stored credential."""
    site = input("Enter site/app name to view: ").strip()
    if site in vault:
        decrypted_pass = decrypt_data(vault[site]["password"], key)
        print("\n🔓 Credentials:")
        print(f"Site: {site}")
        print(f"Username: {vault[site]['username']}")
        print(f"Password: {decrypted_pass}")
    else:
        print("⚠️ No credentials found for that site.")


def list_entries(vault):
    """List all stored sites."""
    if not vault:
        print("No entries stored yet.")
        return
    print("\n🗂️ Stored Accounts:")
    for i, site in enumerate(vault.keys(), 1):
        print(f" {i}. {site}")


def delete_entry(vault):
    """Delete a stored entry."""
    site = input("Enter site/app name to delete: ").strip()
    if site in vault:
        vault.pop(site)
        save_vault(vault)
        print(f"🗑️ Deleted credentials for {site}.")
    else:
        print("⚠️ No credentials found for that site.")


# ------------------------------------------------------
# Master Access System
# ------------------------------------------------------
def check_master_password():
    """Simulate master login for vault."""
    master = "admin123"  # you can change this
    entered = getpass.getpass("Enter master password to unlock vault: ").strip()
    if entered != master:
        print("❌ Access denied. Wrong master password.")
        exit()
    print("🔐 Access granted.\n")


# ------------------------------------------------------
# Main CLI Loop
# ------------------------------------------------------
def main():
    print("=" * 60)
    print(" PASSVAULT – ENCRYPTED PASSWORD MANAGER ".center(60))
    print("=" * 60)
    check_master_password()

    key = load_key()
    vault = load_vault()

    while True:
        print("\nOptions:")
        print(" 1. Add New Credential")
        print(" 2. View Credential")
        print(" 3. List All Entries")
        print(" 4. Delete Credential")
        print(" 5. Exit")
        choice = input("\nSelect an option (1-5): ").strip()

        if choice == "1":
            add_entry(vault, key)
        elif choice == "2":
            view_entry(vault, key)
        elif choice == "3":
            list_entries(vault)
        elif choice == "4":
            delete_entry(vault)
        elif choice == "5":
            print("👋 Exiting PassVault securely...")
            time.sleep(1)
            break
        else:
            print("⚠️ Invalid option, try again.")


if __name__ == "__main__":
    main()
