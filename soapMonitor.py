import serial
import time
import requests

# Configura el puerto serial
conexionArduino = serial.Serial('/dev/ttyACM0', 9600, timeout=1)  # Cambia el puerto si es necesario
time.sleep(2)  # Espera a que se establezca la conexión

# Token bot de Telegram (SoapMonitorBot)
BOT_TOKEN = "7548259457:AAGf7xNIdFipldgMNKHcA6i-L4r2H4g-lcM"

# ID grupo de Telegram (Personal-Aseo)
GROUP_ID = "-4571866446"

# URL para enviar los mensajes de alerta
url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

# Mensajes de advertencia y alerta
mensaje_advertencia = "Advertencia: El nivel de jabón está bajo."
mensaje_alerta = "Acción inmediata: ¡El nivel de jabón es crítico!"



while True:
    # Verifica si hay datos disponibles
    if conexionArduino.in_waiting > 0:
        line = conexionArduino.readline().decode('utf-8').rstrip()  # Lee una línea de datos y decodifica
        print(line)  # Muestra los datos en la terminal

        # Procesa los datos si es necesario
        if "ALERTA CRITICA" in line:
            data = {
                "chat_id": GROUP_ID,
                "text": mensaje_alerta
            }
            
            response = requests.post(url, data=data)
            print(response.status_code, response.text)

        elif "ALERTA" in line:
            data = {
                "chat_id": GROUP_ID,
                "text": mensaje_advertencia
            }
            
            response = requests.post(url, data=data)
            print(response.status_code, response.text)

    time.sleep(30)  # Espera 30 segundo antes de la siguiente lectura
