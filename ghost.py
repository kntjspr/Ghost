try:
    import os
    from sty import fg, bg, ef, rs, Style, RgbFg
    import sty, re, json, requests
except Exception as e:
    os.system("pip install -r requirements.txt")## You can remove try-catch block if you want to install dependencies in a virtual environment.

    print("Packages installed.")
    exit()
    
class Config:
    def __init__(self):
        self.data = json.load(open('config.json'))
        self.api = self.data['API']
        self.proxy = self.data['ProxyProfile']
        self.currentProfile = self.proxy[self.proxy['current_setting']]
        self.proxies = {
            "http": self.currentProfile,
            "https": self.currentProfile
        }
        try:
            response = requests.request("GET", "http://ip-api.com/json/?fields=countryCode,city,zip,timezone,isp,query", proxies=self.proxies)
        except requests.exceptions.ConnectionError:
            print("Can't establish connection to proxy profile: " + self.currentProfile + ". Please edit config.json.")
            exit()
        self.result = response.json()

class Menu:
    def __init__(self):
        self.menu = {
            1: "Check IP Score (Test all + calculate mean score)",
            2: "Check IP SCALTCS API (+ Score)",
            3: "IP Test IPQS API (+ Score)",
            4: "Phone Validation IPQS API",
            5: "Exit"
        }
    def print_menu(self):
        for key in self.menu.keys():
            print (f"{fg.draculaPink}{key}:{fg.rs}  {fg.draculaYellow}{self.menu[key]}{fg.rs}")

class IPQS:
    def __init__(self, silent):
        self.ipqsAPI = Config().api['ipqualityscore']
        self.url = "https://ipqualityscore.com/api/json/ip/" + self.ipqsAPI + "/" + Config().result['query']
        self.response = requests.request("GET", self.url, proxies=Config().proxies).json()
        self.errorCounter = 0
        self.errorDetail = []
        self.checklist = {
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
            for key in self.checklist.keys():
                if self.response[self.checklist[key]] == True:
                    self.errorCounter = self.errorCounter + 1
                    self.errorDetail.append(self.checklist[key] + " = true")
        except:
            print("Unsuccessful request. Check the api.")
        if self.response['fraud_score'] > 25:
            self.errorCounter = self.errorCounter + 1
            self.errorDetail.append("fraud_score > 25, current value: " + str(self.response['fraud_score']))
        if silent == False:
            print("Error Count: " + str(self.errorCounter))
            print("Error Details: " + str(self.errorDetail))

class Scaltcs:
    def __init__(self, silent):
        self.url = "https://scamalytics.com/ip/" + Config().result['query']
        self.response = requests.request("GET", self.url, proxies=Config().proxies)
        if silent == False:
            print(self.response)

class Main:
    def __init__(self):
        self.draculaPinkBG = bg(189, 147, 249)
        self.draculaOrangeBG = bg(255, 150, 50)
        fg.draculaPink = Style(RgbFg(189, 147, 249))
        fg.draculaYellow = Style(RgbFg(241, 218, 87))
        fg.orange = Style(RgbFg(255, 150, 50))
    def clearscreen(self, numlines=100):
        if os.name in ("nt"):
            os.system('cls')
        else:
            print('\n' * numlines)
    def load_config(self):
        self.clearscreen()
        print("Checking config...")
        print(f"Profile Loaded: {Config().proxy['current_setting']}")
        print(f"Loading proxy: {Config().currentProfile}")
        print(f"{fg(201)}{ef.italic}G H O S T  M O D U L E | {Config().data['app-version']}{rs.italic}{fg.rs}".center(os.get_terminal_size().columns))
        print(f"{self.draculaPinkBG}Current IP:{bg.rs} {Config().result['query']}")
        print(f"{self.draculaOrangeBG}Location:{bg.rs} {Config().result['countryCode']}, {Config().result['city']} {Config().result['zip']}")
    def main(self):
        self.clearscreen()
        self.load_config()
        menu = Menu()
        menu.print_menu()
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        if option == 1:
            print('Feature still in development. Exiting...')
            exit()
        elif option == 2:
            Scaltcs(False)
        elif option == 3:
            IPQS(False)
        elif option == 4:
            Scaltcs()
        elif option == 5:
            print('Exiting...')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')
            menu.print_menu()
            option = int(input('Enter your choice: '))

if __name__=="__main__":
    Main().main()
