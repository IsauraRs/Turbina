![CEMIEOLogo](https://github.com/IsauraRs/Turbina/blob/master/Manual/CEMIEOLogo.png)





# Manual de usuario para el sistema de adquisición de datos





![IINGENLogo](https://github.com/IsauraRs/Turbina/blob/master/Manual/IINGENLogo.png)



## Índice:





1. ### Instalación

   

    1. #### Mac OS y Ubuntu

    2. #### Windows

       

2. ### Adquisición de datos

   

3. ### Reportes

   

4. ### Consultas a datos

   

5. ### Consultas a reportes









# 1. Instalación



1.1. Mac OS y Ubuntu

Ingrese a: https://github.com/IsauraRs/Turbina y en la pestaña "Code", seleccione la opción "Download ZIP".

![downloads](https://github.com/IsauraRs/Turbina/blob/master/Manual/downloadSS.png)

Una vez terminada la descarga, extraiga la carpeta "Turbina-master" en una alguna ubicación conozca.

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

En Ubuntu. Es probable que a usted no le aparezcan las alertas que aparecen en amarillo.

Una vez realizado este paso, salga a la carpeta "Turbina-master" e ingrese a  la carpeta "Web" (en la terminal), ya que haya ingresado escriba el siguiente comando:

```
python3 app.py 
```

En caso de que no tenga conectado un arduino, le aparecerá un cuadro de alerta (o más de uno).

![tkWarning](https://github.com/IsauraRs/Turbina/blob/master/Manual/tkSS.png)

Basta con pulsar el botón "OK", si su intención es realizar búsquedas, si su intención es realizar pruebas, será necesario conectar el Sistema de Adquisición de Datos.

