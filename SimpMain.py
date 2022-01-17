from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from structs import page_parse_helper
from structs.user import User, create_user_from_page_json

driver = webdriver.Chrome(ChromeDriverManager().install())

current_popl_count = 10689

while True:
    # get to proper page
    current_popl_count += 1
    url = f"https://poplme.co/{current_popl_count}/r"
    driver.get(url)

    # get page source into a usable form
    profile_json = page_parse_helper.get_user_json(driver.page_source)

    # actually get user data
    user = create_user_from_page_json(profile_json)
