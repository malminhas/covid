import requests
import pandas as pd
import altair as alt
import numpy as np

def getCategoryByCountryFromAPI(category: str, country: str, color: str) ->  pd.DataFrame:
    url = f'https://api.covid19api.com/total/country/{country}/status/{category.lower()}'
    sdf = pd.DataFrame(requests.get(url).json())
    sdf['Date'] = sdf['Date'].apply(pd.to_datetime)
    sdf.rename(columns={"Cases": category}, inplace=True)
    sdf['New'] = sdf[category].diff()
    sdf[f'Log{category}'] = np.log(sdf[category])
    sdf['LogNew'] = np.log(sdf['New'])
    return sdf

def plotByCountryFromAPI(df: pd.DataFrame, xval: str, yval: str) -> None:
    line_chart = alt.Chart(df).mark_line().encode(
        x=f'{xval}:Q',
        y=f'{yval}:Q',
        color=alt.value(color)
    ).properties(
        width=800,
        height=400,
        title=f'Covid-19 {yval} by {xval} in {country}'
    )
    line_chart.display()

what = 'Deaths'
color = 'red'
country = 'us'
plotByCountryFromAPI(getCategoryByCountryFromAPI(what, country, color='red'), f'Log{what}', 'LogNew')
