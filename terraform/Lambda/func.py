import json
import boto3
from decimal import Decimal

def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')
    table = dynamodb.Table('VisitorCount')

    try:
        response = table.update_item(
            Key={'id': 'website-visitor'},
            UpdateExpression='SET #count = #count + :increment',
            ExpressionAttributeNames={'#count': 'count'},
            ExpressionAttributeValues={':increment': 1},
            ReturnValues='UPDATED_NEW'
        )
        
        visitor_count = float(response['Attributes']['count'])  # Convert Decimal to float

        # Create the response object with CORS headers
        response_headers = {
            "Content-Type": "application/json",
            "Access-Control-Allow-Origin": "https://saminthecloud.tech",  # Replace with your allowed origin(s)
            "Access-Control-Allow-Methods": "GET, POST, PUT, DELETE, OPTIONS",  # Adjust the allowed HTTP methods
            "Access-Control-Allow-Headers": "Content-Type, Authorization",  # Adjust the allowed headers
            "Access-Control-Allow-Credentials": "true"  # If you need to allow credentials
        }

        response_body = {
            'visitorCount': visitor_count
        }

        return {
            'statusCode': 200,
            'headers': response_headers,  # Include CORS headers
            'body': json.dumps(response_body)
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'headers': response_headers,  # Include CORS headers even for errors
            'body': json.dumps({'error': str(e)})
        }