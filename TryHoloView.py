# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.3'
#       jupytext_version: 1.0.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# +
import holoviews as hv

hv.extension('matplotlib')

# +
import holoviews as hv

hv.extension('matplotlib')
curve = hv.Curve(([1, 2, 3], [1, 2, 4]))
curve
# -

hv.extension('bokeh')
curve = hv.Curve(([1, 2, 3], [1, 2, 4]))
curve

hv.extension('plotly')
curve = hv.Curve(([1, 2, 3], [1, 2, 4]))
curve

hv.extension('bokeh')
curve = hv.Curve(([1, 2, 3], [1, 2, 4]))
bars = hv.Bars((['a', 'b', 'c'], [3, 2, 1]))
curve + bars

# %%opts Scatter(color='green', size=10)
scatter = hv.Scatter(([1, 2, 3], [1, 2, 4]))
curve * scatter

curve * scatter + bars

# +
import holoviews as hv

print(hv.elements_list)

# +
import holoviews as hv
import numpy as np

hv.extension('bokeh')

np.random.seed(111)
x = np.linspace(-np.pi, np.pi, 100)
# -

hv.Curve((x, np.sin(x)))

hv.Area((x, np.sin(x)))

hv.Points(np.random.randn(100, 2))

hv.Scatter(np.random.randn(100, 2))


hv.Bars((list('abc'), range(1, 4)))

hv.Histogram(np.histogram(np.random.randn(1000)))

hv.Points(np.random.randn(100, 2)).hist()

hv.BoxWhisker(np.random.randn(1000))

hv.ErrorBars([(i, np.sin(i), np.random.rand() / 10)
              for i in x]) * hv.Curve((x, np.sin(x)))

hv.Spread((x, np.sin(x), np.random.rand(100)))

hv.Spikes(np.random.randn(100))

p = hv.Points((np.random.randn(100, 2)))
p << hv.Spikes(p['y']) << hv.Spikes(p['x'])

hv.VectorField((range(10), range(10), np.random.rand(10), np.random.rand(10)))


