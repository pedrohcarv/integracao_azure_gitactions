import logging

import azure.functions as func
import pandas as pd
import json


def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    df = pd.read_csv(r'C:\Users\Desktop\Desktop\Dados\data_factory\datafactory\functions-project\tranformacao-simples\Medals.csv', sep=';')
    df.drop(['Total'], axis=1, inplace=True)
    df_json = df.to_json(orient="index")
    

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully.")
    else:
        return func.HttpResponse(df_json, status_code=200)
