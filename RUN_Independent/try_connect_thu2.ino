
#include <string.h>


//SETTING MOTOR AND DRIVER
const int stepPin1 = 8;
const int dirPin1 = 24;
const int stepPin2 = 9;

const int dirPin2 = 26;
const int stepPin3 = 10;
const int dirPin3 = 28;



// khai báo chân ngắt động cơ
const byte interruptPin1 = 2;
const byte interruptPin2 = 3;
const byte interruptPin3 = 21;


/// chiều quay động cơ
bool dir1 = 1;
bool dir2 = 1;
bool dir3 = 1;



// định nghĩa các hằng số
#define Pi 3.14
#define pitch 2
#define fullStep 156800
#define microStep 16
#define deceleration 49

//khai báo chuỗi
  String pi_cmd;
  // khai báo các thông số của 3 máy bơm
  // pump: tên các máy bơm
  // status: trạng thái máy bơm sẽ chạy. Hút hay là đẩy
  // volume: loại xi lanh vào máy bơm
  // target: thể tích mong muốn thực hiện bơm
  int Pump1 = 0, Pump2 = 0, Pump3 = 0;
  int statusP1 = 0, statusP2 = 0, statusP3 = 0;
  int volumeP1 = 0, volumeP2 = 0, volumeP3 = 0;
  int targetP1 = 0, targetP2 = 0, targetP3 = 0;
  int flowRateP1 = 0, flowRateP2 = 0, flowRateP3 = 0;
  // khai bao thêm các thông số
  int P = 0;
  String pump;
  String volume, comboString, target, flowRate;
  byte phantach;
  byte tach;

  /// thời gian chạy của bơm
  long int time1 = 0;
  long int time2 = 0;
  long int time3 = 0;

  // counter
  long int counter1 = 0;
  long int counter2 = 0;
  long int counter3 = 0;

  long int currentCounter1 = 0;
  long int currentCounter2 = 0;
  long int currentCounter3 = 0;

  // khai báo Speed
  double speed1 = 0, speed2 = 0, speed3 = 0;

  // thời gian delay
long int delay1 = 200;
long int delay2 = 200;
long int delay3 = 200;

// khai báo bán kính của xi lanh
double radius;
// khai báo thể tích xi lanh
double V;
// khai báo diện tích đáy của các xi lanh
double S1, S2, S3;

int steps = 200;

// số bước động cơ cần chạy
long int stepRun1 ;
long int stepRun2 ;
long int stepRun3 ;


void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(stepPin1, OUTPUT);
  pinMode(dirPin1, OUTPUT);
  pinMode(stepPin2, OUTPUT);
  pinMode(dirPin2, OUTPUT);
  pinMode(stepPin3, OUTPUT);
  pinMode(dirPin3, OUTPUT);
  pinMode(interruptPin1, INPUT_PULLUP);
  pinMode(interruptPin2, INPUT_PULLUP);
  pinMode(interruptPin3, INPUT_PULLUP);
}

void loop()
{
  

  // put your main code here, to run repeatedly:
  if (Serial.available() > 1)
  {
    String informationPump = Serial.readStringUntil('\n');
    Serial.println(informationPump);
    // chuoi nhan duoc co dang 1_2_10_1000
    // 1: ky hieu cua may bom vs dong co tuong ung
    // 2: trang thai chay cua dong co(1: chi hut vao, 2: chi day ra, 3: hut vao roi day ra, 4: day ra roi hut vao )
    // 10: dung tich cua xi lanh lap vao (1,3,5,10,20,50)
    // 1000: the tich dung dich ra mong muon (100,200,...1000)
    pi_cmd = informationPump;
    //xu ly tach ky tu dau tien cua chuoi
    switch (pi_cmd.charAt(0))
    {
      case '1':
        Pump1 = 1;
        P = 1;
        Serial.println("Pump1");
        break;
      case '2':
        Pump2 = 2;
        P = 2;
        Serial.println("Pump2");
        break;
      case '3':
        Pump3 = 3;
        P = 3;
        Serial.println("Pump2");
        break;
      default:
        //pump = '0';
        P = 0;
    }
    Serial.print("P:");
    Serial.println(P);
    // xoa bo 2 ky tu
    pi_cmd.remove(0, 2);
    pi_cmd = pi_cmd;
    // xu ly trang thai may bom tu chuoi
    if (P == 1)
    {
      switch (pi_cmd.charAt(0))
      {
        case '1':
          statusP1 = 1;
          Serial.println("Infusion ONLY");
          break;
        case '2':
          statusP1 = 2;
          Serial.println("Withdraw ONLY");
          break;
        case '3':
          statusP1 = 3;
          Serial.println("Infusion/Withdraw");
          break;
        case '4':
          statusP1 = 4;
          Serial.println("Withdraw/Infusion");
          break;
        default:
          statusP1 = 0;
      }
      Serial.println(statusP1);
      Serial.println(pi_cmd);
      // xoa di cac ky tu
      pi_cmd.remove(0, 2);
      pi_cmd = pi_cmd;
      for (int i = 0; i < pi_cmd.length(); i++)
      {
        if (pi_cmd.charAt(i) == ':')
        {
          phantach = i; //tim vi tri cua dau "_"
        }
      }
      // phan tach the tich vao va ra mong muon
      volume = pi_cmd;
      comboString = pi_cmd;
      volume.remove(phantach);
      comboString.remove(0, phantach + 1);
      pi_cmd = comboString;
      for (int i = 0; i < pi_cmd.length(); i++)
      {

        if (pi_cmd.charAt(i) == '_')
        {
          tach = i; //tim vi tri cua dau "_"
        }
      }
      target = pi_cmd;
      flowRate = pi_cmd;
      target.remove(tach);
      //Serial.println(pi_cmd);
      //phantach[0] = 0;
      flowRate.remove(0, tach + 1);
      volumeP1 = volume.toInt();
      targetP1 = target.toInt();
      flowRateP1 = flowRate.toInt();
      Serial.print("volume and target:");
      Serial.println(volumeP1);
      Serial.println(targetP1);
      Serial.print("flowRate:");
      Serial.println(flowRateP1);
    }
    else if (P == 2)
    {
      switch (pi_cmd.charAt(0))
      {
        case '1':
          statusP2 = 1;
          Serial.println("Infusion ONLY");
          break;
        case '2':
          statusP2 = 2;
          Serial.println("Withdraw ONLY");
          break;
        case '3':
          statusP2 = 3;
          Serial.println("Infusion/Withdraw");
          break;
        case '4':
          statusP2 = 4;
          Serial.println("Withdraw/Infusion");
          break;
        default:
          statusP2 = 0;
      }

      pi_cmd.remove(0, 2);
      pi_cmd = pi_cmd;
      for (int i = 0; i < pi_cmd.length(); i++)
      {
        if (pi_cmd.charAt(i) == ':')
        {
          phantach = i; //tim vi tri cua dau "_"
        }
      }
      // phan tach the tich vao va ra mong muon
      volume = pi_cmd;
      comboString = pi_cmd;
      volume.remove(phantach);
      comboString.remove(0, phantach + 1);
      pi_cmd = comboString;
      for (int i = 0; i < pi_cmd.length(); i++)
      {

        if (pi_cmd.charAt(i) == '_')
        {
          tach = i; //tim vi tri cua dau "_"
        }
      }
      target = pi_cmd;
      flowRate = pi_cmd;
      target.remove(tach);
      //Serial.println(pi_cmd);
      //phantach[0] = 0;
      flowRate.remove(0, tach + 1);
      volumeP2 = volume.toInt();
      targetP2 = target.toInt();
      flowRateP2 = flowRate.toInt();
      Serial.print("volume and target:");
      Serial.println(volumeP2);
      Serial.println(targetP2);
      Serial.print("flowRate:");
      Serial.println(flowRateP2);
    }
    else if (P == 3)
    {
      switch (pi_cmd.charAt(0))
      {
        case '1':
          statusP3 = 1;
          Serial.println("Infusion ONLY");
          break;
        case '2':
          statusP3 = 2;
          Serial.println("Withdraw ONLY");
          break;
        case '3':
          statusP3 = 3;
          Serial.println("Infusion/Withdraw");
          break;
        case '4':
          statusP3 = 4;
          Serial.println("Withdraw/Infusion");
          break;
        default:
          statusP3 = 0;
      }

      pi_cmd.remove(0, 2);
      pi_cmd = pi_cmd;

      for (int i = 0; i < pi_cmd.length(); i++)
      {
        if (pi_cmd.charAt(i) == ':')
        {
          phantach = i; //tim vi tri cua dau "_"
        }
      }
      // phan tach the tich vao va ra mong muon
      volume = pi_cmd;
      comboString = pi_cmd;
      volume.remove(phantach);
      comboString.remove(0, phantach + 1);
      pi_cmd = comboString;
      for (int i = 0; i < pi_cmd.length(); i++)
      {

        if (pi_cmd.charAt(i) == '_')
        {
          tach = i; //tim vi tri cua dau "_"
        }
      }
      target = pi_cmd;
      flowRate = pi_cmd;
      target.remove(tach);
      //Serial.println(pi_cmd);
      //phantach[0] = 0;
      flowRate.remove(0, tach + 1);
      volumeP3 = volume.toInt();
      targetP3 = target.toInt();
      flowRateP3 = flowRate.toInt();
      Serial.print("volume and target:");
      Serial.println(volumeP3);
      Serial.println(targetP3);
      Serial.print("flowRate:");
      Serial.println(flowRateP3);
    }
    else
    {
      Serial.println("Not pump choose");
    }

    // khi nhan nut RUN o man hinh cam ung, thong tin truyen vao va chay dong cow
    if (informationPump == "r1")
    {

      // tinh ban kinh cua bom xi lanh

      switch (volumeP1)
      {
        case 1:
          radius = 2.45;
          break;
        case 3:
          //radius = ;
          break;
        case 5:
          //radius = ;
          break;
        case 10:
          //radius = ;
          break;
        case 20:
          //radius = ;
          break;
        case 50:
          //radius =;
          break;
        default:
          radius = 0;
      }
      Serial.print("radius:");
      Serial.println(radius);
      // tinh dien tich day
      S1 = Pi * radius * radius;
      Serial.print("Area:");
      Serial.println(S1);
      // tinh so step can chay tuong ung vs the tich ra mong muon
      if (targetP1 <= (volumeP1 * 1000))
      {
        double lengthRun1 = targetP1 / S1;
        
        stepRun1 = (lengthRun1 / pitch) * fullStep;
        stepRun1 = stepRun1 / (double)deceleration;
        stepRun1 = stepRun1 / (double)microStep;
        stepRun1 = (long int)stepRun1;
      }
      Serial.print("so Step:");
      Serial.println(stepRun1);

      Serial.print("flow Rate");
      Serial.println(flowRateP1);
      flowRateP1 = (double)flowRateP1;
      speed1 = flowRateP1 / (pitch * S1);
      Serial.print("toc do:");
      Serial.println(speed1);
      delay1 = (double)delay1;
      delay1 = 60000000 / (speed1 * steps * microStep * 49);
      delay1 = (int)delay1;

      Serial.print("delay:");
      Serial.println(delay1);
      // setup chieu quay va quay so buoc tuong ung de chay dong co
      switch (statusP1)
      {
        // trang thai chi hut vao
        case 1:
          dir1 = 1;
          time1 = millis();
          digitalWrite(dirPin1, dir1);
          for (long int x = 0; x < stepRun1; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin1, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin1, LOW);
              delayMicroseconds(delay1);
            }
          }
          time1 = millis() - time1;
          Serial.println(time1);
          break;

        // trang thai chi day ra
        case 2:
          dir1 = 0;
          time1 = millis();
          digitalWrite(dirPin1, dir1);
          for (long int x = 0; x < stepRun1; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin1, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin1, LOW);
              delayMicroseconds(delay1);
            }
          }
          time1 = millis() - time1;
          Serial.println(time1);
          break;

        // trang thai hut vao va day ra
        case 3:
          dir1 = 1;
          time1 = millis();
          digitalWrite(dirPin1, dir1);
          for (long int x = 0; x < stepRun1; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin1, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin1, LOW);
              delayMicroseconds(delay1);
            }
          }
          dir1 != dir1;
          digitalWrite(dirPin1, dir1);
          for (long int x = 0; x < stepRun1; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin1, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin1, LOW);
              delayMicroseconds(delay1);
            }
          }
          time1 = millis() - time1;
          Serial.println(time1);
          break;

        // trang thai day ra va hut vao
        case 4:
          dir1 = 0;
          time1 = millis();
          digitalWrite(dirPin1, dir1);
          for (long int x = 0; x < stepRun1; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin1, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin1, LOW);
              delayMicroseconds(delay1);
            }
          }
          dir1 != dir1;
          digitalWrite(dirPin1, dir1);
          for (long int x = 0; x < stepRun1; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin1, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin1, LOW);
              delayMicroseconds(delay1);
            }
          }
          time1 = millis() - time1;
          Serial.println(time1);
          break;
        default:
          time1 = 0;
      }
    }

    //tuong tu voi bom2 khi nhan nut chay
    if (informationPump == "r2")
    {
      //runMotor(1,statusP1,volumeP1,targetP1);
      // tinh ban kinh cua bom xi lanh

      switch (volumeP2)
      {
        case 1:
          radius = 2.45;
          break;
        case 3:
          //radius = ;
          break;
        case 5:
          //radius = ;
          break;
        case 10:
          //radius = ;
          break;
        case 20:
          //radius = ;
          break;
        case 50:
          //radius =;
          break;
        default:
          radius = 0;
      }
      Serial.print("radius:");
      Serial.println(radius);
      // tinh dien tich day
      S2 = Pi * radius * radius;
      Serial.print("Area:");
      Serial.println(S2);
      // tinh so step can chay tuong ung vs the tich ra mong muon
      if (targetP2 <= (volumeP2 * 1000))
      {
        double lengthRun2 = targetP2 / S2;
        
        stepRun2 = (lengthRun2 / pitch) * fullStep;
        stepRun2 = stepRun2 / (double)deceleration;
        stepRun2 = stepRun2 / (double)microStep;
        stepRun2 = (long int)stepRun2;
      }
      Serial.print("so Step:");
      Serial.println(stepRun2);

      Serial.print("flow Rate");
      Serial.println(flowRateP2);
      flowRateP2 = (double)flowRateP2;
      speed2 = flowRateP2 / (pitch * S2);
      Serial.print("toc do:");
      Serial.println(speed2);
      delay2 = (double)delay2;
      delay2 = 60000000 / (speed1 * steps * microStep * 49);
      delay2 = (int)delay2;

      Serial.print("delay:");
      Serial.println(delay2);
      // setup chieu quay va quay so buoc tuong ung de chay dong co
      switch (statusP2)
      {
        // trang thai chi hut vao
        case 1:
          dir2 = 1;
          time2 = millis();
          digitalWrite(dirPin2, dir2);
          for (long int x = 0; x < stepRun2; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin2, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin2, LOW);
              delayMicroseconds(delay2);
            }
          }
          time2 = millis() - time2;
          Serial.println(time2);
          break;

        // trang thai chi day ra
        case 2:
          dir2 = 0;
          time2 = millis();
          digitalWrite(dirPin2, dir2);
          for (long int x = 0; x < stepRun2; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin2, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin2, LOW);
              delayMicroseconds(delay2);
            }
          }
          time2 = millis() - time2;
          Serial.println(time2);
          break;

        // trang thai hut vao va day ra
        case 3:
          dir2 = 1;
          time2 = millis();
          digitalWrite(dirPin2, dir2);
          for (long int x = 0; x < stepRun2; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin2, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin2, LOW);
              delayMicroseconds(delay2);
            }
          }
          dir2 != dir2;
          digitalWrite(dirPin2, dir2);
          for (long int x = 0; x < stepRun2; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin2, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin2, LOW);
              delayMicroseconds(delay2);
            }
          }
          time2 = millis() - time2;
          Serial.println(time2);
          break;

        // trang thai day ra va hut vao
        case 4:
          dir2 = 0;
          time2 = millis();
          digitalWrite(dirPin2, dir2);
          for (long int x = 0; x < stepRun2; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin2, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin2, LOW);
              delayMicroseconds(delay2);
            }
          }
          dir2 != dir2;
          digitalWrite(dirPin2, dir2);
          for (long int x = 0; x < stepRun2; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin2, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin2, LOW);
              delayMicroseconds(delay2);
            }
          }
          time2 = millis() - time2;
          Serial.println(time2);
          break;
        default:
          time2 = 0;
      }
    }

    if (informationPump == "r3")
    {
      //runMotor(1,statusP1,volumeP1,targetP1);
      // tinh ban kinh cua bom xi lanh

      switch (volumeP3)
      {
        case 1:
          radius = 2.45;
          break;
        case 3:
          //radius = ;
          break;
        case 5:
          //radius = ;
          break;
        case 10:
          //radius = ;
          break;
        case 20:
          //radius = ;
          break;
        case 50:
          //radius =;
          break;
        default:
          radius = 0;
      }
      Serial.print("radius:");
      Serial.println(radius);
      // tinh dien tich day
      S3 = Pi * radius * radius;
      Serial.print("Area:");
      Serial.println(S3);
      // tinh so step can chay tuong ung vs the tich ra mong muon
      if (targetP3 <= (volumeP3 * 1000))
      {
        double lengthRun3 = targetP3 / S3;
        
        stepRun3 = (lengthRun3 / pitch) * fullStep;
        stepRun3 = stepRun3 / (double)deceleration;
        stepRun3 = stepRun3 / (double)microStep;
        stepRun3 = (long int)stepRun3;
      }
      Serial.print("so Step:");
      Serial.println(stepRun3);

      Serial.print("flow Rate");
      Serial.println(flowRateP3);
      flowRateP3 = (double)flowRateP3;
      speed3 = flowRateP3 / (pitch * S3);
      Serial.print("toc do:");
      Serial.println(speed3);
      delay3 = (double)delay3;
      delay3 = 60000000 / (speed1 * steps * microStep * 49);
      delay3 = (int)delay3;

      Serial.print("delay:");
      Serial.println(delay3);
      // setup chieu quay va quay so buoc tuong ung de chay dong co
      switch (statusP3)
      {
        // trang thai chi hut vao
        case 1:
          dir3 = 1;
          time3 = millis();
          digitalWrite(dirPin3, dir3);
          for (long int x = 0; x < stepRun3; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin3, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin3, LOW);
              delayMicroseconds(delay3);
            }
          }
          time3 = millis() - time3;
          Serial.println(time3);
          break;

        // trang thai chi day ra
        case 2:
          dir3 = 0;
          time3 = millis();
          digitalWrite(dirPin3, dir3);
          for (long int x = 0; x < stepRun3; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin3, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin3, LOW);
              delayMicroseconds(delay3);
            }
          }
          time3 = millis() - time3;
          Serial.println(time3);
          break;

        // trang thai hut vao va day ra
        case 3:
          dir3 = 1;
          time3 = millis();
          digitalWrite(dirPin3, dir3);
          for (long int x = 0; x < stepRun3; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin3, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin3, LOW);
              delayMicroseconds(delay3);
            }
          }
          dir3 != dir3;
          digitalWrite(dirPin3, dir3);
          for (long int x = 0; x < stepRun3; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin3, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin3, LOW);
              delayMicroseconds(delay3);
            }
          }
          time3 = millis() - time3;
          Serial.println(time3);
          break;

        // trang thai day ra va hut vao
        case 4:
          dir3 = 0;
          time3 = millis();
          digitalWrite(dirPin3, dir3);
          for (long int x = 0; x < stepRun3; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin3, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin3, LOW);
              delayMicroseconds(delay3);
            }
          }
          dir3 != dir3;
          digitalWrite(dirPin3, dir3);
          for (long int x = 0; x < stepRun3; x++)
          {
            for (long int i = 0; i < microStep * deceleration; i++)
            {
              digitalWrite(stepPin3, HIGH);
              delayMicroseconds(1);
              digitalWrite(stepPin3, LOW);
              delayMicroseconds(delay3);
            }
          }
          time3 = millis() - time3;
          Serial.println(time3);
          break;
        default:
          time3 = 0;
      }
    }
    if (informationPump == "q1")
    {
      digitalWrite(interruptPin1, HIGH);
      delayMicroseconds(1);
      attachInterrupt(digitalPinToInterrupt(interruptPin1), stopMotor1, LOW);
      //stopMotor1();
    }
    if (informationPump == "q2")
    {
      digitalWrite(interruptPin2, HIGH);
      delayMicroseconds(1);
      attachInterrupt(digitalPinToInterrupt(interruptPin2), stopMotor2, LOW);
    }
    if (informationPump == "q3")
    {
      digitalWrite(interruptPin3, HIGH);
      delayMicroseconds(1);
      attachInterrupt(digitalPinToInterrupt(interruptPin3), stopMotor3, LOW);
    }
  }
}

void stopMotor1()
{
  digitalWrite(stepPin1, LOW);
}
void stopMotor2()
{
  digitalWrite(stepPin2, LOW);
}
void stopMotor3()
{
  digitalWrite(stepPin3, LOW);
}
