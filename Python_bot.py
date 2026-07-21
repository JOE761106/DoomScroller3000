from playwright.sync_api import sync_playwright
#chooses file path to be able to open yt in a custom user
user =r'C:\playwright_chrome\User Data'

with sync_playwright() as meow:
    #prevents google from messing with the browser opening
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
    gaming =page.get_by_role('link' ,name ='Shorts' )
    gaming.click()
    page.wait_for_timeout(3000) 
    
    
    
    
