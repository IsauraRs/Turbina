![CEMIEOLogo](https://github.com/IsauraRs/Turbina/blob/master/Manual/CEMIEOLogo.png)





# Manual de usuario para el sistema de adquisición de datos





![IINGENLogo](https://github.com/IsauraRs/Turbina/blob/master/Manual/IINGENLogo.png)















## Índice:





1. ### Instalación y conexión.

   

    1. #### Mac OS y Ubuntu.

    2. #### Windows.

       

2. ### Inicio.

     

3. ### Adquisición de datos.

    

4. ### Reportes.

    

5. ### Consultas a datos.

    

6. ### Consultas a reportes.









# 1. Instalación.



## 1.1. Mac OS y Linux.

Ingrese a: https://github.com/IsauraRs/Turbina y en la pestaña "Code", seleccione la opción "Download ZIP". 

_**Nota**: de click derecho sobre el enlace y seleccione "Abrir enlace en una nueva pestaña" o saldrá del manual._



![downloads](https://github.com/IsauraRs/Turbina/blob/master/Manual/downloadSS.png)



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



En  MacOS, o a:



![ubuntuSS](https://github.com/IsauraRs/Turbina/blob/master/Manual/ubuntuSS.png)



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

Para iniciar la aplicación, una vez realizada la instalación y, en caso de requerirlo, la conexión, en la terminal, vaya a la carpeta "Turbina-master" e ingrese a  la carpeta "Web", ya que haya ingresado ejecute el siguiente comando:

```
python3 app.py 
```

En caso de que no tenga conectado un *Arduino*, le aparecerá un cuadro de alerta (o más de uno).



![tkWarning](https://github.com/IsauraRs/Turbina/blob/master/Manual/tkSS.png)



Basta con pulsar el botón "OK", si su intención es realizar búsquedas, si su intención es realizar pruebas, será necesario conectar el Sistema de Adquisición de Datos.

Hecho lo anterior, abra su navegador web y en el buscador escriba  http://127.0.0.1:5000/ , lo que lo llevará a la página principal del Sistema de Adquisición de Datos.



![PaginaPrinc](https://github.com/IsauraRs/Turbina/blob/master/Manual/ppsdad.png)



# 3. Adquisición de datos.

Para comenzar la toma de datos, presione el botón "Begin test".

