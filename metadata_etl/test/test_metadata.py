# -*- coding: utf-8 -*-
""" 
Created by saul ramirez at 5/1/2021

"""

from metadata_etl.metadata import MetaData


def test_init_class():
    process = MetaData()

    return process


def test_set_table():
    process = test_init_class()
    process._set_table()


def test_insert_meta():
    process = test_init_class()
    process._set_table()
    process.dynamo_client
    process._insert_meta()
