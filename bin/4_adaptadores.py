# Eliminar adaptadores de secuencias

with open("data/4_input_adapters.txt") as input_file, open("results/4_no_input_adapters_result.txt","w") as no_adapt:  # Se abre los documentos en sus respectivas carpetas
    
    for line in input_file:

        # Retiro de los adaptadores
        new_line = line.strip()[14:]

        # Impresión en el nuevo archivo
        print(new_line,file=no_adapt,end="\n")
    
    print("\nGeneración del archivo: exitosa.\n") # Creacion de archivo txt