import json

import requests
import numpy as np
from hello import hello_function 
import pyodbc


def lambda_handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """

    a = np.arange(15).reshape(3, 5)
    print(a)

    hello_function()

    # generate sample code to inizialize the connection to the database
    server = 'myserver.database.windows.net'    
    database = 'XXXXXXXXXX'
    username = 'XXXXXXXXXX'
    password = 'XXXXXXXXXX'
    driver = '{ODBC Driver 17 for SQL Server}'
    try:
        cnxn = pyodbc.connect('DRIVER=' + driver + ';SERVER=' + server + ';PORT=1433;DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    except pyodbc.Error as e:
        print(e)

    try:
        ip = requests.get("http://checkip.amazonaws.com/")
    except requests.RequestException as e:
        # Send some context about this error to Lambda Logs
        print(e)

        raise e

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "hello world",
            "location": ip.text.replace("\n", "")
        }),
    }
