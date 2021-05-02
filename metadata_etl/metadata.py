# -*- coding: utf-8 -*-
""" 
Created by saul ramirez at 4/28/2021

"""

import boto3

class MetaData:

    _table = None       # type: str
    _dynamo = None      # type: boto3



    def __init__(self):
        pass

    def _parse_event(self):
        """
        {
  "Records": [
    {
      "eventVersion": "2.0",
      "eventSource": "aws:s3",
      "awsRegion": "us-east-1",
      "eventTime": "1970-01-01T00:00:00.000Z",
      "eventName": "ObjectCreated:Put",
      "userIdentity": {
        "principalId": "EXAMPLE"
      },
      "requestParameters": {
        "sourceIPAddress": "127.0.0.1"
      },
      "responseElements": {
        "x-amz-request-id": "EXAMPLE123456789",
        "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
      },
      "s3": {
        "s3SchemaVersion": "1.0",
        "configurationId": "testConfigRule",
        "bucket": {
          "name": "example-bucket",
          "ownerIdentity": {
            "principalId": "EXAMPLE"
          },
          "arn": "arn:aws:s3:::example-bucket"
        },
        "object": {
          "key": "test/key",
          "size": 1024,
          "eTag": "0123456789abcdef0123456789abcdef",
          "sequencer": "0A1B2C3D4E5F678901"
        }
      }
    }
  ]
}
        """

        pass
    def _get_metadata_event(self):
        pass

    def _insert_meta(self):
        """"
        """
        table = self._dynamo.Table(self._table)
        item = {}

        response = table.put_item(Item=item)
        return response

    @property
    def dynamo_client(self) -> None:
        """Set dynamodb client from boto3+

        Return:
            None
        """

        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        self._dynamo = dynamodb
