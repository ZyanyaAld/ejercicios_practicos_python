# Extraer los primeros tres nucleótidos de cada secuencia dada

#Solicitamos las secuencias
secuencias = input ("Dame secuancias separadas por coma ").upper().split(",")

# Separamos las primeras 3 letras 
codones_inicio= [secuencia.strip()[:3] for secuencia in secuencias]

# Imprimimos las letras guardadas
print(codones_inicio)