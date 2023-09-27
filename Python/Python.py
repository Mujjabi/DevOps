{
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "data": {"url": "data/movies.json"},
    "mark": "point",
    "encoding": {
        "x": {
            "field": "US Gross",
            "type": "quantitative"
        },
        "y": {
            "field": "Worldwide Gross", "type": "quantitative"
        },
        "tooltip": {"field": "Title"}
    }
}

# transformation
{
    "$schema": "https://vega.github.io/schema/vega-lite/v5.json",
    "data": {"url": "data/movies.json"},
    "params": [
        {"name": "myfirstparam", "select": "interval"}],
    "hconcat": [
        {"mark": "bar",
         "encoding": {
             "x": {"field": "IMDB Rating", "type": "quantitative",
                   "bin": true},
             "y": {"aggregate": "mean", "field": "US Gross"}
         }
         },
        {
            "transform": [
                {"filter": {"param": "myfirstparam"}}
            ],
            "mark": "point",
            "encoding": {
                "x": {
                    "field": "US Gross",
                    "type": "quantitative"
                },
                "y": {
                    "field": "Worldwide Gross", "type": "quantitative"}
            }
        }
    ]
}


# With different colors
