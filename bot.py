def copy_content(input_file, output_file):
    try:
        # Abre el archivo de entrada en modo lectura
        with open(input_file, 'r') as file_in:
            # Lee el contenido del archivo
            content = file_in.read()

        # Abre el archivo de salida en modo escritura
        with open(output_file, 'w') as file_out:
            # Escribe el contenido en el archivo de salida
            file_out.write(content)

        print(f"Contenido del archivo '{input_file}' copiado exitosamente en '{output_file}'.")
    except Exception as e:
        print(f"Error: {e}")

# Configuración de archivos
archivo_origen = "/etc/passwd"
archivo_destino = "archivo_destino.txt"

# Llama a la función para copiar el contenido
copy_content(archivo_origen, archivo_destino)
