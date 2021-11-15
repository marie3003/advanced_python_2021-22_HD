#
# The first version of our function!
# Write doc strings 
#
import pandas as pd
import numpy as np
import plotly.graph_objects as go
from collections import deque
from pathlib import Path


class Protein:

    aa_properties = pd.read_csv(Path(__file__).parent.parent/"data/amino_acid_properties.csv")
    aa_properties = aa_properties.rename(columns ={'hydropathy index (Kyte-Doolittle method)': 'hydropathy'})
    aa_properties = aa_properties[['1-letter code', 'pI','hydropathy']]
    aa_properties = aa_properties.set_index('1-letter code')
    metrics = aa_properties.to_dict('dict')
    
    def __init__(self, name, sequence):
        self.sequence = sequence
        self.name = name
    
    def find_metric_values(self, metric = "hydropathy"):
        metric_values = []
        for aa in list(self.sequence):
            metric_values.append(Protein.metrics[metric][aa])
        return metric_values

    def calculate_sliding_window(self, metric ="hydropathy", window_size = 5):
        metric_values = self.find_metric_values(metric)
        window = deque([], maxlen = window_size)
        mean_values = []
        for metric_value in metric_values:
            window.append(metric_value)
            mean_values.append(np.mean(window))
        return mean_values
    
    def create_positions(self):
        pos = list(np.arange(len(self.sequence)))
        return pos
    
    def plot(self, metric ="hydropathy", window_size = 5):
        pos = self.create_positions()
        mean_values = self.calculate_sliding_window(metric, window_size)
        data = [
            go.Bar(
                x=pos,
                y=mean_values,
            )
        ]

        fig = go.Figure(data=data)
        fig.update_layout(template="plotly_dark", title="{} of protein {}".format(metric, self.name))
        fig.show()
        return fig
        
        
"""protein = Protein('G', protein_s)
h_5 = protein.plot(window_size=5)
h_100 = protein.plot(window_size=100)
h_5.write_image("h_5.png")
h_100.write_image("h_100.png")
        
"""