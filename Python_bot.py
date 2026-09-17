from playwright.sync_api import sync_playwright
from send_to_discord import Send_to_discord

url_list = []
user =r'C:\playwright_chrome\User Data'

with sync_playwright() as meow:
    data = meow.chromium.launch_persistent_context(
        user,
        channel="chrome",  
        headless=False,    
        args=[
            "--profile-directory=Profile 26",
            "--no-first-run",
            "--no-default-browser-check"
        ]
    )
   
    
    page = data.new_page()
    page.goto('https://www.youtube.com/')
    
    shorts= page.get_by_role('link', name='Shorts')
    shorts.click()
    
    page.wait_for_timeout(3000)
    i =0
    while i==0:

        page.keyboard.press('ArrowDown')
        url =page.url
        url_list.append(url)
        print(url_list)
        print(url)
        if len(url_list)>=2:
            if url_list[-1]==url_list[-2]:
                url_list.pop()
        Send_to_discord.content = url
        Send_to_discord(url)
        #playlist = "https://www.youtube.com/playlist?list=PLeJk3vJMk3gk"

        page.wait_for_timeout(100) 
