# Discord.py Bot Template
Discord.py Bot Template for discord.

### How to use:

Paste your token in the bot.py file
```python
client.run("Token Here")
```

Paste your desired prefix
```python
prefix = 'prefix here'
 ```
 
# How to install Dependencies

### Ubuntu 20.04
```bash 
sudo apt-get install python3
sudo apt-get install pip
(optional) sudo apt-get install tmux
```

Once you have ran those commands, Update

```bash 
sudo apt-get update
sudo apt-get upgrade
```

Now, Open a new TMUX session (If you installed tmux)

```bash
tmux
```

Now, Let's rename the session to our desired name

```bash
tmux rename-session -t 0(old session name) Bot(new session name)
```

Now, Let's install the python packages
```bash
pip3 install discord
pip3 install requests
```

Now, Let's run the bot file
```bash
python3 bot.py
```

### You are done! Enjoy your discord bot!
( If your OS was not included here, google is your friend ;) )

