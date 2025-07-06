![Statuscord Banner](img/banner.png)

<div id="NanduBit" align="center">
    <h1>Statuscord</h1>
    <p>Make Your Discord Account 24/7 Online with Custom Status!</p>
    <a href="https://github.com/NanduBit/Status-Discord/blob/main/LICENSE"><img src="https://img.shields.io/github/license/NanduBit/Status-Discord?style=for-the-badge"></a>
    <a href="https://github.com/NanduBit"><img src="https://img.shields.io/badge/GITHUB-NanduBit-7289DA?style=for-the-badge"></a>
    <br>
    <img src="https://i.imgur.com/N61T21L.png" height="210">
</div>

---

<p align="center">
⭐ Feel free to star the repository if this helped you!
</p>

## Disclaimer
By using this code, you are automating your Discord Account. This is against Discord's Terms of Service and Community Guidelines. If not used properly, your account(s) might get suspended or terminated by Discord. I, the developer, am not responsible for any consequences that may arise from the use of this code. Use this software at your own risk and responsibility. Learn more about <a href="https://discord.com/terms">Discord's Terms of Service</a> and <a href="https://discord.com/guidelines">Community Guidelines</a>.
#### This repository is in no way affiliated with, authorized, maintained, sponsored, or endorsed by Discord Inc. (discord.com) or any of its affiliates or subsidiaries.

## Warning
**DO <ins>NOT</ins> GIVE YOUR DISCORD TOKENS TO ANYONE.**
#### Giving your token to someone else will give them the ability to log into your account without the password or 2FA.

## Features
- Secure [🔒]
- Modern UI with Rich Text formatting
- Interactive setup for status and activity
- Supports Playing and Streaming statuses
- Supports all Discord status modes (Online, Idle, Do Not Disturb, Invisible)
- Account will stay 24/7 online (if you set it up correctly, asumming you have a machine to run this on for 24/7)
- Automatic token configuration and saving
- Detailed error handling with visual feedback
- Cross-platform compatibility

## Obtaining Your Token ([Video Guide](https://www.youtube.com/watch?v=5SRwnLYdpJs))
You will need an user token in order to use this code. You can obtain it by doing the following:
1. Logging in to your discord account
2. Pressing `Ctrl+Shift+I` to open Chrome Developer Tools
3. Go to the `Network` Tab
4. Keep it open and refresh the page
5. Type `/api` in the filter search box
6. Click the entry that has `science` as the `Name`
7. On the sub-menu, go to `Headers`
8. Scroll down till you see an entry named `Authorization`. Copy the line next to it.
9. This is your token, <ins>**DO NOT GIVE IT TO ANYONE**</ins>.
10. Alternatively, you can use this [tutoriol](https://www.youtube.com/watch?v=5SRwnLYdpJs))

<p align="center">
  <img height="10px" width="10000px" src="https://i.imgur.com/w6MUcN8.png"/>
</p>

## 🛠️ Installation

### · Local Installation
1. Install [Python](https://python.org/downloads) on your machine (Make sure you add it to [PATH](https://i.imgur.com/Ukl6HdQ.png))
2. Clone this repository or download it as a ZIP file and extract it
3. Open a terminal or command prompt in the project directory
4. Run `pip install -r requirements.txt` to install the required dependencies
5. Either modify the token in `config.py` or let the program prompt you for it when running
6. Run the program with `python main.py`

### · 24/7 Hosting Options

#### Replit
1. Create a new Python repl on [Replit](https://replit.com)
2. Upload the project files into the repl
3. Run the repl and follow the prompts
4. Add your repl URL to an uptime monitor (like [UptimeRobot](https://uptimerobot.com/)) to keep it running 24/7

#### VPS/Cloud Hosting
1. Deploy the code to your VPS or cloud instance
2. Install Python and the required dependencies
3. Run the application using `python main.py` or set it up as a service
4. Use tools like `screen`, `tmux`, or `systemd` to keep the process running in the background

<p align="center">
  <img height="10px" width="10000px" src="https://i.imgur.com/w6MUcN8.png"/>
</p>

## 🔧 Known Errors And Fixes

### [Discord] Status is not changing
> Just wait for a few minutes. It takes some time for Discord to refresh your status.

### [Discord] Invalid Token Error
> Make sure you have copied your token correctly. It should be a long string of characters. Follow the token obtaining guide again if needed.

### [Discord] Cloudflare Error/Temporarily banned from accessing Discord's API
> This happens because some hosting platforms have Shared Public IP Addresses. Whenever Discord sees lots of invalid requests coming from a single IP address, it will use Cloudflare to temporarily block any incoming requests.

> Fix:
> - Restart your hosting service
> - Wait for a while before trying again
> - Consider using a different hosting provider

<p align="center">
  <img height="10px" width="10000px" src="https://i.imgur.com/w6MUcN8.png"/>
</p>

## 🛟 Help and Support
If you have any issues or questions regarding this project, feel free to open an issue on GitHub.

<p align="center">
  <img height="10px" width="10000px" src="https://i.imgur.com/w6MUcN8.png"/>
</p>

## Credits
Special thanks to [SealedSaucer](https://github.com/SealedSaucer/Statuscord) for the original idea and README format.

---

<p align="center">Made with ❤️ by <a href="https://github.com/NanduBit">NanduBit</a></p>
<p align="center">Statuscord is licensed under GNU General Public License</p>
