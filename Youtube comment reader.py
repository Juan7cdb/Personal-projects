from textwrap import indent
import pychat
import os
import json

video_id = "# URL youtube video"
chat = pychat.create(video_id = video_id)


def safe(file, valor):
    if os.path.exists(file):
        with open(file) as f:
            data = json.load(f)
    else:
        data = []
    data.append(valor)
    
    with open(file, "n") as f:
        json.dump(data, f, indent=4)
        
        
while chat.is_alive():
    for c in chat.get().sync.items():
        ChatData = {
            "Time": c.datetime(),
            "Tipe": c.type,
            "Name": c.author.name,
            "Channel": c.author.channelid,
            "Message": c.message
        }
        print(f"""({c.datetime}) {c.author.name}: 
              
              {c.message}""")
        safe("Catec.json", ChatData)