import processing.serial.*;
//float [] datos = new float[3];
//Intento1 funciona, usar este
String [] data = new String[3];
Serial port;
int lf = 10;
String datos;
int [] val = new int[3];
//String nombre ["
void setup()
{
  size(700,700);
  port = new Serial(this, "/dev/ttyACM0",9600);
  port.bufferUntil('\n');
}


void draw()
{
  
  background(0);
  textSize(16);
  /*for(i=1;i<data.length;i++)
  {*/
  
  text("Valor Potenciómetro Digital\n" + datos,40,73);
  delay(999);
  //text("Valor Potenciómetro Digital\n" + data[0],120,73);
    
  text("Valor RPM\n" + datos,320,73);
  //text("Valor RPM\n" + data[1],320,73);
  delay(1000);
  text("Valor ADS\n" + datos,600,73);
  //text("Valor ADS\n" + data[],600,73);
  delay(1000);
  //}
  /*if(data[0])
  {
    text("Valor DP \n" + data[0],120,73);
  }*/
   
}

void serialEvent(Serial port)
{
  String bufString = port.readStringUntil('\n');
  datos = bufString;
  
  //Este más o menos funciona yuyu
  //datos = bufString;n
  //println(bufString);
  //for(i=0;i<data.length;i++)
  //{
    bufString = trim(bufString);
    data = split(bufString,",");
    for(int i = 0; i <data.length; i++)
    {
      val[i] = int(data[i]);
      println(data[i]);
    }
    /*
    print("ValorDP");
    println(data[0]);
    print("RPM");
    println(data[1]);
    print("ADS");
    println(data[2]);
  //}*/
}
