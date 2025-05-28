<h1>MERK 0.039.024</h1>

 - [Summary](#Summary)
 - [Making MERK Portable on Windows](#making-merk-portable-on-windows)
 - [Python Requirements](#python-requirements)
 - [Usage](#usage)
 - [Commands](#commands)
 - [Example commandline usage](#example-commandline-usage)
 - [Why does MERK exist?](#why-does-merk-exist)
 - [What does MERK mean?](#what-does-merk-mean)
 - [Does MERK need any help?](#does-merk-need-any-help)

# Summary
  
**MERK** is a graphical [open source](https://www.gnu.org/licenses/gpl-3.0.en.html) [Internet relay chat](https://en.wikipedia.org/wiki/Internet_Relay_Chat) client. The current development version is **0.039.024**. It uses a [multiple-document interface](https://en.wikipedia.org/wiki/Multiple-document_interface), much like the popular Windows IRC client [mIRC](https://www.mirc.com/).  **MERK** is written in Python 3, using the [PyQt5](https://pypi.org/project/PyQt5/) and [Twisted](https://twistedmatrix.com/trac/) libraries, and runs on both Windows and Linux. **MERK** is updated frequently with new features and bugfixes.

**MERK** is still in development, but it works, and can be used for most IRC activities.

Join me on the official **MERK** IRC channel, **#merk** on the Libera Chat network! Connect to  Libera in the client as one of the built-in server suggestions, or at **irc.libera.chat**, port **6667** (you can also connect via SSL on port **6697**). Honestly, I work a lot, so I'm almost always idle, but I pop in and chat a few times a day!

# Making MERK Portable on Windows
If you want to run **MERK** from a USB stick, and save all configuration and user data to the USB stick (or wherever you're running **MERK** from), it's really easy. First, open [Notepad](https://en.wikipedia.org/wiki/Windows_Notepad), and enter this into a new document:

```merk.exe --config-local```

Save this file to wherever you extracted **MERK** to. You can give it any name you'd like, as long as the file extension you save the file to is `BAT`. So, if you'd like to name the file "MyMerk", you'd save the file with the name `MyMerk.bat`. You're done! You've made **MERK** portable.

Whenever you want to run **MERK** off of your USB stick, double click the `.bat` file you created instead of `merk.exe`. This will run **MERK** completely normally, only all configuration files will be saved to the same directory **MERK** "lives" in. So, you can take **MERK** with you on your USB stick, and it will keep all the configuration files and logs on the USB stick.

# Python Requirements

**MERK** requires Python 3, [PyQt5](https://pypi.org/project/PyQt5/), and [Twisted](https://twistedmatrix.com/trac/). PyQt5 and Twisted can be installed by using [**pip**](https://pypi.org/project/pip/):

    pip install pyqt5
    pip install Twisted

To connect to IRC servers via SSL, two additional libraries may be needed:

    pip install pyOpenSSL
    pip install service_identity

**MERK** is being developed with Python 3.13 on Windows 11 and Linux Mint.

If you're running Windows, and you're getting errors when trying to run **MERK**, you may have to install another library, [pywin32](https://pypi.org/project/pywin32/). You can also install this with [**pip**](https://pypi.org/project/pip/):

    pip install pywin32

To run properly on Linux, the latest version of all required software is recommended.

There are three libraries that comes bundled with **MERK**:
 - [qt5reactor](https://github.com/twisted/qt5reactor)
 - [pyspellchecker](https://github.com/barrust/pyspellchecker)
 - [emoji](https://github.com/carpedm20/emoji)

# Usage
```
usage: python merk.py [-h] [--ssl] [-p PASSWORD] [-c CHANNEL[:KEY]] [-n NICKNAME]
                      [-C SERVER:PORT[:PASSWORD]] [-S SERVER:PORT[:PASSWORD]]
                      [-u USERNAME] [-a NICKNAME] [-r REALNAME] [-d] [-x] [-o]
                      [-t] [-E] [-R] [--config-name NAME] [-Q NAME] [-D] [-L]
                      [--config-directory DIRECTORY] [--config-local]
                      [--scripts-directory DIRECTORY] [--user-file FILENAME]
                      [--config-file FILENAME]
                      [SERVER] [PORT]

Connection:
  SERVER                Server to connect to
  PORT                  Server port to connect to (6667)
  --ssl, --tls          Use SSL/TLS to connect to IRC
  -p, --password PASSWORD
                        Use server password to connect
  -c, --channel CHANNEL[:KEY]
                        Join channel on connection
  -C, --connect SERVER:PORT[:PASSWORD]
                        Connect to server via TCP/IP
  -S, --connectssl SERVER:PORT[:PASSWORD]
                        Connect to server via SSL/TLS

User Information:
  -n, --nickname NICKNAME
                        Use this nickname to connect
  -u, --username USERNAME
                        Use this username to connect
  -a, --alternate NICKNAME
                        Use this alternate nickname to connect
  -r, --realname REALNAME
                        Use this realname to connect

Options:
  -h, --help            Show help and usage information
  -d, --donotsave       Do not save new user settings
  -x, --donotexecute    Do not execute connection script
  -t, --reconnect       Reconnect to servers on disconnection
  -E, --simple          Show simplified dialogs
  -R, --run             Don't ask for connection information on start
  -o, --on-top          Application window always on top

Files and Directories:
  --config-name NAME    Name of the configuration file directory (default: .merk)
  --config-directory DIRECTORY
                        Location to store configuration files
  --config-local        Store configuration files in install directory
  --scripts-directory DIRECTORY
                        Location to look for script files
  --user-file FILENAME  File to use for user data
  --config-file FILENAME
                        File to use for configuration data

Appearance:
  -Q, --qtstyle NAME    Set Qt widget style (default: Windows)
  -D, --dark            Run in dark mode
  -L, --light           Run in light mode
```
# Commands
All of these commands can be issued from the text input widget, or from scripts.

| Commands                                | Description                                                                                                 |
|-----------------------------------------|-------------------------------------------------------------------------------------------------------------|
| `/help`                                 | Displays command usage information                                                                          |
| `/me MESSAGE...`                        | Sends a CTCP action message to the current chat                                                             |
| `/msg TARGET MESSAGE...`                | Sends a message                                                                                             |
| `/notice TARGET MESSAGE...`             | Sends a notice                                                                                              |
| `/join CHANNEL [KEY]`                   | Joins a channel                                                                                             |
| `/part CHANNEL [MESSAGE]`               | Leaves a channel                                                                                            |
| `/nick NEW_NICKNAME`                    | Changes your nickname                                                                                       |
| `/topic CHANNEL NEW_TOPIC`              | Sets a channel topic                                                                                        |
| `/mode TARGET MODE...`                  | Sets a mode on a channel or user                                                                            |
| `/invite NICKNAME CHANNEL`              | Sends a channel invitation                                                                                  |
| `/kick CHANNEL NICKNAME [MESSAGE]`      | Kicks a user from a channel                                                                                 |
| `/whois NICKNAME [SERVER]`              | Requests user information from the server                                                                   |
| `/who NICKNAME [o]`                     | Requests user information from the server                                                                   |
| `/whowas NICKNAME [COUNT] [SERVER]`     | Requests information about previously connected users                                                       |
| `/quit [MESSAGE]`                       | Disconnects from the current IRC server                                                                     |
| `/oper USERNAME PASSWORD`               | Logs into an operator account                                                                               |
| `/away [MESSAGE]`                       | Sets status as "away"                                                                                       |
| `/back`                                 | Sets status as "back"                                                                                       |
| `/raw TEXT...`                          | Sends unprocessed data to the server                                                                        |
| `/time`                                 | Requests server time                                                                                        |
| `/version [SERVER]`                     | Requests server version                                                                                     |
| `/connect SERVER [PORT] [PASSWORD]`     | Connects to an IRC server                                                                                   |
| `/connectssl SERVER [PORT] [PASSWORD]`  | Connects to an IRC server via SSL                                                                           |
| `/xconnect SERVER [PORT] [PASSWORD]`    | Connects to an IRC server & executes connection script                                                      |
| `/xconnectssl SERVER [PORT] [PASSWORD]` | Connects to an IRC server via SSL & executes connection script                                              |
| `/print TEXT...`                        | Prints text to the current window                                                                           |
| `/focus [SERVER] WINDOW`                | Switches focus to another window                                                                            |
| `/maximize [SERVER] WINDOW`             | Maximizes a window                                                                                          |
| `/minimize [SERVER] WINDOW`             | Minimizes a window                                                                                          |
| `/restore [SERVER] WINDOW`              | Restores a window                                                                                           |
| `/cascade`                              | Cascades all subwindows                                                                                     |
| `/tile`                                 | Tiles all subwindows                                                                                        |
| `/clear [WINDOW]`                       | Clears a window's chat display                                                                              |
| `/settings`                             | Opens the settings dialog                                                                                   |
| `/style`                                | Edits the current window's style                                                                            |
| `/alias TOKEN TEXT...`                  | Creates an alias that can be referenced by `$TOKEN`                                                           |
| `/alias`                                | Prints a list of all current aliases                                                                        |
| `/script FILENAME`                      | Executes a list of commands in a file                                                                       |
| `/edit [FILENAME]`                      | Opens a script in the editor                                                                                |
| `/play FILENAME`                        | Plays a WAV file                                                                                            |
| `/list [TERMS]`                         | Lists or searches channels on the server; use "*" for multi-character wildcard and "?" for single character |
| `/refresh`                              | Requests a new list of channels from the server                                                             |
| `/wait SECONDS`                         | Pauses script execution for `SECONDS`; can only be called from scripts                                        |


# Example Commandline Usage
In the following examples, the first commandline is how you would do the task using **MERK** as a Python script, and second commandline is how you would do it using the **MERK** Windows executable. Note that the commandlines, other than the initial executable, are the same!

Let's assume that you want to use the commandline to connect **MERK** to the `2600.net` network and join the `#linux` channel:
```
python merk.py --channel "#linux" irc.2600.net 6667
```
```
merk.exe --channel "#linux" irc.2600.net 6667
```
Easy, right? Now let's try something a little more complex. Let's say you want to connect the the `Libera` network, which uses SSL/TLS. You want to use a different nickname than you normally use; you want to use the nickname `merker`, but you don't want to save this nickname as your default. When you join the network, you want to join two channels: `#python` and `#merk`:
```
python merk.py --donotsave -n merker -c "#python" -c "#merk" --ssl irc.libera.chat 6697
```
```
merk.exe --donotsave -n merker -c "#python" -c "#merk" --ssl irc.libera.chat 6697
```
You can do some things with the commandline that you can't do with the GUI. Let's say that you're using **MERK** on a computer that someone else also uses for **MERK**. You want to store your configuration files in a different folder, just for your use. You always want to use light mode, no matter what the configuration file says, and you've stored some **MERK** scripts in the "C:\Merk_Scripts" folder. You don't want **MERK** to ask you for a server to connect to, you just want it to start up, and you can choose a server from the "IRC" menu:
```
python merk.py --light --config-name .mymerk --scripts-directory "C:\Merk_Scripts" --run
```
```
merk.exe --light --config-name .mymerk --scripts-directory "C:\Merk_Scripts" --run
```
Now, let's try something that commonly done with other IRC clients: connecting to multiple servers automatically on startup. You want to use your standard settings, but connect to three different IRC servers as soon as you run **MERK**: you want to connect to the 2600 network and DALNet, using standard TCP/IP,and Libera, using SSL:
```
python merk.py -C irc.2600.net:6667 -S irc.libera.chat:6697 -C us.dal.net:6667
```
```
merk.exe -C irc.2600.net:6667 -S irc.libera.chat:6697 -C us.dal.net:6667
```
This command will start up **MERK** and connect to three of these servers without any extra effort!

You can do a lot of things from the commandline. For a really complicated example, let's try this scenario. Here's what this commandline will do:

 - Connect to Libera via SSL/TLS
 - Connect to DALnet via TCP/IP
 - Make sure that we reconnect automatically if we get disconnected from either of these servers
 - Join the `#merk` and `#python` channels on both networks
 - Make sure that we don't execute any connection scripts we have set up
 - Run in "light mode", regardless of what the configuration settings say

Here's the set of arguments that will make all of that happen:
```
python merk.py -Ltx -S irc.libera.chat:6697 -C us.dal.net:6667 -c "#python" -c "#merk"
```
```
merk.exe -Ltx -S irc.libera.chat:6697 -C us.dal.net:6667 -c "#python" -c "#merk"
```

All commandline options are what they say on the tin: _optional_. Just running the script with no commandline options will initally open up the connection dialog, and you can do just about everything completely inside the GUI.

# Why does MERK exist?
It's simple. I don't currently like any of the other IRC clients. I've used many, _many_ other IRC clients for Windows and Linux, and they just didn't feel _right_. They weren't customizable enough, didn't have features that I wanted, or just plain looked ancient. I wanted a GUI IRC client that looked and felt modern, and could be heavily customized. My previous IRC client was called [**Ərk**](https://github.com/nutjob-laboratories/erk), and although I liked developing it and working on it, I honestly didn't use it that much. I fell out of love with the "single window" interface that so many other IRC clients use, and decided to try something "new" (and by "new" I mean 30 years old). I remembered using [mIRC](https://www.mirc.com/) back when I was younger, and decided to try and write a new client that used the [multiple-document interface](https://en.wikipedia.org/wiki/Multiple-document_interface) style I remember fondly. And thus, __MERK__ was born!

# What does MERK mean?
Well, if you were to pronounce "IRC" as a word and not an acronym, it would probably be pronounced _/Ərk/_. Since the client allows a user to connect to multiple IRC servers at the same time, well, that might be what the "M" stands for. Either that, or "multiple-document interface". "MDIIRC" doesn't exactly roll off the tongue, so we combined the "M" with the word-pronunciation of IRC, and came up with __MERK__!

# Does MERK need any help?
Yes! **MERK** is being written by me, [Dan Hetrick](https://github.com/danhetrick), a software developer that can not do everything that this piece of software needs. There's few things I need help with!

 - **Icons and other graphics work**. I am not a graphic designer, and I think that that shows in this project, heh. I need help with creating better icons, and a better logo for **MERK**. I'm doing my best, here, but I'm a computer programmer, not an artist!
 - **Packaging**. **MERK** now has a [PyInstaller](https://www.pyinstaller.org/)-based distribution! However, I can't seem to get PyInstaller working on a Linux binary for reasons that are beyond me. I'd love some help on getting packaging for Linux, be it with PyInstaller or anything else that's easy for end-users to use. I also know next to nothing about making Python packages for use with  `pip`, but that's another thing I'd love help with!
 - **Using MERK and giving me feedback**. Let me know what you love about **MERK** and what you hate about **MERK**! Got ideas for ways you'd like to customize the client? Features you'd like? Let me know! I can't guarantee that I'll put in everything that you want, but I love hearing new ideas, and I love hearing about how people are using **MERK**!

Contacting me is easy! Drop me an [email](mailto:dhetrick@gmail.com) or say hi in the official **MERK** IRC channel: `#merk` on the Libera network (`irc.libera.chat`, port 6667 for TCP/IP and port 6697 for SSL). I work a lot, so I'm not always active, but I idle in `#merk` everyday, and pop in to talk to people when I have a spare minute.

[//]: # (End of document)

