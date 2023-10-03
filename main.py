import requests as requests
import secrets
import datetime
import subprocess
import time
import uuid

bearer = secrets.bearer
client_id = secrets.client_id
channel_name = secrets.channel_name
client_secret = secrets.client_secret
saving_path = secrets.saving_path


def random_filename():
    random_uuid = uuid.uuid4()
    recorded_filename = (
        channel_name
        + "_"
        + datetime.datetime.now().strftime("%Y-%m-%d")
        + "-"
        + str(random_uuid)
        + ".mp4"
    )
    return recorded_filename


def is_channel_online():
    result = requests.get(
        "https://api.twitch.tv/helix/search/channels?query="
        + channel_name
        + "&live_only=true",
        headers={"Authorization": "Bearer " + bearer, "Client-Id": client_id},
    )
    result.raise_for_status()
    data = result.json()["data"]
    for channel in data:
        print(channel["broadcaster_login"])
        if channel["broadcaster_login"] == channel_name:
            return True, channel["id"]
    return False, None


while True:
    is_online, user_id = is_channel_online()
    recorded_filename = random_filename()
    if is_online:
        subprocess.call(
            [
                "streamlink",
                "--force",
                "--twitch-disable-ads",
                "twitch.tv/" + channel_name,
                "best",
                "-o",
                "{title}_" + recorded_filename,
            ]
        )
        subprocess.call(["mv", "*_" + recorded_filename, saving_path])
    else:
        print("Channel is not online, trying again in 5 minutes")
        time.sleep(300)
