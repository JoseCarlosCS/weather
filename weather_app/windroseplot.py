import numpy as np
from matplotlib import pyplot as plt
import matplotlib.cm as cm
from math import pi
from windrose import WindroseAxes
from io import BytesIO
import base64


def myplot():

    ax = WindroseAxes.from_ax()
    ax = ax.bar([175.0], [2.0], normed=True, opening=0.5, edgecolor='white')
    ax = plt.legend()
    buffer = BytesIO()
    ax = plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    buffer.close()

    graphic = base64.b64encode(image_png)
    graphic = graphic.decode('utf-8')  

    return graphic