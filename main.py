from utils import GetAlbumName
from telethon.sync import TelegramClient, events

# Get this info from https://my.telegram.org/auth > API development
api_id = "¯\_(ツ)_/¯"
api_hash = "¯\_(ツ)_/¯"

# Telegram will ask for your phone number and send you a code.
# Once you enter the code, a .session file will be created and
# you don't have to repeat these steps again.
client = TelegramClient("channel_manager", api_id, api_hash)
client.start()

# Iterate over all messages in the channel and select the ones
# with .message field
msg_html_list = []
for msg in client.iter_messages("gameost1", reverse=True):
    if msg.message != None and "Album:" in msg.message:

        # Prepare message url and album name
        msg_url = f"https://t.me/gameost1/{msg.id}"
        album_name = GetAlbumName(msg.message)
        msg_html = f"<a href={msg_url}>{album_name}</a>\n"

        msg_html_list.append((album_name, msg_html))
        print(msg_url, ">", album_name)

# Sort alphabetically
msg_html_list.sort(key=lambda x: x[0].lower())

msg = ""
for i, item in enumerate(msg_html_list):
    msg += item[1]

    # Send the message every 100 albums
    if (i+1) % 100 == 0:
        client.send_message("me", msg, parse_mode="HTML", link_preview=False)
        msg = ""

# Send the remaining messages
client.send_message("me", msg, parse_mode="HTML", link_preview=False)