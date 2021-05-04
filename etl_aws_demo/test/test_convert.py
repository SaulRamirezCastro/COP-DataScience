# -*- coding: utf-8 -*-
""" 
Created by saul ramirez at 5/2/2021

"""

from etl_aws_demo.convert_file import Convert

def test_init_class():
    process = Convert(Prefix='files/CP_Mexico.txt', Bucket='aws-bronce-bkt')

    return process

# def test_set_prefix():
#     process = test_init_class()
#     process._set_prefix()
#     process._set_key()
#     print(process._prefix)
#
# def test_set_bucket():
#     process = test_init_class()
#     process._set_bucket()
#     print(process._bucket)
#
# def test_get_s3_file_body():
#     process = test_init_class()
#     process._set_prefix()
#     process._set_bucket()
#     process._get_s3_file_body()
#
#
# def test_read_txt():
#     process = test_init_class()
#     process._set_prefix()
#     process._set_bucket()
#     process._set_key()
#     process._read_yaml_file()
#     process._set_delimiter()
#     process._set_bucket_target()
#     process._get_s3_file_body()
#     process._read_txt()
#     process._write_tmp_csv()
#     process._put_object_s3()}


def test_process():
    process = test_init_class()
    process.convert_file()
