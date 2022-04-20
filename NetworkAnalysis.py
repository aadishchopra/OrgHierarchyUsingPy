from pyvis.network import Network
import pandas as pd
net = Network()

#Building Org Hierarchy

#Step 1 --> Read Data
df=pd.read_csv("D:\PythonProjects\Data\OrgHierarchyNames.csv")

#Find unique Employees (Nodes)

uniqval=df.apply(pd.unique)
arr=[]
for items in uniqval:
    for i in items:
        arr.append(i)
arr = [x for x in arr if pd.notnull(x)]
nodes=set(arr)

#Find relationship among employees (Edges)

#Hierarchy depth
hdepth=len(df.columns)-1
colnames=df.columns


rel=[]
i=0
while (i<hdepth):
    rel.append(list(zip(df[colnames[i]], df[colnames[i+1]])))
    i += 1


refinedrel=[]
for i in range(hdepth):
    for a,b in rel[i]:
        if(str(a) != 'nan' and str(b) !='nan'):
            refinedrel.append(tuple([a,b]))

edges=set(refinedrel)

##Constructing an organizational graph




options = """
var options = {
  "nodes": {
    "fixed": {
      "x": true,
      "y": true
    },
    "shape": "box",
    "shapeProperties": {
      "interpolation": false
    }
  },
  "edges": {
    "arrows": {
      "to": {
        "enabled": true
      }
    },
    "color": {
      "inherit": true
    },
    "smooth": false
  },
  "layout": {
    "hierarchical": {
      "enabled": true,
      "levelSeparation": -150,
      "direction": "RL",
      "sortMethod": "directed"
    }
  },
  "physics": {
    "enabled": false,
    "hierarchicalRepulsion": {
      "centralGravity": 0
    },
    "minVelocity": 0.75,
    "solver": "hierarchicalRepulsion"
  }
}
"""
net.set_options(options)
net.add_nodes(nodes)
net.add_edges(edges)
net.show('new_nx.html')


