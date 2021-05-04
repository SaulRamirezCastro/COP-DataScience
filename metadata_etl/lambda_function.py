# -*- coding: utf-8 -*-
""" 
Created by saul ramirez at 5/2/2021

"""

from metadata import MetaData



def lambda_handler(event, contex):

    if event:
        meta = MetaData(event=event)
        meta.metadata()

        response = json.loads(meta.to_json())

        if response.get('output'):
            return str(response)
        else:
            response['output'] = 1
            return str(response)
