# Contar nucleótidos en cada secuencia 

# Solicimos las secuencias
secuencias = input ("Dame secuancias separadas por coma ").upper().split(",")

# Hacemos la cuenta por nucleotido
nucleotides = [(secuencia.count("A"), secuencia.count("T"), secuencia.count("C"), secuencia.count("G"))  for secuencia in secuencias]

# Imprimimos las cuentas que se hicieron por nucleotidos
print(nucleotides)