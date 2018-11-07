from math import log2

entropiaGeral = - (9/14) * log2(9/14) - (5/14) * log2(5/14)
print("Entropia geral = %0.3f\n" %(entropiaGeral))

entropiaEnsolarado = - (2/5) * log2(2/5) - (3/5) * log2(3/5)
print("Entropia ensolarada = %0.3f\n" %(entropiaEnsolarado))

entropiaChuvoso = - (3/5) * log2(3/5) - (2/5) * log2(2/5)
print("Entropia chuvoso = %0.3f\n" %(entropiaChuvoso))

entropiaNublado = - (4/4) * log2(4/4)
print("Entropia nublado = %0.3f\n" %(entropiaNublado))

ganhoPerspectiva = 0.94 - ((5/14 * entropiaEnsolarado) + (5/14 * entropiaChuvoso) + (4/14 * entropiaNublado))
print("PERSPECTIVA = %.3f\n" %(ganhoPerspectiva))

#################################################################################################################

entropiaHumidadeAlta = - (3/7) * log2(3/7) - (4/7) * log2(4/7)
print("Entropia humidade alta = %0.3f\n" %(entropiaHumidadeAlta))

entropiaHumidadeNormal = - (6/7) * log2(6/7) - (1/7) * log2(1/7)
print("Entropia humidade normal = %0.3f\n" %(entropiaHumidadeNormal))

ganhoHumidade = 0.94 - ((7/14 * entropiaHumidadeAlta) + (7/14 * entropiaHumidadeNormal))
print("HUMIDADE = %.3f\n" %(ganhoHumidade))

#################################################################################################################

entropiaVentoForte = - (3/6) * log2(3/6) - (3/6) * log2(3/6)
print("Entropia vento forte = %0.3f\n" %(entropiaVentoForte))

entropiaVentoFraco = - (6/8) * log2(6/8) - (2/8) * log2(2/8)
print("Entropia vento fraco = %0.3f\n" %(entropiaVentoFraco))

ganhoVento = 0.94 - ((6/14 * entropiaVentoForte) + (8/14 * entropiaVentoFraco))
print("VENTO = %.3f\n" %(ganhoVento))

#################################################################################################################

entropiaTemperaturaFresca = - (3/4) * log2(3/4) - (1/4) * log2(1/4)
print("Entropia temperatura fresca = %0.3f\n" %(entropiaTemperaturaFresca))

entropiaTemperaturaQuente = - (2/4) * log2(2/4) - (2/4) * log2(2/4)
print("Entropia temperatura quente = %0.3f\n" %(entropiaTemperaturaQuente))

entropiaTemperaturaModerada = - (4/6) * log2(4/6) - (2/6) * log2(2/6)
print("Entropia temperatura moderada = %0.3f\n" %(entropiaTemperaturaModerada))

ganhoTemperatura = 0.94 - ((4/14 * entropiaTemperaturaFresca) + (6/14 * entropiaTemperaturaModerada) + (4/14 * entropiaTemperaturaQuente))
print("TEMPERATURA = %.3f\n" %(ganhoTemperatura))

#################################################################################################################
#################################################################################################################

'''ENSOLARADO'''


entropiaEnsolaradoTemperaturaQuente = - (2/2) * log2(2/2)
print("Entropia ensolarado quente = %0.3f\n" %(entropiaEnsolaradoTemperaturaQuente))

entropiaEnsolaradoTemperaturaModerado = - (1/2) * log2(1/2) - (1/2) * log2(1/2)
print("Entropia ensolarado moderado = %0.3f\n" %(entropiaEnsolaradoTemperaturaModerado))

entropiaEnsolaradoTemperaturaFresca = - (1/1) * log2(1/1)
print("Entropia ensolarado fresca = %0.3f\n" %(entropiaEnsolaradoTemperaturaFresca))

ganhoEnsolaradoTemperatura = 0.971 - ((2/5 * entropiaEnsolaradoTemperaturaQuente) + (2/5 * entropiaEnsolaradoTemperaturaModerado) + (1/5 * entropiaEnsolaradoTemperaturaFresca))
print("GANHO ENSOLARADO TEMPERATURA = %.3f\n" %(ganhoEnsolaradoTemperatura))

#################################################################################################################

entropiaEnsolaradoHumidadeAlta = - (3/3) * log2(3/3)
print("Entropia ensolarado humidade alta = %0.3f\n" %(entropiaEnsolaradoHumidadeAlta))

entropiaEnsolaradoHumidadeNormal = - (2/2) * log2(2/2)
print("Entropia ensolarado humidade normal = %0.3f\n" %(entropiaEnsolaradoHumidadeNormal))

ganhoEnsolaradoHumidade = 0.971 - ((3/5 * entropiaEnsolaradoHumidadeAlta) + (2/5 * entropiaEnsolaradoHumidadeNormal))
print("GANHO ENSOLARADO HUMIDADE = %.3f\n" %(ganhoEnsolaradoHumidade))


#################################################################################################################

entropiaEnsolaradoVentoForte = - (1/2) * log2(1/2) - (1/2) * log2(1/2)
print("Entropia ensolarado vento forte = %0.3f\n" %(entropiaEnsolaradoVentoForte))

entropiaEnsolaradoVentoFraco = - (1/3) * log2(1/3) - (2/3) * log2(2/3)
print("Entropia ensolarado vento fraco = %0.3f\n" %(entropiaEnsolaradoVentoFraco))

ganhoEnsolaradoVento = 0.971 - ((2/5 * entropiaEnsolaradoVentoForte) + (3/5 * entropiaEnsolaradoVentoFraco))
print("GANHO ENSOLARADO VENTO = %.3f\n" %(ganhoEnsolaradoVento))

##################################################################################################################
''''CHUVOSO'''

entropiaChuvosoTemperaturaModerado = - (2/3) * log2(2/3) - (1/3) * log2(1/3)
print("Entropia Chuvoso moderado = %0.3f\n" %(entropiaChuvosoTemperaturaModerado))

entropiaChuvosoTemperaturaFresca = - (1/2) * log2(1/2) - (1/2) * log2(1/2)
print("Entropia Chuvoso fresca = %0.3f\n" %(entropiaChuvosoTemperaturaFresca))

ganhoChuvosoTemperatura = 0.971 - ((2/5 * entropiaChuvosoTemperaturaModerado) + (1/5 * entropiaEnsolaradoTemperaturaFresca))
print("GANHO CHUVOSO TEMPERATURA = %.3f\n" %(ganhoChuvosoTemperatura))


################################################################################

entropiaChuvosoHumidadeAlta = - (2/2) * log2(2/2)
print("Entropia Chuvoso humidade alta = %0.3f\n" %(entropiaChuvosoHumidadeAlta))

entropiaChuvosoHumidadeNormal = - (2/3) * log2(2/3) - (1/3) * log2(1/3)
print("Entropia Chuvoso humidade normal = %0.3f\n" %(entropiaChuvosoHumidadeNormal))

ganhoChuvosoHumidade = 0.971 - ((2/5 * entropiaChuvosoHumidadeAlta) + (3/5 * entropiaChuvosoHumidadeNormal))
print("GANHO CHUVOSO HUMIDADE = %.3f\n" %(ganhoChuvosoHumidade))

##################################################################################################################


entropiaChuvosoVentoForte = - (2/2) * log2(2/2)
print("Entropia Chuvoso vento forte = %0.3f\n" %(entropiaChuvosoVentoForte))

entropiaChuvosoVentoFraco = - (3/3) * log2(3/3)
print("Entropia Chuvoso vento fraco = %0.3f\n" %(entropiaChuvosoVentoFraco))

ganhoChuvosoVento = 0.971 - ((2/5 * entropiaChuvosoVentoForte) + (3/5 * entropiaChuvosoVentoFraco))
print("GANHO CHUVOSO VENTO = %.3f\n" %(ganhoChuvosoVento))


##################################################################################################################
'''NUBLADO'''

entropiaNubladoTemperaturaQuente = - (2/2) * log2(2/2)
print("Entropia Nublado quente = %0.3f\n" %(entropiaNubladoTemperaturaQuente))

entropiaNubladoTemperaturaModerado = - (1/1) * log2(1/1)
print("Entropia Nublado moderado = %0.3f\n" %(entropiaNubladoTemperaturaModerado))

entropiaNubladoTemperaturaFresca = - (1/1) * log2(1/1)
print("Entropia Nublado fresca = %0.3f\n" %(entropiaNubladoTemperaturaFresca))

ganhoNubladoTemperatura = 0.0 - ((2/5 * entropiaNubladoTemperaturaQuente) + (2/5 * entropiaNubladoTemperaturaModerado) + (1/5 * entropiaNubladoTemperaturaFresca))
print("GANHO NUBLADO TEMPERATURA = %.3f\n" %(ganhoNubladoTemperatura))

##############################################################################33

entropiaNubladoHumidadeAlta = - (2/2) * log2(2/2)
print("Entropia Nublado humidade alta = %0.3f\n" %(entropiaNubladoHumidadeAlta))

entropiaNubladoHumidadeNormal = - (2/2) * log2(2/2)
print("Entropia Nublado humidade normal = %0.3f\n" %(entropiaNubladoHumidadeNormal))

ganhoNubladoHumidade = 0.0 - ((2/5 * entropiaNubladoHumidadeAlta) + (3/5 * entropiaNubladoHumidadeNormal))
print("GANHO NUBLADO HUMIDADE = %.3f\n" %(ganhoNubladoHumidade))

##################################################################################################################

entropiaNubladoVentoForte = - (2/2) * log2(2/2)
print("Entropia Nublado vento forte = %0.3f\n" %(entropiaNubladoVentoForte))

entropiaNubladoVentoFraco = - (2/2) * log2(2/2)
print("Entropia Nublado vento fraco = %0.3f\n" %(entropiaNubladoVentoFraco))

ganhoNubladoVento = 0.0 - ((2/5 * entropiaNubladoVentoForte) + (3/5 * entropiaNubladoVentoFraco))
print("GANHO NUBLADO VENTO = %.3f\n" %(ganhoNubladoVento))

##################################################################################################################
