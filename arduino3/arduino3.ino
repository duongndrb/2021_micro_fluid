
#include <string.h>
//#include <String>

//SETTING MOTOR AND DRIVER
const int stepPin3 = 9;
const int dirPin3 = 8;
//const int enablePin = 6;

// khai báo chân ngắt động cơ
const byte interruptPin3 = 2;

/// chiều quay động cơ
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
int Pump3 = 0;
int statusP3 = 0;
int volumeP3 = 0;
int targetP3 = 0;
int flowRateP3 = 0;
// khai bao thêm các thông số
int P = 0;
String pump;
String volume, comboString, target, flowRate;
byte phantach;
byte tach;

/// thời gian chạy của bơm
long int time3 = 0;

// counter
long int counter3 = 0;

long int currentCounter3 = 0;


// khai báo Speed
double speed3 = 0;

// thời gian delay
long int delay3 = 200;


// khai báo bán kính của xi lanh
double radius;
// khai báo thể tích xi lanh
double V;
// khai báo diện tích đáy của các xi lanh
double S3;

int steps = 200;

// số bước động cơ cần chạy
long int stepRun3 ;


//String informationPump;

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(stepPin3, OUTPUT);
  pinMode(dirPin3, OUTPUT);
  //pinMode(enablePin, OUTPUT);
  //digitalWrite(enablePin,LOW);
  //pinMode(interruptPin3, INPUT_PULLUP);

}

void loop()
{
  // put your main code here, to run repeatedly:
  if (Serial.available() > 1 )
  {
    String informationPump = Serial.readString() ;
    //char nhan = Serial.read();
    //    if ( nhan == '/')
    //         {
    //         if(informationPump.length() >1)
    //         {

    Serial.println(informationPump);
    // chuoi nhan duoc co dang 1:2_10:1000_100
    // 1: ky hieu cua may bom vs dong co tuong ung
    // 2: trang thai chay cua dong co(1: chi hut vao, 2: chi day ra, 3: hut vao roi day ra, 4: day ra roi hut vao )
    // 10: dung tich cua xi lanh lap vao (1,3,5,10,20,50)
    // 1000: the tich dung dich ra mong muon (100,200,...1000)
    // 100
    pi_cmd = informationPump;
    //xu ly tach ky tu dau tien cua chuoi
    switch (pi_cmd.charAt(0))
    {
      case '3':
        Pump3 = 3;
        P = 3;
        Serial.println("Pump3");
        break;
      //      case '2':
      //        Pump2 = 2;
      //        P = 2;
      //        Serial.println("Pump2");
      //        break;
      //      case '3':
      //        Pump3 = 3;
      //        P = 3;
      //        Serial.println("Pump3");
      //        break;
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
    if (P == 3)
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
      Serial.println(statusP3);
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
    //       }
    //       }
    // khi nhan nut RUN o man hinh cam ung, thong tin truyen vao va chay dong cow
    if (informationPump == "r3")
    {

      // tinh ban kinh cua bom xi lanh

      switch (volumeP3)
      {
        case 1:
          radius = 2.45;
          break;
        case 3:
          radius = 5 ;
          break;
        case 5:
          radius = 6 ;
          break;
        case 10:
          radius = 8 ;
          break;
        case 20:
          radius = 10 ;
          break;
        case 50:
          radius = 15 ;
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
      if (targetP3 <= (volumeP3 * 1000 +1))
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
      delay3 = 60000000 / (speed3 * steps * microStep * 49);
      delay3 = (int)delay3;

      Serial.print("delay:");
      Serial.println(delay3);
      // setup chieu quay va quay so buoc tuong ung de chay dong co
      switch (statusP3)
      {
        // trang thai chi hut vao
        case 1:
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

        // trang thai chi day ra
        case 2:
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

        // trang thai hut vao va day ra
        case 3:
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

        // trang thai day ra va hut vao
        case 4:
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
        default:
          time3 = 0;
      }
    }

    //    if (informationPump == "q1")
    //    {
    //      digitalWrite(interruptPin1, HIGH);
    //      delayMicroseconds(1);
    //      attachInterrupt(digitalPinToInterrupt(interruptPin1), stopMotor1, LOW);
    //      //stopMotor1();
    //    }

  }
}

//void stopMotor1()
//{
//  digitalWrite(stepPin1, LOW);
//}
