from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
from selenium.webdriver.chrome.service import Service
s=Service('/chromedriver')
driver = webdriver.Chrome(service=s)
players={} #List to store name of the product
acceptable = {'',' ','Cloud9','Team Liquid','TSM','Even Matchup Gaming','Panda Global','Team Envy','Tempo Storm','Counter Logic Gaming', 'Team Liquid','beastcoast','Panda','Luminosity Gaming','Team SoloMid', 'Polar Ace', 'Halocline Gaming', 'Red Bull eSports','Demise','Balance Gaming','Dignitas','CJ eSports','Thunder Gaming','Echo Fox'}
points = [1000,600,360,180,90,90,45,45]

driver.get('https://liquipedia.net/smash/GENESIS/6/Melee')
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
a  = soup.find('table',href=False, attrs={'class':'wikitable wikitable-bordered prizepooltable collapsed'})
i = 0
points_index = 0
for b in a.findAll('a'):
    print("a",b.text)
    if b.text not in acceptable:
        print("a",b.text)
        if b.text in players:
            players[b.text] = players.get(b.text) + points[points_index]
        else:
            players[b.text] = points[points_index]
        points_index = min(points_index+1,7)

    i +=1
driver.get('https://liquipedia.net/smash/Pound/2019/Melee')
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
a  = soup.find('table',href=False, attrs={'class':'wikitable wikitable-bordered prizepooltable collapsed'})
i = 0
points_index = 0
for b in a.findAll('a'):
    print("a",b.text)
    if b.text not in acceptable:
        print("a",b.text)
        if b.text in players:
            players[b.text] = players.get(b.text) + points[points_index]
        else:
            players[b.text] = points[points_index]
        points_index = min(points_index+1,7)

    i +=1
driver.get('https://liquipedia.net/smash/Get_On_My_Level/2019/Melee')
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
a  = soup.find('table',href=False, attrs={'class':'wikitable wikitable-bordered prizepooltable collapsed'})
i = 0
points_index = 0
for b in a.findAll('a'):
    if b.text not in acceptable:
        if b.text in players:
            players[b.text] = players.get(b.text) + points[points_index]
        else:
            players[b.text] = points[points_index]
        points_index = min(points_index+1,7)

    i +=1
driver.get('https://liquipedia.net/smash/Smash_%27N%27_Splash/5/Melee')
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
a  = soup.find('table',href=False, attrs={'class':'wikitable wikitable-bordered prizepooltable collapsed'})
i = 0
points_index = 0
for b in a.findAll('a'):
    if b.text not in acceptable:
        if b.text in players:
            players[b.text] = players.get(b.text) + points[points_index]
        else:
            players[b.text] = points[points_index]
        points_index = min(points_index+1,7)

    i +=1
driver.get('https://liquipedia.net/smash/Smash_Summit/8')
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
a  = soup.find('table',href=False, attrs={'class':'wikitable wikitable-bordered prizepooltable collapsed'})
i = 0
points_index = 0
for b in a.findAll('a'):
    if b.text not in acceptable:
        if b.text in players:
            players[b.text] = players.get(b.text) + points[points_index]
        else:
            players[b.text] = points[points_index]
        points_index = min(points_index+1,7)

    i +=1
driver.get('https://liquipedia.net/smash/CEO/2019/Melee')
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
a  = soup.find('table',href=False, attrs={'class':'wikitable wikitable-bordered prizepooltable collapsed'})
i = 0
points_index = 0
for b in a.findAll('a'):
    if b.text not in acceptable:
        if b.text in players:
            players[b.text] = players.get(b.text) + points[points_index]
        else:
            players[b.text] = points[points_index]
        points_index = min(points_index+1,7)

    i +=1
driver.get('https://liquipedia.net/smash/Low_Tier_City/7/Melee')
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
a  = soup.find('table',href=False, attrs={'class':'wikitable wikitable-bordered prizepooltable collapsed'})
i = 0
points_index = 0
for b in a.findAll('a'):
    if b.text not in acceptable:
        if b.text in players:
            players[b.text] = players.get(b.text) + points[points_index]
        else:
            players[b.text] = points[points_index]
        points_index = min(points_index+1,7)

    i +=1
driver.get('https://liquipedia.net/smash/Super_Smash_Con/2019/Melee')
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
a  = soup.find('table',href=False, attrs={'class':'wikitable wikitable-bordered prizepooltable collapsed'})
i = 0
points_index = 0
for b in a.findAll('a'):
    if b.text not in acceptable:
        if b.text in players:
            players[b.text] = players.get(b.text) + points[points_index]
        else:
            players[b.text] = points[points_index]
        points_index = min(points_index+1,7)

    i +=1
driver.get('https://liquipedia.net/smash/Shine/2019/Melee')
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
a  = soup.find('table',href=False, attrs={'class':'wikitable wikitable-bordered prizepooltable collapsed'})
i = 0
points_index = 0
for b in a.findAll('a'):
    if b.text not in acceptable:
        if b.text in players:
            players[b.text] = players.get(b.text) + points[points_index]
        else:
            players[b.text] = points[points_index]
        points_index = min(points_index+1,7)

    i +=1
driver.get('https://liquipedia.net/smash/Mainstage/2019/Melee')
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
a  = soup.find('table',href=False, attrs={'class':'wikitable wikitable-bordered prizepooltable collapsed'})
i = 0
points_index = 0
for b in a.findAll('a'):
    if b.text not in acceptable:
        if b.text in players:
            players[b.text] = players.get(b.text) + points[points_index]
        else:
            players[b.text] = points[points_index]
        points_index = min(points_index+1,7)

    i +=1
driver.get('https://liquipedia.net/smash/The_Big_House/9/Melee')
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
a  = soup.find('table',href=False, attrs={'class':'wikitable wikitable-bordered prizepooltable collapsed'})
i = 0
points_index = 0
for b in a.findAll('a'):
    if b.text not in acceptable:
        if b.text in players:
            players[b.text] = players.get(b.text) + points[points_index]
        else:
            players[b.text] = points[points_index]
        points_index = min(points_index+1,7)

    i +=1
driver.get('https://liquipedia.net/smash/Mango%27s_Birthday_Bash/Melee')
content = driver.page_source
soup = BeautifulSoup(content,'html.parser')
a  = soup.find('table',href=False, attrs={'class':'wikitable wikitable-bordered prizepooltable collapsed'})
i = 0
points_index = 0
for b in a.findAll('a'):
    if b.text not in acceptable:
        if b.text in players:
            players[b.text] = players.get(b.text) + points[points_index]
        else:
            players[b.text] = points[points_index]
        points_index = min(points_index+1,7)

    i +=1
df = pd.DataFrame({'players':[players]}) 
df.to_csv('therealrun.csv', index=False, encoding='utf-8')