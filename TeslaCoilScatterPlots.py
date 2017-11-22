# Import Python libraries
import pandas as pd
import numpy as np
import plotly

# Display graph in offline mode
plotly.offline.init_notebook_mode(connected=False)

# Import expirememnt data spreadsheet as .csv file
CoilData = pd.read_csv('C:/Users/K8nn8/Google Drive/School/Fall 2017/Physics 2 Electromagnetism/TeslaCoilDataCSV.csv')

# Create lists of radius values for all three topload configurations
r_Torus = (CoilData['Torus 20V (cm)'], CoilData['Torus 25V (cm)'], CoilData['Torus 30V (cm)'])
r_Sphere = (CoilData['Sphere 20V (cm)'], CoilData['Sphere 25V (cm)'], CoilData['Sphere 30V (cm)'])
r_None = (CoilData['None 20V (cm)'], CoilData['None 25V (cm)'], CoilData['None 30V (cm)'])

# Group radius values into list 'r'
r = [r_Torus, r_Sphere, r_None]

# Define 'theta' as a fuction that rotates findings at intervals of pi/8
theta = np.linspace(0, 2*np.pi, 16)

# List trace names under their topload categories
trace_Torus = ['trace_T20', 'trace_T25', 'trace_T30']
trace_Sphere = ['trace_S20', 'trace_S25', 'trace_S30']
trace_None = ['trace_N20', 'trace_N25', 'trace_N30']

# Group trace names into list
trace_name = [trace_Torus, trace_Sphere, trace_None]

# Lists of various values related to each topload type; indexed for looping
trace_label = ['20 Volts', '25 Volts', '30 Volts']
trace_color = ['blue', 'red', 'green']
data = ['data_Torus', 'data_Sphere', 'data_None']
title = ['Tesla Coil with Torus Topload', 'Tesla Coil with Spherical Topload', 'Tesla Coil with No Topload']
layout = ['layout_Torus', 'layout_Sphere', 'layout_None']
fig = ['fig_Torus', 'fig_Sphere', 'fig_None']
graph = ['Torus', 'Sphere', 'None']
filename = ['Tesla_3dScatter_Torus', 'Tesla_3dScatter_Sphere', 'Tesla_3dScatter_None']

# Loop through each topload configuration
k = 0
for k in range(3):

    # Loop through each voltage setting for each topload config
    i = 0
    for i in range(3):
        x, y, z = (r[k][i]*np.cos(theta[0]), r[k][i]*np.sin(theta[0]), CoilData['Height (cm)'])

        # Loop through each theta value at each voltage setting for each topload config
        j = 1
        for j in range(len(theta)):
            x = x.append(r[k][i]*np.cos(theta[j]), ignore_index=True)
            y = y.append(r[k][i]*np.sin(theta[j]), ignore_index=True)
            z = z.append(CoilData['Height (cm)'], ignore_index=True)
            j = j + 1

        trace_name[k][i] = plotly.graph_objs.Scatter3d(
            x=x,
            y=y,
            z=z,
            mode='markers',
            name=trace_label[i],
            marker=dict(
                size=6,
                line=dict(
                    color=trace_color[i],
                    width=0.5
                ),
                opacity=0.7
                )
            )

        i = i + 1

    data[k] = trace_name[k]
    layout[k] = plotly.graph_objs.Layout(
        title=title[k],
        margin=dict(
            l=0,
            r=0,
            b=0,
            t=0
            )
        )


    fig[k] = plotly.graph_objs.Figure(data=data[k], layout=layout[k])

    graph[k] = plotly.offline.plot(fig[k], filename=filename[k])

    k = k + 1
