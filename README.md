```md
# 🚨 **Smart Log Guardian — Real-Time Error Monitor & Alert System**  

<p align="center">
🌈 **Monitor • Detect • Alert • Automate • Protect** 🌈  
</p>

---

## 🔥 Overview  

**Smart Log Guardian** is an automated Python-based log monitoring tool that scans application log files, detects critical errors, and sends **real-time email alerts** using Gmail SMTP.  

Instead of manually checking logs, this tool acts like a digital watchdog — extracting error patterns, generating structured reports, and notifying you instantly when something goes wrong.  

This project is highly relevant for **DevOps, SRE, Cloud Support, and Production Support roles**.

---

## ✨ Features  

✅ Automatically reads system log files  
✅ Detects all `ERROR` messages  
✅ Generates a separate error report file  
✅ Sends instant email alerts when errors are found  
✅ Fully automated using Python  
✅ Simple, lightweight, and beginner-friendly  

---

## 🛠️ Tech Stack  

- **Python 3.x**  
- **SMTP (Gmail Mail Server)**  
- **File Handling**  
- **Basic Automation**

---

## 📁 Project Files  

```

📂 Smart-Log-Guardian/
│
├── app_log.txt          # Sample application log file
├── error_report.txt     # Auto-generated error report
└── log_monitor_email.py # Main Python script

````

---

## ▶️ How to Run the Project  

### Step 1 — Clone the repository  
```bash
git clone https://github.com/your-username/Smart-Log-Guardian.git
cd Smart-Log-Guardian
````

### Step 2 — Install dependencies

No external libraries required — uses Python’s built-in modules.

### Step 3 — Set up Gmail App Password

* Go to **Google Account → Security → App Passwords**
* Generate a 16-digit password
* Replace it in `log_monitor_email.py`

### Step 4 — Run the script

```bash
python log_monitor_email.py
```

If errors are found in the log file, you will receive an email alert immediately 🚀

---

## 🧠 How It Works

1. Reads `app_log.txt`
2. Searches for lines containing `"ERROR"`
3. Saves them into `error_report.txt`
4. Sends an email with all detected errors
5. Prints total number of errors in terminal

---

## 📌 Sample Output

**Email Subject:**

```
🚨 ALERT: Errors Found in System Logs
```

**Email Body:**

```
ERROR: Payment service failed  
ERROR: Static route timeout  
ERROR: API latency high  
```

---

## 🎯 Resume Impact

You can mention this project as:

> *Built an automated log monitoring system that detects production errors and sends real-time email alerts using Python and SMTP.*

---

## 🚀 Future Enhancements

🔹 Send alerts to Slack
🔹 Store logs in MySQL
🔹 Build a web dashboard
🔹 Connect with AWS CloudWatch
🔹 Add SMS notifications

---

## 👨‍💻 Author

**Harsh Anand**

⭐ If you like this project, please give it a **star on GitHub!**

```
```
