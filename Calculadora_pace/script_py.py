#crie variáveis
nome2 = input(" Favor, insira seu nome [AQUI]: ")
km2 = float(input("Favor, informe seu km total [AQUI]: "))
tempo_2 = float(input("Favor, insira tempo liquido da prova [AQUI]: "))

#divida tempo rodado pelo km total
km_total_2 = tempo_2 / km2

#transformar parte inteira em minutos
minutos_total = (int(km_total_2))

#transformar parte decimal em segundos
segundos_total = (float((km_total_2 - minutos_total)*60))

print(f"Olá, runner {nome2}, ficamos muito feliz em te ver por aqui! Seu pace "
      f" foi {minutos_total} minutos e {segundos_total:.0f} segundos. Parabéns! 👏🏻 ")


























