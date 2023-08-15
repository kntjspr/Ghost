try:
    import os
    from sty import fg, bg, ef, rs, Style, RgbFg
    import sty, re, json, requests
except Exception as e:
    os.system("pip install -r requirements.txt")
    print("Packages installed.")
    exit()
def clearscreen(numlines=100):
  if os.name in ("nt"):
    os.system('cls')
  else:
    print('\n' * numlines)
def load_config():
    clearscreen()
    global data, api, proxy, result, proxies
    print("Checking config...")
    data = json.load(open('config.json'))
    api = data['API']
    proxy = data['ProxyProfile']
    print("Checking last profile loaded")
    currentProfile = proxy[proxy['current_setting']]
    print(f"Profile Loaded: {proxy['current_setting']}")
    print(f"Loading proxy: {currentProfile}")
    proxies = {
        "http": currentProfile,
        "https": currentProfile
    }
    try:
        response = requests.request("GET", "http://ip-api.com/json/?fields=countryCode,city,zip,timezone,isp,query", proxies=proxies)
    except requests.exceptions.ConnectionError:
        print("Can't establish connection to proxy profile: " + currentProfile + ". Please edit config.json.")
        exit()
    result = response.json()
    print(f"{fg(201)}{ef.italic}G H O S T  M O D U L E | {data['app-version']}{rs.italic}{fg.rs}".center(os.get_terminal_size().columns))
    print(f"{draculaPinkBG}Current IP:{bg.rs} {result['query']}")
    print(f"{draculaOrangeBG}Location:{bg.rs} {result['countryCode']}, {result['city']} {result['zip']}")
def print_menu():
    menu = {
    1: "Check IP Score (Test all + calculate mean score)",
    2: "Check IP SCALTCS API (+ Score)",
    3: "IP Test IPQS API (+ Score)",
    4: "Phone Validation IPQS API",
    5: "Exit"
    }
    for key in menu.keys():
        print (f"{fg.draculaPink}{key}:{fg.rs}  {fg.draculaYellow}{menu[key]}{fg.rs}")
def scaltcs(silent):
    url = "https://scamalytics.com/ip/" + result['query']
    response = requests.request("GET", url, proxies=proxies)
    if scaltcs == False:
        print(response)
def checkIPQS(silent):
    ipqsAPI = api['ipqualityscore']
    url = "https://ipqualityscore.com/api/json/ip/" + ipqsAPI + "/" + result['query']
    response = requests.request("GET", url, proxies=proxies).json()
    print(f"Success: {response['success']}")
    errorCounter = 0
    errorDetail = []
    checklist = {
        1: 'fraud_score',
        2: 'is_crawler',
        3: 'proxy',
        4: 'vpn',
        5: 'tor',
        6: 'active_vpn',
        7: 'active_tor',
        8: 'recent_abuse',
        9: 'bot_status'
    }
    try:
        for key in checklist.keys():
            if response[checklist[key]] == True:
                errorCounter = errorCounter + 1
                errorDetail.append(checklist[key] + " = true")
    except:
        print("Unsuccessful request. Check the api.")
    if response['fraud_score'] > 25:
        errorCounter = errorCounter + 1
        errorDetail.append("fraud_score > 25, current value: " + str(response['fraud_score']))
    if silent == False:
        print("Error Count: " + str(errorCounter))
        print("Error Details: " + str(errorDetail))

def main():
    global draculaPinkBG, draculaOrangeBG
    fg.draculaPink = Style(RgbFg(189, 147, 249))
    fg.draculaYellow = Style(RgbFg(241, 218, 87))
    fg.orange = Style(RgbFg(255, 150, 50))
    draculaPinkBG = bg(189, 147, 249)
    draculaOrangeBG = bg(255, 150, 50)
    clearscreen()
    load_config()
    try:
        print_menu()
        option = int(input('Enter your choice: '))
    except:
        print('Wrong input. Please enter a number ...')
    if option == 1:
        print('Feature still in development. Exiting...')
        exit()
    elif option == 2:
        scaltcs(False)
    elif option == 3:
        checkIPQS(False)
    elif option == 4:
        scaltcs()
    elif option == 5:
        print('Exiting...')
        exit()
    else:
        print('Invalid option. Please enter a number between 1 and 4.')
        print_menu()
        option = int(input('Enter your choice: '))

if __name__=="__main__":
    main()
#os.system('cmd /k "wmic process where caption="chrome.exe" get commandline /format:TextvalueList > Output.txt"')

#with open('Output.txt') as txtfile:
#    print(contents)

#ith open("Output.txt", "r") as f:
#      for i in f.readlines():
#        if not i.strip():
#         continue
#        if i:
#          print (i),
