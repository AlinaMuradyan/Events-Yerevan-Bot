# Events-Yerevan-Bot


Welcome to the **Events-Yerevan-Bot** repository! This is a Telegram bot designed to help users find upcoming events in Yerevan, Armenia. The bot allows users to select from three categories: **Concerts**, **Theatre**, and **Opera and Ballet**, and then shows events happening in those categories within the next 3 days.

---

## 🛠️ Features

- **Category-based Event Listings**: Users can choose from three categories: **Concerts**, **Theatre**, and **Opera and Ballet**.
- **Upcoming Events**: The bot fetches and displays events happening in the next 3 days from the selected category.
- **User-friendly Interface**: Simple button-based interaction, no need for complicated commands.

---

## ⚙️ Technologies Used

- **Python**: The core programming language used to build the bot.
- **Selenium**: A Python library for web scraping that automates the process of browsing and fetching event data from websites.
- **python-telegram-bot**: A Python library to interact with the Telegram Bot API.
- **ChromeDriver**: Used with Selenium to interact with the Chrome browser during scraping.

---

## 🏁 Installation

### 📝 Prerequisites

- Python 3.7 or higher
- A Telegram bot token (you can create a bot via [@BotFather](https://core.telegram.org/bots#botfather) on Telegram)
- **Selenium WebDriver**
- Chrome browser and corresponding **ChromeDriver** version
- Libraries: `python-telegram-bot`, `selenium`, `requests` (and any other necessary libraries)

### 🔧 Step 1: Clone the Repository

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/AlinaMuradyan/Events-Yerevan-Bot.git
cd Events-Yerevan-Bot
```

### 📦 Step 2: Install Dependencies

Install the required Python libraries:

```bash
pip install python-telegram-bot
pip install selenium
```

You also need **ChromeDriver** to run Selenium. Make sure to download the appropriate version of **ChromeDriver** that matches your installed version of Chrome from [here](https://sites.google.com/a/chromium.org/chromedriver/downloads), and make sure it's accessible in your system’s PATH.

### 🔑 Step 3: Add Your Telegram Bot Token

In the project directory, open the Python file where the bot token is stored (usually `bot.py` or a similar file). Add your Telegram Bot API token:

```python
TOKEN = 'your-telegram-bot-token'
```

You can get your Telegram bot token by chatting with [@BotFather](https://core.telegram.org/bots#botfather).

### 🚀 Step 4: Run the Bot

You can now run the bot locally:

```bash
python bot.py
```

The bot will be available for testing and usage directly from your local machine.

---

## 🔎 Usage

### Available Commands

1. **`/start`**: Starts the bot and presents the user with buttons to choose one of the event categories: **Concerts**, **Theatre**, or **Opera and Ballet**.
2. **Category Selection**: Once a user clicks on one of the buttons, the bot will display a list of events for the next 3 days in the selected category.

### Example Flow

1. The user types `/start`.
2. The bot responds with three buttons: **Concerts**, **Theatre**, **Opera and Ballet**.
3. The user clicks on one of the buttons.
4. The bot shows a list of events happening in the next 3 days for that selected category (Concerts, Theatre, or Opera and Ballet).

### Sample Interaction

- `/start`: Bot responds with buttons:
  - **Concerts**
  - **Theatre**
  - **Opera and Ballet**

- User clicks **Concerts**:
  - Bot responds with upcoming concerts for the next 3 days in Yerevan.

---

## 🛠️ Contributing

Feel free to fork the repository, submit issues, and open pull requests for any improvements or bug fixes! If you have ideas for additional features, don't hesitate to share them.

### Steps to Contribute:

1. Fork the repository.
2. Clone your fork:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Events-Yerevan-Bot.git
   ```
3. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
4. Make your changes and commit them:
   ```bash
   git commit -m "Added feature"
   ```
5. Push to your fork:
   ```bash
   git push origin feature-name
   ```
6. Open a pull request with a clear description of your changes.

---

## 💡 Acknowledgments

- [python-telegram-bot](https://github.com/python-telegram-bot/python-telegram-bot) for providing the library that interacts with the Telegram Bot API.
- [Selenium](https://www.selenium.dev/documentation/en/) for web scraping and automating the browsing process to collect event data.
- Event sources for providing the information about events in Yerevan.
