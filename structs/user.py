from bs4 import BeautifulSoup

class User:
    name = None
    popl_id = None
    snapchat_username = None
    email = None
    phone_number = None
    tiktok = None

    def save(self):
        print("saving...")

    def is_empty(self):
        if self.name is None:
            return True
        return False

def create_user_from_page_json(profile_json: dict, page_html) -> User:
    new_user = User()
    soup = BeautifulSoup(page_html)
    profile_id_packet_raw = soup.find('p', class_="MuiTypography-root MuiTypography-body1 css-kj7pvm")
    new_user.name = profile_id_packet_raw.text
    if len(new_user.name) == 0:
        new_user.name = None
    user_data = profile_json["props"]["pageProps"]["profile"]
    user_link_data = user_data["linkData"]["data"]
    for section in user_link_data:
        identifier = section["icon_alt"]

        if "snapchat" in identifier:
            new_user.snapchat_username = section["value"]
        elif "phone number" in identifier:
            new_user.phone_number = section["value"]
        elif "email" in identifier:
            new_user.email = section["value"]
        elif "tiktok" in identifier:
            new_user.tiktok = section["value"]
    return new_user
