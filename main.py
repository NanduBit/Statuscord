# Made with ❤ by NanduBit
import logging
import discord
import config
from rich.console import Console
from rich.panel import Panel
from rich.align import Align
from rich.text import Text
from rich.style import Style

# Import keepalive if running on Replit
if config.REPLIT:
    from keepalive import keep_alive

# Completely disable all logging from all libraries


logging.disable(logging.CRITICAL)

client = discord.Client()
console = Console()

# Discord blue gradient colors (no black)
discord_blues = ["#7289DA", "#5865F2", "#4E5D94", "#99AAB5", "#7289DA", "#5865F2"]

ascii_art_lines = [
    '\n'
    "░██████╗████████╗░█████╗░████████╗██╗░░░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░",
    "██╔════╝╚══██╔══╝██╔══██╗╚══██╔══╝██║░░░██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗",
    "╚█████╗░░░░██║░░░███████║░░░██║░░░██║░░░██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║",
    "░╚═══██╗░░░██║░░░██╔══██║░░░██║░░░██║░░░██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║",
    "██████╔╝░░░██║░░░██║░░██║░░░██║░░░╚██████╔╝██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝",
    "╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░"
]

# Build gradient text for ASCII art
gradient_text = Text()
for i, line in enumerate(ascii_art_lines):
    color = discord_blues[i % len(discord_blues)]
    gradient_text.append(line + "\n", style=Style(color=color, bold=True))

panel = Panel(
    Align.center(gradient_text, vertical="middle"),
    title="[bold #7289DA]Sponsored by @NanduBit[/bold #7289DA]",
    border_style="#5865F2",
    padding=(1, 2),
    width=100
)
console.print(panel, justify="center")

def set_default_activity():
    if config.ACTIVITY_TYPE == discord.ActivityType.streaming:
        activity = discord.Streaming(name=config.ACTIVITY["name"], url=config.ACTIVITY["url"])
    elif config.ACTIVITY_TYPE == discord.ActivityType.playing:
        activity = discord.Game(config.ACTIVITY["name"])
    else:
        warn_text = Text(f"Unsupported activity type '{config.ACTIVITY_TYPE}', defaulting to game activity.", style=Style(color="#7289DA", bold=True))
        console.print(warn_text)
        activity = discord.Game(config.ACTIVITY["name"])

    if config.STATUS not in [discord.Status.online, discord.Status.idle, discord.Status.dnd, discord.Status.invisible]:
        warn_text = Text(f"Invalid status '{config.STATUS}', defaulting to online.", style=Style(color="#7289DA", bold=True))
        console.print(warn_text)
        config.STATUS = discord.Status.online

    console.print(
        Text("Activity set to default values.. you can view/edit it at config.py!\n", style="#99AAB5"),
        justify="center"
    )

    return activity

def prompt_activity_setup():
    # Show prompt with proper coloring and only supported types
    console.print(
        "\n[bold #7289DA]Choose an option (1 or enter for default, 2 for setup):[/bold #7289DA]",
        justify="center"
    )
    console.print(
        "[#7289DA][[/][#99AAB5]1[/][#7289DA]] Default  [[/][#99AAB5]2[/][#7289DA]] Setup[/]",
        justify="center"
    )
    # Centered input prompt
    console.print(" " * 35 + "> ", end="", style="#7289DA")
    choice = input().strip()
    
    # Store the activity configuration
    activity = ''
    
    if choice == "" or choice == "1":
        activity = set_default_activity()
    elif choice == "2":
        # Ask for status
        console.print(
            "[bold #7289DA]Select status:[/bold #7289DA]",
            justify="center"
        )
        console.print(
            "[#7289DA][[/][#99AAB5]1[/][#7289DA]] Online [[/][#99AAB5]2[/][#7289DA]] Idle [[/][#99AAB5]3[/][#7289DA]] Do Not Disturb [[/][#99AAB5]4[/][#7289DA]] Invisible[/]",
            justify="center"
        )
        console.print("[#7289DA]Enter number:[/]", justify="center")
        console.print(" " * 35 + "> ", end="", style="#7289DA")
        status_num = input().strip()
        status_map = {
            "1": discord.Status.online,
            "2": discord.Status.idle,
            "3": discord.Status.dnd,
            "4": discord.Status.invisible
        }
        if status_num not in status_map:
            config.STATUS = discord.Status.online
            console.print(
                Text("Status code set to Online.\n", style="#99AAB5"),
                justify="center"
            )
        else:
            console.print(
                    "[#FFCC00]Due to an unfixable bug which I belive is unfixable by me,\n any status other than online will lead to an error.\n Threfore, status is set to online.[/]",
                    justify="center"
                )
            chosen_status = discord.Status.online 
            # chosen_status = status_map[status_num]
            if chosen_status == discord.Status.invisible:
                console.print(
                    "[#FFCC00]Having Invisible Status will not show your activity, it is same as being offline :)[/]",
                    justify="center"
                )
                exit(0)
            config.STATUS = chosen_status
            console.print(
                f"[#99AAB5]Status code set to {chosen_status.name.capitalize()}.\n[/]",
                justify="center"
            )

        # Only allow playing and streaming
        console.print(
            "[bold #7289DA]Select activity type:[/bold #7289DA]",
            justify="center"
        )
        console.print(
            "[#7289DA][[/][#99AAB5]1[/][#7289DA]] Playing [[/][#99AAB5]2[/][#7289DA]] Streaming[/]",
            justify="center"
        )
        console.print("[#7289DA]Enter number:[/]", justify="center")
        console.print(" " * 35 + "> ", end="", style="#7289DA")
        act_type_num = input().strip()
        if act_type_num == "2":
            console.print(
                "[#99AAB5]ActivityType set to Streaming.\n[/]",
                justify="center"
            )
            act_type = discord.ActivityType.streaming
        else:
            console.print(
                "[#99AAB5]ActivityType set to Playing.\n[/]",
                justify="center"
            )
            act_type = discord.ActivityType.playing
        # Ask for name
        console.print("[bold #7289DA]Enter activity name:[/bold #7289DA]", justify="center")
        console.print(" " * 35 + "> ", end="", style="#7289DA")
        act_name = input().strip()

        # Check for blank values
        if not act_name or act_name.isspace():
            console.print(
                "[#FFCC00]Blank value passed to activity name.\nThis means no activity will be shown on your profile.\nOnly inputed status will show and the account will\nstay online as long as this code is running.\n[/]",
                justify="center"
            )
            

        console.print(
            f"[#99AAB5]ActivityName set to: {act_name}.\n[/]",
            justify="center"
        )
        
        # If streaming, ask for URL
        if act_type == discord.ActivityType.streaming:
            console.print("[#7289DA]Enter stream URL:[/]", justify="center")
            console.print(" " * 35 + "> ", end="", style="#7289DA")
            act_url = input().strip()
            
            # Check if URL is a valid Twitch URL
            if "https://twitch.tv/" not in act_url:
                console.print(
                    "[#FFCC00]A valid Twitch URL (e.g., https://twitch.tv/yourname)\nmust be entered for streaming activity to display correctly.[/]",
                    justify="center"
                )
                exit(0)
                
            console.print(
                f"[#99AAB5]Stream URL is set to: {act_url}\n[/]",
                justify="center"
            )
            activity = discord.Streaming(name=act_name, url=act_url)
        else:
            activity = discord.Game(act_name)
    else:
        console.print("[#FFCC00]Invalid input, using default activity settings.\n[/]", justify="center")
        activity = set_default_activity()

    return activity

@client.event
async def on_ready():
    console.print("\n[bold #7289DA]Connection established! Setting up your activity...[/bold #7289DA]", justify="center")
    activity = prompt_activity_setup()

    # Apply the activity with a try-except block to catch any errors
    try:
        await client.change_presence(status=config.STATUS, activity=activity)  # Ensure no unsupported arguments are passed
    except Exception as e:
        console.print(f"[bold #FF5555]Failed to apply activity settings: {str(e)}[/bold #FF5555]", justify="center")
        console.print("[#FFCC00]Attempting to set status without activity...[/]", justify="center")
        
        # Try again with just status in case the activity is causing issues
        try:
            await client.change_presence(status=config.STATUS)  # Only set status
            console.print("[#99AAB5]Status applied successfully without activity.[/]", justify="center")
        except Exception as e2:
            console.print(f"[bold #FF5555]Failed to apply status: {str(e2)}[/bold #FF5555]", justify="center")

    console.print("\n", justify="center")  # Add more spacing
    login_message = Text.assemble(
        ("Logged in as ", Style(color="#7289DA", bold=True)),
        (f"{client.user}", Style(color="#99AAB5", bold=True))  # lighter blue/gray for username
    )
    panel = Panel(
        Align.center(login_message, vertical="middle"),
        title="[bold #7289DA]Discord Self Bot[/bold #7289DA]",
        border_style="#5865F2",
        padding=(1, 4),
        width=60
    )
    console.print(panel, justify="center")
    
    # Add confirmation that the bot is ready and running with distinctive styling
    console.print("\n[bold #5865F2]Self Bot is ready and running! Press Ctrl+C to exit.[/bold #5865F2]", justify="center")

try:
    # If running on Replit, start the keepalive server
    if config.REPLIT:
        keep_alive()
        console.print("[#99AAB5]Keepalive server started for Replit 24/7 operation[/]", justify="center")
    
    # Check if token is default and prompt for input if needed
    if config.TOKEN == "YOUR_TOKEN":
        console.print("\n[bold #FFCC00]Token not configured in config.py[/bold #FFCC00]", justify="center")
        console.print("[#99AAB5]Tutorial on how to get your Discord token:\nhttps://www.youtube.com/watch?v=5SRwnLYdpJs[/]", justify="center")
        console.print("[#FFCC00]Please enter your Discord token:[/]", justify="center")
        console.print(" " * 35 + "> ", end="", style="#7289DA")
        user_token = input().strip()
        
        if not user_token:
            error_message = Text.assemble(
                ("No Token Provided", Style(color="#FF5555", bold=True)),
                ("\n\nYou must provide a valid Discord token to continue.", Style(color="#FFAAAA"))
            )
            error_panel = Panel(
                Align.center(error_message, vertical="middle"),
                title="[bold #FF5555]Configuration Error[/bold #FF5555]",
                border_style="#FF0000",
                padding=(1, 4),
                width=60
            )
            console.print(error_panel, justify="center")
            exit(1)
            
        # Update config file with the new token
        try:
            with open('./config.py', 'r') as file:
                config_content = file.read()
                
            # Replace the token line while preserving format
            updated_content = config_content.replace('TOKEN = "YOUR_TOKEN"', f'TOKEN = "{user_token}"')
            # Also handle the case where the token has been replaced before
            if updated_content == config_content:
                # Try to find the TOKEN line with regex pattern
                import re
                token_pattern = re.compile(r'TOKEN\s*=\s*"[^"]*"')
                updated_content = token_pattern.sub(f'TOKEN = "{user_token}"', config_content)
            
            with open('./config.py', 'w') as file:
                file.write(updated_content)
                
            console.print("[#99AAB5]Token saved to config.py[/]", justify="center")
            config.TOKEN = user_token
        except Exception as e:
            console.print(f"[bold #FF5555]Failed to update config.py: {str(e)}[/bold #FF5555]", justify="center")
            console.print("[#99AAB5]Continuing with provided token for this session only.[/]", justify="center")
            # Continue with the token provided in input even if saving fails
            config.TOKEN = user_token

    client.run(config.TOKEN)
except discord.LoginFailure:
    error_message = Text.assemble(
        ("Invalid Token", Style(color="#FF5555", bold=True)),
        ("\n\nThe provided Discord token is invalid or has been revoked.\n Replace `TOKEN` in `config.py` with a valid one.", Style(color="#FFAAAA"))
    )
    error_panel = Panel(
        Align.center(error_message, vertical="middle"),
        title="[bold #FF5555]Authentication Error[/bold #FF5555]",
        border_style="#FF0000",
        padding=(1, 4),
        width=60
    )
    console.print(error_panel, justify="center")
except Exception as e:
    error_message = Text.assemble(
        ("Error Occurred", Style(color="#FF5555", bold=True)),
        (f"\n\n{str(e)}", Style(color="#FFAAAA"))
    )
    error_panel = Panel(
        Align.center(error_message, vertical="middle"),
        title="[bold #FF5555]Runtime Error[/bold #FF5555]",
        border_style="#FF0000",
        padding=(1, 4),
        width=60
    )
    console.print(error_panel, justify="center")