![CEMIEOLogo](https://github.com/IsauraRs/Turbina/blob/master/Manual/CEMIEOLogo.png)





# Manual de usuario para el sistema de adquisición de datos





![IINGENLogo](https://github.com/IsauraRs/Turbina/blob/master/Manual/IINGENLogo.png)















## Índice:





1. ### [Instalación](https://github.com/IsauraRs/Turbina/blob/master/Manual/Manual_de_usuario.md#1-instalaci%C3%B3n) y [conexión.](https://github.com/IsauraRs/Turbina/blob/master/Manual/Manual_de_usuario.md#conexi%C3%B3n)

   

    1. #### Mac OS y Ubuntu.

    2.  #### Windows.

       

2. ### [Inicio.](https://github.com/IsauraRs/Turbina/blob/master/Manual/Manual_de_usuario.md#2-inicio)

     

3. ### [Adquisición de datos.](https://github.com/IsauraRs/Turbina/blob/master/Manual/Manual_de_usuario.md#3-adquisici%C3%B3n-de-datos)

   

4. ### [Reportes.](https://github.com/IsauraRs/Turbina/blob/master/Manual/Manual_de_usuario.md#4-reportes)

      

5. ### [Consultas a datos.](https://github.com/IsauraRs/Turbina/blob/master/Manual/Manual_de_usuario.md#5--consultas-a-datos)

      

6. ### [Consultas a reportes.](https://github.com/IsauraRs/Turbina/blob/master/Manual/Manual_de_usuario.md#6-consultas-a-reportes)



7. ### [Salir del sistema.](https://github.com/IsauraRs/Turbina/blob/master/Manual/Manual_de_usuario.md#7-salir-del-sistema)



8. ### [Conexiones de hardware.](https://github.com/IsauraRs/Turbina/blob/master/Manual/Manual_de_usuario.md#8--conexiones-de-hardware)







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

 Busque en la lista el dispositivo de nombre "SDAdD", de click en él y luego en "Conectar", en caso de que solicite la contraseña ingrese " 1234 " o " 0000 ".

En Linux: Ingrese a "Configuración", diríjase a "Bluetooth" y seleccione el dispositivo de nombre "SDAdD", ingrese la contraseña " 1234 ", en caso de que la contraseña sea incorrecta, ingrese " 0000 ".

Si su distribución es Ubuntu (o alguna distribución basada en Debian) y falla la conexión con el paso anterior, vaya nuevamente a "Configuración", seleccione el dispositivo "SDAdD", revise y copie la dirección del dispositivo.



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

Empareje el dispositivo cuya dirección corresponda a la de "SDAdD":

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





# 4. Reportes.

### Envío de reporte correspondiente a una prueba.

Una vez que decida concluir una prueba, para almacenar los datos en un reporte y enviarlo por correo electrónico, deberá dirijirse a la parte inferior de la página, donde encontrará un apartado en el cual deberá asignar un nombre al reporte y otro en el cual tendrá que ingresar el correo electrónico de destino. 

 Este reporte será almacenado en una base de datos, por lo que, de requerirlo, podrá consultarlo posteriormente. Para saber más acerca de la consulta de reportes diríjase a la sección seis (6) ["Consultas a reportes"](https://github.com/IsauraRs/Turbina/blob/master/Manual/Manual_de_usuario.md#6-consultas-a-reportes) de este manual.

_**Nota:** debido a que el sistema continuará registrando datos, deberá hacer el paso anterior lo más rápido posible, o con el tiempo suficiente, ya que este apartado se desplazará hacia abajo._



![DatosCorreo](https://github.com/IsauraRs/Turbina/blob/master/Manual/envioReporteP.png)

_Figura12. Apartado para la generación del reporte._



Ya que ha ingresado el nombre para el reporte y el correo electrónico al que será enviado, presione el botón _"Send"_ . Esto puede demorar un par de segundos.



![EnviarReporte](https://github.com/IsauraRs/Turbina/blob/master/Manual/enviarReporte.png)

_Figura13. Enviar reporte._



Esto cerrará el puerto serial de Arduino y lo dirigirá a la página principal, en donde verá un mensaje en el cual se indica el destinatario del reporte.



![ReporteEnviado](https://github.com/IsauraRs/Turbina/blob/master/Manual/paginaInicioRE.png)

_Figura14. Página de inicio una vez que se ha enviado el reporte._



_**Nota:** esto genera que el puerto serial de Arduino se cierre, por lo que, para realizar una nueva prueba inmediatamente después de la que ha concluido, tendrá que "matar" la aplicación desde la terminal presionando las teclas ctrl y c simultáneamente y correr de nuevo la aplicación como lo hizo en el apartado dos (2)  ["Inicio"](https://github.com/IsauraRs/Turbina/blob/master/Manual/Manual_de_usuario.md#2-inicio) en este manual. De no realizar este paso, la prueba no se reiniciará, sino que continuará a partir del útlimo valor de la prueba anterior, generando error en los cálculos._





# 5.- Consultas a datos.

Para realizar consultas a datos, presione el botón "Query".



![QueryButton](https://github.com/IsauraRs/Turbina/blob/master/Manual/QueryButton.png)

_Figura15. Botón para consultar datos_



Esto desplegará una lista de opciones de  parámetros a consultar.



![OpcionesDeConsulta](https://github.com/IsauraRs/Turbina/blob/master/Manual/QueryRes4-00.png)

![OpcionesDeConsulta2](https://github.com/IsauraRs/Turbina/blob/master/Manual/QueryRes4-14.png)

_Figuras16 y 17. Página de consultas._



 Para obtener un resultado, ingrese un valor a la casilla correspondiente al parámetro. Por ejemplo:



![ConsultaDP](https://github.com/IsauraRs/Turbina/blob/master/Manual/DPQ.png)

![ResultadoConsultaDP](https://github.com/IsauraRs/Turbina/blob/master/Manual/DPRes.png)

_Figuras18 y 19. Ejemplo de búsqueda de determiado valor del potenciómetro digital._



![ConsultaRPM](https://github.com/IsauraRs/Turbina/blob/master/Manual/RPMQ.png)

![ResultadoConsultaRPM](https://github.com/IsauraRs/Turbina/blob/master/Manual/RPMRes.png)

_Figuras20 y 21. Ejemplo de búsqueda de cierto valor de revoluciones por minuto._



![ConsultaDVin](https://github.com/IsauraRs/Turbina/blob/master/Manual/DVinQ.png)

![ResultadoConsultaDVin](https://github.com/IsauraRs/Turbina/blob/master/Manual/DVinRes.png)

_Figuras22 y 23. Ejemplo de consulta a un valor de diferencial de voltaje de entrada (en el generador)._



![ConsultaVin](https://github.com/IsauraRs/Turbina/blob/master/Manual/VinQ.png)

![ResultadoConsultaVin](https://github.com/IsauraRs/Turbina/blob/master/Manual/VinRes.png)

_Figuras24 y 25. Ejemplo de consulta a determinado valor de voltaje de entrada (en el generador)._



![ConsultaDVout](https://github.com/IsauraRs/Turbina/blob/master/Manual/DVoutQ.png)

![ResultadoConsultaDVout](https://github.com/IsauraRs/Turbina/blob/master/Manual/DVoutRes.png)

_Figuras26 y 27. Ejemplo de consulta a un valor de diferencial de voltaje de salida (en la turbina)._



![ConsultaVout](https://github.com/IsauraRs/Turbina/blob/master/Manual/VoutQ.png)

![ResultadoConsultaVout](https://github.com/IsauraRs/Turbina/blob/master/Manual/VoutRes.png)

_Figuras28 y 29. Ejemplo de búsqueda de un valor de voltaje de salida (en la turbina)._



![ConsultaTiempo](https://github.com/IsauraRs/Turbina/blob/master/Manual/TiempoQ.png)

![ResultadoConsultaTiempo](https://github.com/IsauraRs/Turbina/blob/master/Manual/TiempoRes.png)

_Figuras30 y 31. Ejemplo de consulta a determinado valor de tiempo._



![ConsultaPotencia](https://github.com/IsauraRs/Turbina/blob/master/Manual/PotenciaQ.png)

![ResultadoConsultaPotencia](https://github.com/IsauraRs/Turbina/blob/master/Manual/PotenciaRes.png)

_Figuras32 y 33. Ejemplo de búsqueda de cierto valor de potencia._



Para consultar una gráfica, deberá ingresar la fecha de la prueba en la que se realizó en formato año[4 dígitos]-mes[2 dígitos]-día[2 dígitos], por ejemplo:



![ConsultaRvsRPM](https://github.com/IsauraRs/Turbina/blob/master/Manual/RvsRPMQ.png)

![ResultadoRvsRPM](https://github.com/IsauraRs/Turbina/blob/master/Manual/RvsRPMRes.png)

_Figuras34 y 35. Ejemplo de búsqueda de gráfica de resistencia vs revoluciones por minuto._



![ConsultaRvsEfG](https://github.com/IsauraRs/Turbina/blob/master/Manual/RvsEfGQ.png)

![ResultadoRvsEfG](https://github.com/IsauraRs/Turbina/blob/master/Manual/RvsEfGRes.png)

_Figuras36 y 37. Ejemplo de consulta a gráfica de resistencia vs eficiencia del generador._



![ConsultaRvsEfT](https://github.com/IsauraRs/Turbina/blob/master/Manual/RvsEfTQ.png)

![ResultadoRvsEfT](https://github.com/IsauraRs/Turbina/blob/master/Manual/RvsEfTRes.png)

_Figuras38 y 39. Ejemplo de consulta de gráfica de resistencia vs eficiencia de la turbina._



_**Nota**: Para buscar una gráfica después de haber consultado otra  de un mismo parámetro, por ejemplo, consultar la gráfica de resistencia vs revoluciones por minuto con fecha 2020-12-10 y posteriormente querer consultar la gráfica de  resistencia vs revoluciones por minuto con fecha 2021-01-06, después de presionar el botón "Send" y que traiga un resultado, debe "refrescar" o "volver a cargar" la página para que aparezca la gráfica correcta con el botón en forma de flecha , de otro modo, la que aparecerá será la de la búsqueda anterior._



![Refresh](https://github.com/IsauraRs/Turbina/blob/master/Manual/refreshGraph.png)

_Figura40. Símbolo "refresh"._





# 6. Consultas a reportes.

Como se ha descrito en la sección cuatro (4) ["Reportes"](https://github.com/IsauraRs/Turbina/blob/master/Manual/Manual_de_usuario.md#4-reportes) , es posible almacenar los reportes correspondientes a las pruebas realizadas si se han realizado los pasos mencionados en dicha sección, y del mismo modo, es posible consultarlos, presione el botón "Vew reports".



![VewReportsButton](https://github.com/IsauraRs/Turbina/blob/master/Manual/ViewReportsButton.png)

_Figura41. Botón "View reports"._



Esto desplegará una lista con todos los nombres de los reportes que han sido almacenados. Para obtener alguno, ingrese su correo electrónico en la casilla inmediata al nombre del reporte y de click en el botón "Send".



![VewReportsRes](https://github.com/IsauraRs/Turbina/blob/master/Manual/ViewReportsRes.png) 

_Figura42. Ejemplo del listado de reportes._



Consulte en la bandeja de entrada o en correos no deseados (o Spam) del correo que ingresó, el asunto del correo es "Reporte SdAD" y contendrá dos archivos, el reporte en formato PDF y en formato xlsx.



![ReportesEnviados](https://github.com/IsauraRs/Turbina/blob/master/Manual/ReportesEnviados.png)

_Figura43. Ejemplo del correo recibido como resultado de la consulta a un reporte._





# 7. Salir del sistema.

Para salir del sistema diríjase a la página principal del Sistema de Adquisición de Datos y de click en el botón "Exit".



![ExitButton](https://github.com/IsauraRs/Turbina/blob/master/Manual/ExitButton.png)

_Figura44. Botón "Exit"._



Esto provocará que se cierre la conexión con el servidor, sin embargo, para detener completamente la aplicación en su dispositivo, vaya a la terminal en donde "corrió" la aplicación y presione las teclas ctrl y c simultáneamente.



![ClosedServer](https://github.com/IsauraRs/Turbina/blob/master/Manual/ExitRes.png)

_Figura45. Conexión perdida con el servidor._



_**Nota**: Para regresar a la página de inicio del Sistema de Adquisición de Datos desde cualquier apartado del mismo, puede dar click sobre el logotipo del Insituto de Ingeniería._



![BackButton](https://github.com/IsauraRs/Turbina/blob/master/Manual/backButton.png)

_Figura46. Logotipo del Instituto de Ingeniería como botón de regreso ._







# 8.- Conexiones de hardware.

El sistema de adquisición de datos cuenta con nueve cables, tres de ellos van conectados al sensor de efecto Hall (anaranjado, amarillo y verde), los otros seis son para el generador y para la turbina o el motor (dependiendo del uso), el cable negro debe ir conectado al polo negativo del generador, el rojo al polo positivo del generador, el gris al polo negativo de la tubina o motor y el blanco/beige debe ir conectado al polo positivo de la turbina o motor. Estos cables son para la lectura del diferencial de voltaje de cada uno.

Los cables restantes, amarillo y verde, deben ir a la alimentación del generador, siendo el amarillo al polo positivo y el verde al polo negativo.



![Conexiones](https://github.com/IsauraRs/Turbina/blob/master/Manual/ConexHardware_bb.png)

_Figura47. Vista de planta del esquema en fritzing del sistema de adquisición de datos, el motor del lado derecho representa al generador y el del lado izquierdo a la tubina o motor a caracterizar._