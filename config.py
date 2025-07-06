import discord

# Here you can set your token and change defaultvalues of status, activity type and activity name.
# Caution: Do not share your token with anyone, as it can be used to control your account.
TOKEN = "YOUR_TOKEN"  # Replace with your Discord token

STATUS = discord.Status.online  # This can be "online", "idle", "dnd", or "invisible"

ACTIVITY_TYPE = discord.ActivityType.streaming  # This can be "playing", or "streaming"... these are currently supported via self bot

ACTIVITY = {
    "name": "Leageue of Legends",  # Replace with your activity name
    "url": "https://twitch.tv/yourchannel"  # Replace with your stream URL, this is only applicable in "streaming" mode"
}

# Set to True if running on Replit to enable the keepalive server
REPLIT = False