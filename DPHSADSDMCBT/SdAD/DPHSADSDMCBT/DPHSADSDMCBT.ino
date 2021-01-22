//Este codigo abarca el manejo del sensor de efecto hall,
//This code incorporates the hall effect sensor,
//The digital potentiometer x9c103S
//And the ADS1115 module in its differential mode
//This version sends data to python

//Bluetooth module
#include<SoftwareSerial.h>

int RX = 1 , TX = 0;

SoftwareSerial BT = SoftwareSerial(RX , TX);

char ser;
char BTData;

//Relay bot
int foco=6;
char estado;

//ADS1115 library
#include <Wire.h>

#include <Adafruit_ADS1015.h>

//Digital potentiometer library
#include <DigiPotX9Cxxx.h>
 //Este si funciona
 
//Create ads class object  
Adafruit_ADS1115 ads;

//Conversion scale factor
float factorEscala = 0.0078125F;

//Digital potentiometer pins 
DigiPot pot(8,7,9);

//Hall effect sensor
int hallsensor = 2;

volatile int counter;

unsigned int rpm;

unsigned long passedtime;

unsigned long it = 0;
unsigned long ts = 0;
unsigned long tt = 0;
unsigned long nt = 0;

//Counter
void isr()


 {
   
      //contador++;
      counter++;

 }


void setup(void) 
{
  Serial.begin(9600);
  //delay(200);
  
  //Bluetooth module
  BT.begin(9600);
  
  //Relay
  pinMode(foco,OUTPUT);
  
  //Ads gain
  ads.setGain(GAIN_SIXTEEN);
  
  //Starts ADS1115
  ads.begin();
  
  //Hall effect
  attachInterrupt(0, isr, RISING); 
  
  pinMode(hallsensor, INPUT); 
  
  //contador = 0;
  counter = 0;
  
  rpm = 0;
  
  passedtime = 0;
  nt = 0;
  it = 0;
  tt = 0;
  
}
 
void loop(void) 
{
  if (Serial.available()>0)
  {
    ser = Serial.read();
    if (ser == 'Y')
    {
      DP();
    }
  }
}



void DP()
{

  //Potenciometro digital
  //Serial.println("\t\t\t Potenciometro Digital");  

  for (float i=0; i<100; i++) { //1023
    for(float j = 1; j<41; j++)
    {
      
      nt = millis();
      digitalWrite(foco,LOW);
      //0,1023
      //Serial.print("Aumentando, i = ");
      //Serial.print("ValDP: ");
      Serial.println((i), DEC); //i+1023    ------------1
      pot.increase(i);//1); //i+1000
      //Serial.print(",");
      //Efecto Hall
      //delay(999);//Update RPM every second
      
      detachInterrupt(0); //Interrupts are disabled
    
      //rpm = 60*contador;
      rpm = counter / (passedtime/1000);
      rpm = rpm * 60;
      
      if (rpm != 0)
      {
        
        digitalWrite(foco,HIGH);
        delay(1000);
        digitalWrite(foco,LOW);
        
      }
      
      
      passedtime = millis();
      
      //contador = 0;
      counter = 0;
      //Serial.print("RPM= ");
      
      Serial.println(rpm); //Print out result to monitor ----------2
      
      attachInterrupt(0, isr, RISING);   //Restart the interrupt processing
      
      //Serial.print(",");
      
      //delay(1000);
      
      // Obtiene datos del pin A0 y A1 del ADS1115 y los imprime
      //short adc0 = ads.readADC_SingleEnded(0);
      //Serial.print("ADS: "); 
      //Serial.println(adc0);
  
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
     
      //Delay del DP
      //delay(1000);
  
      ts = nt - it;
      tt = (ts*0.001);
      //Serial.println("Time: ");
      Serial.println(tt);                          // ----------------7
      //
         
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
      delay(1000); //3000
    }
    if (i == 99)
    {
      for (i==99; i>=0; i--) {
        for(float j = 1; j<41; j++)
        {
          //1023
          nt = millis();
          digitalWrite(foco,LOW);
          //0,1023
          //Serial.print("Aumentando, i = ");
          //Serial.print("ValDP: ");
          Serial.println((i), DEC); //i+1023
          pot.increase(i);//1); //i+1000
          //Serial.print(",");
          //Efecto Hall
          //delay(999);//Update RPM every second
          
          detachInterrupt(0); //Interrupts are disabled
        
          //rpm = 60*contador;
          rpm = counter / (passedtime/1000);
          rpm = rpm * 60;
          
          if (rpm != 0)
          {
            
            digitalWrite(foco,HIGH);
            delay(1000);
            digitalWrite(foco,LOW);
            
          }
          
          
          passedtime = millis();
          
          //contador = 0;
          counter = 0;
          //Serial.print("RPM= ");
          
          Serial.println(rpm); //Print out result to monitor
          
          attachInterrupt(0, isr, RISING);   //Restart the interrupt processing
          
          //Serial.print(",");
          
          //delay(1000);
          
          // Obtiene datos del pin A0 y A1 del ADS1115 y los imprime
          //short adc0 = ads.readADC_SingleEnded(0);
          //Serial.print("ADS: "); 
          //Serial.println(adc0);
      
          short diferencia_0_1 = ads.readADC_Differential_0_1();
          float volts = (diferencia_0_1 * factorEscala)/1000.0;
          short diferencia_2_3 = ads.readADC_Differential_2_3();
          float voltsEntregados = (diferencia_2_3 * factorEscala)/1000.0;
          
          //Serial.print("Diferencia 0-1");
          Serial.println(diferencia_0_1);
          //Serial.print("Voltaje: ");
          Serial.println(volts,4);
          //Serial.print("difEntr");
          Serial.println(diferencia_2_3);
          //Serial.print("voltsEnt");
          Serial.println(voltsEntregados,4);
         
          //Delay del DP
          //delay(1000);
      
          ts = nt - it;
          tt = (ts*0.001);
          //Serial.println("Time: ");
          Serial.println(tt);
          
          if (j <41)
          {
            i = i;
          }
          //Serial.println("i es igual");
          //Serial.print(i);
          else {
            i++;
            //Serial.print("Ya aumento i");
          }
          delay(1000); //3000
        }
      /*while (i == 99)
     {
       nt = millis();
       digitalWrite(foco,LOW);
       //0,1023
       //Serial.print("Aumentando, i = ");
       //Serial.print("ValDP: ");
       Serial.println((i), DEC);
       pot.increase(i);//1);
       //Serial.print(",");
       //Efecto Hall
       //delay(999);//Update RPM every second
       detachInterrupt(0); //Interrupts are disabled
       //rpm = 60*contador;
       rpm = 60*counter;
        
       if (rpm != 0)
       {
         
         digitalWrite(foco,HIGH);
         delay(1000);
         digitalWrite(foco,LOW);
          
       }
       
        
        
       passedtime = millis();
        
       //contador = 0;
       counter = 0;
       //Serial.print("RPM= ");
        
       Serial.println(rpm); //Print out result to monitor
        
       attachInterrupt(0, isr, RISING);   //Restart the interrupt processing
        
        //Serial.print(",");
        
        //delay(1000);
        
        // Obtiene datos del pin A0 y A1 del ADS1115 y los imprime
        //short adc0 = ads.readADC_SingleEnded(0);
        //Serial.print("ADS: "); 
        //Serial.println(adc0);
    
       short diferencia_0_1 = ads.readADC_Differential_0_1();
       float volts = (diferencia_0_1 * factorEscala)/1000.0;
       short diferencia_2_3 = ads.readADC_Differential_2_3();
       float voltsEntregados = (diferencia_2_3 * factorEscala)/1000.0;
       //Serial.print("Diferencia 0-1");
       Serial.println(diferencia_0_1);
       //Serial.print("Voltaje: ");
       Serial.println(volts,4);
       //Serial.print("difEntr");
       Serial.println(diferencia_2_3);
       //sSerial.print("voltsEnt");
       
       Serial.println(voltsEntregados,4);
       
       //Delay del DP
       //delay(1000);
    
       ts = nt - it;
       tt = (ts*0.001);
       //Serial.println("Time: ");
       Serial.println(tt);
       delay(3000);
       i = 99;
       */
     
    }
    
  }
  
 }
}
