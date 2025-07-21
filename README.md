# File-Integrity-Checker

# 🔐 File Integrity Checker

A simple Python project to monitor and verify the integrity of important files using SHA-256 hashing.

## 📌 Features

- Generates SHA-256 hashes for files
- Stores original hash values in `hashes.json`
- Compares current file hashes with baseline to detect tampering
- Command-line menu for easy interaction

## 🚀 How It Works

1. **Create Baseline Hashes**  
   Generates and stores hashes for your selected files.

2. **Check File Integrity**  
   Compares current file hash with stored value and alerts if any file has changed.

## 🛠️ Technologies Used

- Python 3.x
- `hashlib`, `json`, `os` libraries (standard)

## 🎮 How to Run

```bash
python file_integrity_checker.py
