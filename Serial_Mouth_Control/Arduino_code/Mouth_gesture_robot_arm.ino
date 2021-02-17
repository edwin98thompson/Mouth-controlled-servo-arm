#include <SoftwareSerial.h>//bluetooth signal decoder library
SoftwareSerial BTserial(0, 1); //bluetooth in/out (tx/rx) assigned
#include <Servo.h>

Servo servo1;
Servo servo2;
Servo servo3;
Servo servo4;
Servo servo5;
char serialInput;
int InitAngle = 90;
int angle;

void setup() {
  // put your setup code here, to run once:
  //pinMode(pin, OUTPUT);
  //digitalWrite(pin, LOW);
  Serial.begin(9600);
  BTserial.begin(9600);
  Serial.println("Arduino is ready");
  Serial.println("Remember to select Both NL & CR in the serial monitor");

  servo1.attach(13);  // attaches the servo on pin 9 to the servo object
  servo2.attach(12);
  servo3.attach(11);
  servo4.attach(10);
  servo5.attach(9);

  servo1.write(InitAngle);
  servo2.write(0);
  servo3.write(0);
  servo4.write(InitAngle);
  servo5.write(InitAngle);
}

void loop() {
  // put your main code here, to run repeatedly:

  int angle1 = servo1.read();
  int angle2 = servo2.read();
  int angle3 = servo3.read();
  int angle4 = servo4.read();
  int angle5 = servo5.read();
  if (BTserial.available() > 0) //statement checks if serial input from bluetooth device is readable
  {
    serialInput = BTserial.read();//variable assigned to reading
    Serial.println(serialInput);//reading is prinred to monitor
    //Serial.println();

  }

  if (serialInput == '1')
  {
    angle4+=5;
    servo4.write(angle4);
    delay(10);
    serialInput = 0;
  }
  if (serialInput == '2')
  {
    angle4-=5;
    servo4.write(angle4);
    delay(10);
    serialInput = 0;
  }



}
