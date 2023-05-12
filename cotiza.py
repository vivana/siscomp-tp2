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
                     + 'source=crypto'  #+ '&places=6'
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
#print('BASE: ' + str(BTC_USD))
#print('TASA: '+ str(USD_ARS))
#print('ejecutado en py: ' + str(BTC_USD*USD_ARS) )

#print('llamado desde c: '+ str(convertir(BTC_USD, USD_ARS)))



# res = requests.get('https://api.exchangerate.host/latest?places=8&source=crypto&base=USD&symbols=USD,EUR,ARS,BTC,BUSD')
# data = res.json()

# print(json.dumps(res.json(), indent=4))
# print('1 USD = ' + str(res.json()['rates']['BTC']) + ' BITCOIN')
# print('1 USD = ' + str(res.json()['rates']['BUSD']) + ' BNB')

# res = requests.get('https://api.exchangerate.host/latest?places=8&source=crypto&base=BTC&symbols=USD,EUR,ARS,BTC,BUSD')
# data = res.json()

# print(json.dumps(res.json(), indent=4))
# print('1 BTC = ' + str(res.json()['rates']['USD']) + ' USD')
# print('1 BTC = ' + str(res.json()['rates']['BUSD']) + ' BUSD')

# res = requests.get('https://api.exchangerate.host/latest?places=8&source=crypto&base=BUSD&symbols=USD,EUR,ARS,BTC,BUSD')
# data = res.json()

# print(json.dumps(res.json(), indent=4))
# print('1 BUSD = ' + str(res.json()['rates']['USD']) + ' USD')
# print('1 BTC = ' + str(res.json()['rates']['BUSD']) + ' BUSD')


# # res = requests.get('https://openexchangerates.org/api/latest.json?places=8&app_id=b37be17f100e4ab1bda9034eb87e3db4&base=BTC&show_alternative=1&symbols=USD,EUR,ARS,BTC,ETH')
# # print(json.dumps(res.json(), indent=4))
# # print(1/res.json()['rates']['BTC'])
