# Copyright 2017-2020 Spotify AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# TODO: Add support for the format parameter.
from chartify import Chart as ChartifyChart
from bokeh.io import show
from bokeh.plotting import figure as BokehFigure
from typing import Iterable


class ChartGrid:
    """Collection of chartify.Chart objects

    Properties
        - .charts: List of chartify Charts.
        - .show(): Render all the charts.
    """

    def __init__(self, charts: Iterable = None):
        if charts is None:
            charts = []
        self.charts = charts

    def show(self, format="html"):
        for chart in self.charts:
            if type(chart) == ChartifyChart:
                chart.show(format=format)
            elif type(chart) == BokehFigure:
                show(chart)
            else:
                print("Unsupported chart type: ", type(chart))
