# Convertir archivos de txt a fasta

with open("data/5_dna_sequences.txt", "r") as dnaseq, open("results/5_dna_sequences_result.fa","w") as dnaseq_fa: # Abriendo el archivo txt y generando un nuevo archivo en results

    for line in dnaseq:
        # Obtenemos ID y secuencias
        columns = line.strip("\t").split()
        id_seq = columns[0]
        seq = columns[1].upper()

        # Imprimimos en el nuevo archivo
        dnaseq_fa.write(f"> {id_seq}\n{seq}\n")

    print("\nArchivo FASTA generado.\n") #Se genera el archivo en FASTA