# 🛡️ File Integrity Checker

This is a simple **Python-based tool** to **monitor changes in files** by calculating and comparing their cryptographic hash values. It helps detect unauthorized changes or corruption — a key practice in cybersecurity.

> ✅ Built as part of my internship at **CodTech** for the **File Integrity Checking** task.

---

## 📌 Why This Tool?

When a file changes, its hash changes. This tool uses **SHA-256** (a cryptographic hash function) to:

- 🔐 Create a **baseline** of original file hashes  
- 🔍 Detect if a file was **modified**, **deleted**, or **replaced**  
- ✅ Confirm file integrity over time

---

## 🚀 Features

- ✔️ Save baseline hash values of multiple files  
- ✔️ Re-check files and detect changes  
- ✔️ Easy command-line interface  
- ✔️ Auto-generates a `hashes.json` to store file hashes securely  

---

## 🛠️ Technologies Used

| Library     | Why It’s Used                                   |
|-------------|-------------------------------------------------|
| `hashlib`   | To compute secure SHA-256 hash values           |
| `os`        | To check file existence                         |
| `json`      | To store and load hash values persistently      |

---

## 📂 Project Structure

```
File-Integrity-Checker/
│
├── file_integrity_checker.py   # Main script
├── hashes.json                 # (Auto-generated after baseline)
├── README.md                   # Project guide
└── important.txt               # Sample test file
```

---

## ⚙️ How to Run

### 🔹 Step 1: Save hash baseline
```bash
python file_integrity_checker.py
```
- Choose option `1`
- Enter file names separated by comma (example: `important.txt,report.pdf`)

### 🔹 Step 2: Check integrity later
- Choose option `2`
- The tool will compare current hashes with stored ones

### 🔹 Step 3: Exit the program
- Choose option `3`

---

## 🧪 Example Usage

```
Enter choice (1/2/3): 1  
Enter file names (comma-separated): important.txt, report.pdf  
✅ Baseline saved  

Enter choice (1/2/3): 2  
❌ important.txt has been CHANGED!  
✅ report.pdf is OK  
```

---

## 🧠 How It Works (In My Words)

- It reads the file in binary and computes its **SHA-256 hash**  
- On "baseline", it saves these hashes to a JSON file  
- Later, it re-computes hashes and compares with baseline  
- If different, the file is flagged as **modified**

---

## 📈 Learning Outcome

> I learned how to build a real-world File Integrity Monitoring tool using core Python concepts like file I/O, hashing, JSON handling, and condition checks — with a solid understanding of why each piece is important in cybersecurity.

---

## ✅ Task Status

- [x] Task 1: File Integrity Checker ✅  
- [ ] Task 2: *(Pending)*  
- [ ] Task 3: *(Pending)*  
- [ ] Task 4: *(Pending)*  

---

## 🏁 Internship Goal

Complete all 4 tasks and publish them on GitHub to qualify for the **completion certificate** on internship end date.

---

## 👨‍💻 Author

**Adhyan Raghav**  
Cybersecurity Intern at CodTech  
GitHub: [github.com/AdhyanRaghav](https://github.com/AdhyanRaghav)
