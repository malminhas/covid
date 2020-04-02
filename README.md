# covid <a name="top-of-covid-notebook"></a>
> Visualise the John Hopkins Covid-19 dataset.


## Contents
1. [Introduction](#covid-intro)
2. [Installation](#covid-install)
3. [Graphing current counts](#covid-current)
4. [Graphing time series counts](#covid-timeseries)
5. [Graphing current and time series counts using Covid API](#covid-api)

## 1. Introduction <a name="covid-intro"></a>
#### [back](#top-of-covid-notebook)

The `covid` module provides convenience utilities for graphing the covid-19 dataset published by John Hopkins University (JHU) [here](https://github.com/CSSEGISandData/COVID-19).  The JHU dataset is updated daily with the latest in separate time series csv files covering [here](https://github.com/CSSEGISandData/COVID-19/tree/master/csse_covid_19_data/csse_covid_19_time_series):
* `time_series_covid19_confirmed_global.csv`
* `time_series_covid19_deaths_global.csv`
* `time_series_covid19_recovered_global.csv`

Daily reports are kept in [this directory](https://github.com/CSSEGISandData/COVID-19/blob/master/csse_covid_19_data/csse_covid_19_daily_reports) and conform to the format `dd-mm-2020.csv`.

## 2. Installation <a name="covid-install"></a>
#### [back](#top-of-covid-notebook)

This code is not yet in PyPI.  You can clone the repo and the corresponding functions described below will all be available in the accompanying `covid` module.  The `covid` module has the following dependencies which will need to be pip installed: `requests`,`pandas`,`matplotlib`,`seaborn`

## 3. Graphing current counts <a name="covid-current"></a>
#### [back](#top-of-covid-notebook)

You can use `getCountriesDailyReport` to obtain a `pandas` dataframe `df` holding the latest values for each of `["Confirmed","Deaths","Recovered"]` by both `Province_State` and `Country_Region` as follows:

```python
which = getDayBeforeYesterday()
df = getCountriesDailyReport(which)
```

You can view the structure of `df` as follows:

```python
n = 1
nrows,ncols = df.shape
print(f'df has {nrows} rows and {ncols} columns with column names {df.columns.to_list()}')
print(f'First {n} rows are:')
print(df.iloc[:n,:])
```

    df has 2434 rows and 12 columns with column names ['FIPS', 'Admin2', 'Province_State', 'Country_Region', 'Last_Update', 'Lat', 'Long_', 'Confirmed', 'Deaths', 'Recovered', 'Active', 'Combined_Key']
    First 1 rows are:
          FIPS     Admin2  Province_State Country_Region         Last_Update  \
    0  45001.0  Abbeville  South Carolina             US 2020-03-31 23:43:56   
    
             Lat      Long_  Confirmed  Deaths  Recovered  Active  \
    0  34.223334 -82.461707          4       0          0       0   
    
                        Combined_Key  
    0  Abbeville, South Carolina, US  


You can plot this data aggregated by country and `kind` as follows.  Note here that `setDefaults` configures graphs to be drawn using the [seaborn](https://seaborn.pydata.org/introduction.html) visualisation library by default or the `altair` visualisation library as in this example:

```python
setDefaults()
plotCountriesDailyReport(getCountriesDailyReport(which), which, topN=15, color='red', kind='Deaths',visualisation='altair')
```



<div id="altair-viz-c8490d6840954fb6a40de27ea0d353a7"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    const outputDiv = document.getElementById("altair-viz-c8490d6840954fb6a40de27ea0d353a7");
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.0.2?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-9887c0cd3cb89fe5740d702d4ac765bc"}, "mark": {"type": "bar", "size": 30}, "encoding": {"color": {"value": "red"}, "opacity": {"value": 0.9}, "x": {"type": "nominal", "field": "Country", "sort": "-y"}, "y": {"type": "quantitative", "field": "Deaths"}}, "height": 450, "title": "Total Deaths by top 15 countries as of 03-31-2020", "width": 1000, "$schema": "https://vega.github.io/schema/vega-lite/v4.0.2.json", "datasets": {"data-9887c0cd3cb89fe5740d702d4ac765bc": [{"Country": "Italy", "Deaths": 12428}, {"Country": "Spain", "Deaths": 8464}, {"Country": "US", "Deaths": 3873}, {"Country": "France", "Deaths": 3532}, {"Country": "China", "Deaths": 3309}, {"Country": "Iran", "Deaths": 2898}, {"Country": "United Kingdom", "Deaths": 1793}, {"Country": "Netherlands", "Deaths": 1040}, {"Country": "Germany", "Deaths": 775}, {"Country": "Belgium", "Deaths": 705}, {"Country": "Switzerland", "Deaths": 433}, {"Country": "Turkey", "Deaths": 214}, {"Country": "Brazil", "Deaths": 201}, {"Country": "Sweden", "Deaths": 180}, {"Country": "Korea, South", "Deaths": 162}]}}, {"mode": "vega-lite"});
</script>


We can also dig into the breakdown per country if available as follows:

```python
plotCountryDailyReport(getCountriesDailyReport(which), 'US', which, topN=15, color='red', kind='Deaths', visualisation='altair')
```



<div id="altair-viz-5d55974935804f7691fa23bed6d667e7"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    const outputDiv = document.getElementById("altair-viz-5d55974935804f7691fa23bed6d667e7");
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.0.2?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-146f26af9975ac89382d9ca1191b6a99"}, "mark": {"type": "bar", "size": 30}, "encoding": {"color": {"value": "red"}, "opacity": {"value": 0.9}, "x": {"type": "nominal", "field": "Province_State", "sort": "-y"}, "y": {"type": "quantitative", "field": "Deaths"}}, "height": 450, "title": "Total Deaths for top 15 regions of US as of 03-31-2020", "width": 1000, "$schema": "https://vega.github.io/schema/vega-lite/v4.0.2.json", "datasets": {"data-146f26af9975ac89382d9ca1191b6a99": [{"Province_State": "New York", "Deaths": 1550}, {"Province_State": "New Jersey", "Deaths": 267}, {"Province_State": "Michigan", "Deaths": 259}, {"Province_State": "Louisiana", "Deaths": 239}, {"Province_State": "Washington", "Deaths": 225}, {"Province_State": "California", "Deaths": 173}, {"Province_State": "Georgia", "Deaths": 111}, {"Province_State": "Illinois", "Deaths": 99}, {"Province_State": "Massachusetts", "Deaths": 89}, {"Province_State": "Florida", "Deaths": 85}, {"Province_State": "Connecticut", "Deaths": 69}, {"Province_State": "Colorado", "Deaths": 69}, {"Province_State": "Pennsylvania", "Deaths": 63}, {"Province_State": "Ohio", "Deaths": 55}, {"Province_State": "Texas", "Deaths": 54}]}}, {"mode": "vega-lite"});
</script>


## 4. Graphing time series counts <a name="covid-timeseries"></a>
#### [back](#top-of-covid-notebook)

We can look at how infection and death counts have varied for a county over time if we aggregate by doing a `groupby` on `country`.  We should see an equal number of values per country following this aggregation:  

```python
df = procTimeSeriesConfirmed()
print(f'Found {df.shape} (rows, cols) of cols={df.columns.values}')
ddf = df.groupby('country')['Confirmed'].count().sort_values(ascending=True)
print(f'max={ddf.max()}, min={ddf.min()}, count={len(ddf)}')
```

    Found (12600, 3) (rows, cols) of cols=['day' 'country' 'Confirmed']
    max=70, min=70, count=180


Now we can plot a time series of confirmed cases of Covid-19 in China, Italy, US and UK as follows:

```python
plotCountriesTimeSeries(df, ['China', 'Italy', 'US', 'United Kingdom'], which, 'Confirmed', visualisation='altair')
```



<div id="altair-viz-7d2f39fc5e1b497490edff0fbf1e9b6a"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    const outputDiv = document.getElementById("altair-viz-7d2f39fc5e1b497490edff0fbf1e9b6a");
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.0.2?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-f1c15d8ac512d42c54be48cdb0f16fae"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "country"}, "x": {"type": "temporal", "field": "day"}, "y": {"type": "quantitative", "field": "Confirmed"}}, "height": 450, "title": "Confirmed in ['China', 'Italy', 'US', 'United Kingdom'] as of 03-31-2020", "width": 1000, "$schema": "https://vega.github.io/schema/vega-lite/v4.0.2.json", "datasets": {"data-f1c15d8ac512d42c54be48cdb0f16fae": [{"day": "2020-01-22T00:00:00", "country": "China", "Confirmed": 548}, {"day": "2020-01-23T00:00:00", "country": "China", "Confirmed": 643}, {"day": "2020-01-24T00:00:00", "country": "China", "Confirmed": 920}, {"day": "2020-01-25T00:00:00", "country": "China", "Confirmed": 1406}, {"day": "2020-01-26T00:00:00", "country": "China", "Confirmed": 2075}, {"day": "2020-01-27T00:00:00", "country": "China", "Confirmed": 2877}, {"day": "2020-01-28T00:00:00", "country": "China", "Confirmed": 5509}, {"day": "2020-01-29T00:00:00", "country": "China", "Confirmed": 6087}, {"day": "2020-01-30T00:00:00", "country": "China", "Confirmed": 8141}, {"day": "2020-01-31T00:00:00", "country": "China", "Confirmed": 9802}, {"day": "2020-02-01T00:00:00", "country": "China", "Confirmed": 11891}, {"day": "2020-02-02T00:00:00", "country": "China", "Confirmed": 16630}, {"day": "2020-02-03T00:00:00", "country": "China", "Confirmed": 19716}, {"day": "2020-02-04T00:00:00", "country": "China", "Confirmed": 23707}, {"day": "2020-02-05T00:00:00", "country": "China", "Confirmed": 27440}, {"day": "2020-02-06T00:00:00", "country": "China", "Confirmed": 30587}, {"day": "2020-02-07T00:00:00", "country": "China", "Confirmed": 34110}, {"day": "2020-02-08T00:00:00", "country": "China", "Confirmed": 36814}, {"day": "2020-02-09T00:00:00", "country": "China", "Confirmed": 39829}, {"day": "2020-02-10T00:00:00", "country": "China", "Confirmed": 42354}, {"day": "2020-02-11T00:00:00", "country": "China", "Confirmed": 44386}, {"day": "2020-02-12T00:00:00", "country": "China", "Confirmed": 44759}, {"day": "2020-02-13T00:00:00", "country": "China", "Confirmed": 59895}, {"day": "2020-02-14T00:00:00", "country": "China", "Confirmed": 66358}, {"day": "2020-02-15T00:00:00", "country": "China", "Confirmed": 68413}, {"day": "2020-02-16T00:00:00", "country": "China", "Confirmed": 70513}, {"day": "2020-02-17T00:00:00", "country": "China", "Confirmed": 72434}, {"day": "2020-02-18T00:00:00", "country": "China", "Confirmed": 74211}, {"day": "2020-02-19T00:00:00", "country": "China", "Confirmed": 74619}, {"day": "2020-02-20T00:00:00", "country": "China", "Confirmed": 75077}, {"day": "2020-02-21T00:00:00", "country": "China", "Confirmed": 75550}, {"day": "2020-02-22T00:00:00", "country": "China", "Confirmed": 77001}, {"day": "2020-02-23T00:00:00", "country": "China", "Confirmed": 77022}, {"day": "2020-02-24T00:00:00", "country": "China", "Confirmed": 77241}, {"day": "2020-02-25T00:00:00", "country": "China", "Confirmed": 77754}, {"day": "2020-02-26T00:00:00", "country": "China", "Confirmed": 78166}, {"day": "2020-02-27T00:00:00", "country": "China", "Confirmed": 78600}, {"day": "2020-02-28T00:00:00", "country": "China", "Confirmed": 78928}, {"day": "2020-02-29T00:00:00", "country": "China", "Confirmed": 79356}, {"day": "2020-03-01T00:00:00", "country": "China", "Confirmed": 79932}, {"day": "2020-03-02T00:00:00", "country": "China", "Confirmed": 80136}, {"day": "2020-03-03T00:00:00", "country": "China", "Confirmed": 80261}, {"day": "2020-03-04T00:00:00", "country": "China", "Confirmed": 80386}, {"day": "2020-03-05T00:00:00", "country": "China", "Confirmed": 80537}, {"day": "2020-03-06T00:00:00", "country": "China", "Confirmed": 80690}, {"day": "2020-03-07T00:00:00", "country": "China", "Confirmed": 80770}, {"day": "2020-03-08T00:00:00", "country": "China", "Confirmed": 80823}, {"day": "2020-03-09T00:00:00", "country": "China", "Confirmed": 80860}, {"day": "2020-03-10T00:00:00", "country": "China", "Confirmed": 80887}, {"day": "2020-03-11T00:00:00", "country": "China", "Confirmed": 80921}, {"day": "2020-03-12T00:00:00", "country": "China", "Confirmed": 80932}, {"day": "2020-03-13T00:00:00", "country": "China", "Confirmed": 80945}, {"day": "2020-03-14T00:00:00", "country": "China", "Confirmed": 80977}, {"day": "2020-03-15T00:00:00", "country": "China", "Confirmed": 81003}, {"day": "2020-03-16T00:00:00", "country": "China", "Confirmed": 81033}, {"day": "2020-03-17T00:00:00", "country": "China", "Confirmed": 81058}, {"day": "2020-03-18T00:00:00", "country": "China", "Confirmed": 81102}, {"day": "2020-03-19T00:00:00", "country": "China", "Confirmed": 81156}, {"day": "2020-03-20T00:00:00", "country": "China", "Confirmed": 81250}, {"day": "2020-03-21T00:00:00", "country": "China", "Confirmed": 81305}, {"day": "2020-03-22T00:00:00", "country": "China", "Confirmed": 81435}, {"day": "2020-03-23T00:00:00", "country": "China", "Confirmed": 81498}, {"day": "2020-03-24T00:00:00", "country": "China", "Confirmed": 81591}, {"day": "2020-03-25T00:00:00", "country": "China", "Confirmed": 81661}, {"day": "2020-03-26T00:00:00", "country": "China", "Confirmed": 81782}, {"day": "2020-03-27T00:00:00", "country": "China", "Confirmed": 81897}, {"day": "2020-03-28T00:00:00", "country": "China", "Confirmed": 81999}, {"day": "2020-03-29T00:00:00", "country": "China", "Confirmed": 82122}, {"day": "2020-03-30T00:00:00", "country": "China", "Confirmed": 82198}, {"day": "2020-03-31T00:00:00", "country": "China", "Confirmed": 82279}, {"day": "2020-01-22T00:00:00", "country": "Italy", "Confirmed": 0}, {"day": "2020-01-23T00:00:00", "country": "Italy", "Confirmed": 0}, {"day": "2020-01-24T00:00:00", "country": "Italy", "Confirmed": 0}, {"day": "2020-01-25T00:00:00", "country": "Italy", "Confirmed": 0}, {"day": "2020-01-26T00:00:00", "country": "Italy", "Confirmed": 0}, {"day": "2020-01-27T00:00:00", "country": "Italy", "Confirmed": 0}, {"day": "2020-01-28T00:00:00", "country": "Italy", "Confirmed": 0}, {"day": "2020-01-29T00:00:00", "country": "Italy", "Confirmed": 0}, {"day": "2020-01-30T00:00:00", "country": "Italy", "Confirmed": 0}, {"day": "2020-01-31T00:00:00", "country": "Italy", "Confirmed": 2}, {"day": "2020-02-01T00:00:00", "country": "Italy", "Confirmed": 2}, {"day": "2020-02-02T00:00:00", "country": "Italy", "Confirmed": 2}, {"day": "2020-02-03T00:00:00", "country": "Italy", "Confirmed": 2}, {"day": "2020-02-04T00:00:00", "country": "Italy", "Confirmed": 2}, {"day": "2020-02-05T00:00:00", "country": "Italy", "Confirmed": 2}, {"day": "2020-02-06T00:00:00", "country": "Italy", "Confirmed": 2}, {"day": "2020-02-07T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-08T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-09T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-10T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-11T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-12T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-13T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-14T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-15T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-16T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-17T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-18T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-19T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-20T00:00:00", "country": "Italy", "Confirmed": 3}, {"day": "2020-02-21T00:00:00", "country": "Italy", "Confirmed": 20}, {"day": "2020-02-22T00:00:00", "country": "Italy", "Confirmed": 62}, {"day": "2020-02-23T00:00:00", "country": "Italy", "Confirmed": 155}, {"day": "2020-02-24T00:00:00", "country": "Italy", "Confirmed": 229}, {"day": "2020-02-25T00:00:00", "country": "Italy", "Confirmed": 322}, {"day": "2020-02-26T00:00:00", "country": "Italy", "Confirmed": 453}, {"day": "2020-02-27T00:00:00", "country": "Italy", "Confirmed": 655}, {"day": "2020-02-28T00:00:00", "country": "Italy", "Confirmed": 888}, {"day": "2020-02-29T00:00:00", "country": "Italy", "Confirmed": 1128}, {"day": "2020-03-01T00:00:00", "country": "Italy", "Confirmed": 1694}, {"day": "2020-03-02T00:00:00", "country": "Italy", "Confirmed": 2036}, {"day": "2020-03-03T00:00:00", "country": "Italy", "Confirmed": 2502}, {"day": "2020-03-04T00:00:00", "country": "Italy", "Confirmed": 3089}, {"day": "2020-03-05T00:00:00", "country": "Italy", "Confirmed": 3858}, {"day": "2020-03-06T00:00:00", "country": "Italy", "Confirmed": 4636}, {"day": "2020-03-07T00:00:00", "country": "Italy", "Confirmed": 5883}, {"day": "2020-03-08T00:00:00", "country": "Italy", "Confirmed": 7375}, {"day": "2020-03-09T00:00:00", "country": "Italy", "Confirmed": 9172}, {"day": "2020-03-10T00:00:00", "country": "Italy", "Confirmed": 10149}, {"day": "2020-03-11T00:00:00", "country": "Italy", "Confirmed": 12462}, {"day": "2020-03-12T00:00:00", "country": "Italy", "Confirmed": 12462}, {"day": "2020-03-13T00:00:00", "country": "Italy", "Confirmed": 17660}, {"day": "2020-03-14T00:00:00", "country": "Italy", "Confirmed": 21157}, {"day": "2020-03-15T00:00:00", "country": "Italy", "Confirmed": 24747}, {"day": "2020-03-16T00:00:00", "country": "Italy", "Confirmed": 27980}, {"day": "2020-03-17T00:00:00", "country": "Italy", "Confirmed": 31506}, {"day": "2020-03-18T00:00:00", "country": "Italy", "Confirmed": 35713}, {"day": "2020-03-19T00:00:00", "country": "Italy", "Confirmed": 41035}, {"day": "2020-03-20T00:00:00", "country": "Italy", "Confirmed": 47021}, {"day": "2020-03-21T00:00:00", "country": "Italy", "Confirmed": 53578}, {"day": "2020-03-22T00:00:00", "country": "Italy", "Confirmed": 59138}, {"day": "2020-03-23T00:00:00", "country": "Italy", "Confirmed": 63927}, {"day": "2020-03-24T00:00:00", "country": "Italy", "Confirmed": 69176}, {"day": "2020-03-25T00:00:00", "country": "Italy", "Confirmed": 74386}, {"day": "2020-03-26T00:00:00", "country": "Italy", "Confirmed": 80589}, {"day": "2020-03-27T00:00:00", "country": "Italy", "Confirmed": 86498}, {"day": "2020-03-28T00:00:00", "country": "Italy", "Confirmed": 92472}, {"day": "2020-03-29T00:00:00", "country": "Italy", "Confirmed": 97689}, {"day": "2020-03-30T00:00:00", "country": "Italy", "Confirmed": 101739}, {"day": "2020-03-31T00:00:00", "country": "Italy", "Confirmed": 105792}, {"day": "2020-01-22T00:00:00", "country": "US", "Confirmed": 1}, {"day": "2020-01-23T00:00:00", "country": "US", "Confirmed": 1}, {"day": "2020-01-24T00:00:00", "country": "US", "Confirmed": 2}, {"day": "2020-01-25T00:00:00", "country": "US", "Confirmed": 2}, {"day": "2020-01-26T00:00:00", "country": "US", "Confirmed": 5}, {"day": "2020-01-27T00:00:00", "country": "US", "Confirmed": 5}, {"day": "2020-01-28T00:00:00", "country": "US", "Confirmed": 5}, {"day": "2020-01-29T00:00:00", "country": "US", "Confirmed": 5}, {"day": "2020-01-30T00:00:00", "country": "US", "Confirmed": 5}, {"day": "2020-01-31T00:00:00", "country": "US", "Confirmed": 7}, {"day": "2020-02-01T00:00:00", "country": "US", "Confirmed": 8}, {"day": "2020-02-02T00:00:00", "country": "US", "Confirmed": 8}, {"day": "2020-02-03T00:00:00", "country": "US", "Confirmed": 11}, {"day": "2020-02-04T00:00:00", "country": "US", "Confirmed": 11}, {"day": "2020-02-05T00:00:00", "country": "US", "Confirmed": 11}, {"day": "2020-02-06T00:00:00", "country": "US", "Confirmed": 11}, {"day": "2020-02-07T00:00:00", "country": "US", "Confirmed": 11}, {"day": "2020-02-08T00:00:00", "country": "US", "Confirmed": 11}, {"day": "2020-02-09T00:00:00", "country": "US", "Confirmed": 11}, {"day": "2020-02-10T00:00:00", "country": "US", "Confirmed": 11}, {"day": "2020-02-11T00:00:00", "country": "US", "Confirmed": 12}, {"day": "2020-02-12T00:00:00", "country": "US", "Confirmed": 12}, {"day": "2020-02-13T00:00:00", "country": "US", "Confirmed": 13}, {"day": "2020-02-14T00:00:00", "country": "US", "Confirmed": 13}, {"day": "2020-02-15T00:00:00", "country": "US", "Confirmed": 13}, {"day": "2020-02-16T00:00:00", "country": "US", "Confirmed": 13}, {"day": "2020-02-17T00:00:00", "country": "US", "Confirmed": 13}, {"day": "2020-02-18T00:00:00", "country": "US", "Confirmed": 13}, {"day": "2020-02-19T00:00:00", "country": "US", "Confirmed": 13}, {"day": "2020-02-20T00:00:00", "country": "US", "Confirmed": 13}, {"day": "2020-02-21T00:00:00", "country": "US", "Confirmed": 15}, {"day": "2020-02-22T00:00:00", "country": "US", "Confirmed": 15}, {"day": "2020-02-23T00:00:00", "country": "US", "Confirmed": 15}, {"day": "2020-02-24T00:00:00", "country": "US", "Confirmed": 51}, {"day": "2020-02-25T00:00:00", "country": "US", "Confirmed": 51}, {"day": "2020-02-26T00:00:00", "country": "US", "Confirmed": 57}, {"day": "2020-02-27T00:00:00", "country": "US", "Confirmed": 58}, {"day": "2020-02-28T00:00:00", "country": "US", "Confirmed": 60}, {"day": "2020-02-29T00:00:00", "country": "US", "Confirmed": 68}, {"day": "2020-03-01T00:00:00", "country": "US", "Confirmed": 74}, {"day": "2020-03-02T00:00:00", "country": "US", "Confirmed": 98}, {"day": "2020-03-03T00:00:00", "country": "US", "Confirmed": 118}, {"day": "2020-03-04T00:00:00", "country": "US", "Confirmed": 149}, {"day": "2020-03-05T00:00:00", "country": "US", "Confirmed": 217}, {"day": "2020-03-06T00:00:00", "country": "US", "Confirmed": 262}, {"day": "2020-03-07T00:00:00", "country": "US", "Confirmed": 402}, {"day": "2020-03-08T00:00:00", "country": "US", "Confirmed": 518}, {"day": "2020-03-09T00:00:00", "country": "US", "Confirmed": 583}, {"day": "2020-03-10T00:00:00", "country": "US", "Confirmed": 959}, {"day": "2020-03-11T00:00:00", "country": "US", "Confirmed": 1281}, {"day": "2020-03-12T00:00:00", "country": "US", "Confirmed": 1663}, {"day": "2020-03-13T00:00:00", "country": "US", "Confirmed": 2179}, {"day": "2020-03-14T00:00:00", "country": "US", "Confirmed": 2727}, {"day": "2020-03-15T00:00:00", "country": "US", "Confirmed": 3499}, {"day": "2020-03-16T00:00:00", "country": "US", "Confirmed": 4632}, {"day": "2020-03-17T00:00:00", "country": "US", "Confirmed": 6421}, {"day": "2020-03-18T00:00:00", "country": "US", "Confirmed": 7783}, {"day": "2020-03-19T00:00:00", "country": "US", "Confirmed": 13677}, {"day": "2020-03-20T00:00:00", "country": "US", "Confirmed": 19100}, {"day": "2020-03-21T00:00:00", "country": "US", "Confirmed": 25489}, {"day": "2020-03-22T00:00:00", "country": "US", "Confirmed": 33276}, {"day": "2020-03-23T00:00:00", "country": "US", "Confirmed": 43847}, {"day": "2020-03-24T00:00:00", "country": "US", "Confirmed": 53740}, {"day": "2020-03-25T00:00:00", "country": "US", "Confirmed": 65778}, {"day": "2020-03-26T00:00:00", "country": "US", "Confirmed": 83836}, {"day": "2020-03-27T00:00:00", "country": "US", "Confirmed": 101657}, {"day": "2020-03-28T00:00:00", "country": "US", "Confirmed": 121478}, {"day": "2020-03-29T00:00:00", "country": "US", "Confirmed": 140886}, {"day": "2020-03-30T00:00:00", "country": "US", "Confirmed": 161807}, {"day": "2020-03-31T00:00:00", "country": "US", "Confirmed": 188172}, {"day": "2020-01-22T00:00:00", "country": "United Kingdom", "Confirmed": 0}, {"day": "2020-01-23T00:00:00", "country": "United Kingdom", "Confirmed": 0}, {"day": "2020-01-24T00:00:00", "country": "United Kingdom", "Confirmed": 0}, {"day": "2020-01-25T00:00:00", "country": "United Kingdom", "Confirmed": 0}, {"day": "2020-01-26T00:00:00", "country": "United Kingdom", "Confirmed": 0}, {"day": "2020-01-27T00:00:00", "country": "United Kingdom", "Confirmed": 0}, {"day": "2020-01-28T00:00:00", "country": "United Kingdom", "Confirmed": 0}, {"day": "2020-01-29T00:00:00", "country": "United Kingdom", "Confirmed": 0}, {"day": "2020-01-30T00:00:00", "country": "United Kingdom", "Confirmed": 0}, {"day": "2020-01-31T00:00:00", "country": "United Kingdom", "Confirmed": 2}, {"day": "2020-02-01T00:00:00", "country": "United Kingdom", "Confirmed": 2}, {"day": "2020-02-02T00:00:00", "country": "United Kingdom", "Confirmed": 2}, {"day": "2020-02-03T00:00:00", "country": "United Kingdom", "Confirmed": 2}, {"day": "2020-02-04T00:00:00", "country": "United Kingdom", "Confirmed": 2}, {"day": "2020-02-05T00:00:00", "country": "United Kingdom", "Confirmed": 2}, {"day": "2020-02-06T00:00:00", "country": "United Kingdom", "Confirmed": 2}, {"day": "2020-02-07T00:00:00", "country": "United Kingdom", "Confirmed": 3}, {"day": "2020-02-08T00:00:00", "country": "United Kingdom", "Confirmed": 3}, {"day": "2020-02-09T00:00:00", "country": "United Kingdom", "Confirmed": 3}, {"day": "2020-02-10T00:00:00", "country": "United Kingdom", "Confirmed": 8}, {"day": "2020-02-11T00:00:00", "country": "United Kingdom", "Confirmed": 8}, {"day": "2020-02-12T00:00:00", "country": "United Kingdom", "Confirmed": 9}, {"day": "2020-02-13T00:00:00", "country": "United Kingdom", "Confirmed": 9}, {"day": "2020-02-14T00:00:00", "country": "United Kingdom", "Confirmed": 9}, {"day": "2020-02-15T00:00:00", "country": "United Kingdom", "Confirmed": 9}, {"day": "2020-02-16T00:00:00", "country": "United Kingdom", "Confirmed": 9}, {"day": "2020-02-17T00:00:00", "country": "United Kingdom", "Confirmed": 9}, {"day": "2020-02-18T00:00:00", "country": "United Kingdom", "Confirmed": 9}, {"day": "2020-02-19T00:00:00", "country": "United Kingdom", "Confirmed": 9}, {"day": "2020-02-20T00:00:00", "country": "United Kingdom", "Confirmed": 9}, {"day": "2020-02-21T00:00:00", "country": "United Kingdom", "Confirmed": 9}, {"day": "2020-02-22T00:00:00", "country": "United Kingdom", "Confirmed": 9}, {"day": "2020-02-23T00:00:00", "country": "United Kingdom", "Confirmed": 9}, {"day": "2020-02-24T00:00:00", "country": "United Kingdom", "Confirmed": 13}, {"day": "2020-02-25T00:00:00", "country": "United Kingdom", "Confirmed": 13}, {"day": "2020-02-26T00:00:00", "country": "United Kingdom", "Confirmed": 13}, {"day": "2020-02-27T00:00:00", "country": "United Kingdom", "Confirmed": 15}, {"day": "2020-02-28T00:00:00", "country": "United Kingdom", "Confirmed": 20}, {"day": "2020-02-29T00:00:00", "country": "United Kingdom", "Confirmed": 23}, {"day": "2020-03-01T00:00:00", "country": "United Kingdom", "Confirmed": 36}, {"day": "2020-03-02T00:00:00", "country": "United Kingdom", "Confirmed": 40}, {"day": "2020-03-03T00:00:00", "country": "United Kingdom", "Confirmed": 51}, {"day": "2020-03-04T00:00:00", "country": "United Kingdom", "Confirmed": 86}, {"day": "2020-03-05T00:00:00", "country": "United Kingdom", "Confirmed": 116}, {"day": "2020-03-06T00:00:00", "country": "United Kingdom", "Confirmed": 164}, {"day": "2020-03-07T00:00:00", "country": "United Kingdom", "Confirmed": 207}, {"day": "2020-03-08T00:00:00", "country": "United Kingdom", "Confirmed": 274}, {"day": "2020-03-09T00:00:00", "country": "United Kingdom", "Confirmed": 322}, {"day": "2020-03-10T00:00:00", "country": "United Kingdom", "Confirmed": 384}, {"day": "2020-03-11T00:00:00", "country": "United Kingdom", "Confirmed": 459}, {"day": "2020-03-12T00:00:00", "country": "United Kingdom", "Confirmed": 459}, {"day": "2020-03-13T00:00:00", "country": "United Kingdom", "Confirmed": 802}, {"day": "2020-03-14T00:00:00", "country": "United Kingdom", "Confirmed": 1144}, {"day": "2020-03-15T00:00:00", "country": "United Kingdom", "Confirmed": 1145}, {"day": "2020-03-16T00:00:00", "country": "United Kingdom", "Confirmed": 1551}, {"day": "2020-03-17T00:00:00", "country": "United Kingdom", "Confirmed": 1960}, {"day": "2020-03-18T00:00:00", "country": "United Kingdom", "Confirmed": 2642}, {"day": "2020-03-19T00:00:00", "country": "United Kingdom", "Confirmed": 2716}, {"day": "2020-03-20T00:00:00", "country": "United Kingdom", "Confirmed": 4014}, {"day": "2020-03-21T00:00:00", "country": "United Kingdom", "Confirmed": 5067}, {"day": "2020-03-22T00:00:00", "country": "United Kingdom", "Confirmed": 5745}, {"day": "2020-03-23T00:00:00", "country": "United Kingdom", "Confirmed": 6726}, {"day": "2020-03-24T00:00:00", "country": "United Kingdom", "Confirmed": 8164}, {"day": "2020-03-25T00:00:00", "country": "United Kingdom", "Confirmed": 9640}, {"day": "2020-03-26T00:00:00", "country": "United Kingdom", "Confirmed": 11812}, {"day": "2020-03-27T00:00:00", "country": "United Kingdom", "Confirmed": 14745}, {"day": "2020-03-28T00:00:00", "country": "United Kingdom", "Confirmed": 17312}, {"day": "2020-03-29T00:00:00", "country": "United Kingdom", "Confirmed": 19780}, {"day": "2020-03-30T00:00:00", "country": "United Kingdom", "Confirmed": 22453}, {"day": "2020-03-31T00:00:00", "country": "United Kingdom", "Confirmed": 25481}]}}, {"mode": "vega-lite"});
</script>


And we can plot a time series of recorded deaths in these same countries as follows:

```python
df = procTimeSeriesDeaths()
plotCountriesTimeSeries(df, ['China', 'Italy', 'US', 'United Kingdom'], which, 'Deaths', visualisation='altair')
```



<div id="altair-viz-632f8e60f7bb4818ad09898256b7ab67"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    const outputDiv = document.getElementById("altair-viz-632f8e60f7bb4818ad09898256b7ab67");
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.0.2?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-82d521662def88ad7f28c056fa68523a"}, "mark": "line", "encoding": {"color": {"type": "nominal", "field": "country"}, "x": {"type": "temporal", "field": "day"}, "y": {"type": "quantitative", "field": "Deaths"}}, "height": 450, "title": "Deaths in ['China', 'Italy', 'US', 'United Kingdom'] as of 03-31-2020", "width": 1000, "$schema": "https://vega.github.io/schema/vega-lite/v4.0.2.json", "datasets": {"data-82d521662def88ad7f28c056fa68523a": [{"day": "2020-01-22T00:00:00", "country": "China", "Deaths": 17}, {"day": "2020-01-23T00:00:00", "country": "China", "Deaths": 18}, {"day": "2020-01-24T00:00:00", "country": "China", "Deaths": 26}, {"day": "2020-01-25T00:00:00", "country": "China", "Deaths": 42}, {"day": "2020-01-26T00:00:00", "country": "China", "Deaths": 56}, {"day": "2020-01-27T00:00:00", "country": "China", "Deaths": 82}, {"day": "2020-01-28T00:00:00", "country": "China", "Deaths": 131}, {"day": "2020-01-29T00:00:00", "country": "China", "Deaths": 133}, {"day": "2020-01-30T00:00:00", "country": "China", "Deaths": 171}, {"day": "2020-01-31T00:00:00", "country": "China", "Deaths": 213}, {"day": "2020-02-01T00:00:00", "country": "China", "Deaths": 259}, {"day": "2020-02-02T00:00:00", "country": "China", "Deaths": 361}, {"day": "2020-02-03T00:00:00", "country": "China", "Deaths": 425}, {"day": "2020-02-04T00:00:00", "country": "China", "Deaths": 491}, {"day": "2020-02-05T00:00:00", "country": "China", "Deaths": 563}, {"day": "2020-02-06T00:00:00", "country": "China", "Deaths": 633}, {"day": "2020-02-07T00:00:00", "country": "China", "Deaths": 718}, {"day": "2020-02-08T00:00:00", "country": "China", "Deaths": 805}, {"day": "2020-02-09T00:00:00", "country": "China", "Deaths": 905}, {"day": "2020-02-10T00:00:00", "country": "China", "Deaths": 1012}, {"day": "2020-02-11T00:00:00", "country": "China", "Deaths": 1112}, {"day": "2020-02-12T00:00:00", "country": "China", "Deaths": 1117}, {"day": "2020-02-13T00:00:00", "country": "China", "Deaths": 1369}, {"day": "2020-02-14T00:00:00", "country": "China", "Deaths": 1521}, {"day": "2020-02-15T00:00:00", "country": "China", "Deaths": 1663}, {"day": "2020-02-16T00:00:00", "country": "China", "Deaths": 1766}, {"day": "2020-02-17T00:00:00", "country": "China", "Deaths": 1864}, {"day": "2020-02-18T00:00:00", "country": "China", "Deaths": 2003}, {"day": "2020-02-19T00:00:00", "country": "China", "Deaths": 2116}, {"day": "2020-02-20T00:00:00", "country": "China", "Deaths": 2238}, {"day": "2020-02-21T00:00:00", "country": "China", "Deaths": 2238}, {"day": "2020-02-22T00:00:00", "country": "China", "Deaths": 2443}, {"day": "2020-02-23T00:00:00", "country": "China", "Deaths": 2445}, {"day": "2020-02-24T00:00:00", "country": "China", "Deaths": 2595}, {"day": "2020-02-25T00:00:00", "country": "China", "Deaths": 2665}, {"day": "2020-02-26T00:00:00", "country": "China", "Deaths": 2717}, {"day": "2020-02-27T00:00:00", "country": "China", "Deaths": 2746}, {"day": "2020-02-28T00:00:00", "country": "China", "Deaths": 2790}, {"day": "2020-02-29T00:00:00", "country": "China", "Deaths": 2837}, {"day": "2020-03-01T00:00:00", "country": "China", "Deaths": 2872}, {"day": "2020-03-02T00:00:00", "country": "China", "Deaths": 2914}, {"day": "2020-03-03T00:00:00", "country": "China", "Deaths": 2947}, {"day": "2020-03-04T00:00:00", "country": "China", "Deaths": 2983}, {"day": "2020-03-05T00:00:00", "country": "China", "Deaths": 3015}, {"day": "2020-03-06T00:00:00", "country": "China", "Deaths": 3044}, {"day": "2020-03-07T00:00:00", "country": "China", "Deaths": 3072}, {"day": "2020-03-08T00:00:00", "country": "China", "Deaths": 3100}, {"day": "2020-03-09T00:00:00", "country": "China", "Deaths": 3123}, {"day": "2020-03-10T00:00:00", "country": "China", "Deaths": 3139}, {"day": "2020-03-11T00:00:00", "country": "China", "Deaths": 3161}, {"day": "2020-03-12T00:00:00", "country": "China", "Deaths": 3172}, {"day": "2020-03-13T00:00:00", "country": "China", "Deaths": 3180}, {"day": "2020-03-14T00:00:00", "country": "China", "Deaths": 3193}, {"day": "2020-03-15T00:00:00", "country": "China", "Deaths": 3203}, {"day": "2020-03-16T00:00:00", "country": "China", "Deaths": 3217}, {"day": "2020-03-17T00:00:00", "country": "China", "Deaths": 3230}, {"day": "2020-03-18T00:00:00", "country": "China", "Deaths": 3241}, {"day": "2020-03-19T00:00:00", "country": "China", "Deaths": 3249}, {"day": "2020-03-20T00:00:00", "country": "China", "Deaths": 3253}, {"day": "2020-03-21T00:00:00", "country": "China", "Deaths": 3259}, {"day": "2020-03-22T00:00:00", "country": "China", "Deaths": 3274}, {"day": "2020-03-23T00:00:00", "country": "China", "Deaths": 3274}, {"day": "2020-03-24T00:00:00", "country": "China", "Deaths": 3281}, {"day": "2020-03-25T00:00:00", "country": "China", "Deaths": 3285}, {"day": "2020-03-26T00:00:00", "country": "China", "Deaths": 3291}, {"day": "2020-03-27T00:00:00", "country": "China", "Deaths": 3296}, {"day": "2020-03-28T00:00:00", "country": "China", "Deaths": 3299}, {"day": "2020-03-29T00:00:00", "country": "China", "Deaths": 3304}, {"day": "2020-03-30T00:00:00", "country": "China", "Deaths": 3308}, {"day": "2020-03-31T00:00:00", "country": "China", "Deaths": 3309}, {"day": "2020-01-22T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-01-23T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-01-24T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-01-25T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-01-26T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-01-27T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-01-28T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-01-29T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-01-30T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-01-31T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-01T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-02T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-03T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-04T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-05T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-06T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-07T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-08T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-09T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-10T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-11T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-12T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-13T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-14T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-15T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-16T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-17T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-18T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-19T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-20T00:00:00", "country": "Italy", "Deaths": 0}, {"day": "2020-02-21T00:00:00", "country": "Italy", "Deaths": 1}, {"day": "2020-02-22T00:00:00", "country": "Italy", "Deaths": 2}, {"day": "2020-02-23T00:00:00", "country": "Italy", "Deaths": 3}, {"day": "2020-02-24T00:00:00", "country": "Italy", "Deaths": 7}, {"day": "2020-02-25T00:00:00", "country": "Italy", "Deaths": 10}, {"day": "2020-02-26T00:00:00", "country": "Italy", "Deaths": 12}, {"day": "2020-02-27T00:00:00", "country": "Italy", "Deaths": 17}, {"day": "2020-02-28T00:00:00", "country": "Italy", "Deaths": 21}, {"day": "2020-02-29T00:00:00", "country": "Italy", "Deaths": 29}, {"day": "2020-03-01T00:00:00", "country": "Italy", "Deaths": 34}, {"day": "2020-03-02T00:00:00", "country": "Italy", "Deaths": 52}, {"day": "2020-03-03T00:00:00", "country": "Italy", "Deaths": 79}, {"day": "2020-03-04T00:00:00", "country": "Italy", "Deaths": 107}, {"day": "2020-03-05T00:00:00", "country": "Italy", "Deaths": 148}, {"day": "2020-03-06T00:00:00", "country": "Italy", "Deaths": 197}, {"day": "2020-03-07T00:00:00", "country": "Italy", "Deaths": 233}, {"day": "2020-03-08T00:00:00", "country": "Italy", "Deaths": 366}, {"day": "2020-03-09T00:00:00", "country": "Italy", "Deaths": 463}, {"day": "2020-03-10T00:00:00", "country": "Italy", "Deaths": 631}, {"day": "2020-03-11T00:00:00", "country": "Italy", "Deaths": 827}, {"day": "2020-03-12T00:00:00", "country": "Italy", "Deaths": 827}, {"day": "2020-03-13T00:00:00", "country": "Italy", "Deaths": 1266}, {"day": "2020-03-14T00:00:00", "country": "Italy", "Deaths": 1441}, {"day": "2020-03-15T00:00:00", "country": "Italy", "Deaths": 1809}, {"day": "2020-03-16T00:00:00", "country": "Italy", "Deaths": 2158}, {"day": "2020-03-17T00:00:00", "country": "Italy", "Deaths": 2503}, {"day": "2020-03-18T00:00:00", "country": "Italy", "Deaths": 2978}, {"day": "2020-03-19T00:00:00", "country": "Italy", "Deaths": 3405}, {"day": "2020-03-20T00:00:00", "country": "Italy", "Deaths": 4032}, {"day": "2020-03-21T00:00:00", "country": "Italy", "Deaths": 4825}, {"day": "2020-03-22T00:00:00", "country": "Italy", "Deaths": 5476}, {"day": "2020-03-23T00:00:00", "country": "Italy", "Deaths": 6077}, {"day": "2020-03-24T00:00:00", "country": "Italy", "Deaths": 6820}, {"day": "2020-03-25T00:00:00", "country": "Italy", "Deaths": 7503}, {"day": "2020-03-26T00:00:00", "country": "Italy", "Deaths": 8215}, {"day": "2020-03-27T00:00:00", "country": "Italy", "Deaths": 9134}, {"day": "2020-03-28T00:00:00", "country": "Italy", "Deaths": 10023}, {"day": "2020-03-29T00:00:00", "country": "Italy", "Deaths": 10779}, {"day": "2020-03-30T00:00:00", "country": "Italy", "Deaths": 11591}, {"day": "2020-03-31T00:00:00", "country": "Italy", "Deaths": 12428}, {"day": "2020-01-22T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-01-23T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-01-24T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-01-25T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-01-26T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-01-27T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-01-28T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-01-29T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-01-30T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-01-31T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-01T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-02T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-03T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-04T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-05T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-06T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-07T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-08T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-09T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-10T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-11T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-12T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-13T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-14T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-15T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-16T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-17T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-18T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-19T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-20T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-21T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-22T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-23T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-24T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-25T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-26T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-27T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-28T00:00:00", "country": "US", "Deaths": 0}, {"day": "2020-02-29T00:00:00", "country": "US", "Deaths": 1}, {"day": "2020-03-01T00:00:00", "country": "US", "Deaths": 1}, {"day": "2020-03-02T00:00:00", "country": "US", "Deaths": 6}, {"day": "2020-03-03T00:00:00", "country": "US", "Deaths": 7}, {"day": "2020-03-04T00:00:00", "country": "US", "Deaths": 11}, {"day": "2020-03-05T00:00:00", "country": "US", "Deaths": 12}, {"day": "2020-03-06T00:00:00", "country": "US", "Deaths": 14}, {"day": "2020-03-07T00:00:00", "country": "US", "Deaths": 17}, {"day": "2020-03-08T00:00:00", "country": "US", "Deaths": 21}, {"day": "2020-03-09T00:00:00", "country": "US", "Deaths": 22}, {"day": "2020-03-10T00:00:00", "country": "US", "Deaths": 28}, {"day": "2020-03-11T00:00:00", "country": "US", "Deaths": 36}, {"day": "2020-03-12T00:00:00", "country": "US", "Deaths": 40}, {"day": "2020-03-13T00:00:00", "country": "US", "Deaths": 47}, {"day": "2020-03-14T00:00:00", "country": "US", "Deaths": 54}, {"day": "2020-03-15T00:00:00", "country": "US", "Deaths": 63}, {"day": "2020-03-16T00:00:00", "country": "US", "Deaths": 85}, {"day": "2020-03-17T00:00:00", "country": "US", "Deaths": 108}, {"day": "2020-03-18T00:00:00", "country": "US", "Deaths": 118}, {"day": "2020-03-19T00:00:00", "country": "US", "Deaths": 200}, {"day": "2020-03-20T00:00:00", "country": "US", "Deaths": 244}, {"day": "2020-03-21T00:00:00", "country": "US", "Deaths": 307}, {"day": "2020-03-22T00:00:00", "country": "US", "Deaths": 417}, {"day": "2020-03-23T00:00:00", "country": "US", "Deaths": 557}, {"day": "2020-03-24T00:00:00", "country": "US", "Deaths": 706}, {"day": "2020-03-25T00:00:00", "country": "US", "Deaths": 942}, {"day": "2020-03-26T00:00:00", "country": "US", "Deaths": 1209}, {"day": "2020-03-27T00:00:00", "country": "US", "Deaths": 1581}, {"day": "2020-03-28T00:00:00", "country": "US", "Deaths": 2026}, {"day": "2020-03-29T00:00:00", "country": "US", "Deaths": 2467}, {"day": "2020-03-30T00:00:00", "country": "US", "Deaths": 2978}, {"day": "2020-03-31T00:00:00", "country": "US", "Deaths": 3873}, {"day": "2020-01-22T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-01-23T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-01-24T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-01-25T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-01-26T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-01-27T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-01-28T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-01-29T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-01-30T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-01-31T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-01T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-02T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-03T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-04T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-05T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-06T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-07T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-08T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-09T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-10T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-11T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-12T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-13T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-14T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-15T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-16T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-17T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-18T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-19T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-20T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-21T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-22T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-23T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-24T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-25T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-26T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-27T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-28T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-02-29T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-03-01T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-03-02T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-03-03T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-03-04T00:00:00", "country": "United Kingdom", "Deaths": 0}, {"day": "2020-03-05T00:00:00", "country": "United Kingdom", "Deaths": 1}, {"day": "2020-03-06T00:00:00", "country": "United Kingdom", "Deaths": 2}, {"day": "2020-03-07T00:00:00", "country": "United Kingdom", "Deaths": 2}, {"day": "2020-03-08T00:00:00", "country": "United Kingdom", "Deaths": 3}, {"day": "2020-03-09T00:00:00", "country": "United Kingdom", "Deaths": 4}, {"day": "2020-03-10T00:00:00", "country": "United Kingdom", "Deaths": 6}, {"day": "2020-03-11T00:00:00", "country": "United Kingdom", "Deaths": 8}, {"day": "2020-03-12T00:00:00", "country": "United Kingdom", "Deaths": 8}, {"day": "2020-03-13T00:00:00", "country": "United Kingdom", "Deaths": 8}, {"day": "2020-03-14T00:00:00", "country": "United Kingdom", "Deaths": 21}, {"day": "2020-03-15T00:00:00", "country": "United Kingdom", "Deaths": 21}, {"day": "2020-03-16T00:00:00", "country": "United Kingdom", "Deaths": 56}, {"day": "2020-03-17T00:00:00", "country": "United Kingdom", "Deaths": 56}, {"day": "2020-03-18T00:00:00", "country": "United Kingdom", "Deaths": 72}, {"day": "2020-03-19T00:00:00", "country": "United Kingdom", "Deaths": 138}, {"day": "2020-03-20T00:00:00", "country": "United Kingdom", "Deaths": 178}, {"day": "2020-03-21T00:00:00", "country": "United Kingdom", "Deaths": 234}, {"day": "2020-03-22T00:00:00", "country": "United Kingdom", "Deaths": 282}, {"day": "2020-03-23T00:00:00", "country": "United Kingdom", "Deaths": 336}, {"day": "2020-03-24T00:00:00", "country": "United Kingdom", "Deaths": 423}, {"day": "2020-03-25T00:00:00", "country": "United Kingdom", "Deaths": 466}, {"day": "2020-03-26T00:00:00", "country": "United Kingdom", "Deaths": 580}, {"day": "2020-03-27T00:00:00", "country": "United Kingdom", "Deaths": 761}, {"day": "2020-03-28T00:00:00", "country": "United Kingdom", "Deaths": 1021}, {"day": "2020-03-29T00:00:00", "country": "United Kingdom", "Deaths": 1231}, {"day": "2020-03-30T00:00:00", "country": "United Kingdom", "Deaths": 1411}, {"day": "2020-03-31T00:00:00", "country": "United Kingdom", "Deaths": 1793}]}}, {"mode": "vega-lite"});
</script>


## 5. Graphing current and time series counts using Covid API <a name="covid-api"></a>
#### [back](#top-of-covid-notebook)

[This site](https://covid19api.com/) details an API that nicely wraps up the same JHU dataset and presents it as `json` via a REST API which allows us to go from API call to formatted graph showing cases and deaths by country using `altair` as follows:

```python
plotCountriesDailyReportFromAPI(visualisation='altair')
```



<div id="altair-viz-37013f4b8fd3436b94c043c27402c3f2"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    const outputDiv = document.getElementById("altair-viz-37013f4b8fd3436b94c043c27402c3f2");
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.0.2?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-2e95aae0418724caf4117fb2670b86aa"}, "mark": {"type": "bar", "size": 10}, "encoding": {"color": {"type": "nominal", "field": "Category", "legend": {"title": "Category"}, "scale": {"domain": ["TotalRecovered", "TotalConfirmed", "TotalDeaths"], "range": ["green", "orange", "red"]}}, "order": {"type": "nominal", "field": "Category", "sort": "descending"}, "x": {"type": "nominal", "field": "Country", "sort": "-y"}, "y": {"type": "quantitative", "field": "Count"}}, "height": 450, "title": "Covid-19 cases and deaths", "transform": [{"fold": ["TotalRecovered", "TotalConfirmed", "TotalDeaths"], "as": ["Category", "Count"]}], "width": 1000, "$schema": "https://vega.github.io/schema/vega-lite/v4.0.2.json", "datasets": {"data-2e95aae0418724caf4117fb2670b86aa": [{"Country": "US", "Slug": "us", "NewConfirmed": 26365, "TotalConfirmed": 188172, "NewDeaths": 895, "TotalDeaths": 3873, "NewRecovered": 1380, "TotalRecovered": 7024}, {"Country": "Italy", "Slug": "italy", "NewConfirmed": 4053, "TotalConfirmed": 105792, "NewDeaths": 837, "TotalDeaths": 12428, "NewRecovered": 1109, "TotalRecovered": 15729}, {"Country": "Spain", "Slug": "spain", "NewConfirmed": 7967, "TotalConfirmed": 95923, "NewDeaths": 748, "TotalDeaths": 8464, "NewRecovered": 2479, "TotalRecovered": 19259}, {"Country": "China", "Slug": "china", "NewConfirmed": 81, "TotalConfirmed": 82279, "NewDeaths": 1, "TotalDeaths": 3309, "NewRecovered": 283, "TotalRecovered": 76206}, {"Country": "Germany", "Slug": "germany", "NewConfirmed": 4923, "TotalConfirmed": 71808, "NewDeaths": 130, "TotalDeaths": 775, "NewRecovered": 2600, "TotalRecovered": 16100}, {"Country": "France", "Slug": "france", "NewConfirmed": 7657, "TotalConfirmed": 52827, "NewDeaths": 502, "TotalDeaths": 3532, "NewRecovered": 1549, "TotalRecovered": 9513}, {"Country": "Iran", "Slug": "iran", "NewConfirmed": 3110, "TotalConfirmed": 44605, "NewDeaths": 141, "TotalDeaths": 2898, "NewRecovered": 745, "TotalRecovered": 14656}, {"Country": "Iran (Islamic Republic of)", "Slug": "iran", "NewConfirmed": 3110, "TotalConfirmed": 44605, "NewDeaths": 141, "TotalDeaths": 2898, "NewRecovered": 745, "TotalRecovered": 14656}, {"Country": "United Kingdom", "Slug": "united-kingdom", "NewConfirmed": 3028, "TotalConfirmed": 25481, "NewDeaths": 382, "TotalDeaths": 1793, "NewRecovered": 8, "TotalRecovered": 179}, {"Country": "Switzerland", "Slug": "switzerland", "NewConfirmed": 683, "TotalConfirmed": 16605, "NewDeaths": 74, "TotalDeaths": 433, "NewRecovered": 0, "TotalRecovered": 1823}, {"Country": "Turkey", "Slug": "turkey", "NewConfirmed": 2704, "TotalConfirmed": 13531, "NewDeaths": 46, "TotalDeaths": 214, "NewRecovered": 81, "TotalRecovered": 243}, {"Country": "Belgium", "Slug": "belgium", "NewConfirmed": 876, "TotalConfirmed": 12775, "NewDeaths": 192, "TotalDeaths": 705, "NewRecovered": 169, "TotalRecovered": 1696}, {"Country": "Netherlands", "Slug": "netherlands", "NewConfirmed": 850, "TotalConfirmed": 12667, "NewDeaths": 175, "TotalDeaths": 1040, "NewRecovered": 0, "TotalRecovered": 253}, {"Country": "Austria", "Slug": "austria", "NewConfirmed": 562, "TotalConfirmed": 10180, "NewDeaths": 20, "TotalDeaths": 128, "NewRecovered": 459, "TotalRecovered": 1095}, {"Country": "South Korea", "Slug": "korea-south", "NewConfirmed": 125, "TotalConfirmed": 9786, "NewDeaths": 4, "TotalDeaths": 162, "NewRecovered": 180, "TotalRecovered": 5408}, {"Country": "Korea, South", "Slug": "korea-south", "NewConfirmed": 125, "TotalConfirmed": 9786, "NewDeaths": 4, "TotalDeaths": 162, "NewRecovered": 180, "TotalRecovered": 5408}, {"Country": "Republic of Korea", "Slug": "korea-south", "NewConfirmed": 125, "TotalConfirmed": 9786, "NewDeaths": 4, "TotalDeaths": 162, "NewRecovered": 180, "TotalRecovered": 5408}, {"Country": "Canada", "Slug": "canada", "NewConfirmed": 1129, "TotalConfirmed": 8527, "NewDeaths": 21, "TotalDeaths": 101, "NewRecovered": 1126, "TotalRecovered": 1592}, {"Country": "Portugal", "Slug": "portugal", "NewConfirmed": 1035, "TotalConfirmed": 7443, "NewDeaths": 20, "TotalDeaths": 160, "NewRecovered": 0, "TotalRecovered": 43}, {"Country": "Brazil", "Slug": "brazil", "NewConfirmed": 1138, "TotalConfirmed": 5717, "NewDeaths": 42, "TotalDeaths": 201, "NewRecovered": 7, "TotalRecovered": 127}, {"Country": "Israel", "Slug": "israel", "NewConfirmed": 663, "TotalConfirmed": 5358, "NewDeaths": 4, "TotalDeaths": 20, "NewRecovered": 63, "TotalRecovered": 224}, {"Country": "Norway", "Slug": "norway", "NewConfirmed": 196, "TotalConfirmed": 4641, "NewDeaths": 7, "TotalDeaths": 39, "NewRecovered": 1, "TotalRecovered": 13}, {"Country": "Australia", "Slug": "australia", "NewConfirmed": 198, "TotalConfirmed": 4559, "NewDeaths": 1, "TotalDeaths": 18, "NewRecovered": 101, "TotalRecovered": 358}, {"Country": "Sweden", "Slug": "sweden", "NewConfirmed": 407, "TotalConfirmed": 4435, "NewDeaths": 34, "TotalDeaths": 180, "NewRecovered": 0, "TotalRecovered": 16}, {"Country": "Czechia", "Slug": "czechia", "NewConfirmed": 307, "TotalConfirmed": 3308, "NewDeaths": 8, "TotalDeaths": 31, "NewRecovered": 20, "TotalRecovered": 45}, {"Country": "Ireland", "Slug": "ireland", "NewConfirmed": 325, "TotalConfirmed": 3235, "NewDeaths": 17, "TotalDeaths": 71, "NewRecovered": 0, "TotalRecovered": 5}, {"Country": "Denmark", "Slug": "denmark", "NewConfirmed": 284, "TotalConfirmed": 3039, "NewDeaths": 13, "TotalDeaths": 90, "NewRecovered": 4, "TotalRecovered": 77}, {"Country": "Malaysia", "Slug": "malaysia", "NewConfirmed": 140, "TotalConfirmed": 2766, "NewDeaths": 6, "TotalDeaths": 43, "NewRecovered": 58, "TotalRecovered": 537}, {"Country": "Chile", "Slug": "chile", "NewConfirmed": 289, "TotalConfirmed": 2738, "NewDeaths": 4, "TotalDeaths": 12, "NewRecovered": 0, "TotalRecovered": 156}, {"Country": "Russia", "Slug": "russia", "NewConfirmed": 501, "TotalConfirmed": 2337, "NewDeaths": 8, "TotalDeaths": 17, "NewRecovered": 55, "TotalRecovered": 121}, {"Country": "Russian Federation", "Slug": "russia", "NewConfirmed": 501, "TotalConfirmed": 2337, "NewDeaths": 8, "TotalDeaths": 17, "NewRecovered": 55, "TotalRecovered": 121}, {"Country": "Poland", "Slug": "poland", "NewConfirmed": 256, "TotalConfirmed": 2311, "NewDeaths": 2, "TotalDeaths": 33, "NewRecovered": 0, "TotalRecovered": 7}, {"Country": "Romania", "Slug": "romania", "NewConfirmed": 136, "TotalConfirmed": 2245, "NewDeaths": 17, "TotalDeaths": 82, "NewRecovered": 11, "TotalRecovered": 220}, {"Country": "Ecuador", "Slug": "ecuador", "NewConfirmed": 278, "TotalConfirmed": 2240, "NewDeaths": 15, "TotalDeaths": 75, "NewRecovered": 51, "TotalRecovered": 54}, {"Country": "Luxembourg", "Slug": "luxembourg", "NewConfirmed": 190, "TotalConfirmed": 2178, "NewDeaths": 1, "TotalDeaths": 23, "NewRecovered": 40, "TotalRecovered": 80}, {"Country": "Philippines", "Slug": "philippines", "NewConfirmed": 538, "TotalConfirmed": 2084, "NewDeaths": 10, "TotalDeaths": 88, "NewRecovered": 7, "TotalRecovered": 49}, {"Country": "Japan", "Slug": "japan", "NewConfirmed": 87, "TotalConfirmed": 1953, "NewDeaths": 2, "TotalDeaths": 56, "NewRecovered": 0, "TotalRecovered": 424}, {"Country": "Pakistan", "Slug": "pakistan", "NewConfirmed": 221, "TotalConfirmed": 1938, "NewDeaths": 5, "TotalDeaths": 26, "NewRecovered": 0, "TotalRecovered": 76}, {"Country": "Indonesia", "Slug": "indonesia", "NewConfirmed": 114, "TotalConfirmed": 1528, "NewDeaths": 14, "TotalDeaths": 136, "NewRecovered": 6, "TotalRecovered": 81}, {"Country": "Finland", "Slug": "finland", "NewConfirmed": 66, "TotalConfirmed": 1418, "NewDeaths": 4, "TotalDeaths": 17, "NewRecovered": 0, "TotalRecovered": 10}, {"Country": "India", "Slug": "india", "NewConfirmed": 146, "TotalConfirmed": 1397, "NewDeaths": 3, "TotalDeaths": 35, "NewRecovered": 21, "TotalRecovered": 123}, {"Country": "Greece", "Slug": "greece", "NewConfirmed": 102, "TotalConfirmed": 1314, "NewDeaths": 6, "TotalDeaths": 49, "NewRecovered": 0, "TotalRecovered": 52}, {"Country": "Panama", "Slug": "panama", "NewConfirmed": 192, "TotalConfirmed": 1181, "NewDeaths": 6, "TotalDeaths": 30, "NewRecovered": 5, "TotalRecovered": 9}, {"Country": "Dominican Republic", "Slug": "dominican-republic", "NewConfirmed": 208, "TotalConfirmed": 1109, "NewDeaths": 9, "TotalDeaths": 51, "NewRecovered": 1, "TotalRecovered": 5}, {"Country": "Mexico", "Slug": "mexico", "NewConfirmed": 101, "TotalConfirmed": 1094, "NewDeaths": 8, "TotalDeaths": 28, "NewRecovered": 0, "TotalRecovered": 35}, {"Country": "Peru", "Slug": "peru", "NewConfirmed": 115, "TotalConfirmed": 1065, "NewDeaths": 6, "TotalDeaths": 30, "NewRecovered": 341, "TotalRecovered": 394}, {"Country": "Argentina", "Slug": "argentina", "NewConfirmed": 234, "TotalConfirmed": 1054, "NewDeaths": 4, "TotalDeaths": 27, "NewRecovered": 12, "TotalRecovered": 240}, {"Country": "Colombia", "Slug": "colombia", "NewConfirmed": 108, "TotalConfirmed": 906, "NewDeaths": 4, "TotalDeaths": 16, "NewRecovered": 16, "TotalRecovered": 31}, {"Country": "Serbia", "Slug": "serbia", "NewConfirmed": 115, "TotalConfirmed": 900, "NewDeaths": 0, "TotalDeaths": 16, "NewRecovered": 0, "TotalRecovered": 0}, {"Country": "Slovenia", "Slug": "slovenia", "NewConfirmed": 46, "TotalConfirmed": 802, "NewDeaths": 4, "TotalDeaths": 15, "NewRecovered": 0, "TotalRecovered": 10}, {"Country": "Algeria", "Slug": "algeria", "NewConfirmed": 132, "TotalConfirmed": 716, "NewDeaths": 9, "TotalDeaths": 44, "NewRecovered": 9, "TotalRecovered": 46}, {"Country": "Egypt", "Slug": "egypt", "NewConfirmed": 54, "TotalConfirmed": 710, "NewDeaths": 5, "TotalDeaths": 46, "NewRecovered": 7, "TotalRecovered": 157}, {"Country": "Iraq", "Slug": "iraq", "NewConfirmed": 64, "TotalConfirmed": 694, "NewDeaths": 4, "TotalDeaths": 50, "NewRecovered": 18, "TotalRecovered": 170}, {"Country": "Ukraine", "Slug": "ukraine", "NewConfirmed": 97, "TotalConfirmed": 645, "NewDeaths": 4, "TotalDeaths": 17, "NewRecovered": 2, "TotalRecovered": 10}, {"Country": "Morocco", "Slug": "morocco", "NewConfirmed": 61, "TotalConfirmed": 617, "NewDeaths": 3, "TotalDeaths": 36, "NewRecovered": 9, "TotalRecovered": 24}, {"Country": "Hungary", "Slug": "hungary", "NewConfirmed": 45, "TotalConfirmed": 492, "NewDeaths": 1, "TotalDeaths": 16, "NewRecovered": 3, "TotalRecovered": 37}, {"Country": "Lebanon", "Slug": "lebanon", "NewConfirmed": 24, "TotalConfirmed": 470, "NewDeaths": 1, "TotalDeaths": 12, "NewRecovered": 2, "TotalRecovered": 37}, {"Country": "Bosnia and Herzegovina", "Slug": "bosnia-and-herzegovina", "NewConfirmed": 52, "TotalConfirmed": 420, "NewDeaths": 3, "TotalDeaths": 13, "NewRecovered": 0, "TotalRecovered": 17}, {"Country": "Andorra", "Slug": "andorra", "NewConfirmed": 6, "TotalConfirmed": 376, "NewDeaths": 4, "TotalDeaths": 12, "NewRecovered": 0, "TotalRecovered": 10}, {"Country": "Burkina Faso", "Slug": "burkina-faso", "NewConfirmed": 15, "TotalConfirmed": 261, "NewDeaths": 2, "TotalDeaths": 14, "NewRecovered": 1, "TotalRecovered": 32}, {"Country": "Albania", "Slug": "albania", "NewConfirmed": 20, "TotalConfirmed": 243, "NewDeaths": 4, "TotalDeaths": 15, "NewRecovered": 8, "TotalRecovered": 52}, {"Country": "San Marino", "Slug": "san-marino", "NewConfirmed": 6, "TotalConfirmed": 236, "NewDeaths": 1, "TotalDeaths": 26, "NewRecovered": 0, "TotalRecovered": 13}]}}, {"mode": "vega-lite"});
</script>


Note that not all the country names are fully normalised - Iran and South Korea appear twice.  You can normalise the data by passing in a `normalise=True` flag:

```python
plotCountriesDailyReportFromAPI(normalised=True, visualisation='altair')
```



<div id="altair-viz-a711a348c0fa48f48de38dc737888f81"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    const outputDiv = document.getElementById("altair-viz-a711a348c0fa48f48de38dc737888f81");
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.0.2?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-a7ca74cea67e9fd03a9f0351a83a40bf"}, "mark": {"type": "bar", "size": 10}, "encoding": {"color": {"type": "nominal", "field": "Category", "legend": {"title": "Category"}, "scale": {"domain": ["TotalRecovered", "TotalConfirmed", "TotalDeaths"], "range": ["green", "orange", "red"]}}, "order": {"type": "nominal", "field": "Category", "sort": "descending"}, "x": {"type": "nominal", "field": "Country", "sort": "-y"}, "y": {"type": "quantitative", "field": "Count"}}, "height": 450, "title": "Covid-19 cases and deaths", "transform": [{"fold": ["TotalRecovered", "TotalConfirmed", "TotalDeaths"], "as": ["Category", "Count"]}], "width": 1000, "$schema": "https://vega.github.io/schema/vega-lite/v4.0.2.json", "datasets": {"data-a7ca74cea67e9fd03a9f0351a83a40bf": [{"Country": "US", "NewConfirmed": 26365, "TotalConfirmed": 188172, "NewDeaths": 895, "TotalDeaths": 3873, "NewRecovered": 1380, "TotalRecovered": 7024}, {"Country": "Italy", "NewConfirmed": 4053, "TotalConfirmed": 105792, "NewDeaths": 837, "TotalDeaths": 12428, "NewRecovered": 1109, "TotalRecovered": 15729}, {"Country": "Spain", "NewConfirmed": 7967, "TotalConfirmed": 95923, "NewDeaths": 748, "TotalDeaths": 8464, "NewRecovered": 2479, "TotalRecovered": 19259}, {"Country": "Iran", "NewConfirmed": 6220, "TotalConfirmed": 89210, "NewDeaths": 282, "TotalDeaths": 5796, "NewRecovered": 1490, "TotalRecovered": 29312}, {"Country": "China", "NewConfirmed": 81, "TotalConfirmed": 82279, "NewDeaths": 1, "TotalDeaths": 3309, "NewRecovered": 283, "TotalRecovered": 76206}, {"Country": "Germany", "NewConfirmed": 4923, "TotalConfirmed": 71808, "NewDeaths": 130, "TotalDeaths": 775, "NewRecovered": 2600, "TotalRecovered": 16100}, {"Country": "France", "NewConfirmed": 7657, "TotalConfirmed": 52827, "NewDeaths": 502, "TotalDeaths": 3532, "NewRecovered": 1549, "TotalRecovered": 9513}, {"Country": "United Kingdom", "NewConfirmed": 3028, "TotalConfirmed": 25481, "NewDeaths": 382, "TotalDeaths": 1793, "NewRecovered": 8, "TotalRecovered": 179}, {"Country": "South Korea", "NewConfirmed": 250, "TotalConfirmed": 19572, "NewDeaths": 8, "TotalDeaths": 324, "NewRecovered": 360, "TotalRecovered": 10816}, {"Country": "Switzerland", "NewConfirmed": 683, "TotalConfirmed": 16605, "NewDeaths": 74, "TotalDeaths": 433, "NewRecovered": 0, "TotalRecovered": 1823}, {"Country": "Turkey", "NewConfirmed": 2704, "TotalConfirmed": 13531, "NewDeaths": 46, "TotalDeaths": 214, "NewRecovered": 81, "TotalRecovered": 243}, {"Country": "Belgium", "NewConfirmed": 876, "TotalConfirmed": 12775, "NewDeaths": 192, "TotalDeaths": 705, "NewRecovered": 169, "TotalRecovered": 1696}, {"Country": "Netherlands", "NewConfirmed": 850, "TotalConfirmed": 12667, "NewDeaths": 175, "TotalDeaths": 1040, "NewRecovered": 0, "TotalRecovered": 253}, {"Country": "Austria", "NewConfirmed": 562, "TotalConfirmed": 10180, "NewDeaths": 20, "TotalDeaths": 128, "NewRecovered": 459, "TotalRecovered": 1095}, {"Country": "Republic of Korea", "NewConfirmed": 125, "TotalConfirmed": 9786, "NewDeaths": 4, "TotalDeaths": 162, "NewRecovered": 180, "TotalRecovered": 5408}, {"Country": "Canada", "NewConfirmed": 1129, "TotalConfirmed": 8527, "NewDeaths": 21, "TotalDeaths": 101, "NewRecovered": 1126, "TotalRecovered": 1592}, {"Country": "Portugal", "NewConfirmed": 1035, "TotalConfirmed": 7443, "NewDeaths": 20, "TotalDeaths": 160, "NewRecovered": 0, "TotalRecovered": 43}, {"Country": "Brazil", "NewConfirmed": 1138, "TotalConfirmed": 5717, "NewDeaths": 42, "TotalDeaths": 201, "NewRecovered": 7, "TotalRecovered": 127}, {"Country": "Israel", "NewConfirmed": 663, "TotalConfirmed": 5358, "NewDeaths": 4, "TotalDeaths": 20, "NewRecovered": 63, "TotalRecovered": 224}, {"Country": "Norway", "NewConfirmed": 196, "TotalConfirmed": 4641, "NewDeaths": 7, "TotalDeaths": 39, "NewRecovered": 1, "TotalRecovered": 13}, {"Country": "Australia", "NewConfirmed": 198, "TotalConfirmed": 4559, "NewDeaths": 1, "TotalDeaths": 18, "NewRecovered": 101, "TotalRecovered": 358}, {"Country": "Sweden", "NewConfirmed": 407, "TotalConfirmed": 4435, "NewDeaths": 34, "TotalDeaths": 180, "NewRecovered": 0, "TotalRecovered": 16}, {"Country": "Czechia", "NewConfirmed": 307, "TotalConfirmed": 3308, "NewDeaths": 8, "TotalDeaths": 31, "NewRecovered": 20, "TotalRecovered": 45}, {"Country": "Ireland", "NewConfirmed": 325, "TotalConfirmed": 3235, "NewDeaths": 17, "TotalDeaths": 71, "NewRecovered": 0, "TotalRecovered": 5}, {"Country": "Denmark", "NewConfirmed": 284, "TotalConfirmed": 3039, "NewDeaths": 13, "TotalDeaths": 90, "NewRecovered": 4, "TotalRecovered": 77}, {"Country": "Malaysia", "NewConfirmed": 140, "TotalConfirmed": 2766, "NewDeaths": 6, "TotalDeaths": 43, "NewRecovered": 58, "TotalRecovered": 537}, {"Country": "Chile", "NewConfirmed": 289, "TotalConfirmed": 2738, "NewDeaths": 4, "TotalDeaths": 12, "NewRecovered": 0, "TotalRecovered": 156}, {"Country": "Russia", "NewConfirmed": 501, "TotalConfirmed": 2337, "NewDeaths": 8, "TotalDeaths": 17, "NewRecovered": 55, "TotalRecovered": 121}, {"Country": "Russian Federation", "NewConfirmed": 501, "TotalConfirmed": 2337, "NewDeaths": 8, "TotalDeaths": 17, "NewRecovered": 55, "TotalRecovered": 121}, {"Country": "Poland", "NewConfirmed": 256, "TotalConfirmed": 2311, "NewDeaths": 2, "TotalDeaths": 33, "NewRecovered": 0, "TotalRecovered": 7}, {"Country": "Romania", "NewConfirmed": 136, "TotalConfirmed": 2245, "NewDeaths": 17, "TotalDeaths": 82, "NewRecovered": 11, "TotalRecovered": 220}, {"Country": "Ecuador", "NewConfirmed": 278, "TotalConfirmed": 2240, "NewDeaths": 15, "TotalDeaths": 75, "NewRecovered": 51, "TotalRecovered": 54}, {"Country": "Luxembourg", "NewConfirmed": 190, "TotalConfirmed": 2178, "NewDeaths": 1, "TotalDeaths": 23, "NewRecovered": 40, "TotalRecovered": 80}, {"Country": "Philippines", "NewConfirmed": 538, "TotalConfirmed": 2084, "NewDeaths": 10, "TotalDeaths": 88, "NewRecovered": 7, "TotalRecovered": 49}, {"Country": "Japan", "NewConfirmed": 87, "TotalConfirmed": 1953, "NewDeaths": 2, "TotalDeaths": 56, "NewRecovered": 0, "TotalRecovered": 424}, {"Country": "Pakistan", "NewConfirmed": 221, "TotalConfirmed": 1938, "NewDeaths": 5, "TotalDeaths": 26, "NewRecovered": 0, "TotalRecovered": 76}, {"Country": "Indonesia", "NewConfirmed": 114, "TotalConfirmed": 1528, "NewDeaths": 14, "TotalDeaths": 136, "NewRecovered": 6, "TotalRecovered": 81}, {"Country": "Finland", "NewConfirmed": 66, "TotalConfirmed": 1418, "NewDeaths": 4, "TotalDeaths": 17, "NewRecovered": 0, "TotalRecovered": 10}, {"Country": "India", "NewConfirmed": 146, "TotalConfirmed": 1397, "NewDeaths": 3, "TotalDeaths": 35, "NewRecovered": 21, "TotalRecovered": 123}, {"Country": "Greece", "NewConfirmed": 102, "TotalConfirmed": 1314, "NewDeaths": 6, "TotalDeaths": 49, "NewRecovered": 0, "TotalRecovered": 52}, {"Country": "Panama", "NewConfirmed": 192, "TotalConfirmed": 1181, "NewDeaths": 6, "TotalDeaths": 30, "NewRecovered": 5, "TotalRecovered": 9}, {"Country": "Dominican Republic", "NewConfirmed": 208, "TotalConfirmed": 1109, "NewDeaths": 9, "TotalDeaths": 51, "NewRecovered": 1, "TotalRecovered": 5}, {"Country": "Mexico", "NewConfirmed": 101, "TotalConfirmed": 1094, "NewDeaths": 8, "TotalDeaths": 28, "NewRecovered": 0, "TotalRecovered": 35}, {"Country": "Peru", "NewConfirmed": 115, "TotalConfirmed": 1065, "NewDeaths": 6, "TotalDeaths": 30, "NewRecovered": 341, "TotalRecovered": 394}, {"Country": "Argentina", "NewConfirmed": 234, "TotalConfirmed": 1054, "NewDeaths": 4, "TotalDeaths": 27, "NewRecovered": 12, "TotalRecovered": 240}, {"Country": "Colombia", "NewConfirmed": 108, "TotalConfirmed": 906, "NewDeaths": 4, "TotalDeaths": 16, "NewRecovered": 16, "TotalRecovered": 31}, {"Country": "Serbia", "NewConfirmed": 115, "TotalConfirmed": 900, "NewDeaths": 0, "TotalDeaths": 16, "NewRecovered": 0, "TotalRecovered": 0}, {"Country": "Slovenia", "NewConfirmed": 46, "TotalConfirmed": 802, "NewDeaths": 4, "TotalDeaths": 15, "NewRecovered": 0, "TotalRecovered": 10}, {"Country": "Algeria", "NewConfirmed": 132, "TotalConfirmed": 716, "NewDeaths": 9, "TotalDeaths": 44, "NewRecovered": 9, "TotalRecovered": 46}, {"Country": "Egypt", "NewConfirmed": 54, "TotalConfirmed": 710, "NewDeaths": 5, "TotalDeaths": 46, "NewRecovered": 7, "TotalRecovered": 157}, {"Country": "Iraq", "NewConfirmed": 64, "TotalConfirmed": 694, "NewDeaths": 4, "TotalDeaths": 50, "NewRecovered": 18, "TotalRecovered": 170}, {"Country": "Ukraine", "NewConfirmed": 97, "TotalConfirmed": 645, "NewDeaths": 4, "TotalDeaths": 17, "NewRecovered": 2, "TotalRecovered": 10}, {"Country": "Morocco", "NewConfirmed": 61, "TotalConfirmed": 617, "NewDeaths": 3, "TotalDeaths": 36, "NewRecovered": 9, "TotalRecovered": 24}, {"Country": "Hungary", "NewConfirmed": 45, "TotalConfirmed": 492, "NewDeaths": 1, "TotalDeaths": 16, "NewRecovered": 3, "TotalRecovered": 37}, {"Country": "Lebanon", "NewConfirmed": 24, "TotalConfirmed": 470, "NewDeaths": 1, "TotalDeaths": 12, "NewRecovered": 2, "TotalRecovered": 37}, {"Country": "Bosnia and Herzegovina", "NewConfirmed": 52, "TotalConfirmed": 420, "NewDeaths": 3, "TotalDeaths": 13, "NewRecovered": 0, "TotalRecovered": 17}, {"Country": "Andorra", "NewConfirmed": 6, "TotalConfirmed": 376, "NewDeaths": 4, "TotalDeaths": 12, "NewRecovered": 0, "TotalRecovered": 10}, {"Country": "Burkina Faso", "NewConfirmed": 15, "TotalConfirmed": 261, "NewDeaths": 2, "TotalDeaths": 14, "NewRecovered": 1, "TotalRecovered": 32}, {"Country": "Albania", "NewConfirmed": 20, "TotalConfirmed": 243, "NewDeaths": 4, "TotalDeaths": 15, "NewRecovered": 8, "TotalRecovered": 52}, {"Country": "San Marino", "NewConfirmed": 6, "TotalConfirmed": 236, "NewDeaths": 1, "TotalDeaths": 26, "NewRecovered": 0, "TotalRecovered": 13}]}}, {"mode": "vega-lite"});
</script>


It's also possible to do timeseries representation using this API by country using `altair` as follows:

```python
plotCategoryByCountryFromAPI('Confirmed', 'united-kingdom', color='orange', visualisation='altair')
```



<div id="altair-viz-07e1e966c0b44ac6a18dcb1277190c51"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    const outputDiv = document.getElementById("altair-viz-07e1e966c0b44ac6a18dcb1277190c51");
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.0.2?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-5f9ec0e10e99454a29ff6fce68048707"}, "mark": "line", "encoding": {"color": {"value": "orange"}, "x": {"type": "temporal", "field": "Date"}, "y": {"type": "quantitative", "field": "Cases"}}, "height": 450, "title": "Covid-19 Confirmed in united-kingdom", "width": 1000, "$schema": "https://vega.github.io/schema/vega-lite/v4.0.2.json", "datasets": {"data-5f9ec0e10e99454a29ff6fce68048707": [{"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-11T00:00:00+00:00", "Cases": 1259, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-12T00:00:00+00:00", "Cases": 459, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-13T00:00:00+00:00", "Cases": 801, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-14T00:00:00+00:00", "Cases": 1143, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-15T00:00:00+00:00", "Cases": 1144, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-16T00:00:00+00:00", "Cases": 1551, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-17T00:00:00+00:00", "Cases": 1960, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-18T00:00:00+00:00", "Cases": 2642, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-19T00:00:00+00:00", "Cases": 2716, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-20T00:00:00+00:00", "Cases": 4014, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-21T00:00:00+00:00", "Cases": 5067, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-22T00:00:00+00:00", "Cases": 5741, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-23T00:00:00+00:00", "Cases": 6726, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-24T00:00:00+00:00", "Cases": 8164, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-25T00:00:00+00:00", "Cases": 9640, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-26T00:00:00+00:00", "Cases": 11812, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-27T00:00:00+00:00", "Cases": 14745, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-28T00:00:00+00:00", "Cases": 17312, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-29T00:00:00+00:00", "Cases": 19780, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-30T00:00:00+00:00", "Cases": 22453, "Status": "confirmed"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-31T00:00:00+00:00", "Cases": 25481, "Status": "confirmed"}]}}, {"mode": "vega-lite"});
</script>


```python
plotCategoryByCountryFromAPI('Deaths', 'united-kingdom', color='red', visualisation='altair')
```



<div id="altair-viz-a5ec2a7b6f274dde89ada2470e47e969"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    const outputDiv = document.getElementById("altair-viz-a5ec2a7b6f274dde89ada2470e47e969");
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.0.2?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-7a5bf850b7e4125632d3cd21c4f61f02"}, "mark": "line", "encoding": {"color": {"value": "red"}, "x": {"type": "temporal", "field": "Date"}, "y": {"type": "quantitative", "field": "Cases"}}, "height": 450, "title": "Covid-19 Deaths in united-kingdom", "width": 1000, "$schema": "https://vega.github.io/schema/vega-lite/v4.0.2.json", "datasets": {"data-7a5bf850b7e4125632d3cd21c4f61f02": [{"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-11T00:00:00+00:00", "Cases": 16, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-12T00:00:00+00:00", "Cases": 8, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-13T00:00:00+00:00", "Cases": 8, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-14T00:00:00+00:00", "Cases": 21, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-15T00:00:00+00:00", "Cases": 21, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-16T00:00:00+00:00", "Cases": 56, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-17T00:00:00+00:00", "Cases": 56, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-18T00:00:00+00:00", "Cases": 72, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-19T00:00:00+00:00", "Cases": 138, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-20T00:00:00+00:00", "Cases": 178, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-21T00:00:00+00:00", "Cases": 234, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-22T00:00:00+00:00", "Cases": 282, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-23T00:00:00+00:00", "Cases": 336, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-24T00:00:00+00:00", "Cases": 423, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-25T00:00:00+00:00", "Cases": 466, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-26T00:00:00+00:00", "Cases": 580, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-27T00:00:00+00:00", "Cases": 761, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-28T00:00:00+00:00", "Cases": 1021, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-29T00:00:00+00:00", "Cases": 1231, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-30T00:00:00+00:00", "Cases": 1411, "Status": "deaths"}, {"Country": "United Kingdom", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-31T00:00:00+00:00", "Cases": 1793, "Status": "deaths"}]}}, {"mode": "vega-lite"});
</script>


We can also look at the US data:

```python
plotCategoryByCountryFromAPI('Deaths', 'us', color='red', visualisation='altair')
```



<div id="altair-viz-6e48b18f18d749d1b94dfaf1259da754"></div>
<script type="text/javascript">
  (function(spec, embedOpt){
    const outputDiv = document.getElementById("altair-viz-6e48b18f18d749d1b94dfaf1259da754");
    const paths = {
      "vega": "https://cdn.jsdelivr.net/npm//vega@5?noext",
      "vega-lib": "https://cdn.jsdelivr.net/npm//vega-lib?noext",
      "vega-lite": "https://cdn.jsdelivr.net/npm//vega-lite@4.0.2?noext",
      "vega-embed": "https://cdn.jsdelivr.net/npm//vega-embed@6?noext",
    };

    function loadScript(lib) {
      return new Promise(function(resolve, reject) {
        var s = document.createElement('script');
        s.src = paths[lib];
        s.async = true;
        s.onload = () => resolve(paths[lib]);
        s.onerror = () => reject(`Error loading script: ${paths[lib]}`);
        document.getElementsByTagName("head")[0].appendChild(s);
      });
    }

    function showError(err) {
      outputDiv.innerHTML = `<div class="error" style="color:red;">${err}</div>`;
      throw err;
    }

    function displayChart(vegaEmbed) {
      vegaEmbed(outputDiv, spec, embedOpt)
        .catch(err => showError(`Javascript Error: ${err.message}<br>This usually means there's a typo in your chart specification. See the javascript console for the full traceback.`));
    }

    if(typeof define === "function" && define.amd) {
      requirejs.config({paths});
      require(["vega-embed"], displayChart, err => showError(`Error loading script: ${err.message}`));
    } else if (typeof vegaEmbed === "function") {
      displayChart(vegaEmbed);
    } else {
      loadScript("vega")
        .then(() => loadScript("vega-lite"))
        .then(() => loadScript("vega-embed"))
        .catch(showError)
        .then(() => displayChart(vegaEmbed));
    }
  })({"config": {"view": {"continuousWidth": 400, "continuousHeight": 300}}, "data": {"name": "data-bd5515918ff4269e3af3116cccb07448"}, "mark": "line", "encoding": {"color": {"value": "red"}, "x": {"type": "temporal", "field": "Date"}, "y": {"type": "quantitative", "field": "Cases"}}, "height": 450, "title": "Covid-19 Deaths in us", "width": 1000, "$schema": "https://vega.github.io/schema/vega-lite/v4.0.2.json", "datasets": {"data-bd5515918ff4269e3af3116cccb07448": [{"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-01-22T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-01-23T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-01-24T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-01-25T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-01-26T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-01-27T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-01-28T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-01-29T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-01-30T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-01-31T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-01T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-02T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-03T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-04T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-05T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-06T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-07T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-08T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-09T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-10T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-11T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-12T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-13T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-14T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-15T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-16T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-17T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-18T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-19T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-20T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-21T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-22T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-23T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-24T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-25T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-26T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-27T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-28T00:00:00+00:00", "Cases": 0, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-02-29T00:00:00+00:00", "Cases": 1, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-01T00:00:00+00:00", "Cases": 1, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-02T00:00:00+00:00", "Cases": 6, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-03T00:00:00+00:00", "Cases": 7, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-04T00:00:00+00:00", "Cases": 11, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-05T00:00:00+00:00", "Cases": 12, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-06T00:00:00+00:00", "Cases": 14, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-07T00:00:00+00:00", "Cases": 17, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-08T00:00:00+00:00", "Cases": 21, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-09T00:00:00+00:00", "Cases": 22, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-10T00:00:00+00:00", "Cases": 28, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-11T00:00:00+00:00", "Cases": 37, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-12T00:00:00+00:00", "Cases": 40, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-13T00:00:00+00:00", "Cases": 47, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-14T00:00:00+00:00", "Cases": 54, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-15T00:00:00+00:00", "Cases": 63, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-16T00:00:00+00:00", "Cases": 85, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-17T00:00:00+00:00", "Cases": 108, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-18T00:00:00+00:00", "Cases": 118, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-19T00:00:00+00:00", "Cases": 200, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-20T00:00:00+00:00", "Cases": 244, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-21T00:00:00+00:00", "Cases": 307, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-22T00:00:00+00:00", "Cases": 417, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-23T00:00:00+00:00", "Cases": 552, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-24T00:00:00+00:00", "Cases": 706, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-25T00:00:00+00:00", "Cases": 942, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-26T00:00:00+00:00", "Cases": 1209, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-27T00:00:00+00:00", "Cases": 1581, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-28T00:00:00+00:00", "Cases": 2026, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-29T00:00:00+00:00", "Cases": 2467, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-30T00:00:00+00:00", "Cases": 2978, "Status": "deaths"}, {"Country": "US", "Province": "", "Lat": 0, "Lon": 0, "Date": "2020-03-31T00:00:00+00:00", "Cases": 3873, "Status": "deaths"}]}}, {"mode": "vega-lite"});
</script>

