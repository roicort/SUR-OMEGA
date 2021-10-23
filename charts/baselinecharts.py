import plotly.graph_objects as go

labels = ['Automovil','Microbus','Campero','Camioneta']
values = [59.3, 0.0, 6.6, 34.6]

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig.update_layout(title='Distribución del parque automotor colombiano por clase, 2019')
fig.write_image("Desktop/lb-clase.svg")

labels = ['Gasolina','Gasolina-Eléctrico','Eléctrico','Gas Gasol', "Diésel"]
values = [92.1, 0.2, 0.1, 0.4, 7.3]

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig.update_layout(title="Distribución del parque automotor colombiano por tipo de combustible")
fig.write_image("Desktop/lb-combustible.svg")