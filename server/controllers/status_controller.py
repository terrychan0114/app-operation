import connexion
import six
import pandas as pd
from pandas import ExcelFile
import json
from flask import Response
from loguru import logger
from datetime import datetime

from server.models.status_info import StatusInfo  # noqa: E501
from server import util

# file = "/usr/src/app/doc/kaizen_board.xlsx"
file = "X:/S1-Operations Shared/PAT Production Meeting/test_production.xlsx"

def get_statusnj(sorting, group=None):  # noqa: E501
    """Get all status at Paterson

     # noqa: E501

    :param sorting: This is getting the suggestion status with sorting order
    :type sorting: str
    :param group: This is getting a specific status group
    :type group: str

    :rtype: List[StatusInfo]
    """
    df = pd.read_excel(file, sheet_name='Sheet1')

    result = df.to_json(orient="records")
    df_json = json.loads(result)
    for i in range(len(df_json)):
        
        df_json[i]["number"] = df_json[i].pop("number")
        df_json[i]["state"] = df_json[i].pop("New/Carry Over")
        df_json[i]["type"] = df_json[i].pop("Clamp/Latch")
        df_json[i]["part_number"] = df_json[i].pop("Part #")
        df_json[i]["quantity"] = df_json[i].pop("Qty.")
        df_json[i]["needs"] = df_json[i].pop("Needs")
        df_json[i]["status"] = df_json[i].pop("Status")
        df_json[i]["ship_date"] = df_json[i].pop("Ship by:")
        try:
            timestamp = df_json[i]["Date added"]/1000
            date = datetime.fromtimestamp(timestamp)
            df_json[i]["date_added"] = date.strftime("%m/%d/%Y")
            df_json[i].pop("Date added")
        except:
            logger.debug("This is not a timestamp")

        
    if sorting == "number":
        return_json = sorted(df_json,key=lambda i:i[sorting])
    else:
        return_json = sorted(df_json,key=lambda i:i[sorting], reverse=True)
    # logger.debug(df_json_sort)
    return return_json
