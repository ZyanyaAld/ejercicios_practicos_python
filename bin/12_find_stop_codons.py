# Encontrar secuencias que contengan un codón de parada

#Solicitamos secuencias de DNA
secuencias = input ("Dame secuancias separadas por coma ").upper().split(",")

#Indicamos las secuencias a reconocer
stop_codons = {"TAA", "TAG", "TGA"}

# Reconocemos en las secuencias dadas nuestros codones de paro
seq = [secuencia for secuencia in secuencias if any(codon in secuencia for codon in stop_codons)]

#imprimimos las secuencias que tengan las secuencias de paro
print(seq)