from django.shortcuts import render
from .windroseplot import myplot
from .requestinfo import clean_data





# Create your views here.
def main(request):

    # Funcion que requestea la informacion de current weather y forecasting
    try:
        data = clean_data()
    except:
        return render(request, "error.html")

    # Funcion que hace grafica de rosa de los vientos
    try:
        graphic = myplot(data[0]['wind_dir_degrees'], data[0]['wind_kph'])
    except:
        return render(request, "error.html")
        
    return render(request, "data.html", {'graphic':graphic, 'current': data[0], 'future': data[1]})




