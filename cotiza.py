import requests
import ctypes
import json

# Cargamos la libreria 
libconversorc = ctypes.CDLL('./libconversorc.so')

# Definimos los tipos de los argumentos de la funcion convertir
libconversorc.convertir_asm.argtypes = (ctypes.c_float,ctypes.c_float)

# Definimos el tipo del retorno de la funcion convertir
libconversorc.convertir_asm.restype = ctypes.c_double


# Creamos nuestra funcion factorial en Python
# hace de Wrapper para llamar a la funcion de C
def convertir(base, tasa ):
    return libconversorc.convertir_asm(base,tasa)  



def tasa_de_cambio(base, symbol):
  res = requests.get('https://api.exchangerate.host/latest?'  
                     + 'source=crypto'  
                     + '&base=' + base 
                     + '&symbols=' + symbol)
  data = res.json()

  return float(data['rates'][symbol])



BTC_USD = tasa_de_cambio('BTC','USD')
BUSD_USD = tasa_de_cambio('BUSD','USD')
USD_ARS = tasa_de_cambio('USD','ARS')
USD_EUR = tasa_de_cambio('USD','EUR')
ADA_USD = tasa_de_cambio('ADA','USD')

print('Valor de Bitcoin (BTC) = ' 
+ str(BTC_USD) + ' USD' + ' | ' 
+ str(convertir(BTC_USD, USD_ARS))+ ' ARS' + ' | '
+ str(convertir(BTC_USD, USD_EUR))+ ' EUR')

print('Valor de Binance (BNB) = ' 
+ str(BUSD_USD) + ' USD' + ' | ' 
+ str(convertir(BUSD_USD, USD_ARS))+ ' ARS' + ' | '
+ str(convertir(BUSD_USD, USD_EUR))+ ' EUR')

print('Valor de Cardano (ADA) = ' 
+ str(ADA_USD) + ' USD' + ' | '
+ str(convertir(ADA_USD, USD_ARS))+ ' ARS' + ' | '
+ str(convertir(ADA_USD, USD_EUR))+ ' EUR')
