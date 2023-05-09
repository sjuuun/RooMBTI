import plotly.graph_objs as go

def half_ring_plot(percentage):
    fig = go.FigureWidget()
    fig.add_barpolar(
        r=[1 for _ in range(100)],
        theta=[180 - i for i in range(180)],
        offset=0,
        marker={'color': [1 if i <= percentage*1.8 else 2 for i in range(180)]}
    )
    fig.layout.polar.radialaxis.title = dict(text="Similarity")
    fig.layout.polar.hole = 0.8
    fig.layout.polar.angularaxis.showgrid = False
    fig.layout.polar.radialaxis.showgrid = False
    fig.layout.polar.radialaxis.range = [0, 1]
    fig.layout.polar.radialaxis.tickvals = []
    fig.layout.polar.bargap = 0.9
    fig.layout.polar.sector = [0, 180]
    fig.layout.polar.domain.x = [0, 1]
    return fig