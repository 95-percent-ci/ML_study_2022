import plotly.graph_objects as go
from abc import ABC


class Meta(ABC):
    """Abstract base class. Outlines Class member functions and variables for plotting using Plotly

    """

    def __init__(self, x, y, marker='markers'):
        self.x = x
        self.y = y
        self.fig = go.Figure()
        self.marker_type = marker

    def plot(self):
        pass


class ScatterPlot(Meta):
    """Class for creating Plotly Scatter Graphs using go object in less verbose manner

    """

    def __init__(self, x, y, marker='markers'):
        super().__init__(x, y)
        self.fig.add_trace(go.Scatter(x=self.x, y=self.y, mode=self.marker_type))

    def plot(self):
        self.fig.show()

    def addLabels(self, xlabel, ylabel):
        self.fig.update_layout(xaxis_title=xlabel, yaxis_title=ylabel)


class graphOpt(Meta):
    """

    """
    font = dict(family="Courier New, monospace", size=14, color="Black")

    def plot(self):
        if self.type == "parity":
            data_dict = {"scatter": [self.x, self.y, "Actual vs Predicted"], "parity": [self.y, self.y, "y=x line"]}
            for key in data_dict:
                val = data_dict[key]
                self.fig.add_trace(go.Scatter(x=val[0], y=val[1], mode='markers', name=val[2]))

            self.fig.update_layout(xaxis_title="Predicted", yaxis_title="Actual", font=self.font)

        if self.type == 'residual':
            self.fig.add_trace(go.Scatter(x=self.x, y=self.y, mode='markers', name='Residual plot'))

            self.fig.update_layout(xaxis_title="Predicted", yaxis_title="Residuals", font=self.font)
