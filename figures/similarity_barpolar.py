import plotly.graph_objs as go

def half_ring_plot(percentage):
    fig = go.Figure(go.Indicator(
    mode = "gauge+number",
    value = percentage,
    domain = {'x': [0, 1], 'y': [0, 1]},
    gauge={
        'axis': {'range': [0, 100]}
    },
    title = {'text': "Similarity"}))
    return fig