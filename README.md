# goestools-to-discord
Send Images From GoesTools to Discord webhook


Takes images from [goestools](https://github.com/pietern/goestools) and sends them to the configured discord webhook. 

<hr>

## How To Use

### Set the webhook
Set your discord webhook on line 6: `discord_webhook_url = "your webhook here"`

### Set the desired folder
Next set the folder you want uploaded in line 9, it must be lowest parent directory before the dated folders containing pictures. 

By default goestools uses a folder structure of `satellite -> image type -> YYYY-MM-DD`

example `/goes16/fd/fc/YYYY-MM-DD`

For example you would set the directory as `/home/pi/goes16/fd/fc` and the script will scan and post images from every dated sub folder. 

`directory = "/home/pi/goes16/fd/fc"`

As every picture is posted its file name is logged in `postedlist.txt` so that it doesnt get reposted on the next run. 


## Auto Run
The easiest way to run the script automatically is to run it as a chron job. 

Edit the chrontab: 
`chrontab -e`

Add a new task with the scheduled time you want it to run and path to `goes-discord.py`:

`*/5 * * * * python3 /home/goes-discord.py`

This will run the goes-discord.py file every 5min. This can be changed to whatever you want though it's not advised to go less than 5min to avoid api lockouts on discord. 