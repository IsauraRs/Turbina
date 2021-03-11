#include <Wire.h>

#include <Adafruit_ADS1015.h>

//Digital potentiometer library
#include <DigiPotX9Cxxx.h>

//Bluetooth module
#include<SoftwareSerial.h>

int RX = 1 , TX = 0;

SoftwareSerial BT = SoftwareSerial(RX , TX);

char ser;
char BTData;

Adafruit_ADS1115 ads;

//Conversion scale factor
float factorEscala = 0.0078125F;

//Digital potentiometer pins 
DigiPot pot(8,7,9);


const int hall_pin = 5;
const int LEDPin = 13;
const int LEDPin2= 6;
// Límite de pulsos del hall para cálculo de RPM
// Entre más grande sea este número, mejor precisión
float hall_thresh = 11.0;
 
void setup() {
  
  pinMode(LEDPin, OUTPUT);
  pinMode(LEDPin2, OUTPUT);
  Serial.begin(115200);
  pinMode(hall_pin, INPUT);
  ads.setGain(GAIN_SIXTEEN);
  
  //Starts ADS1115
  ads.begin();

  Serial.begin(9600);
  //delay(200);
  
  //Bluetooth module
  BT.begin(9600);
}
 
void loop() {

if (Serial.available()>0)
{
  // Definición de parámetros para el contador
  float hall_count = 1.0;
  // Inicio de conteo de tiempo en microsegundos
  float start = micros();
  bool on_state = false;
  // Conteo de pulsos para cálculo de frecuencia
  // Ciclo infinito
  
  for (float i=0; i<100; i++) {//DP
    for(float j = 1; j<101; j++) //Data#
    {
      while(true){
   
        // Se detectan bajos y no altos en el hall
        if (digitalRead(hall_pin)==0){
          if (on_state==false){
            on_state = true;
            hall_count+=1.0;
            digitalWrite(LEDPin, HIGH); 
          }
        } else{
          // Esta sección elimina el posible doble conteo 
          on_state = false;
          digitalWrite(LEDPin, LOW);
        }
        
        if (hall_count>=hall_thresh){
          digitalWrite(LEDPin2, HIGH);
          delay(100); 
          digitalWrite(LEDPin2, LOW);
          break;
        }
      }
      
      // Impresión de datos en serial
      float end_time = micros();
      float time_passed = ((end_time-start)/1000000.0);
    //  Serial.print("Time Passed: ");
      Serial.print(time_passed);
    //  Serial.println("s");
      float rpm_val = (hall_count/time_passed)*60.0;
      Serial.print(" ");
      Serial.print( rpm_val);
    //  Serial.println(" RPM");
      float hz_val = (hall_count/time_passed);
      Serial.print(" ");
      Serial.println( hz_val);
    //  Serial.println(" Hz");
      delay(1); // delay entre lecturas para estabilidad
      
      Serial.println((i), DEC); //i+1023    ------------1
      pot.increase(i);//1); //i+1000
      
      short diferencia_0_1 = ads.readADC_Differential_0_1();
      float volts = (diferencia_0_1 * factorEscala)/1000.0;
      short diferencia_2_3 = ads.readADC_Differential_2_3();
      float voltsEntregados = (diferencia_2_3 * factorEscala)/1000.0;
      
      //Serial.print("Diferencia 0-1");
      Serial.println(diferencia_0_1);              //-----------3
      //Serial.print("Voltaje: ");
      Serial.println(volts,4);                   // ---------------4
      //Serial.print("difEntr");
      Serial.println(diferencia_2_3);             //-----------------5
      //Serial.print("voltsEnt");
      Serial.println(voltsEntregados,4);            // --------------6
      
      if (j <41)
      {
        i = i;
        //Serial.println("i es igual");
        //Serial.print(i);
      }
      else {
        i++;
        //Serial.print("Ya aumento i");
      }
      delay(1000);
    }
      
      if (i == 99)
      {
        for (i==99; i>=0; i--) {
          for(float j = 1; j<101; j++)
          {
            while(true){
              // Se detectan bajos y no altos en el hall
              if (digitalRead(hall_pin)==0){
                if (on_state==false){
                  on_state = true;
                  hall_count+=1.0;
                  digitalWrite(LEDPin, HIGH); 
                }
              } else{
                // Esta sección elimina el posible doble conteo 
                on_state = false;
                digitalWrite(LEDPin, LOW);
              }
              
              if (hall_count>=hall_thresh){
                digitalWrite(LEDPin2, HIGH);
                delay(100); 
                digitalWrite(LEDPin2, LOW);
                break;
              }
            }
            
            // Impresión de datos en serial
            float end_time = micros();
            float time_passed = ((end_time-start)/1000000.0);
          //  Serial.print("Time Passed: ");
            Serial.print(time_passed);
          //  Serial.println("s");
            float rpm_val = (hall_count/time_passed)*60.0;
            Serial.print(" ");
            Serial.print( rpm_val);
          //  Serial.println(" RPM");
            float hz_val = (hall_count/time_passed);
            Serial.print(" ");
            Serial.println( hz_val);
          //  Serial.println(" Hz");
            delay(1); // delay entre lecturas para estabilidad
            
            Serial.println((i), DEC); //i+1023    ------------1
            pot.increase(i);//1); //i+1000
            
            short diferencia_0_1 = ads.readADC_Differential_0_1();
            float volts = (diferencia_0_1 * factorEscala)/1000.0;
            short diferencia_2_3 = ads.readADC_Differential_2_3();
            float voltsEntregados = (diferencia_2_3 * factorEscala)/1000.0;
            
            //Serial.print("Diferencia 0-1");
            Serial.println(diferencia_0_1);              //-----------3
            //Serial.print("Voltaje: ");
            Serial.println(volts,4);                   // ---------------4
            //Serial.print("difEntr");
            Serial.println(diferencia_2_3);             //-----------------5
            //Serial.print("voltsEnt");
            Serial.println(voltsEntregados,4);            // --------------6
            
            if (j <41)
            {
              i = i;
              //Serial.println("i es igual");
              //Serial.print(i);
            }
            else {
              i++;
              //Serial.print("Ya aumento i");
            }
            delay(1000);
          }
        }
      }
    }
  
}

            
}
