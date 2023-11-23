import panel as pn
import plotly.express as px
import numpy as np


pn.extension('plotly')


# Fungsi untuk membuat plot Plotly
def create_plot(value):
    x = np.linspace(0, 10, 100)
    y = np.sin(value * x)
    df = {"x": x, "y": y}
    fig = px.line(df, x='x', y='y', title=f'Sin({value} * x)')
    return fig


# Membuat widget slider
slider = pn.widgets.FloatSlider(name='Frequency', start=1, end=5, value=1)


# Membuat panel dengan plot Plotly dan slider
@pn.depends(slider.param.value)
def update_plot(value):
    plot = create_plot(value)
    return plot


paragraf = pn.pane.HTML(
    """
    <h1>Realisasi Inflow Danau Poso</h1>
    <p>\Forecast inflow rata-rata danau poso menggunakan algoritma Extream
    Gradient Booting atau disingkat XGBoost, Xgboost adalah algoritma yang cukup
     Baik yang bisa digunakan untuk data regresi dan time series</p>
    """
)

# Membuat layout
layout = pn.Column(
    '# Plotly Plot with Slider',
    slider,
    update_plot,
    paragraf
)

# Menyajikan aplikasi
layout.servable()
