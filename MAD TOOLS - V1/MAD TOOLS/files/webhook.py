import time, requests, pyfiglet, threading

print(pyfiglet.figlet_format("MAD TOOLS"))

msg = input("Message a spam : ")
webhook = input("WebHook URL: ")
th = int(input('Nombre de fois a spam : '))
sleep = int(input("temps d attente: "))
def spam():
    while True:
        try:
            data = requests.post(webhook, json={'content': msg})
            if data.status_code == 204:
                print(f"Sent MSG {msg}")
        except:
            print("Bad Webhook :" + webhook)
        time.sleep(sleep)
    
for x in range(th):
    t = threading.Thread(target = spam)
    t.start()