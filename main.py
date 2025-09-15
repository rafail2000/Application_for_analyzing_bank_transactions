from pprint import pprint

from src.services import main_services
from src.views import main_page




if __name__ == "__main__":
    pprint(main_page("2020-05-20 12:30:30"))
    pprint(main_services("2020", "05"))