import boto3
import json
import os
from datetime import date

client = boto3.client("dynamodb")
web_page_counter = os.environ.get('DataBaseName')
curr_date = date.today().strftime("%m/%d/%y")


def test_lambda(event, context):
    response_body = client.update_item(
        TableName=web_page_counter,
        Key={"Date": {"S": curr_date}},
        UpdateExpression="ADD total_views :view",
        ExpressionAttributeValues={":view": {"N": "1"}},
        ReturnValues="ALL_NEW"
    )

    res = response_body["Attributes"]["total_views"]["N"]

    response = \
        {
            "isBase64Encoded": True,
            "statusCode": 200,
            "headers":
                {
                    'Access-Control-Allow-Headers': "Content-Type",
                    'Access-Control-Allow-Origin': "https://www.geoffreynguyendo-resume.com",
                    'Access-Control-Allow-Methods': 'OPTIONS,POST,GET'
                },
            # "multiValueHeaders": {},
            "body": json.dumps(res, indent=1)
        }
    return response
