import serial // Importar libreria que permite la conexion serial
import time  // Importar libreria para trabajar con el tiempo

# Configuracion del puerto serial
conexionArduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # El puerto USB utilizado puede variar
time.sleep(2)  # Espera a que se establezca la conexión

while True:
    # Verifica si hay datos disponibles
    if conexionArduino.in_waiting > 0:
        line = conexionArduino.readline().decode('utf-8').rstrip()  # Lee una línea de datos y decodifica
        print(line)  # Muestra los datos en la terminal

        # Procesa los datos si es necesario
        if "ALERTA CRITICA" in line:
            print("Acción inmediata: ¡El nivel de jabón es crítico!")
        elif "ALERTA" in line:
            print("Advertencia: El nivel de jabón está bajo.")

    time.sleep(1)  # Espera 1 segundo antes de la siguiente lectura
