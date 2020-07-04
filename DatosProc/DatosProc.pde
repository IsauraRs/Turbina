import processing.serial.*;
//Intento1 funciona, usar este
Serial port;
String datos;
void setup()
{
  size(700,700);
  //Revisar que el puerto coincida con el que se está utilizando en arduino
  port = new Serial(this, "/dev/ttyACM0",9600);
  port.bufferUntil('\n');
}


void draw()
{
  
  background(0);
  textSize(16);
  
  text("Valor Potenciómetro Digital\n" + datos,40,73);
  delay(999);
  
  text("Valor RPM\n" + datos,320,73);
  delay(1000);
  text("Valor ADS\n" + datos,600,73);
  delay(1000);
}

void serialEvent(Serial port)
{

  String bufString = port.readStringUntil('\n');
  datos = bufString;

}
