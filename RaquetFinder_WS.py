from bs4 import BeautifulSoup
import requests
import pandas as pd

# Raquetas 100
# url = 'http://www.racquetfinder.com/?name=&manufacturer=&hsMin=100&hsMax=100&lMin=&lMax=&wMin=&wMax=&swMin=&swMax=&fMin=&fMax=&bpMin=&bpMax=&bwMin=&bwMax=&mains=&crosses=&current=N'
# Raquetas 98
# url = 'http://www.racquetfinder.com/?name=&manufacturer=&hsMin=98&hsMax=98&lMin=&lMax=&wMin=&wMax=&swMin=&swMax=&fMin=&fMax=&bpMin=&bpMax=&bwMin=&bwMax=&mains=&crosses=&current=N'
# Raquetas 97
# url = 'http://www.racquetfinder.com/?name=&manufacturer=&hsMin=97&hsMax=97&lMin=&lMax=&wMin=&wMax=&swMin=&swMax=&fMin=&fMax=&bpMin=&bpMax=&bwMin=&bwMax=&mains=&crosses=&current=N'
#  Babolat
# url = 'http://www.racquetfinder.com/?name=&manufacturer=Babolat&hsMin=&hsMax=&lMin=&lMax=&wMin=&wMax=&swMin=&swMax=&fMin=&fMax=&bpMin=&bpMax=&bwMin=&bwMax=&mains=&crosses=&currentcheckbox=ASICS&current=Y'
# Yonex
# url = 'http://www.racquetfinder.com/?name=&manufacturer=Yonex&hsMin=&hsMax=&lMin=&lMax=&wMin=&wMax=&swMin=&swMax=&fMin=&fMax=&bpMin=&bpMax=&bwMin=&bwMax=&mains=&crosses=&currentcheckbox=ASICS&current=Y'
# Head
# url = 'http://www.racquetfinder.com/?name=&manufacturer=Head&hsMin=&hsMax=&lMin=&lMax=&wMin=&wMax=&swMin=&swMax=&fMin=&fMax=&bpMin=&bpMax=&bwMin=&bwMax=&mains=&crosses=&currentcheckbox=ASICS&current=Y'
# Wilson
url = 'http://www.racquetfinder.com/?name=&manufacturer=Wilson&hsMin=&hsMax=&lMin=&lMax=&wMin=&wMax=&swMin=&swMax=&fMin=&fMax=&bpMin=&bpMax=&bwMin=&bwMax=&mains=&crosses=&currentcheckbox=ASICS&current=Y'

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
productos = soup.find_all('div', class_='product')

datos = []

for producto in productos:
    nombre = producto.find('div', class_='rac_name').text.strip()
    especificaciones = producto.find_all('div', class_='spec_col')
    especificaciones_dict = {'Nombre': nombre}
    for spec in especificaciones:
        tabla = spec.find('table')
        filas = tabla.find_all('tr')
        for fila in filas:
            th = fila.find('th').text.strip()
            td = fila.find('td').text.strip()
            especificaciones_dict[th] = td
    datos.append(especificaciones_dict)

df = pd.DataFrame(datos)
print(df)

df.to_excel('Wilson.xlsx', index=False)



