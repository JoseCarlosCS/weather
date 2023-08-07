from django.shortcuts import render
from .windroseplot import myplot
from .requestinfo import clean_data





# Create your views here.
def main(request):

    # Funcion que requestea la informacion

    try:
        data = clean_data()

    except:
        return render(request, "error.html")

    # Hacer grafica de rosa de los vientos
    try:
        graphic = myplot()
    except:
        return render(request, "error.html")
    
    
    return render(request, "data.html", {'graphic':graphic, 'current': data[0], 'future': data[1]})




