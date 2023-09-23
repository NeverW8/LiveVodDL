# LiveVodDL
Download your *own* twitch streams live.

## Requirements

You will need streamlink as a binary for you system

Debian
`
apt install streamlink
`
or get it [here](https://streamlink.github.io/)

You will also need to install > requests

You can do so by running:

`
pip3 install requests
`

## How it works
It checks via the API for **your own** stream and if it is online, if it isnt, then it will wait for 5 minutes before trying again.

It will stream directly to file, which means that live audio/music will be captured, which is nice to save your own vods locally before twitch removes music i.e.

## TOS
It goes without saying, don't steal other peoples content. Use it against your own stream.

## Can I suggest changes?
Go ahead, its just something I did on a saturday evening (or sunday morning..) as a hobby project.

So feel free to change it or submit a PR.

