from playwright.sync_api import sync_playwright
url_list = []
with sync_playwright() as meow:
    browser = meow.chromium.launch(headless=False , slow_mo=500)
    page = browser.new_page()
    page.goto('https://www.youtube.com/')
    gaming =page.get_by_role('link' ,name ='Shorts' )
    gaming.click()
   
    page.wait_for_timeout(3000)
    
    i = 0

    while i==0:

        page.keyboard.press('ArrowDown')
        url =page.url
        url_list.append(url)
        print(url_list)
        print(url)
        if len(url_list)>=2:
            if url_list[-1]==url_list[-2]:
                url_list.pop()

   

        page.wait_for_timeout(4000) 


   
    
    
    
    

    
