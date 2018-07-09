# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 10:39:33 2018

@author: jimmybow
"""
from dash import Dash
from dash.dependencies import Input, State, Output
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import string, random
from flask_caching import Cache

def Add_Dash(server):
    app = Dash(server=server, url_base_pathname='/dash')
    app.config.supress_callback_exceptions = True
    
    cache = Cache(app.server, config={
        'CACHE_TYPE': 'filesystem',
        'CACHE_DIR': 'cache-directory',
        'CACHE_THRESHOLD': 10  # should be equal to maximum number of active users
    })
    
    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),
        html.Div(id='index')
    ])
    
    @cache.memoize()
    def create_secret(secret):
        return ''.join(random.choice(string.ascii_letters + string.digits) for x in range(100))

    @app.callback(
            Output('index', 'children'),
            [Input('url', 'search')]     )
    def display_page(request_args):
        if request_args:
            rr = pd.Series(str(request_args)[1:].split('&')).str.split('=')
            key = rr.str.get(0)
            value = rr.str.slice(1,).str.join('=')   
            if 'secret' in list(key) and value[key == 'secret'].iloc[0] == create_secret('secret'):
                return  html.Div([
                            html.Div(id='target'),
                            dcc.Input(id='input', type='text', value='')
                        ])
        return html.Div('Error ! 不可訪問 !')
    
    @app.callback(
            Output('target', 'children'),
            [Input('input', 'value')])
    def callback(text):
        return "callback received value: {}".format(text)
    
    return app.server, create_secret