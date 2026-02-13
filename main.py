import discord
import json
import asyncio
import random
import os
from datetime import datetime

# Load configuration
def load_config():
    if not os.path.exists('config.json'):
        print("Error: config.json not found!")
        return None
    with open('config.json', 'r') as f:
        return json.load(f)

config = load_config()

if not config:
    exit(1)

TOKEN = config.get('token')
CHANNELS = config.get('channels', [])
INTERVAL_MINUTES = config.get('interval_minutes', 30)

if not TOKEN or TOKEN == "YOUR_USER_TOKEN_HERE":
    print("Error: Please set your user token in config.json")
    exit(1)

class AutoBumpBot(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.bump_task = None

    async def on_ready(self):
        print(f'Logged in as {self.user} (ID: {self.user.id})')
        print(f'Running autobump every {INTERVAL_MINUTES} minutes on {len(CHANNELS)} channels.')
        
        if not self.bump_task:
            self.bump_task = self.loop.create_task(self.bump_loop())

    async def bump_loop(self):
        await self.wait_until_ready()
        while not self.is_closed():
            print(f"\n--- Starting bump cycle at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ---")
            
            for channel_id in CHANNELS:
                channel = self.get_channel(int(channel_id))
                if not channel:
                    print(f"Could not find channel with ID: {channel_id}")
                    continue

                try:
                    # Sending the /bump command
                    DISBOARD_BOT_ID = 302050872383242240
                    
                    found_command = None
                    try:
                        # Search for the command in the channel's visible commands
                        async for command in channel.slash_commands(query="bump"):
                            if command.application_id == DISBOARD_BOT_ID and command.name == "bump":
                                found_command = command
                                break
                    except Exception as e:
                        print(f"Error searching for command in {channel.name}: {e}")

                    if found_command:
                        await found_command(channel)
                        print(f"Bumped in {channel.name} ({channel.id})")
                    else:
                        print(f"Could not find '/bump' command in {channel.name} ({channel.id}). Make sure Disboard is invited.")

                except Exception as e:
                    print(f"Failed to bump in channel {channel_id}: {e}")
                
                # Sleep briefly between channels
                await asyncio.sleep(random.uniform(5, 15))

            # Calculate sleep time
            variance = INTERVAL_MINUTES * 0.05
            sleep_time_minutes = INTERVAL_MINUTES + random.uniform(-variance, variance)
            seconds = sleep_time_minutes * 60
            
            print(f"Cycle complete. Sleeping for {sleep_time_minutes:.2f} minutes...")
            await asyncio.sleep(seconds)

client = AutoBumpBot()
client.run(TOKEN)
