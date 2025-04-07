# Events-Yerevan-Bot


Welcome to the **Events-Yerevan-Bot** repository! This is a Telegram bot designed to help users find upcoming events in Yerevan, Armenia. The bot allows users to select from three categories: **Concerts**, **Theatre**, and **Opera and Ballet**, and then shows events happening in those categories within the next 3 days.

---

## 🛠️ Features

- **Category-based Event Listings**: Choose from three categories: **Concerts**, **Theatre**, and **Opera and Ballet**.
- **Upcoming Events**: The bot fetches and displays a list of events happening within the next 3 days for the selected category.
- **Real-time Event Scraping**: The bot uses **Selenium** to scrape event data from websites in real-time.
- **Telegram Bot Interaction**: Users interact with the bot using inline keyboard buttons, making it simple and user-friendly.
- **Headless Web Scraping**: The bot uses **headless browsing** to scrape event data efficiently without opening a visible browser window.

---

## ⚙️ Technologies Used

- **Python 3.x**: The core programming language used for building the bot.
- **Selenium**: A Python library for automating web browsers and scraping event data from dynamic websites.
- **Chromedriver-autoinstaller**: Automatically installs the correct version of **ChromeDriver** based on the version of Chrome installed.
- **Telegram Bot API**: Using the `pyTelegramBotAPI` library to interact with the Telegram Bot API and create the bot.
- **Headless Chrome**: Used for efficient web scraping without opening a visible browser window.

---

## 🏁 Installation

### 📝 Prerequisites

Before running the bot, make sure you have the following installed:

- **Python 3.7 or higher**: The core programming language for the bot.
- **Telegram Bot Token**: You can get your bot token by chatting with [@BotFather](https://core.telegram.org/bots#botfather) on Telegram.
- **Google Chrome**: Ensure Google Chrome is installed on your machine.
- **ChromeDriver**: The `chromedriver-autoinstaller` will handle the installation of the correct version of ChromeDriver.

### 🔧 Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone https://github.com/AlinaMuradyan/Events-Yerevan-Bot.git
cd Events-Yerevan-Bot
```

### 📦 Step 2: Install Dependencies

To install the required Python libraries, run the following command:

```bash
pip install selenium chromedriver-autoinstaller pyTelegramBotAPI
```

### 🔑 Step 3: Set Up Telegram Bot Token

Create a `.env` file (or you can directly insert it into your code) and add your Telegram bot token, which you get from **@BotFather**. In your code, make sure you reference the token like this:

```python
TOKEN = 'your-telegram-bot-token'
```

### 🚀 Step 4: Run the Bot

You can now run the bot by executing the Python script. Make sure the main script is named something like `bot.py` (or adjust according to your file name). To run the bot, use:

```bash
python bot.py
```

Once the bot is running, it will be available on Telegram. You can start interacting with it using `/start` and choosing the available categories.

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
