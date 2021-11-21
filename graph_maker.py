

import altair as alt
import pandas as pd
import os

alt.data_transformers.enable("default", max_rows=None)
alt.data_transformers.enable('data_server')
from vega_datasets import data

alt.renderers.enable('default')


def functionChart (url_1,x,y,u):
    select_Equipment=alt.selection_multi(fields=['Equipment'], bind ='legend')
    chart_test =alt.Chart(url_1).mark_circle(size =10,clip=True).encode( 
                alt.X(x+':Q',impute=alt.ImputeParams(value=None),scale=alt.Scale(zero=False,domain=[10,250]),axis =alt.Axis (title ='BodyWeight(Kgs)')),
                alt.Y(y+':Q',impute=alt.ImputeParams(value=None),scale=alt.Scale(zero=False,domain = [10,u]),axis =alt.Axis (title =y+'(Kgs)')),
                alt.Color('Equipment:N'),[alt.Tooltip(x+":Q", title="Body Weight Kilograms"),alt.Tooltip("BestSquatKg:Q", title="Best Squat Kilogram"),alt.Tooltip("BestBenchKg:Q", title="Best Bench Kilogram"),alt.Tooltip("BestDeadliftKg:Q", title="Best Dead Lift Kilogram"),alt.Tooltip("Equipment:N", title="Equipment")],
                opacity=alt.condition(select_Equipment,alt.value(0.80),alt.value(0))).transform_filter(alt.datum[x] >0).transform_filter(alt.datum[y] >0).properties(width=300,height=300)
    chrat_test=chart_test.transform_regression(x,y,extent=[20,225],groupby=['Equipment']).mark_line(size=4).properties(width=300,height=300)
    chart_test_1=(chart_test+chrat_test).add_selection(select_Equipment)
    return chart_test_1
    