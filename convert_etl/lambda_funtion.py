# -*- coding: utf-8 -*-
""" 
Created by saul ramirez at 5/3/2021

"""

from urllib.parse import unquote_plus

from convert_file import Convert


def lambda_handler(event, contex):

    for row in event:
        bucket = row.get('bucket')
        prefix = row.get('prefix')

        convert = Convert(Prefix=prefix, Bucket=bucket)