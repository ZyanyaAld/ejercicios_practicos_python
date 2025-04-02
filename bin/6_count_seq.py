# Contar numero de secuencias en un archivo FASTA

with open("data/6_secuencias.fa") as seqfa: #Abrimos el archivo que se encuentra en la carpeta data
    
    #Hacemos la cuenta de las lineas
    counts = len([line.strip() for line in seqfa if line.strip().startswith(">")])
    
    #Imprimimos en pantalla el resultado
    print(f"\nEl archivo FASTA tiene {counts} secuencias.\n") 