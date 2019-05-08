from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
#Dynmapをｽｸﾚｲﾋﾟﾝｸﾞしてｻｰﾊﾞｰの情報をﾘｱﾙﾀｲﾑに取得するﾔﾂ
options = Options()
options.add_argument('--headless')
driver = webdriver.Chrome(executable_path=r"driver_PATH", options=options)
driver.get("Dynmap_URL")
sleep(0.1)
print("ready")
n = 1
while True:
    try:
        content = driver.find_element_by_css_selector("#mcmap > div.chat > div > div:nth-child({})".format(n)).text#長時間動かすとnがやばいことになるのなんとかしたい
        print(content)
        n = n+1
    except NoSuchElementException:#要素見つからない例外をcontinueしてループさせることで擬似的にストリーミングを再現
        continue
