import os
import discord
from discord.ext import commands

# 1. Enable permissions (intents)
intents = discord.Intents.default()
intents.message_content = True

# 2. Set up your bot prefix (e.g., !ping)
bot = commands.Bot(command_prefix="!", intents=intents)

# 3. Print a message when the bot turns online
@bot.event
async def on_ready():
    print(f"Logged in successfully as {bot.user.name}!")

# 4. A basic test command
@bot.command()
async def ping(ctx):
    await ctx.send("Pong! 🏓 Your bot is alive and hosted on Render!")

# 5. Securely grab the token from Render's Environment Variables
TOKEN = os.getenv("DISCORD_TOKEN")
if TOKEN:
    bot.run(TOKEN)
else:
    print("Error: DISCORD_TOKEN environment variable not found.")
