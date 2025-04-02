# Invertir secuencias de ADN

#Solicitamos secuencias al usuario
secuencias = input ("Dame secuancias separadas por coma ").upper().split(",")

#Invertimos la secuencia
secuencia_invertida = [secuencia[::-1] for secuencia in secuencias] 

#Imprimimos
print(secuencia_invertida)