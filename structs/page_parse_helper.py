import json
from bs4 import BeautifulSoup


def get_user_json(html: str) -> dict:
    soup = BeautifulSoup(html)
    profile_id_packet_raw = soup.find('script', id="__NEXT_DATA__")
    profile_id_packet_str = profile_id_packet_raw.text
    profile_json = json.loads(profile_id_packet_str)
    return profile_json
