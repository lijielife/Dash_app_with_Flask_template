# -*- coding: utf-8 -*-
"""
Created on Sun Jul  8 10:39:33 2018

@author: jimmybow
"""
from dash import Dash
from dash.dependencies import Input, State, Output
import dash_core_components as dcc
import dash_html_components as html

def Add_Dash(server):
    app = Dash(server=server, url_base_pathname='/dash2')
    app.layout = html.Div('Dash App 2')
    
    return app.server