# -*- coding: utf-8 -*-
""" 
Created by saul ramirez at 4/28/2021

"""
import csv
import logging
import boto3
import json
import tempfile
import gzip
import yaml

from botocore.exceptions import ClientError

logger = logging.getLogger(__name__)
logger.addHandler(logging.StreamHandler())
logger.setLevel(logging.INFO)


class Convert:

    _raw = None             # type: list
    _yaml_config = None     # type: dict
    _bucket = None          # type: str
    _prefix = None          # type: str
    _path = None            # type: str
    _kwargs = None          # type: dict
    _delimiter = None       # type: str
    _target_bkt = None      # type: str

    def __init__(self, **kwargs):
        logger.info("Initialize Class Convert")
        self._kwargs = kwargs

    def _read_txt(self):

        data = csv.reader(self._raw, delimiter=self._delimiter)
        tmp = list(data)

        if tmp:
            self._raw = tmp

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

    def _set_delimiter(self):

        if self._yaml_config.get('Delimiter'):
            self._delimiter = self._yaml_config.get('Delimiter')

    def _get_s3_file_body(self) -> None:
        """"get the body from the file in S3

        Return:
            None
        """
        s3 = self._s3_resource
        obj = s3.Object(self._bucket, self._prefix)
        obj = obj.get()['Body'].read().decode('utf-8')

        if obj:
            self._raw = obj.splitlines()

    def _put_object_s3(self) -> None:
        """"Put files(objects)  from local or /tmp to  s3 bucket

        Raise:
            ClientError: is something fail to upload the file
        Return:
            None
        """
        try:
            key = self._path.split('/')[-1]
            prefix = self._prefix.split('/')[:-2]
            key = f"{prefix}/{key}"
            self._s3_client.upload_file(self._path, self._target_bkt, key)

        except ClientError as e:
            logger.error(f"Error to put objects in S3, error{e}")

    def _write_tmp_csv(self):
        """"
        """
        tmp = tempfile.gettempdir()
        file = f"{tmp}/tmp.csv.gz"
        with gzip.open(file, 'wt') as file_out:
            for row in self._raw:
                file_out.writelines(row)

        self._path = str(file)

    def _set_prefix(self) -> None:
        """"Set the prefix  value from Arguments and store in the class variable _prefix
        Raise:
            Exception: if the prefix is not define in the arguments
        Return:
            None
        """
        if not self._kwargs.get('Prefix'):
            logger.error("Don't define Prefix in the Arguments")
            raise Exception

        self._prefix = self._kwargs.get('Prefix')

    def _set_bucket(self) -> None:
        """"set bucket value from Arguments and store in the class variable _bucket, if the bucket are not in arguments
        take the value from yaml config file.

        Return:
            None
        """
        if self._kwargs.get('Bucket'):
            self._bucket = self._kwargs.get('Bucket')

    def _set_bucket_target(self) -> None:
        """"set bucket value from Arguments and store in the class variable _bucket, if the bucket are not in arguments
        take the value from yaml config file.

        Return:
            None
        """
        if self._yaml_config.get('target_bkt'):
            self._target_bkt = self._yaml_config.get('target_bkt')

    @property
    def _s3_resource(self) -> boto3.client:
        """"Get S3 connection

        Return:
            S3 connection
        """
        return boto3.resource('s3')

    @property
    def _s3_client(self) -> boto3.client:
        """"Get S3 connection

        Return:
            S3 connection
        """
        return boto3.client('s3')

    @staticmethod
    def _clear_tmp(path: str) -> None:
        """"remove the file from tmp directory
         Args:
             path(str): path from the file
        Return:
            None
        """
        os.remove(path)

