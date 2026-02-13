# Discord Autobump Bot (Vercel + Vite Edition)

A 24/7 Discord Autobump bot hosted on Vercel Serverless Functions with a modern React Dashboard.

## Features
- **Serverless Architecture**: Runs on Vercel (Free Tier compatible).
- **Cron Jobs**: Automatically bumps every 30 minutes.
- **Modern Dashboard**: Monitor status and trigger manual bumps via a sleek UI.
- **Stealth Mode**: Uses `discord.py-self` to automate user accounts.

## Deployment Guide (Vercel)

### Option 1: Vercel CLI (Recommended if you have it)
1. Run `vercel` in this directory.
2. Follow the prompts.
3. Set Environment Variables (see below).

### Option 2: GitHub Integration
1. Push this code to a GitHub repository.
2. Import the project in Vercel Dashboard.
3. Vercel will automatically detect the Vite frontend and Python API.

### Environment Variables
For security, set these in Vercel Project Settings (Settings -> Environment Variables):
- `DISCORD_TOKEN`: Your user token.
- `CHANNELS`: JSON array of channel IDs, e.g., `["123456789", "987654321"]`.

> **Note**: The bot will fallback to `config.json` if these are not set, but using Environment Variables is more secure.

## Local Development
1. **Backend**:
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   python api/index.py
   ```
2. **Frontend** (Requires Node.js):
   ```bash
   npm install
   npm run dev
   ```

## Cron Job
The bot is configured to run every 30 minutes via `vercel.json`. You can check the "Cron Jobs" tab in your Vercel Dashboard to see execution history.
# autobump2.0
