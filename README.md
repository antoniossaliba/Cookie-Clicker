# 🍪 Automated Cookie Clicker Bot using Selenium

This project is a Python automation script that plays the [Cookie Clicker](https://orteil.dashnet.org/cookieclicker/) game using Selenium WebDriver. It automatically clicks the cookie and purchases upgrades to maximize cookie production over time.

## 📸 Demo
![Demo GIF](demo.gif) <!-- You can include a screen recording of your bot running -->

---

## 🚀 Features

- Automatic cookie clicking at high speed
- Intelligent purchase of upgrades and items to increase efficiency
- Configurable time limits and speed
- Logs performance data in the console

---

## 🧰 Requirements

- Python 3.7+
- Google Chrome (or any supported browser)
- ChromeDriver (compatible with your Chrome version)
- Required Python packages:
  - `selenium`
  - `time`

---

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/cookie-clicker-bot.git
   cd cookie-clicker-bot
🧠 How It Works
Opens the Cookie Clicker website.

Continuously clicks the big cookie.

Every few seconds, checks available upgrades and purchases the most expensive affordable ones.

Continues running until the specified time limit is reached.

📝 Usage
bash
Copy
Edit
python cookie_clicker_bot.py
You can optionally edit the script to:

Adjust click speed

Set runtime duration

Customize upgrade-buying strategy

⚠️ Disclaimer
This project is for educational and entertainment purposes only. Do not use automation to interact with web services in ways that violate their terms of service.

💡 Ideas for Improvements
Add GUI controls using Tkinter

Save and load progress using cookies/localStorage

Use multi-threading for better performance

Add analytics on CPS (cookies per second) over time

📜 License
This project is licensed under the MIT License. See LICENSE for details
