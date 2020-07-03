//Este codigo abarca el manejo del sensor de efecto hall,
//el potenciometro digital X9C103S
//Y el ADS1115 en modo diferencial
//Version que envia datos a processing, usar este

//BotRelevador
int foco=6;
char estado;

//ADS1115 
#include <Wire.h>

#include <Adafruit_ADS1015.h>

//libreria del potenciometro digital
#include <DigiPotX9Cxxx.h>
 //Este si funciona
 
// Crear objeto de la clase
Adafruit_ADS1115 ads;

//Factor de escala para conversion
float factorEscala = 0.1875F;

//Pines del potenciometro
DigiPot pot(8,7,9);

//Sensor de efecto Hall
int hallsensor = 2;

volatile int contador;

unsigned int rpm;

unsigned long passedtime;

//Contador 
void isr()


 {
   
      contador++;

 }


void setup(void) 
{
  Serial.begin(9600);
  delay(200);
  
  //Relevador
  pinMode(foco,OUTPUT);
  
  //Para leer variaciones mas pequeñas
  //ads.setGain(GAIN_ONE);
  ads.setGain(GAIN_TWOTHIRDS);
  
  //Se inicia el ADS1115
  ads.begin();
  
  //Efecto Hall
  attachInterrupt(0, isr, RISING); 
  
  pinMode(hallsensor, INPUT); 
  
  contador = 0;
  
  rpm = 0;
  
  passedtime = 0;

}
 
void loop(void) 
{
  //Hall();
  //ADS11l();
  DP();
  if(Serial.available()>0)
  {
    estado=Serial.read();
    if(estado=='N')
    {
      digitalWrite(foco,LOW);
    }
    else if(estado=='Y')
    {
      digitalWrite(foco,HIGH);
    }
  }

  
}

/*void Hall()
{
  //Efecto Hall
  delay(999);//Update RPM every second
  
  detachInterrupt(0); //Interrupts are disabled

  rpm = 60*contador;
  
  passedtime = millis();
  
  contador = 0;
  //Serial.print("RPM=");
  
  Serial.println(rpm); //Print out result to monitor
  
  attachInterrupt(0, isr, RISING);   //Restart the interrupt processing
}

void ADS11l()
{
  // Obtiene datos del pin A0 del ADS1115 y los imprime
  short adc0 = ads.readADC_SingleEnded(0);
  //Serial.print("\t\t A0: "); 
  Serial.println(adc0);
 
  delay(1000);
}*/

void DP()
{

  //Potenciometro digital
  //Serial.println("\t\t\t Potenciometro Digital");  

  for (int i=0; i<1023; i++) {
    //0,1023
    //Serial.print("Aumentando, i = ");
    Serial.print("ValDP: ");
    Serial.println(i, DEC);
    pot.increase(1);
    //Serial.print(",");
    //Efecto Hall
    delay(999);//Update RPM every second
    
    detachInterrupt(0); //Interrupts are disabled
  
    rpm = 60*contador;
    
    passedtime = millis();
    
    contador = 0;
    Serial.print("RPM= ");
    
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
    Serial.print("Diferencia 0-1");
    Serial.println(diferencia_0_1);
    Serial.print("Voltaje: ");
    Serial.println(volts,4);
   
    //delay(1000);

    //Serial.print(",");
    //Delay del DP
    delay(1000);
    //Serial.println();
  }

  for (int i=0; i<1023; i++) {
    Serial.print("ValDP:");
//Serial.print("Disminuyendo, i = ");

    Serial.println(i, DEC);
    pot.decrease(1);
    
    //Serial.print(",");
    //Efecto Hall
    delay(999);//Update RPM every second
    
    detachInterrupt(0); //Interrupts are disabled
  
    rpm = 60*contador;
    
    passedtime = millis();
    
    contador = 0;
    Serial.print("RPM= ");
    
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
    Serial.print("Diferencia 0-1");    
    Serial.println(diferencia_0_1);
    Serial.print("Voltaje: ");
    Serial.println(volts,4);
 
    //delay(1000);

    //Serial.print(",");
    //Delay del DP
    
    delay(1000);
    //Serial.println();
  }
}
