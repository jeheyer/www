import base64
import json
from webapps import ping


def lambda_handler(event, context):

    print(event)

    http_request = {
        'host': event['headers']['host'],
        'path': event['path'],
        'query_string': event['queryStringParameters'],
        'client_ip': event['headers']['x-forwarded-for']
    }

    http_response = {
        'statusCode': None,
        'headers': { 
            'Content-Type': "text/plain",
            'Cache-Control': "no-cache, no-store",
            'Pragma': "no-cache"
        },
        'body': ""
    }

    try:
        data = ping(dict(http_request))
        http_response['statusCode'] = 200
        if isinstance(data, dict):
            http_response['headers']['Content-Type'] = "application/json"
            http_response['body'] = json.dumps(data)
        elif isinstance(data, str):
            http_response['body'] = format(data)
        else:
            http_response['isBase64Encoded'] = True
            http_response['body'] = base64.b64encode(data).decode("utf-8")

    except Exception as e:

        http_response['statusCode'] = 500
        http_response['body'] = format(e)
     
    print(http_response)
    return http_response 
 
