const int stepPin = 9; 
const int dirPin = 8;

long int time1 =0;
int delay1 = 200;
int count = 1;
bool dir = 1;
void setup() {
  // Sets the two pins as Outputs
  Serial.begin(9600);
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
}
void loop() {
  Serial.print(count);
  Serial.print("-Start-");
  Serial.println(delay1);
  time1 = millis();
  digitalWrite(dirPin,dir); // Enables the motor to move in a particular direction
  // Makes 200 pulses for making one full cycle rotation
  for(long int x = 0; x < 3200*7 ; x++) {
    for(long int i = 0; i < 7 ; i++){
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(1); 
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(delay1);
    }
  }
  time1 = millis() - time1;
  Serial.println(time1);
  Serial.println("end");
  delay(1000); // One second delay
  count++;
  dir = !dir;
    if(count > 20)
    {
      delay1 += 200; 
       count = 1 ;
    }
  }
