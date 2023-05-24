from discord_webhook import DiscordWebhook
from modules.shared import opts
import io
import os
import pprint
import datetime

webhook_url = opts.data.get('deforum_discord_webhook_url')

def send_completed_message(start_time,end_time,last_frame):
    duration_str = str(datetime.timedelta(seconds=round(end_time-start_time)))
    message = f"Generation completed in {duration_str}"
    webhook = DiscordWebhook(url=webhook_url, content=message)
    print(last_frame)
    with io.BytesIO() as image_binary:
            last_frame.save(image_binary, 'PNG')
            image_binary.seek(0)
            webhook.add_file(file=image_binary.getvalue(), filename="output.png")
            response = webhook.execute()