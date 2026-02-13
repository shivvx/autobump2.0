# Discord Autobump Bot

A self-bot script to automatically run the `/bump` command in specified Discord channels.

> ⚠️ **WARNING**: Automating user accounts (self-botting) is against Discord's Terms of Service. Use this software at your own risk. The author is not responsible for any account bans or restrictions.

## Prerequisites

- Python 3.8 or higher
- A Discord user token (DO NOT SHARE THIS WITH ANYONE)

## Installation

1.  **Initialize the virtual environment**:
    ```bash
    python3 -m venv venv
    ```

2.  **Install dependencies**:
    ```bash
    ./venv/bin/pip install -r requirements.txt
    ```

## Configuration

1.  Open `config.json` in a text editor.
2.  Replace `"YOUR_USER_TOKEN_HERE"` with your actual Discord user token.
3.  Update the `channels` list with the Channel IDs where you want to send the bump command.
4.  (Optional) Adjust `interval_minutes` if you want a different frequency (default is 30 minutes).

```json
{
  "token": "YOUR_TOKEN",
  "channels": [
    "CHANNEL_ID_1",
    "CHANNEL_ID_2"
  ],
  "interval_minutes": 30
}
```

## 🚀 How to Run

1.  Open your **Terminal**.
2.  Navigate to the project folder:
    ```bash
    cd /Users/shiv/Documents/autobump
    ```
3.  **Run the bot with this command:**
    ```bash
    ./venv/bin/python main.py
    ```

> Note: Make sure you have installed the dependencies first (see Installation section).

The bot will log in and start the loop. It will check for the `/bump` command (specifically for Disboard) in the specified channels and trigger it.

## Troubleshooting

- **Webhook Error 404**: If you see `Failed to send webhook log: 404`, check that your Webhook URL in `config.json` is correct and hasn't been deleted.
- **"Could not find '/bump' command"**: Ensure that the Disboard bot is in the server and you have permissions to view and use its commands in that channel.
- **Login errors**: Double-check your user token.
# discordbump
