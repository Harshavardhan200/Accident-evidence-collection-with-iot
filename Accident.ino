
#include <Adafruit_MPU6050.h>
#include <Adafruit_Sensor.h>
#define echoPin   ECHO_PIN_NUMBER
#define trigPin TRIG_PIN
#define smoke SMOKE_SENSOR_PIN
#define flame FLAME_SENSOR_PIN
#define vibration VIBRATION_SENSOR_PIN
long duration;
int distance, acc, smoke_sensor, vibration_sensor, flame_sensor;
Adafruit_MPU6050 mpu;
int previous = 0;
int t=0;
int diff;
void setup() 
{
  pinMode(smoke, INPUT);
  pinMode(vibration, INPUT);
  pinMode(flame, INPUT);
  Serial.begin(115200);
  pinMode(trigPin, OUTPUT);
  pinMode(echoPin, INPUT); 
  if (!mpu.begin()) {
    while (1) {
      delay(10);
    }
  }
}

void loop()
{
  sensors_event_t a, g, temp;
  mpu.getEvent(&a, &g, &temp);
int smoke_sensor = digitalRead(smoke);
int vibration_sensor = digitalRead(vibration);
int flame_sensor = digitalRead(flame);
acc = sqrt(pow(a.acceleration.x, 2) + pow(a.acceleration.y, 2) + pow(a.acceleration.z, 2));
  if(t==0){
    previous = acc;
    t++;
  }
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance = duration * 0.034 / 2;
  diff = abs(previous - acc);
  Serial.print("distance: ");
  Serial.println(distance);
  Serial.print("difference: ");
  Serial.println(diff);
  Serial.print("smoke: ");
  Serial.println(smoke_sensor);
  Serial.print("flame: ");
  Serial.println(flame_sensor);
  Serial.print("vibration: ");
  Serial.println(vibration_sensor);
  delay(1500);

  
}
