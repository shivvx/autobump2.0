from flask import Flask, jsonify
import discord
import asyncio
import os
import json

app = Flask(__name__)

# Config - Ideally these come from Environment Variables on Vercel
# But for now we'll try to read config.json if it exists, or Env Vars
def get_config():
    if os.path.exists('config.json'):
        with open('config.json', 'r') as f:
            return json.load(f)
    return {
        "token": os.environ.get("DISCORD_TOKEN"),
        "channels": json.loads(os.environ.get("CHANNELS", "[]"))
    }

config = get_config()
TOKEN = config.get('token')
CHANNELS = config.get('channels', [])

class OneTimeBumper(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bumped_count = 0
        self.errors = []

    async def on_ready(self):
        print(f'Logged in as {self.user}')
        await self.perform_bumps()
        await self.close()

    async def perform_bumps(self):
        for channel_id in CHANNELS:
            try:
                channel = self.get_channel(int(channel_id))
                if not channel:
                    self.errors.append(f"Channel {channel_id} not found")
                    continue

                # DISBOARD_BOT_ID = 302050872383242240
                found_command = None
                try:
                    # Search for slash command
                    async for command in channel.slash_commands(query="bump"):
                        if command.name == "bump": # Relaxed check for now
                            found_command = command
                            break
                except Exception as e:
                    self.errors.append(f"Error searching commands in {channel_id}: {str(e)}")

                if found_command:
                    await found_command(channel)
                    self.bumped_count += 1
                    print(f"Bumped in {channel.name}")
                    await asyncio.sleep(2) # Short delay to ensure it goes through
                else:
                    self.errors.append(f"No bump command found in {channel_id}")

            except Exception as e:
                self.errors.append(f"Failed in {channel_id}: {str(e)}")

async def run_bot():
    if not TOKEN:
        return {"status": "error", "message": "No token provided"}
    
    client = OneTimeBumper()
    try:
        await client.start(TOKEN)
    except Exception as e:
        return {"status": "error", "message": str(e)}
    
    return {
        "status": "success",
        "bumped": client.bumped_count,
        "errors": client.errors
    }

@app.route('/api/bump', methods=['GET'])
def trigger_bump():
    # Run the async bot logic using a fresh event loop
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    result = loop.run_until_complete(run_bot())
    loop.close()
    return jsonify(result)

@app.route('/')
def home():
    return "Autobump Bot API is running. Use /api/bump to trigger."

if __name__ == '__main__':
    app.run(debug=True)
