![CEMIEOLogo](https://github.com/IsauraRs/Turbina/blob/master/Manual/CEMIEOLogo.png)





# Manual de usuario para el sistema de adquisición de datos





![IINGENLogo](https://github.com/IsauraRs/Turbina/blob/master/Manual/IINGENLogo.png)















## Índice:





1. ### Instalación y conexión.

   

    1. #### Mac OS y Ubuntu.

    2.  #### Windows.

       

2. ### Inicio.

     

3. ### Adquisición de datos.

    

    	1. #### Envío de reporte correspondiente a una prueba.

​    

4. ### Reportes.

     

5. ### Consultas a datos.

     

6. ### Consultas a reportes.









# 1. Instalación.



## 1.1. Mac OS y Linux.

Ingrese a: https://github.com/IsauraRs/Turbina y en la pestaña "Code", seleccione la opción "Download ZIP". 

_**Nota**: de click derecho sobre el enlace y seleccione "Abrir enlace en una nueva pestaña" o saldrá del manual._



![downloads](https://github.com/IsauraRs/Turbina/blob/master/Manual/downloadSS.png)

_Figura1. Descarga de archivos desde github._



Una vez terminada la descarga, extraiga la carpeta "Turbina-master" en una ubicación que conozca y/o recuerde.

Ingrese a su terminal y diríjase a la ruta donde se encuentra la carpeta "Turbina-master", que extrajo en el paso anterior. Una vez que esté en dicha ruta, ingrese a la carpeta "Instalación" y escriba lo siguiente:

```
chmod 777 Instalacions.sh
```

Y después:

```
./Instalacions.sh
```

Lo siguiente que aparecerá en su terminal debe parecerse a:



![macSS](https://github.com/IsauraRs/Turbina/blob/master/Manual/macSS.png)

_Figura2. Ejecución del archivo de instalación en MacOS._ 



En  MacOS, o a:



![ubuntuSS](https://github.com/IsauraRs/Turbina/blob/master/Manual/ubuntuSS.png)

_Figura3. Ejecución del archivo de instalación desde Ubuntu._



En Linux. Es probable que a usted no le aparezcan las alertas que aparecen en amarillo.

_**Nota** : En caso de que aparezca un error con pyserial o serial, tendrá que desinstalarlas e instalarlas manualmente de la siguiente manera._

```
sudo pip3 uninstall pyserial
```

```
sudo pip3 install pyserial
```

Para el caso de pyserial. Y:

```
pip3 uninstall serial
```

```
sudo pip3 install serial
```



## Conexión.

En MacOS: ingrese al menú en el logo "Apple", de click en "Preferencias del Sistema" y posteriormente de click en "Bluetooth".

 Busque en la lista el dispositivo de nombre "GUS", de click en él y luego en "Conectar", en caso de que solicite la contraseña ingrese " 1234 " o " 0000 ".

En Linux: Ingrese a "Configuración", diríjase a "Bluetooth" y seleccione el dispositivo de nombre "GUS", ingrese la contraseña " 1234 ", en caso de que la contraseña sea incorrecta, ingrese " 0000 ".

Si su distribución es Ubuntu (o alguna distribución basada en Debian) y falla la conexión con el paso anterior, vaya nuevamente a "Configuración", seleccione el dispositivo "GUS", revise y copie la dirección del dispositivo.



![BTdirection](https://github.com/IsauraRs/Turbina/blob/master/Manual/BTdir.png)

_Figura4. Dirección del dispositivo bluetooth._



Abria una nueva terminal e ingrese los siguientes comandos:

```
sudo apt-get update
```

```
sudo apt-get upgrade
```

```
sudo apt-get install bluez bluetooth blueman
```

```
sudo systemctl start bluetooth
```

```
sudo bluetoothctl
```

Ya que esté dentro de bluetoothctl, defina "default-agent":

```
default-agent
```

Y busque los dispositivos:

```
scan on
```

Empareje el dispositivo cuya dirección corresponda a la de "GUS":

```
pair 20:18:07:13:62:E2
```

Establezca el dispositivo como dispositivo de confianza

```
trust 20:18:07:13:62:E2
```

_**Nota**: esta es la configuración inicial en caso de fallar el método convencional de conexión, por lo que solo es necesario realizarla la primera vez. 
En adelante los únicos pasos que tendrá que realizar son los siguientes._

```
sudo hciconfig hci0 up
```

```
sudo rfcomm bind 0 20:18:07:13:62:E2 1
```

```
sudo rfcomm connect 0 20:18:07:13:62:E2
```

Si falla, realice lo siguiente:

```
sudo rfcomm release 0
```

```
sudo rfcomm connect 0 20:18:07:13:62:E2
```



# 2. Inicio.

Para iniciar la aplicación, una vez realizada la instalación y, en caso de requerirlo, la conexión, en la terminal, vaya a la carpeta "Turbina-master" e ingrese a  la carpeta "_Web_", ya que haya ingresado ejecute el siguiente comando:

```
python3 app.py 
```

En caso de que no tenga conectado un *Arduino*, le aparecerá un cuadro de alerta (o más de uno).



![tkWarning](https://github.com/IsauraRs/Turbina/blob/master/Manual/tkSS.png)

_Figura5.  Mensaje de alerta en caso de que no esté conectado un Arduino._



Basta con pulsar el botón "_OK_", si su intención es realizar búsquedas, si su intención es realizar pruebas, será necesario conectar el Sistema de Adquisición de Datos.

Hecho lo anterior, abra su navegador web y en el buscador escriba  http://127.0.0.1:5000/ , lo que lo llevará a la página principal del Sistema de Adquisición de Datos.



![PaginaPrinc](https://github.com/IsauraRs/Turbina/blob/master/Manual/ppsdad.png)

_Figura6. Página de inicio de la aplicación._



# 3. Adquisición de datos.

Para comenzar la toma de datos, presione el botón "_Begin test_".



![BeginTest](https://github.com/IsauraRs/Turbina/blob/master/Manual/bgtSS.png)

_Figura7. Botón "Begin test"._



Esto hará que se active el arduino y comience la toma de datos.



![Test](https://github.com/IsauraRs/Turbina/blob/master/Manual/testSS.png)

_Figura8. Inicio de prueba._



El sistema toma 40 datos por cada valor de resistencia. Mientras el valor del potenciómetro digital sea cero, no habrá valores de eficiencia ni de potencia.

Para ver las gráficas correspondientes a resistencia vs potencia, resistencia vs eficiencia  del generador y resistencia vs eficiencia de la turbina, tomadas en tiempo real, presione el botón "Mostrar".



![MostrarButton](https://github.com/IsauraRs/Turbina/blob/master/Manual/mosSS.png)

_Figura9. Botón "Mostrar"._



Esto desplegará las tres gráficas, mientras los valores de resistencia sean cero y uno, las gráficas que aparecerán no corresponderán a los datos de esa prueba, debido a que estos se actualizan a partir del valor de resistencia uno del potenciómetro digital, sin embargo, los puntos graficados son un promedio de estas pruebas, por lo que se actualizará hasta que se obtengan cuarenta datos de un solo valor de resistencia, por lo tanto, los valores que corresponden a su prueba comenzarán a graficarse hasta que comience a obtener los datos en el valor dos de resistencia.

_**Nota:** Las figuras que se muestren al inicio pueden variar._



 ![Graficas](https://github.com/IsauraRs/Turbina/blob/master/Manual/graficas1.png)

_Figura10. Gráfica de resistencia vs revoluciones por minuto y de resistencia vs eficiencia del generador._



![Gráficas2](https://github.com/IsauraRs/Turbina/blob/master/Manual/graficas2.png)

_Figura11. Gráfica de resistencia vs eficiencia del generador y resistencia vs eficiencia de la turbina._



## 3.1. Envío de reporte correspondiente a una prueba



Una vez que decida concluir una prueba, para almacenar los datos en un reporte y enviarlo por correo electrónico, deberá dirijirse a la parte inferior de la página, donde encontrará un apartado en el cual deberá asignar un nombre al reporte y otro en el cual tendrá que ingresar el correo electrónico de destino. 

 Este reporte será almacenado en una base de datos, por lo que, de requerirlo, podrá consultarlo posteriormente. Para saber más acerca de la consulta de reportes diríjase a la sección cinco (5) de este manual.

_**Nota:** debido a que el sistema continuará registrando datos, deberá hacer el paso anterior lo más rápido posible, o con el tiempo suficiente, ya que este apartado se desplazará hacia abajo._



![DatosCorreo](https://github.com/IsauraRs/Turbina/blob/master/Manual/envioReporteP.png)

_Figura12. Apartado para la generación del reporte._



Ya que ha ingresado el nombre para el reporte y el correo electrónico al que será enviado, presione el botón _"Send"_ . Esto puede demorar un par de segundos.



![EnviarReporte](https://github.com/IsauraRs/Turbina/blob/master/Manual/enviarReporte.png)

_Figura13. Enviar reporte._



Esto cerrará el puerto serial de Arduino y lo dirigirá a la página principal, en donde verá un mensaje en el cual se indica el destinatario del reporte.



![ReporteEnviado](https://github.com/IsauraRs/Turbina/blob/master/Manual/paginaInicioRE.png)

_Figura14. Página de inicio una vez que se ha enviado el reporte._



_**Nota:** esto genera que el puerto serial de Arduino se cierre, por lo que, para realizar una nueva prueba inmediatamente después de la que ha concluido, tendrá que "matar" la aplicación desde la terminal presionando las teclas ctrl y c simultáneamente y correr de nuevo la aplicación como lo hizo en el apartado dos (2)  "Inicio" en este manual. De no realizar este paso, la prueba no se reiniciará, sino que continuará a partir del útlimo valor de la prueba anterior, generando error en los cálculos._

