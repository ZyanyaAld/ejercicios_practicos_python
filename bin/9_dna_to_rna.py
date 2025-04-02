# Transformar secuencias de ADN en ARN

# Solicitamos las secuencias
secuencias = input ("Dame secuancias separadas por coma ").upper().split(",")

# Reemplazamos las T por U
secuencias_arn = [secuencia.replace("T", "U") for secuencia in secuencias] 

# Regresamos las secuencias
print(secuencias_arn)