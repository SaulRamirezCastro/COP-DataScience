# -*- coding: utf-8 -*-
""" 
Created by saul ramirez at 11/06/2024

"""
import json

import boto3
import logging
import yaml
from urllib.parse import unquote_plus


logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


class MetaData:

    _table = None       # type: str
    _dynamo = None      # type: boto3
    _yaml_config = None # type: dict
    _kwargs = None    # type: dict

    def __init__(self, **kwargs):
        logger.info("Class to Persist Metadata")
        self._kwargs = kwargs

    def json(self):

        return json.dumps(self._meta)

    def metadata(self):

        self._set_kwargs()
        self._read_yaml_file()
        self._set_table()
        self.dynamo_client
        self._parse_event()
        meta = self._get_metadata()
        if meta:
            self._insert_meta()

    def _set_kwargs(self):

        if self._kwargs:
            data = self._kwargs.get('event')

        if data:
            self._kwargs = data

    def _read_yaml_file(self) -> None:
        """Read the Yaml file configuration and set into the class variable
        '_yaml_config'
        Return:
            None
        """
        yaml_file = "config.yml"
        with open(yaml_file) as f:
            data = yaml.safe_load(f)

        if data:
            self._yaml_config = data

    def _set_table(self) -> None:
        """Set table value from yaml config file
        Return:
            None
        """
        table = self._yaml_config.get('table')

        if table:
            self._table = table

    def _parse_event(self) -> None:
        """Parser the event(dict) and generate the meta data from the file
        Return:
            None
        """

        for record in self._kwargs['Records']:
            checksum = record['s3']['object']['eTag']
            bucket = record['s3']['bucket']['name']
            key = unquote_plus(record['s3']['object']['key'])
            event_time = record['eventTime']

        meta = {
            "Id": checksum,
            "checksum": checksum,
            "bucket":  bucket,
            "key": key,
            "time": event_time
            }

        if meta:
            self._meta = meta

    def _get_metadata(self) -> dict:
        """get meta data from dynamo table

        Return:
            Item(dict): values from dynamo table
        """

        table = self._dynamo.Table(self._table)
        key = {"Id": self._meta.get('Id'),
               "checksum": self._meta.get('checksum')}
        data = table.get_item(Key=key)

        if data.get('Item'):
            return data.get('Item')
        else:
            return None

    def _insert_meta(self):
        """"Insert Meta data in dynamodb table

        Return:
            response(dict):
        """
        table = self._dynamo.Table(self._table)

        response = table.put_item(Item=self._meta)
        return response

    @property
    def dynamo_client(self) -> None:
        """Set dynamodb client from boto3

        Return:
            None
        """

        dynamodb = boto3.resource('dynamodb', region_name='us-east-1')

        self._dynamo = dynamodb
