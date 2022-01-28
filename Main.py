import pathlib
import time

from msedge.selenium_tools import Edge, EdgeOptions

# currently supported version: Microsoft Edge: 97.0.1072.69 (Official build) (64-bit)
# MS-Edge driver url - https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
# Note: to check your ms edge browser version:
# 1. Open your MS Edge
# 2. Navigate to url input textbox
# 3. type: chrome:version
# 4. You should see something similar to this: Microsoft Edge: 97.0.1072.69 (Official build) (64-bit)


current_path = str(pathlib.Path().absolute()) + r'\edgedriver_win64\msedgedriver.exe'
# Target site to fill the health tracker
site_url = ''
# this starts with PH (see GT&E under your profile to know your GPN #)
gpn_number = ''
mobile_num = ''
address = ''

# check if mobile number is empty assign value same
if len(mobile_num.strip()) == 0:
    mobile_num = 'same'

print(current_path)

# Launch Microsoft Edge (EdgeHTML)

options = EdgeOptions()
options.use_chromium = True
options.add_argument(r"--user-data-dir={}\AppData\Local\Microsoft\Edge\User Data".format(pathlib.Path().home()))

driver = Edge(current_path, options=options)

try:
    driver.get(site_url)
    time.sleep(10)
    driver.implicitly_wait(2)

    # Input the gpn number
    gpn = driver.find_element_by_xpath(
        '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[2]/div/div[2]/div/div/input')
    gpn.click()
    gpn.clear()
    gpn.send_keys(gpn_number)

    time.sleep(2)

    # click I agree
    rad_consent = driver.find_element_by_xpath(
        '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[1]/div/label/span')

    label_description = str(rad_consent.text).lower().strip()

    if label_description == 'yes, i agree and give consent. proceed to answer the form' or 'yes, i agree' in label_description:
        rad_consent.click()
    else:
        rad_consent = driver.find_element_by_xpath(
            '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div[2]/div/div[2]/div/label/span')
        rad_consent.click()

    time.sleep(2)

    # click I'm feeling well
    rad_feeling = driver.find_element_by_xpath(
        '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[4]/div/div[2]/div/div[1]/div/label/span')
    rad_feeling.click()

    time.sleep(2)

    # click working from home
    rad_WFH = driver.find_element_by_xpath(
        '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[5]/div/div[2]/div/div[1]/div/label/span')
    rad_WFH.click()

    time.sleep(2)

    txt_current_residing = driver.find_element_by_xpath(
        '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[6]/div/div[2]/div/div/input')
    txt_current_residing.click()
    txt_current_residing.clear()
    txt_current_residing.send_keys(address)

    rad_been_diagnosed = driver.find_element_by_xpath(
        '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[7]/div/div[2]/div/div[2]/div/label/span')
    rad_been_diagnosed.click()

    time.sleep(2)

    rad_close_contact = driver.find_element_by_xpath(
        '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[8]/div/div[2]/div/div[2]/div/label/span')
    rad_close_contact.click()

    time.sleep(2)

    rad_travel_outside = driver.find_element_by_xpath(
        '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[9]/div/div[2]/div/div[2]/div/label/span')
    rad_travel_outside.click()

    time.sleep(2)

    rad_travel_NCR = driver.find_element_by_xpath(
        '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[10]/div/div[2]/div/div[2]/div/label/span')
    rad_travel_NCR.click()

    time.sleep(2)

    txt_contact_number = driver.find_element_by_xpath(
        '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[12]/div/div[2]/div/div/input')
    txt_contact_number.click()
    txt_contact_number.clear()
    txt_contact_number.send_keys(mobile_num)

    time.sleep(2)

    rad_confirmation = driver.find_element_by_xpath(
        '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[2]/div[13]/div/div[2]/div/div/div/label/span')
    rad_confirmation.click()

    time.sleep(2)

    send_me_receipt = driver.find_element_by_xpath(
        '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[3]/div/div/label/span')
    send_me_receipt.click()

    time.sleep(2)

    button_submit = driver.find_element_by_xpath(
        '//*[@id="form-container"]/div/div/div[1]/div/div[1]/div[2]/div[4]/div[1]/button/div')
    button_submit.click()

    input("\n\nSuccessfully submit health tracker press enter key to close the application.")
finally:
    driver.close()