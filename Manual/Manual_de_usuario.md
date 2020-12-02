```HTML
<img src = "/home/isaura/Documentos/Datos/Web/static/img/image4.png">
```



![image4](/home/isaura/Documentos/Datos/Web/static/img/image4.png)



# Manual de usuario para el sistema de adquisición de datos



![Logo IINGEN](/home/isaura/Documentos/Datos/Web/static/img/image72.png)



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

![image-20201201144947068](/home/isaura/snap/typora/31/.config/Typora/typora-user-images/image-20201201144947068.png)

![image-20201201145314180](/home/isaura/snap/typora/31/.config/Typora/typora-user-images/image-20201201145314180.png)

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

![image-20201201185057708](/home/isaura/snap/typora/31/.config/Typora/typora-user-images/image-20201201185057708.png)

En  MacOS, o a:

![image-20201201185632045](/home/isaura/snap/typora/31/.config/Typora/typora-user-images/image-20201201185632045.png)

En Ubuntu. Es probable que a usted no le aparezcan las alertas que aparecen en amarillo.

Una vez realizado este paso, salga a la carpeta "Turbina-master" e ingrese a  la carpeta "Web" (en la terminal), ya que haya ingresado escriba el siguiente comando:

```
python3 app.py 
```

En caso de que no tenga conectado un arduino, le aparecerá un cuadro de alerta (o más de uno).

![image-20201201192419402](/home/isaura/snap/typora/31/.config/Typora/typora-user-images/image-20201201192419402.png)

Basta con pulsar el botón "OK", si su intención es realizar búsquedas, si su intención es realizar pruebas, será necesario conectar el Sistema de Adquisición de Datos.

