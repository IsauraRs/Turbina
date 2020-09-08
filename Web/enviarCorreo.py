import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#Envía correo de una prueba
###Correo con un PDF adjunto
def enviar_correo_archivo(correo_destinatario, asunto):
    remitente = 'isaura.rs29@gmail.com'
    destinatarios = []
    destinatarios.append(correo_destinatario)
    asunto = asunto
    cuerpo = "Reporte del sistema de adquisición de datos "
    ruta_adjunto = 'table.pdf'
    nombre_adjunto = 'table.pdf'
    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    # Establecemos los atributos del mensaje
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    # Abrimos el archivo que vamos a adjuntar
    archivo_adjunto = open(ruta_adjunto, 'rb')
    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    mensaje.attach(adjunto_MIME)
    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # Ciframos la conexión
    sesion_smtp.starttls()
    # Iniciamos sesión en el servidor
    sesion_smtp.login('isaura.rs29@gmail.com','Irs290797')
    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()
    # Enviamos el mensaje
    try:
        sesion_smtp.sendmail(remitente, destinatarios, texto)
    except:
        print("No se Pudo enviar el Correo a:")
    # Cerramos la conexión
    sesion_smtp.quit()

#Envía reporte de una consulta 
###Correo con un PDF adjunto
def enviar_correo_archivo2(correo_destinatario, asunto):
    remitente = 'isaura.rs29@gmail.com'
    destinatarios = []
    destinatarios.append(correo_destinatario)
    asunto = asunto
    cuerpo = "Reporte del sistema de adquisición de datos "
    ruta_adjunto = 'ReporteAEnviar.pdf'
    nombre_adjunto = 'ReporteAEnviar.pdf'
    # Creamos el objeto mensaje
    mensaje = MIMEMultipart()
    # Establecemos los atributos del mensaje
    mensaje['From'] = remitente
    mensaje['To'] = ", ".join(destinatarios)
    mensaje['Subject'] = asunto
    # Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
    mensaje.attach(MIMEText(cuerpo, 'plain'))
    # Abrimos el archivo que vamos a adjuntar
    archivo_adjunto = open(ruta_adjunto, 'rb')
    # Creamos un objeto MIME base
    adjunto_MIME = MIMEBase('application', 'octet-stream')
    # Y le cargamos el archivo adjunto
    adjunto_MIME.set_payload((archivo_adjunto).read())
    # Codificamos el objeto en BASE64
    encoders.encode_base64(adjunto_MIME)
    # Agregamos una cabecera al objeto
    adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
    # Y finalmente lo agregamos al mensaje
    mensaje.attach(adjunto_MIME)
    # Creamos la conexión con el servidor
    sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)
    # Ciframos la conexión
    sesion_smtp.starttls()
    # Iniciamos sesión en el servidor
    sesion_smtp.login('isaura.rs29@gmail.com','Irs290797')
    # Convertimos el objeto mensaje a texto
    texto = mensaje.as_string()
    # Enviamos el mensaje
    try:
        sesion_smtp.sendmail(remitente, destinatarios, texto)
    except:
        print("No se Pudo enviar el Correo a:")
    # Cerramos la conexión
    sesion_smtp.quit()