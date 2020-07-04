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
  
  DP();

  //Activa el relay por medio de telegram
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


void DP()
{

  //Potenciometro digital
  for (int i=0; i<1023; i++) {

    Serial.print("ValDP: ");
    Serial.println(i, DEC);
    pot.increase(1);
    //Efecto Hall
    delay(999);//Actualiza RPM cada segundo
    
    detachInterrupt(0); //Se deshabilitan las interrupciones
  
    rpm = 60*contador;
    
    passedtime = millis();
    
    contador = 0;
    Serial.print("RPM= ");
    
    Serial.println(rpm); //Imprime las RPM
    
    attachInterrupt(0, isr, RISING);   //Reinicia el interruptor de inicio
    
    delay(1000);
    
    // Obtiene datos del pin A0 y A1 del ADS1115 y los imprime

    short diferencia_0_1 = ads.readADC_Differential_0_1();
    float volts = (diferencia_0_1 * factorEscala)/1000.0;
    Serial.print("Diferencia 0-1");
    Serial.println(diferencia_0_1);
    Serial.print("Voltaje: ");
    Serial.println(volts,4);
   
    //Delay del DP
    delay(1000);

  }

  for (int i=0; i<1023; i++) {
    Serial.print("ValDP:");

    Serial.println(i, DEC);
    pot.decrease(1);
    
    //Efecto Hall
    delay(999);//Actualiza las RPM cada segundo
    
    detachInterrupt(0); //Se deshabilitan las interrupciones
  
    rpm = 60*contador;
    
    passedtime = millis();
    
    contador = 0;
    Serial.print("RPM= ");
    
    Serial.println(rpm); //Imprime RPM
    
    attachInterrupt(0, isr, RISING);   //Reinicia el interruptor 
    
    delay(1000);
    
    // Obtiene datos del pin A0 y A1 del ADS1115 y los imprime
    short diferencia_0_1 = ads.readADC_Differential_0_1();
    float volts = (diferencia_0_1 * factorEscala)/1000.0;
    Serial.print("Diferencia 0-1");    
    Serial.println(diferencia_0_1);
    Serial.print("Voltaje: ");
    Serial.println(volts,4);
    //Delay del DP
    
    delay(1000);

  }

}
