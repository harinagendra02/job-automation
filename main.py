Read links.txt
↓

Open each LinkedIn Search URL

↓

Get newest post

↓

Check duplicate

↓

Send to Google Sheet

↓

Send to Discord

from sheets import add_row
from discord_sender import send_message

with open("links.txt") as f:
    links = f.readlines()

for link in links:

    posts = scrape_linkedin(link)

    for post in posts:

        message = f"""
State : TX
Author : {post['author']}

{post['text']}

{post['url']}
"""

        add_row([
            post['time'],
            post['author'],
            post['text'],
            post['url']
        ])

        send_message(message)
