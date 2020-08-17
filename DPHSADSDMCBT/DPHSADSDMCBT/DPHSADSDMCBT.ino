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
float factorEscala = 0.1875F;

//Digital potentiometer pins 
DigiPot pot(8,7,9);

//Hall effect sensor
int hallsensor = 2;

volatile int counter;

unsigned int rpm;

unsigned long passedtime;

unsigned long it = 0;

//Counter
void isr()


 {
   
      //contador++;
      counter++;

 }


void setup(void) 
{
  Serial.begin(9600);
  delay(200);
  
  //Bluetooth module
  BT.begin(9600);
  
  //Relay
  pinMode(foco,OUTPUT);
  
  //Ads gain
  ads.setGain(GAIN_TWOTHIRDS);
  
  //Starts ADS1115
  ads.begin();
  
  //Hall effect
  attachInterrupt(0, isr, RISING); 
  
  pinMode(hallsensor, INPUT); 
  
  //contador = 0;
  counter = 0;
  
  rpm = 0;
  
  passedtime = 0;

}
 
void loop(void) 
{
  
  DP();
  
}



void DP()
{

  //Potenciometro digital
  //Serial.println("\t\t\t Potenciometro Digital");  

  for (int i=0; i<=1023; i++) {
    
    unsigned long nt = millis();
    digitalWrite(foco,LOW);
    //0,1023
    //Serial.print("Aumentando, i = ");
    //Serial.print("ValDP: ");
    Serial.println(i, DEC);
    pot.increase(i);//1);
    //Serial.print(",");
    //Efecto Hall
    delay(999);//Update RPM every second
    
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
    
    delay(1000);
    
    // Obtiene datos del pin A0 del ADS1115 y los imprime
    //short adc0 = ads.readADC_SingleEnded(0);
    //Serial.print("ADS: "); 
    //Serial.println(adc0);

    short diferencia_0_1 = ads.readADC_Differential_0_1();
    float volts = (diferencia_0_1 * factorEscala)/1000.0;
    //Serial.print("Diferencia 0-1");
    Serial.println(diferencia_0_1);
    //Serial.print("Voltaje: ");
    Serial.println(volts,4);
   
    //delay(1000);

    //Serial.print(",");
    //Delay del DP
    delay(1000);
    //Serial.println();
    
    unsigned long ts = nt - it;
    unsigned long tt = (ts*0.001);
    //Serial.println("Time: ");
    Serial.println(tt);
    
  }

}
