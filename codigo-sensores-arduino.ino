const int TriggerPin = 9;  // Pin conectado a Trig
const int EchoPin = 10;    // Pin conectado a Echo

long duration;
int distance;
const int Distancia_Vacia = 13;  // Distancia medida cuando el dispensador está vacío (en cm)
const int Distancia_Llena = 3;   // Distancia medida cuando el dispensador está lleno (en cm)
const int CapacidadMaxima = 500; // Capacidad máxima del dispensador (en ml)

// Definir umbrales (en ml)
const int UmbralAlerta = 250;    // Nivel óptimo por debajo del cual se da una alerta
const int UmbralCritico = 50;    // Nivel crítico que requiere acción inmediata

void setup() {
  pinMode(TriggerPin, OUTPUT);
  pinMode(EchoPin, INPUT);
  Serial.begin(9600); // Iniciar conexión serial con Raspberry Pi 5
}

void loop() {
  // Limpiar el pin Trigger
  digitalWrite(TriggerPin, LOW);
  delayMicroseconds(2);

  // Enviar un pulso de 10 microsegundos en el TriggerPin
  digitalWrite(TriggerPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(TriggerPin, LOW);

  // Leer la duración del pulso en el EchoPin
  duration = pulseIn(EchoPin, HIGH);

  // Calcular la distancia (duración / 2) * velocidad del sonido (34300 cm/s)
  distance = duration * 0.034 / 2;

  // Asegurarse que la lectura esté dentro del rango válido
  if (distance >= Distancia_Llena && distance <= Distancia_Vacia) {
    // Calcular el volumen de jabón restante en ml
    int volumen_jabon = ((Distancia_Vacia - distance) * CapacidadMaxima) / (Distancia_Vacia - Distancia_Llena);

    // Enviar datos a la Raspberry Pi 5
    Serial.print("Volumen:");
    Serial.println(volumen_jabon);

    // Verificar los umbrales y generar alertas
    if (volumen_jabon <= UmbralCritico) {
      Serial.println("ALERTA CRÍTICA: El nivel de jabón es muy bajo. ¡Reponer inmediatamente!");
    } else if (volumen_jabon <= UmbralAlerta) {
      Serial.println("ALERTA: El nivel de jabón está por debajo del nivel óptimo.");
    }
  } else {
    Serial.println("Lectura fuera de rango");
  }

  delay(1000); // Esperar un segundo antes de la siguiente medición
}
