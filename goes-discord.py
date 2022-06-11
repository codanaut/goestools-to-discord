# import required modules
import os
import requests

# Configure webhook URL
discord_webhook_url = "your webhook here"

# assign directory to scan, must be lowest parent directory before dated folders containing pictures.
directory = "/home/pi/goes16/fd/fc"



# create postedlist.txt if it doesnt exist already.
postedList = open('postedlist.txt','a+')
postedList.close()

# List all files and directories
scannedDirectory = os.scandir(directory)
print(f"\nScanning: {directory} \n")

for folder in scannedDirectory :
    if folder.is_dir():
        print(f"\nScanned Directory: {folder.name}\n")

        obj2 = os.scandir(folder.path)
        for pic in obj2:
            if pic.is_file():
                if pic.name.endswith(('.png','.jpg','jpeg','.PNG','.gif')):
                  test = pic.name + "\n"
                  if test not in open("postedlist.txt", "r"):
                
                    print("Sending to discord...")
                    print(pic.name)

                    # Build payload for Discord webhook
                    payload={'payload_json': '{"content": " "}'}
                    files=[
                        ('file1',(pic.name ,open(pic.path,'rb'),'text/plain'))
                    ]

                    # Post the message to the Discord webhook
                    response = requests.request("POST", discord_webhook_url, data=payload, files=files)
                    print(response.text + "\n")

                    # Update postedlist.txt with posted images
                    updateList = open("postedlist.txt", "a")
                    updateList.write(pic.name + '\n')
                    updateList.close()

                  else:
                      print(f"{pic.name} : already posted... skipping")

                    


