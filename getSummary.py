import requests
import pandas as pd
import altair as alt

url = 'https://api.covid19api.com/summary'
sdf = pd.DataFrame(requests.get(url).json().get('Countries')).sort_values(by=['TotalConfirmed'], ascending=False)
print(sdf.head())
target = ['TotalRecovered','TotalConfirmed','TotalDeaths']
targetColors = ['green','orange','red']
bar_chart = alt.Chart(sdf[sdf.TotalDeaths > 10]).transform_fold(
    target,
    as_ = ['Category','Count']
).mark_bar(size=10).encode(
    x=alt.X('Country',sort='-y'),
    y='Count:Q',
    order=alt.Order(# Sort the segments of the bars by this field
        'Category:N',
        sort='descending'
    ),        
    color = alt.Color('Category:N',
        scale = alt.Scale(domain=target, range=targetColors),
        legend = alt.Legend(title="Category")
    )
).properties(
    width=800,
    height=400,
    title='Covid-19 cases and deaths'
)
bar_chart.display()    
