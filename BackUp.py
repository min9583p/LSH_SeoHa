import shutil
from datetime import date
import time

today = date.today()  
date_format = time.strftime("%Y-%m-%d_%H시%M분%S초")

dst_name=date_format+'_UserDB_BackUp'

shutil.copy('./userDB.xlsx', f'./BackUp/{dst_name}.xlsx')

  