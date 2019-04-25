# encoding: utf-8

"""
File: qzone.py
Author: Rock Johnson
"""
import os, time, random
from datetime import datetime
from threading import Timer
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

# 参数
Random = []
Random_i = random.randrange(0, 11)

for i in range(11):
    if i != Random_i:
        Random.append("活")
    else:
        Random.append("死")

uname = "836867547"
upwd = "whylifehappy?503"
# uname = "1358485504"
# upwd = "k836867547"
url = "https://xui.ptlogin2.qq.com/cgi-bin/xlogin?proxy_url=https%3A//qzs.qq.com/qzone/v6/portal/proxy.html&daid=5&&hide_title_bar=1&low_login=0&qlogin_auto_login=1&no_verifyimg=1&link_target=blank&appid=549000912&style=22&target=self&s_url=https%3A%2F%2Fqzs.qzone.qq.com%2Fqzone%2Fv5%2Floginsucc.html%3Fpara%3Dizone&pt_qr_app=手机QQ空间&pt_qr_link=http%3A//z.qzone.com/download.html&self_regurl=https%3A//qzs.qq.com/qzone/v6/reg/index.html&pt_qr_help_link=http%3A//z.qzone.com/download.html&pt_no_auth=0"


def wait(browser, cname):
    try:
        WebDriverWait(browser, 60).until(
            ec.presence_of_element_located((By.CSS_SELECTOR, cname))
        )
    except:
        browser.quit()

def Qzone(state):
    try:
        # 启动chrome
        browser = webdriver.Chrome(executable_path=os.path.abspath("chromedriver"))
        browser.get(url)

        # 登录qq空间
        wait(browser, "#switcher_plogin")
        switcher = browser.find_element_by_css_selector("#switcher_plogin")
        switcher.click()

        uname_input = browser.find_element_by_css_selector("#u")
        upwd_input = browser.find_element_by_css_selector("#p")
        login_btn = browser.find_element_by_css_selector("#login_button")

        uname_input.send_keys(uname)
        upwd_input.send_keys(upwd)
        login_btn.click()

        # 发说说
        wait(browser, "#aIcenter")
        browser.find_element_by_css_selector("#aIcenter").click()

        wait(browser, ".qz-inputer div.c_tx3")
        sub_input = browser.find_element_by_css_selector(".qz-inputer div.c_tx3")
        sub_input.click()

        txt_input = browser.find_element_by_css_selector(".qz-inputer div.c_tx2")
        txt_input.send_keys(str(datetime.now().replace(microsecond=0)).split(" ")[0] + ": " + state)

        wait(browser, ".qz-poster-ft .op .btn-post")
        poster_btn = browser.find_element_by_css_selector(".qz-poster-ft .op .btn-post")
        poster_btn.click()

        # 退出chrome
        time.sleep(10)
        browser.quit()
    except:
        Qzone(state)

def run():
    state = random.choice(Random.pop(random.randrange(0, len(Random))))
    if state != "死":
        t = Timer(86400, run)
        t.start()
    Qzone(state)

if __name__ == '__main__':
    time.sleep(86100)
    run()