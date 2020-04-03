import requests
import pandas as pd
import altair as alt
import numpy as np
import warnings
warnings.filterwarnings("ignore", category=RuntimeWarning) # for handling log(0)

PROGRAM = 'getNewVsExisting.py'
VERSION = ''

def getCategoryByCountryFromAPI(category: str, country: str, color: str) ->  pd.DataFrame:
    url = f'https://api.covid19api.com/total/country/{country}/status/{category.lower()}'
    sdf = pd.DataFrame(requests.get(url).json())
    sdf['Date'] = sdf['Date'].apply(pd.to_datetime)
    sdf.rename(columns={"Cases": category}, inplace=True)
    sdf['New'] = sdf[category].diff()
    sdf[f'Log{category}'] = np.log(sdf[category])
    sdf['LogNew'] = np.log(sdf['New'])
    return sdf

def plotByCountryFromAPI(df: pd.DataFrame, xval: str, yval: str) -> alt.vegalite.v4.api.Chart:
    line_chart = alt.Chart(df).mark_line().encode(
        x=f'{xval}:Q',
        y=f'{yval}:Q',
        color=alt.value(color)
    ).properties(
        width=800,
        height=400,
        title=f'Covid-19 {yval} by {xval} in {country}'
    )
    return line_chart

def getColor(category :str) -> str:
    d = {'Deaths':'red', 'Recovered':'green', 'Confirmed':'orange'}
    return d.get(category) or 'black'

if __name__ == '__main__':
    import docopt
    usage="""
    {}
    --------------------------
    Usage:
    {} path <category> <country>
    {} -h | --help
    {} -v | --verbose
    {} -V | --version 

    Options:
    -h --help               Show this screen.
    -v --verbose            Verbose mode.
    -V --version            Show version.
 
    Examples:
    """.format(*tuple([PROGRAM] * 5))

    arguments = docopt.docopt(usage)
    verbose = False
    slack = False
    if arguments.get('--verbose') or arguments.get('-v'):
        verbose = True
    if arguments.get('--version') or arguments.get('-V'):
        print("%s version %s" % (PROGRAM,VERSION))
    elif arguments.get('--help') or arguments.get('-h'):
        print(usage)
    elif arguments.get('path'):
        category = arguments.get('<category>').capitalize() or 'Confirmed'
        country = arguments.get('<country>').lower() or 'united-kingdom'
        color = getColor(category)
        chart = plotByCountryFromAPI(getCategoryByCountryFromAPI(category, country, color='red'), f'Log{category}', 'LogNew')
        target = 'newvsexisting.png'
        chart.save(target)
        print(f'successfully generated {target}')