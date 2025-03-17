# Tanami Capital QA Testing Challenge

## 📌 Overview
This repository contains the comprehensive QA test plan, manual test cases, API testing strategy, and automation scripts for Tanami Capital's Payment Processing Module.

## 📂 Repository Structure
```
📂 tanami-qa-task/
│── 📂 docs/                  # Documentation Files
│    ├── Selenium_Automation_Script.pdf
│    ├── Bonus_Tasks.pdf
│    ├── Comprehensive_Test_Plan.pdf
│    ├── Detailed_Manual_Test_Cases.pdf
│    ├── API_Testing_Strategy.pdf
│── 📂 automation/            # Selenium Automation Scripts
│    ├── test_successful_payment.py
│    ├── test_data.json
│    ├── test_logs.log
│── README.md                 # Project Overview & Setup Instructions
```

---

## 🚀 Setup Instructions

### 1️⃣ Clone the repository
To get started, clone this repository to your local machine using:
```sh
git clone https://github.com/aliaaosama97/tanami-qa-task.git
```
Then navigate into the project directory:
```sh
cd tanami-qa-task
```

### 2️⃣ Install Required Dependencies
Make sure you have **Python** installed on your system. You also need to install Selenium to run the automation scripts. Run the following command:
```sh
pip install selenium
```

If you don't have **Google Chrome** and **Chrome WebDriver**, install them:
- **Download Chrome**: [https://www.google.com/chrome/](https://www.google.com/chrome/)
- **Download ChromeDriver**: [https://chromedriver.chromium.org/downloads](https://chromedriver.chromium.org/downloads)

Place `chromedriver.exe` in the same directory as your Selenium script or add it to your system path.

### 3️⃣ Run the Selenium Automation Test
To execute the test script, run:
```sh
python automation/test_successful_payment.py
```

---

## 🛠️ Tools Used
- **Selenium WebDriver** - For UI automation testing.
- **Python** - Used for scripting automation tests.
- **Git & GitHub** - For version control and repository management.

---

