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
    df_json_sort = []
    for i in range(len(df_json)):
        if df_json[i]["Part #"] == None:
            logger.debug("Empty entry")
            continue
        else:
            df_json[i]["number"] = df_json[i].pop("#")
            df_json[i]["state"] = df_json[i].pop("New/Carry Over")
            df_json[i]["type"] = df_json[i].pop("Clamp/Latch")
            df_json[i]["cert"] = df_json[i].pop("Certs Needed")
            df_json[i]["npx"] = df_json[i].pop("NPX or DLT Needed")
            df_json[i]["po"] = df_json[i].pop("PO / File #")
            df_json[i]["part_number"] = df_json[i].pop("Part #")
            df_json[i]["quantity"] = df_json[i].pop("Qty.")
            df_json[i]["needs"] = df_json[i].pop("Needs")
            df_json[i]["status"] = df_json[i].pop("Status")
            df_json[i]["notes"] = df_json[i].pop("Notes")
            df_json[i]["ship_date"] = df_json[i].pop("Ship by:")
            
            try:
                timestamp = df_json[i]["ship_date"]/1000
                date = datetime.fromtimestamp(timestamp)
                df_json[i]["ship_date"] = date.strftime("%m/%d/%Y")
            except:
                logger.debug("Timestamp not avalible")

            if df_json[i]["status"] == "Shipped/ Shipping":
                df_json[i]["color"] = "green"
            elif df_json[i]["status"] == "Waiting on Virginia":
                df_json[i]["color"] = "yellow"
            elif df_json[i]["status"] == "Job is stopped":
                df_json[i]["color"] = "red"
            elif df_json[i]["status"] == "Stock items need to be pulled":
                df_json[i]["color"] = "lightblue"
            elif df_json[i]["status"] == "Job is delayed":
                df_json[i]["color"] = "orange"
            else:
                df_json[i]["color"] = "white"

            if group == 'C':
                if df_json[i]['type'] == "C":
                    logger.debug("clamps")
                    df_json_sort.append(df_json[i])
                else:
                    continue
            elif group == 'L':
                if df_json[i]['type'] == "L":
                    logger.debug("latches")
                    df_json_sort.append(df_json[i])
                else:
                    continue
            else:
                df_json_sort.append(df_json[i])
                continue
        
    if sorting == "number":
        return_json = sorted(df_json_sort,key=lambda i:i[sorting])
    else:
        return_json = sorted(df_json_sort,key=lambda i:i[sorting], reverse=True)

    return return_json
