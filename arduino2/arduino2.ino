
#include <string.h>
//#include <String>

//SETTING MOTOR AND DRIVER
const int stepPin2 = 9 ;
const int dirPin2 = 8;
//const int enablePin = 6;

// khai báo chân ngắt động cơ
const byte interruptPin2 = 2;

/// chiều quay động cơ
bool dir2 = 1;

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
int Pump2 = 0;
int statusP2 = 0;
int volumeP2 = 0;
int targetP2 = 0;
int flowRateP2 = 0;
// khai bao thêm các thông số
int P = 0;
String pump;
String volume, comboString, target, flowRate;
byte phantach;
byte tach;

/// thời gian chạy của bơm
long int time2 = 0;

// counter
long int counter2 = 0;

long int currentCounter2 = 0;


// khai báo Speed
double speed2 = 0;

// thời gian delay
long int delay2 = 200;


// khai báo bán kính của xi lanh
double radius;
// khai báo thể tích xi lanh
double V;
// khai báo diện tích đáy của các xi lanh
double S2;

int steps = 200;

// số bước động cơ cần chạy
long int stepRun2 ;


//String informationPump;

void setup()
{
  // put your setup code here, to run once:
  Serial.begin(9600);
  pinMode(stepPin2, OUTPUT);
  pinMode(dirPin2, OUTPUT);
  //pinMode(enablePin, OUTPUT);
  //digitalWrite(enablePin,LOW);
  //pinMode(interruptPin2, INPUT_PULLUP);

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
      case '2':
        Pump2 = 2;
        P = 2;
        Serial.println("Pump2");
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
    if (P == 2)
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
      Serial.println(statusP2);
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
      volumeP2 = volume.toInt();
      targetP2 = target.toInt();
      flowRateP2 = flowRate.toInt();
      Serial.print("volume and target:");
      Serial.println(volumeP2);
      Serial.println(targetP2);
      Serial.print("flowRate:");
      Serial.println(flowRateP2);
    }
    else
    {
      Serial.println("Not pump choose");
    }
    //       }
    //       }
    // khi nhan nut RUN o man hinh cam ung, thong tin truyen vao va chay dong cow
    if (informationPump == "r2")
    {

      // tinh ban kinh cua bom xi lanh

      switch (volumeP2)
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
      S2 = Pi * radius * radius;
      Serial.print("Area:");
      Serial.println(S2);
      // tinh so step can chay tuong ung vs the tich ra mong muon
      if (targetP2 <= (volumeP2 * 1000 + 1))
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
      delay2 = 60000000 / (speed2 * steps * microStep * 49);
      delay2 = (int)delay2;

      Serial.print("delay:");
      Serial.println(delay2);
      // setup chieu quay va quay so buoc tuong ung de chay dong co
      switch (statusP2)
      {
        // trang thai chi hut vao
        case 1:
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

        // trang thai chi day ra
        case 2:
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

        // trang thai hut vao va day ra
        case 3:
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

        // trang thai day ra va hut vao
        case 4:
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
        default:
          time2 = 0;
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
