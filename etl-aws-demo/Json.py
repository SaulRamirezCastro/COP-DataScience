# -*- coding: utf-8 -*-
""" 
Created by saul ramirez at 4/28/2021

"""
import csv
import logging
import boto3
import json
import gzip

logger = logging.getLogger(__name__)


class Json:

    _raw = None        # type: list

    def __init__(self):
        pass

    def _read_txt(self):

        with open('resyt', w) as f_in:
            data = csv.reader(self._raw, delimiter='')

        if data:
            self._raw = data

    def _get_s3_file_body(self) -> None:
        """"get the body from the file in S3

        Return:
            None
        """
        s3 = self._s3_client
        obj = s3.Object(self._bucket, self._prefix)
        obj = obj.get()['Body'].read()

        if obj:
            self._raw = obj.splitlines()

    def _put_object_s3(self, key: str, path: str) -> None:
        """"Put files(objects)  from local or /tmp to  s3 bucket

        Raise:
            ClientError: is something fail to upload the file
        Return:
            None
        """
        try:
            obj_key = f"{path}/{key}"
            self._s3_client.upload_file(key, self._bucket, obj_key)

        except ClientError as e:
            logger.error(f"Error to put objects in S3, error{e}")

    def _write_tmp_csv(self):
        """"
        """
        with gzip.open(self._path, 'wb') as file:
            file.writelines(self._raw)

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
        if not self._kwargs.get('Bucket'):
            self._bucket = self._yaml_config['constants']['bucket_config'][self._stage]
        else:
            self._bucket = self._kwargs.get('Bucket')

    @property
    def _s3_client(self) -> boto3.resource:
        """"Get S3 connection

        Return:
            S3 connection
        """
        s3 = boto3.client('s3')

        return s3

    @staticmethod
    def _clear_tmp(path: str) -> None:
        """"remove the file from tmp directory
         Args:
             path(str): path from the file
        Return:
            None
        """
        os.remove(path)

