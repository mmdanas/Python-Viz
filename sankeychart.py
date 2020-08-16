#import plotly to viz the data
import plotly.graph_objects as go

#labeling data

label = ["ZERO","ONE","TWO","THREE","FOUR","FIVE"]
source = [0,0,1,1,0]
target = [2,3,4,5,4]
value = [8,2,2,8,4]

#data to dict and dict to sankey flow

#link is to assign source - target dimensions

link = dict(source = source, target = target, value = value)
node = dict(label = label, pad = 50, thickness = 5)
data = go.Sankey(link = link, node = node)
print(data)
fig = go.Figure(data)
fig.show()
