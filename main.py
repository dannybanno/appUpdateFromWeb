import requests

#optional //
import pymsgbox as msg
#\\


#raw pastebin of just the verison. For this it is just ver 1.0
url = 'https://pastebin.com/raw/sz6b6jCD'

#gets the verison
web = requests.get(url)

currentVer = 1.0

#changes to float
versionWeb = float(web.text)

#checks if current version is upto date
if versionWeb <= currentVer:
    #print('app is up to date!')

    #optional//
    msg.alert(f'app is up to date. Verison {currentVer}')
    #\\
else:
    #optional //
    msg.confirm(f'Your verison is {currentVer} there is an update to {versionWeb}', f'Update for {versionWeb}', ['ok', 'cancel'])
    #\\

    #print(f'Your verison is {currentVer} there is an update to {versionWeb}')