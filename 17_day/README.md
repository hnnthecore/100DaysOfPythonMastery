# 🔐 Day 17 – PassVault: Encrypted Password Manager

> *"Because even developers deserve privacy."*

---

![PassVault Illustration](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/passvault.png)

---

### 🧠 Concepts Practised
- AES Encryption & Decryption using `cryptography.fernet`
- Secure File Storage and Key Management
- JSON Database Handling
- CLI-Based User Interaction
- Password Input with `getpass` for Privacy
- Error Handling and Persistence

---

### 💡 Project Overview
**PassVault** is a command-line password manager that safely stores your credentials in an **encrypted vault**.  
It uses AES-level encryption to secure your data with a unique key, and only you can decrypt it.

No online servers, no third-party storage — everything stays **offline and private**.

---

### ⚙️ Features
✅ Generate & store an encrypted key (`vault.key`)  
✅ Add, view, delete, and list credentials  
✅ Password input hidden during entry  
✅ Auto-saves all data in `vault_data.json`  
✅ Master password access control  
✅ Works 100% offline  

---

### 🧩 Screenshots & Output

#### 💻 Program Output

![Program Output](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day17_output.png)

#### 💾 Encrypted JSON File

![Vault JSON](https://raw.githubusercontent.com/hnnthecore/100DaysOfPythonMastery/refs/heads/main/assets/day17_jsonfile.png)

---

### 🚀 How to Run
1. Install dependency:
   ```bash
   pip install cryptography
