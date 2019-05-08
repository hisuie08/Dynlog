from time import sleep

import discord
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.options import Options


client = discord.Client()
@client.event
async def on_ready():
    CHANNEL_ID = int(000000000)#ﾁｬﾝﾈﾙIDの見方はggってください
    channel = client.get_channel(CHANNEL_ID)

    options = Options()
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=r"C:\work\chromedriver.exe", options=options)
    driver.get("Dynmap_URL")
    sleep(0.1)
    print("ready")
    n = 1
    while True:#この辺の処理はdyncheckの移植
        try:
            content = driver.find_element_by_css_selector("#mcmap > div.chat > div > div:nth-child({})".format(n)).text
            print(content)
            n = n+1
            chat = str(content)
            await channel.send(chat)
        except NoSuchElementException:
            continue


client.run('TOKEN')#BOTのﾄｰｸﾝをここに