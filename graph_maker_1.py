import altair as alt
import pandas as pd
import os

alt.data_transformers.enable("default", max_rows=None)
alt.data_transformers.enable('data_server')
from vega_datasets import data

alt.renderers.enable('default')

#writing a function

def functionChart1 (url_1,x,y):
    chart_test =alt.Chart(url_1).mark_circle(size =40,clip=True).encode( 
                alt.X(x+':Q',impute=alt.ImputeParams(value=None),bin=alt.Bin(maxbins=30),title ='BodyWeight(Kgs)'),
                alt.Y(y+':Q',impute=alt.ImputeParams(value=None),bin=alt.Bin(maxbins=30),title =y+'(Kgs)'),
                alt.Color('count()')).transform_filter(alt.datum[x] >0).transform_filter(alt.datum[y] >0)
    chart_test_1 = chart_test.facet(('Sex:N')).resolve_scale(y='independent')
    return chart_test_1
        
        
   
    
