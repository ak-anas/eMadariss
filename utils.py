# Winreg
from winreg import HKEY_CURRENT_USER, OpenKey, QueryValueEx
# Trello
from trello import TrelloApi
# Others
from dotenv import load_dotenv
import os

load_dotenv()

class Browser:
    def get_browser_name() -> str:
        register_path = r'Software\Microsoft\Windows\Shell\Associations\UrlAssociations\https\UserChoice'
        with OpenKey(HKEY_CURRENT_USER, register_path) as key:
            return str(QueryValueEx(key, "ProgId")[0])
        
class Trello:
    global client
    API_KEY = os.getenv("API_KEY")
    TOKEN = os.getenv("TOKEN")
    client = TrelloApi(API_KEY, TOKEN)

    def get_cards():
        cards = client.boards.get_card(board_id="656dba17f101c2326899c90b")
        names = []
        for card in cards:
            names.append(card["name"])

        return names

    def send_card(name, description, label_id, list_id="656dba17f101c2326899c912"):
        client.cards.new(name=name, desc=description, idList=list_id, idLabels=[label_id])