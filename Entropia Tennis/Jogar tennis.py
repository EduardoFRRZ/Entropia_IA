from math import log2

#############################################################################################################################################################

entropiaGeral = - (9/14) * log2(9/14) - (5/14) * log2(5/14)
print("Entropia geral = %0.3f\n" %(entropiaGeral))

#############################################################################################################################################################

## * ENTROPIA VENTO * ##

ventoForte = - (3/6) * log2(3/6) - (3/6) * log2(3/6)
print("Entropia vento forte = %0.3f\n" %(ventoForte))


ventoFraco = - (6/8) * log2(6/8) - (2/8) * log2(2/8)
print("Entropia vento fraco = %0.3f\n" %(ventoFraco))

#############################################################################################################################################################

## * ENTROPIA HUMIDADE * ##

humidadeAlta = - (3/7) * log2(3/7) - (4/7) * log2(4/7)
print("Entropia humidade alta = %0.3f\n" %(humidadeAlta))


humidadeNormal = - (6/7) * log2(6/7) - (1/7) * log2(1/7)
print("Entropia humidade normal = %0.3f\n" %(humidadeNormal))


#############################################################################################################################################################

## * ENTROPIA TEMPERATURA * ##

temperaturaQuente = - (2/4) * log2(2/4) - (2/4) * log2(2/4)
print("Entropia temperatura quente = %0.3f\n" %(temperaturaQuente))

temperaturaModerada = - (4/6) * log2(4/6) - (2/6) * log2(2/6)
print("Entropia temperatura moderada = %0.3f\n" %(temperaturaModerada))

temperaturaFresca = - (3/4) * log2(3/4) - (1/4) * log2(1/4)
print("Entropia temperatura fresca = %0.3f\n" %(temperaturaFresca))

#############################################################################################################################################################

## * ENTROPIA PERSPECTIVA * ##

perspectivaEnsolarado = - (2/5) * log2(2/5) - (3/5) * log2(3/5)
print("Entropia perspectiva ensolarado = %0.3f\n" %(perspectivaEnsolarado))

perspectivaNublado = - (4/4) * log2(4/4)
print("Entropia perspectiva nublado = %0.3f\n" %(perspectivaNublado))

perspectivaChuvoso = - (3/5) * log2(3/5) - (2/5) * log2(2/5)
print("Entropia perspectiva chuvoso = %0.3f\n" %(perspectivaChuvoso))

#############################################################################################################################################################

## * GANHOS * ##

ganhoVento = entropiaGeral - (8/14) * ventoFraco - (6/14) * ventoForte
ganhoHumidade = entropiaGeral - (7/14) * humidadeAlta - (7/14) * humidadeNormal
ganhoTemperatura = entropiaGeral - (4/14) * temperaturaQuente - (6/14) * temperaturaModerada - (4/14) * temperaturaFresca
ganhoPerspectiva = entropiaGeral - (5/14) * perspectivaEnsolarado - (4/14) * perspectivaNublado - (5/14) * perspectivaChuvoso

print("Ganho vento = %0.3f\n" %(ganhoVento))
print("Ganho humidade = %0.3f\n" %(ganhoHumidade))
print("Ganho temperatura = %0.3f\n" %(ganhoTemperatura))
print("Ganho perspectiva = %0.3f\n" %(ganhoPerspectiva))

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

entropiaGerealEnsolarado = - (2/5) * log2(2/5) - (3/5) * log2(3/5)
print("Entropia geral ensolarado = %0.3f\n" %(entropiaGerealEnsolarado))

#############################################################################################################################################################

## * ENTROPIA PERSPECTIVA ENSOLARADO TEMPERATURA * ##

ensolaradoTemperaturaFresco = - (1/1) * log2(1/1)
print("Entropia ensolarado temperatura fresco = %0.3f\n" %(ensolaradoTemperaturaFresco))

ensolaradoTemperaturaModerada = - (1/2) * log2(1/2) - (1/2) * log2(1/2)
print("Entropia ensolarado temperatura moderada = %0.3f\n" %(ensolaradoTemperaturaModerada))

ensolaradoTemperaturaQuente = - (2/2) * log2(2/2)
print("Entropia ensolarado temperatura quente = %0.3f\n" %(ensolaradoTemperaturaQuente))

#############################################################################################################################################################

## * ENTROPIA PERSPECTIVA ENSOLARADO UMIDADE * ##

ensolaradoUmidadeAlta = - (3/3) * log2(3/3)
print("Entropia ensolarado umidade alta = %0.3f\n" %(ensolaradoUmidadeAlta))

ensolaradoUmidadeNormal = - (2/2) * log2(2/2)
print("Entropia ensolarado umidade normal = %0.3f\n" %(ensolaradoUmidadeNormal))

#############################################################################################################################################################

## * ENTROPIA PERSPECTIVA ENSOLARADO VENTO * ##

ensolaradoVentoForte = - (1/2) * log2(1/2) - (1/2) * log2(1/2)
print("Entropia ensolarado vento forte = %0.3f\n" %(ensolaradoVentoForte))

ensolaradoVentoFraco = - (1/3) * log2(1/3) - (2/3) * log2(2/3)
print("Entropia ensolarado vento fraco = %0.3f\n" %(ensolaradoVentoFraco))

#############################################################################################################################################################

## * PERSPECTIVA GANHOS * ##

ganhoPespectivaEnsolaradoTemperatura = entropiaGerealEnsolarado - (1/5) * ensolaradoTemperaturaFresco - (2/5) * ensolaradoTemperaturaModerada - (2/5) * ensolaradoTemperaturaQuente
ganhoPespectivaEnsolaradoVento = entropiaGerealEnsolarado - (2/5) * ensolaradoVentoForte - (3/5) * ensolaradoVentoFraco
ganhoPespectivaEnsolaradoUmidade = entropiaGerealEnsolarado - (3/5) * ensolaradoUmidadeAlta - (2/5) * ensolaradoUmidadeNormal

print("Ganho perspectiva ensolarado temperatura = %0.3f\n" %(ganhoPespectivaEnsolaradoTemperatura))
print("Ganho perspectiva ensolarado umidade = %0.3f\n" %(ganhoPespectivaEnsolaradoUmidade))
print("Ganho perspectiva ensolarado vento = %0.3f\n" %(ganhoPespectivaEnsolaradoVento))

#############################################################################################################################################################

entropiaGerealChuvoso = - (2/2) * log2(2/2)
print("Entropia geral chuvoso = %0.3f\n" %(entropiaGerealChuvoso))

#############################################################################################################################################################

## * ENTROPIA PERSPECTIVA CHUVOSO TEMPERATURA * ##

chuvosoTemperaturaFresco = - (1/2) * log2(1/2) - (1/2) * log2(1/2)
print("Entropia chuvoso temperatura fresco = %0.3f\n" %(chuvosoTemperaturaFresco))

chuvosoTemperaturaModerada = - (2/3) * log2(2/3) - (1/3) * log2(1/3)
print("Entropia chuvoso temperatura moderada = %0.3f\n" %(chuvosoTemperaturaModerada))

#############################################################################################################################################################

## * ENTROPIA PERSPECTIVA CHUVOSO VENTO * ##

chuvosoVentoForte = - (2/2) * log2(2/2)
print("Entropia chuvoso vento forte = %0.3f\n" %(chuvosoVentoForte))

chuvosoVentoFraco = - (3/3) * log2(3/3)
print("Entropia chuvoso vento fraco = %0.3f\n" %(chuvosoVentoFraco))

#############################################################################################################################################################

## * PERSPECTIVA GANHOS * ##

ganhoPespectivaChuvosoTemperatura = entropiaGerealChuvoso - (3/5) * chuvosoTemperaturaModerada - (2/5) * chuvosoTemperaturaFresco
print("Ganho perspectiva chuvoso temperatura = %0.3f\n" %(ganhoPespectivaChuvosoTemperatura))

ganhoPespectivaChuvosoVento = entropiaGerealChuvoso - (3/5) * chuvosoVentoFraco - (2/5) * chuvosoVentoForte
print("Ganho perspectiva chuvoso vento = %0.3f\n" %(ganhoPespectivaChuvosoVento))