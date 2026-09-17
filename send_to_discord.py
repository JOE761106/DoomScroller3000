import requests
def Send_to_discord(yt_url):
    #link
    webhook = 'WEBHOOK_LINK'
    #tells discord name of the bot and what to send
    content ="ee"
    params ={
        'user' : 'SAGI_SCROLLER3000',
        "content" :f'{yt_url}'
    }
    print("sending")
    response = requests.post(webhook, json=params)

    #handeles responce codes
    if response.status_code == 204:
        print("sending to discord")
    else:
        print(f"error {response.status_code}")    
        
