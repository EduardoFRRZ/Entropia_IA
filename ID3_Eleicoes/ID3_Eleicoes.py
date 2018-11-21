from math import log2
import csv

#############################################################################################################################################################

# Bolsonaro - Haddad - Ciro Gomes - Alckmin #

entropiaGeral = - (38/55) * log2(38/55) - (6/55) * log2(6/55) - (10/55) * log2(10/55) - (1/55) * log2(1/55)
print("Entropia geral = %0.3f\n" %(entropiaGeral))

#############################################################################################################################################################

## * ENTROPIA ESTADO EM QUE VOTOU * ##

estadoSC = - (36/53) * log2(36/53) - (6/53) * log2(6/53) - (10/53) * log2(10/53) - (1/53) * log2(1/53)
print("Entropia estado SC = %0.3f\n" %(estadoSC))

estadoRS = - (2/2) * log2(2/2)
print("Entropia estado RS = %0.3f\n" %(estadoRS))

#############################################################################################################################################################

## * ENTROPIA TRABALHA * ##

trabalhaSim = - (30/43) * log2(30/43) - (6/43) * log2(6/43) - (6/43) * log2(6/43) - (1/43) * log2(1/43)
print("Entropia trabalha Sim = %0.3f\n" %(trabalhaSim))

trabalhaNao = - (8/12) * log2(8/12) - (4/12) * log2(4/12)
print("Entropia trabalha Nao = %0.3f\n" %(trabalhaNao))

#############################################################################################################################################################

## * ENTROPIA ESTUDANTE UNOESC CHAPECÓ * ##

estudanteUnoesc = - (36/52) * log2(36/52) - (5/52) * log2(5/52) - (10/52) * log2(10/52) - (1/52) * log2(1/52)
print("Entropia estuda na UNOESC = %0.3f\n" %(estudanteUnoesc))

naoEstudanteUnoesc = - (2/3) * log2(2/3) - (1/3) * log2(1/3)
print("Entropia não estuda na UNOESC = %0.3f\n" %(naoEstudanteUnoesc))

#############################################################################################################################################################

## * ENTROPIA ESTUDANTE UNOESC CHAPECÓ * ##

idadeMenor_30 = (34/51) * log2(34/51) - (6/51) * log2(6/51) - (10/51) * log2(10/51) - (1/51) * log2(1/51)
print("Entropia idade >30 = %0.3f\n" %(idadeMenor_30))

idadeMaiorIgual_30 = (4/4) * log2(4/4)
print("Entropia idade <=30 = %0.3f\n" %(idadeMaiorIgual_30))

#############################################################################################################################################################

## * GANHOS * ##

ganhoEstado = entropiaGeral - (53/55) * estadoSC - (2/55) * estadoRS
ganhoTrabalho = entropiaGeral - (43/55) * trabalhaSim - (12/55) * trabalhaNao
ganhoEstudanteUnoesc = entropiaGeral - (52/55) * estudanteUnoesc - (3/55) * naoEstudanteUnoesc
ganhoIdade = entropiaGeral - (51/55) * idadeMenor_30 - (4/55) * idadeMaiorIgual_30

print("Ganho estado = %0.3f\n" %(ganhoEstado))
print("Ganho trabalho = %0.3f\n" %(ganhoTrabalho))
print("Ganho estudante = %0.3f\n" %(ganhoEstudanteUnoesc))
print("Ganho idade = %0.3f\n" %(ganhoIdade)) # IDADE É A RAIZ #

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# * ENTROPIA GERAL IDADE <=30 * #

entropiaGeralIdadeMaiorIgual_30 = - (4/4) * log2(4/4)
print("Entropia geral idade <=30 = %0.3f\n" %(entropiaGeralIdadeMaiorIgual_30))

#############################################################################################################################################################

# * ENTROPIA IDADE <=30 ESTUDANTE * #

idadeMaiorIgual_30_EstudaUnoesc = - (3/3) * log2(3/3)
print("Entropia idade <=30 estuda UNOESC = %0.3f\n" %(idadeMaiorIgual_30_EstudaUnoesc))

idadeMaiorIgual_30_NaoEstudaUnoesc = - (1/1) * log2(1/1)
print("Entropia idade <=30 nao estuda UNOESC = %0.3f\n" %(idadeMaiorIgual_30_NaoEstudaUnoesc))

#############################################################################################################################################################

# * ENTROPIA IDADE <=30 TRABALHA * #

idadeMaiorIgual_30_Trabalha = - (3/3) * log2(3/3)
print("Entropia idade <=30 trabalha = %0.3f\n" %(idadeMaiorIgual_30_Trabalha))

idadeMaiorIgual_30_NaoTrabalha = - (1/1) * log2(1/1)
print("Entropia idade <=30 trabalha = %0.3f\n" %(idadeMaiorIgual_30_NaoTrabalha))

#############################################################################################################################################################

# * ENTROPIA IDADE <=30 ESTADO * #

idadeMaiorIgual_30_EtadoSC = - (3/3) * log2(3/3)
print("Entropia idade <=30 estado SC = %0.3f\n" %(idadeMaiorIgual_30_EtadoSC))

idadeMaiorIgual_30_EtadoRS = - (1/1) * log2(1/1)
print("Entropia idade <=30 estado RS = %0.3f\n" %(idadeMaiorIgual_30_EtadoRS))

#############################################################################################################################################################

## * GANHOS * ##

ganhoIdadeMaiorIgual_30_Estudante = entropiaGeralIdadeMaiorIgual_30 - (3/4) * idadeMaiorIgual_30_EstudaUnoesc - (1/4) * idadeMaiorIgual_30_NaoEstudaUnoesc
ganhoIdadeMaiorIgual_30_Trabalha = entropiaGeralIdadeMaiorIgual_30 - (3/4) * idadeMaiorIgual_30_Trabalha - (1/4) * idadeMaiorIgual_30_NaoTrabalha
ganhoIdadeMaiorIgual_30_Estado = entropiaGeralIdadeMaiorIgual_30 - (3/4) * idadeMaiorIgual_30_EtadoSC - (1/4) * idadeMaiorIgual_30_EtadoRS

print("Ganho idade <=30 Estudante = %0.3f\n" %(ganhoIdadeMaiorIgual_30_Estudante))
print("Ganho idade <=30 trabalha = %0.3f\n" %(ganhoIdadeMaiorIgual_30_Trabalha))
print("Ganho idade <=30 estado = %0.3f\n" %(ganhoIdadeMaiorIgual_30_Estado))

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# * ENTROPIA GERAL IDADE >30 * #

entropiaGeralIdadeMenor_30 = - (34/51) * log2(34/51) - (6/51) * log2(6/51) - (10/51) * log2(10/51) - (1/51) * log2(1/51)
print("Entropia geral idade >30 = %0.3f\n" %(entropiaGeralIdadeMenor_30))

#############################################################################################################################################################

# * ENTROPIA IDADE >30 ESTUDANTE * #

idadeMenor_30_EstudaUnoesc = - (33/49) * log2(33/49) - (5/49) * log2(5/49) - (10/49) * log2(10/49) - (1/49) * log2(1/49)
print("Entropia idade >30 estuda UNOESC = %0.3f\n" %(idadeMenor_30_EstudaUnoesc))

idadeMenor_30_NaoEstudaUnoesc = - (1/2) * log2(1/2) - (1/2) * log2(1/2)
print("Entropia idade >30 nao estuda UNOESC = %0.3f\n" %(idadeMenor_30_NaoEstudaUnoesc))

#############################################################################################################################################################

# * ENTROPIA IDADE >30 TRABALHA * #

idadeMenor_30_Trabalha = - (27/40) * log2(27/40) - (6/40) * log2(6/40) - (6/40) * log2(6/40) - (1/40) * log2(1/40)
print("Entropia idade >30 trabalha = %0.3f\n" %(idadeMenor_30_Trabalha))

idadeMenor_30_NaoTrabalha  = - (7/11) * log2(7/11) - (4/11) * log2(4/11)
print("Entropia idade >30 nao trabalha = %0.3f\n" %(idadeMenor_30_NaoTrabalha))

#############################################################################################################################################################

# * ENTROPIA IDADE >30 ESTADO * #

idadeMenor_30_EtadoSC = - (33/50) * log2(33/50) - (6/50) * log2(6/50) - (10/50) * log2(10/50) - (1/50) * log2(1/50)
print("Entropia idade >30 estado SC = %0.3f\n" %(idadeMenor_30_EtadoSC))

idadeMenor_30_EtadoRS  = - (1/1) * log2(1/1)
print("Entropia idade >30 estado RS = %0.3f\n" %(idadeMenor_30_EtadoRS))

#############################################################################################################################################################

## * GANHOS * ##

ganhoIdadeMenor_30_Estudante = entropiaGeralIdadeMenor_30 - (49/51) * idadeMenor_30_EstudaUnoesc - (2/51) * idadeMenor_30_NaoEstudaUnoesc
ganhoIdadeMenor_30_Trabalha = entropiaGeralIdadeMenor_30 - (40/51) * idadeMenor_30_Trabalha - (11/51) * idadeMenor_30_NaoTrabalha
ganhoIdadeMenor_30_Estado = entropiaGeralIdadeMenor_30 - (50/51) * idadeMenor_30_EtadoSC - (1/51) * idadeMenor_30_EtadoRS

print("Ganho idade >30 Estudante = %0.3f\n" %(ganhoIdadeMenor_30_Estudante))
print("Ganho idade >30 trabalha = %0.3f\n" %(ganhoIdadeMenor_30_Trabalha))
print("Ganho idade >30 estado = %0.3f\n" %(ganhoIdadeMenor_30_Estado))

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# * ENTROPIA GERAL IDADE >30 TRABALHA * #

entropiaGeralIdadeMenor_30_trabalha = - (27/40) * log2(27/40) - (6/40) * log2(6/40) - (6/40) * log2(6/40) - (1/40) * log2(1/40)
print("Entropia geral idade >30 trabalha = %0.3f\n" %(entropiaGeralIdadeMenor_30_trabalha))

#############################################################################################################################################################

# * ENTROPIA IDADE >30 TRABALHA ESTUDANTE * #

idadeMenor_30_TrabalhaEstudante = - (26/38) * log2(26/38) - (5/38) * log2(5/38) - (6/38) * log2(6/38) - (1/38) * log2(1/38)
print("Entropia idade >30 trabalha estudante = %0.3f\n" %(idadeMenor_30_TrabalhaEstudante))

idadeMenor_30_TrabalhaNaoEstudante = - (1/2) * log2(1/2) - (1/2) * log2(1/2)
print("Entropia idade >30 trabalha estudante = %0.3f\n" %(idadeMenor_30_TrabalhaNaoEstudante))

#############################################################################################################################################################

# * ENTROPIA IDADE >30 TRABALHA ESTADO * #

idadeMenor_30_TrabalhaEstadoSC = - (27/40) * log2(27/40) - (6/40) * log2(6/40) - (6/40) * log2(6/40) - (1/40) * log2(1/40)
print("Entropia idade >30 trabalha estado SC = %0.3f\n" %(idadeMenor_30_TrabalhaEstadoSC))

idadeMenor_30_TrabalhaEstadoRS = 0
print("Entropia idade >30 trabalha estado RS = %0.3f\n" %(idadeMenor_30_TrabalhaEstadoRS))

#############################################################################################################################################################

## * GANHOS * ##

ganhoIdadeMenor_30_TrabalhoEstudante = entropiaGeralIdadeMenor_30_trabalha - (38/40) * idadeMenor_30_TrabalhaEstudante - (2/40) * idadeMenor_30_TrabalhaNaoEstudante
ganhoIdadeMenor_30_TrabalhoEstado = entropiaGeralIdadeMenor_30_trabalha - (40/40) * idadeMenor_30_TrabalhaEstadoSC

print("Ganho idade >30 trabalha estudante = %0.3f\n" %(ganhoIdadeMenor_30_TrabalhoEstudante))
print("Ganho idade >30 trabalha estado = %0.3f\n" %(ganhoIdadeMenor_30_TrabalhoEstado))

#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

# * ENTROPIA GERAL IDADE >30 NÃO TRABALHA * #

entropiaGeralIdadeMenor_30_Naotrabalha = - (7/11) * log2(7/11) - (4/11) * log2(4/11)
print("Entropia geral idade >30 nao trabalha = %0.3f\n" %(entropiaGeralIdadeMenor_30_Naotrabalha))

#############################################################################################################################################################

# * ENTROPIA IDADE >30 NÃO TRABALHA ESTUDANTE * #

#idadeMenor_30_NaoTrabalhaEstudante = - (7/11) * log2(7/11) - (4/11) * log2(4/11) 
#print("Entropia idade >30 nao trabalha estudante = %0.3f\n" %(idadeMenor_30_NaoTrabalhaEstudante))

#idadeMenor_30_NaoTrabalhaNaoEstudante = 0
#print("Entropia idade >30 nao trabalha nao estudante = %0.3f\n" %(idadeMenor_30_NaoTrabalhaNaoEstudante))

#############################################################################################################################################################

# * ENTROPIA IDADE >30 NÃO TRABALHA ESTADO * #

idadeMenor_30_NaoTrabalhaEstadoSC = - (6/10) * log2(6/10) - (4/10) * log2(4/10)
print("Entropia idade >30 Nao trabalha estado SC = %0.3f\n" %(idadeMenor_30_NaoTrabalhaEstadoSC))

idadeMenor_30_NaoTrabalhaEstadoRS = - (1/1) * log2(1/1)
print("Entropia idade >30 Nao trabalha estado RS = %0.3f\n" %(idadeMenor_30_NaoTrabalhaEstadoRS))

#############################################################################################################################################################

## * GANHOS * ##

#ganhoIdadeMenor_30_NaoTrabalhoEstudante = entropiaGeralIdadeMenor_30_Naotrabalha - (11/11) * idadeMenor_30_NaoTrabalhaEstudante
ganhoIdadeMenor_30_NaoTrabalhoEstado = entropiaGeralIdadeMenor_30_Naotrabalha - (10/11) * idadeMenor_30_NaoTrabalhaEstadoSC - (1/11) * idadeMenor_30_NaoTrabalhaEstadoRS

#print("Ganho idade >30 nao trabalha estudante = %0.3f\n" %(ganhoIdadeMenor_30_NaoTrabalhoEstudante))
print("Ganho idade >30 nao trabalha estado = %0.3f\n" %(ganhoIdadeMenor_30_NaoTrabalhoEstado))

#############################################################################################################################################################
#############################################################################################################################################################
#################################################################### * FIM DA ENTROPIA * ####################################################################
#############################################################################################################################################################
#############################################################################################################################################################
#############################################################################################################################################################

print("ESQUEMA ARVORE\n")

print ("0 IDADE [<= 30]")
print ("0 IDADE [> 30]\n")

print ("1 BOLSONARO [<= 30]")
print ("1 TRABALHA [ > 30, SIM ]")
print ("1 TRABALHA [ > 30, NAO]\n")

print ("2 ESTUDA [ > 30, SIM, SIM ]")
print ("2 ESTUDA [ > 30, SIM, NAO ]")
print ("2 ESTADO [ > 30, NAO, SC ]")
print ("2 ESTADO [ > 30, NAO, RS ]\n")

print ("3 BOLSONARO [ > 30, SIM, SIM ]")
print ("3 BOLSONARO [ > 30, SIM, NAO ]")
print ("3 BOLSONARO [ > 30, NAO, SC ]")
print ("3 BOLSONARO [ > 30, NAO, RS ]\n")

def main():
	#BaseValidar = list(readCSV('BaseValidar.csv'))
	BaseValidar = open("BaseValidar.csv").read().replace(' ', '').splitlines()
	print(BaseValidar, "\n\n")

	for x in BaseValidar:
		dados = x.split(';')
		#n_colunas = (len(dados))
		#for y in n_colunas:
		if dados[0] == "<= 30":
			print("BOLSONARO")
			check_candidato = "JairBolsonaro"
		else:
			if dados[1] == "sim":
				if dados[2] == "sim":
					print("BOLSONARO")
					check_candidato = "JairBolsonaro"
				else:
					print("BOLSONARO")
			else:
				if (dados[3] == "SC") or (dados[3] == "sc"):
					print("BOLSONARO")
					check_candidato = "JairBolsonaro"
				else:
					print("BOLSONARO")
					check_candidato = "JairBolsonaro"
		if(check_candidato == dados[4]):
			print("ID3 acertou\n\n")
		else:
			print("ID3 errou")
			print("A pessoa tinha votado em %s\n\n" %(dados[4]))
			
main()