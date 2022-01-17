from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from structs import page_parse_helper
from structs.user import User, create_user_from_page_json

mobile_emulation = {
    "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 },
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Mobile Safari/535.19"
}

chrome_options = Options()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
# driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

current_popl_count = 10938

while True:
    # get to proper page
    current_popl_count += 1
    url = f"https://poplme.co/{current_popl_count}/r"
    driver.get(url)
    if "popl" not in driver.current_url:
        continue

    # get page source into a usable form
    profile_json = page_parse_helper.get_user_json(driver.page_source)

    # actually get user data
    user = create_user_from_page_json(profile_json, driver.page_source)
    if user.is_empty():
        continue
    print(user.name)
    print(user.phone_number)
    print(user.email)
    print(user.snapchat_username)
    print(user.tiktok)
    print("----------------------")


