# -*- coding: utf-8 -*-
""" 
Created by saul ramirez at 5/2/2021

"""

from metadata import MetaData



def lambda_handler(event, contex):

    if event:
        meta = MetaData(event=event)

        if meta:
            pass
        else:
            return meta
