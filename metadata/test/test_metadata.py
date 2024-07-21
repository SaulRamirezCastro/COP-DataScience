# -*- coding: utf-8 -*-
""" 
Created by saul ramirez at 5/1/2021

"""

from metadata.metadata import MetaData


def test_init_class():
    process = MetaData()

    return process


# def test_parse_event():
#     process = test_init_class()
#     process._kwargs =         {
#   "Records": [
#     {
#       "eventVersion": "2.0",
#       "eventSource": "aws:s3",
#       "awsRegion": "us-east-1",
#       "eventTime": "1970-01-01T00:00:00.000Z",
#       "eventName": "ObjectCreated:Put",
#       "userIdentity": {
#         "principalId": "EXAMPLE"
#       },
#       "requestParameters": {
#         "sourceIPAddress": "127.0.0.1"
#       },
#       "responseElements": {
#         "x-amz-request-id": "EXAMPLE123456789",
#         "x-amz-id-2": "EXAMPLE123/5678abcdefghijklambdaisawesome/mnopqrstuvwxyzABCDEFGH"
#       },
#       "s3": {
#         "s3SchemaVersion": "1.0",
#         "configurationId": "testConfigRule",
#         "bucket": {
#           "name": "example-bucket",
#           "ownerIdentity": {
#             "principalId": "EXAMPLE"
#           },
#           "arn": "arn:aws:s3:::example-bucket"
#         },
#         "object": {
#           "key": "test/key",
#           "size": 1024,
#           "eTag": "0123456789abcdef0123456789abcdef",
#           "sequencer": "0A1B2C3D4E5F678901"
#         }
#       }
#     }
#   ]
# }
#     process._parse_event()


def test_set_table():
    process = test_init_class()
    process._read_yaml_file()
    process._set_table()


def test_insert_meta():
    process = test_init_class()
    process._read_yaml_file()
    process._set_table()
    process.dynamo_client
    process._kwargs = {
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
    process._parse_event()
    process._insert_meta()


def test_get_meta():
    process = test_init_class()
    process._read_yaml_file()
    process._set_table()
    process._kwargs = {
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
    process.dynamo_client
    process._parse_event()
    process._get_metadata()


def test_metadata():
    process = test_init_class()
    process._kwargs = {
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
    response = process.metadata()
    print(response)


def test_set__kwargs():
    kwargs = {
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
    process = MetaData(event=kwargs)
    data = process.metadata()
    print(data)
