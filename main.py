from pprint import pprint

import pandas as pd

from config import PATH_TO_EXCEL
from src.reports import main_service
from src.services import main_services
from src.views import main_page




if __name__ == "__main__":
    pprint(main_page("2020-05-20 12:30:30"))
    pprint(main_services("2020", "05"))

    df = pd.read_excel(PATH_TO_EXCEL)
    pprint(main_service(df, "Супермаркеты", "31.12.2021"))