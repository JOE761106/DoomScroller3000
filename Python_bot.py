from playwright.sync_api import sync_playwright
with sync_playwright() as meow:
    browser = meow.chromium.launch(headless=False , slow_mo=500)
    page = browser.new_page()
    page.goto('https://www.youtube.com/')
    gaming =page.get_by_role('link' ,name ='Shorts' )
    gaming.click()
    page.wait_for_timeout(3000) 
    
    
    
    