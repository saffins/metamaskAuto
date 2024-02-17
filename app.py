import json
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

#PLEASE SET PASSCODE BELOW
MNEMONIC = 'ginger angle tornado ribbon flush unique usage nominee mesh raw harvest half'.split(' ')
#MNEMONIC = 'rare rib fortune olive february forum warfare summer vote fragile season language'.split(' ')
PASSWORD = '11111111'

#--------------------------------------------------selenium config
chrome_options = Options()
chrome_options.add_extension('MetaMask_Chrome.crx')
chrome_options.add_argument("user-data-dir=C:\\Users\\alienware\\AppData\\Local\\Google\\Chrome\\User Data")
chrome_options.add_argument("profile-directory=Profile 2")
driver = webdriver.Chrome(options=chrome_options)
driver.maximize_window()
driver.implicitly_wait(10)
time.sleep(4)
driver.switch_to.window(driver.window_handles[1])
time.sleep(0.5)
#--------------------------------------------------

# fix "Message: unknown error: Runtime.callFunctionOn threw exception: Error: LavaMoat"
# solution: https://github.com/LavaMoat/LavaMoat/pull/360#issuecomment-1547271080
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/ul/li[1]/div/input').click() # agree to TOS
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/ul/li[3]/button').click() # import
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div/button[2]').click() # no thanks
time.sleep(0.5)
for i in range(3): driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # locate mnemonic box
for word in MNEMONIC:
    driver.switch_to.active_element.send_keys(word) # input each mnemonic to current textbox
    for i in range(2): driver.find_element(By.CSS_SELECTOR, 'body').send_keys(Keys.TAB) # switch to next textbox
    # time.sleep(0.5)
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[4]/div/button').click() # confirm
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[1]/label/input').send_keys(PASSWORD) # enter password
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[2]/label/input').send_keys(PASSWORD) # enter password twice
time.sleep(0.5)
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/form/div[3]/label/input').click() # I understand
driver.find_element('xpath', '//*[@id="app-content"]/div/div[2]/div/div/div/div[2]/form/button').click() # import my wallet
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # got it
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # next page
driver.find_element('xpath', '/html/body/div[1]/div/div[2]/div/div/div/div[2]/button').click() # done
time.sleep(1)
driver.switch_to.window(driver.window_handles[0])
driver.get("https://decentralize.metis.io/#szn2")
time.sleep(4)
aa = driver.execute_script('return document.querySelector("#root > div.season_one > div._header_12hqq_1 > div:nth-child(2) > div > w3m-button").shadowRoot.querySelector("w3m-connect-button").shadowRoot.querySelector("wui-connect-button")')
driver.execute_script('arguments[0].click();',aa)
ab = driver.execute_script('return document.querySelector("body > w3m-modal").shadowRoot.querySelector("wui-flex > wui-card > w3m-router").shadowRoot.querySelector("div > w3m-connect-view").shadowRoot.querySelector("wui-flex > wui-list-wallet:nth-child(3)").shadowRoot.querySelector("button > wui-text")')
driver.execute_script('arguments[0].click();',ab)
time.sleep(3)
driver.switch_to.window(driver.window_handles[2])
driver.find_element(By.XPATH,"//*[text()='Next']").click()
driver.find_element(By.XPATH,"//*[text()='Connect']").click()
driver.switch_to.window(driver.window_handles[0])
time.sleep(4)
chain = driver.execute_script('return document.querySelector("#szn2 > div > center > w3m-network-button").shadowRoot.querySelector("wui-network-button").shadowRoot.querySelector("button")')
driver.execute_script('arguments[0].click();',chain)
choosen = driver.execute_script('return document.querySelector("body > w3m-modal").shadowRoot.querySelector("wui-flex > wui-card > w3m-router").shadowRoot.querySelector("div > w3m-networks-view").shadowRoot.querySelector("wui-grid > wui-card-select").shadowRoot.querySelector("button")')
driver.execute_script('arguments[0].click();',choosen)
time.sleep(5)
driver.switch_to.window(driver.window_handles[2])
driver.find_element(By.XPATH,"//*[text()='Approve']").click()
driver.find_element(By.XPATH,"//*[text()='Switch network']").click()
driver.switch_to.window(driver.window_handles[0])
time.sleep(3)

# #GRAB TOKEN CODE BELOW
# # grabToken = driver.execute_script('return document.querySelector("#szn2 > div > div._cards_a8idn_1 > div:nth-child(1)")')
# # driver.execute_script('arguments[0].click();',grabToken)
#
# #claimbtn = driver.find_elements(By.XPATH,"//*[text()='Start Now']")
#
# grabTokenStatus = driver.find_elements(By.XPATH,"//*[text()='Completed']")
# if len(grabTokenStatus) > 0:
#     pass
# else:
#     pass
#
#
# #if len(claimbtn)>0:
#  #   claimbtn[0].click()
# # else:
# #     driver.find_element(By.XPATH, "(//*[@class='container'])[2]/div[3]/following::div[1]//input").click()
# #     print("unable to claim tokens 24 hours not passed yet")
#
#
#
# #SPIN PURCHASE CODE BELOW
# driver.find_element(By.XPATH, "(//*[@class='container'])[2]/div[3]/following::div[1]//input").clear()
#
# driver.find_element(By.XPATH, "(//*[@class='container'])[2]/div[3]/following::div[1]//input").send_keys("1")
# time.sleep(2)
# driver.find_element(By.XPATH, "(//*[@class='container'])[2]/div[3]/following::div[1]//button").click()
# time.sleep(3)
# driver.switch_to.window(driver.window_handles[2])
# driver.find_element(By.XPATH,"//*[text()='Confirm']").click()
# time.sleep(3)
# driver.switch_to.window(driver.window_handles[0])
#
# WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'SUCCESS')]")))
# print("User won "+ driver.find_element(By.XPATH,"//span[contains(text(),'SUCCESS')]/parent::div/following::div[1]").text)
# driver.find_element(By.XPATH,"//span[contains(text(),'SUCCESS')]/parent::div/parent::div/parent::div/div[1]/div").click()
#
#
# errorSpin = driver.find_elements(By.XPATH,"//*[text()='ERROR']")
# if(len(errorSpin)>0):
#     driver.find_element(By.XPATH, "(//*[@class='container'])[2]/div[3]/following::div[1]//input").clear()
#
#     driver.find_element(By.XPATH, "(//*[@class='container'])[2]/div[3]/following::div[1]//input").send_keys("1")
#     time.sleep(2)
#     driver.find_element(By.XPATH, "(//*[@class='container'])[2]/div[3]/following::div[1]//button").click()
#     time.sleep(3)
#     driver.switch_to.window(driver.window_handles[2])
#     driver.find_element(By.XPATH, "//*[text()='Confirm']").click()
#     time.sleep(3)
#
#
#
#
# driver.switch_to.window(driver.window_handles[0])
# #driver.find_element(By.XPATH,"//*[@class='_modal_header_close_12tym_30']").click()
#
#
# #driver.switch_to.window(driver.window_handles[2])
# grabToken = driver.execute_script('return document.querySelector("#szn2 > div > div.wheel-container > div > div:nth-child(5)")')
# driver.execute_script('arguments[0].click();',grabToken)
# time.sleep(3)
# driver.switch_to.window(driver.window_handles[2])
# driver.find_element(By.XPATH,"//*[text()='Confirm']").click()
# driver.switch_to.window(driver.window_handles[0])
# time.sleep(2)
# WebDriverWait(driver, 30).until(EC.visibility_of_element_located((By.XPATH, "//span[contains(text(),'SUCCESS')]")))
# print("User won "+ driver.find_element(By.XPATH,"//span[contains(text(),'SUCCESS')]/parent::div/following::div[1]").text)
# driver.find_element(By.XPATH,"//span[contains(text(),'SUCCESS')]/parent::div/parent::div/parent::div/div[1]/div").click()

driver.find_element(By.XPATH,"//*[text()='Enki']").click()
driver.find_element(By.XPATH,"//button[text()='Start Now']").click()
driver.switch_to.window(driver.window_handles[2])

driver.find_element(By.XPATH,"(//*[@class='sc-eqUAAy llnyos middle primary  false sc-fqkvVR eSlQxx'])[1]").click()
driver.find_element(By.XPATH,"//*[text()='Connect by Metamask']").click()
time.sleep(3)
driver.switch_to.window(driver.window_handles[3])
driver.find_element(By.XPATH,"//*[text()='Next']").click()

driver.find_element(By.XPATH,"//*[text()='Connect']").click()
time.sleep(2)
driver.switch_to.window(driver.window_handles[2])
driver.find_element(By.XPATH,"//*[text()='Launch App']").click()
driver.find_element(By.XPATH,"//*[@class='tokenWrapper']/following::input").send_keys("0.01")
driver.find_element(By.XPATH,"//*[text()='Approve']").click()
time.sleep(60000)
