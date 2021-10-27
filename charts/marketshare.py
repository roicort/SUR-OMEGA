import plotly.graph_objects as go

labels = ['Colombia','México','Brasil','Corea','Japón','China', 'USA', 'Tailandia', 'Argentina', 'Alemania', 'Otros']
values = [19.1, 18.8, 18.2, 9.6,8.5,5.9,3.4,3.3,3.1,2.5,7.6]

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig.write_image("marketshare-origen.svg")

labels = ['Nacional','Importaciones']
values = [19.1, 80.9]

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig.write_image("importaciones.svg")

labels = ['Renault','Chevrolet','Mazda','Nissan','Toyota', 'KIA', 'VolksWagen','Suzuki', 'Hyundai','Otros']
values = [20.7,13.9,10.1,8.5,7.4,6.9,5.1,4.8,2.8,19.8]

# Use `hole` to create a donut-like pie chart
fig = go.Figure(data=[go.Pie(labels=labels, values=values, hole=.3)])
fig.write_image("marketshare.svg")