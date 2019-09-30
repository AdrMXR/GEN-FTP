<p align="center"><img src="https://byteweb.es/storage/elementor/thumbs/Como-funciona-el-protocolo-FTP-o1h0xe4trsdyfwb8sagoops4lvsx8yg8ujzuatpjxc.png" /></p>

## Acerca de
FTP es un protocolo de transferencia de archivos entre sistemas conectados a una red TCP basado en la arquitectura cliente-servidor, de manera que desde un equipo cliente nos podemos conectar a un servidor para descargar archivos desde él o para enviarle nuestros propios archivos independientemente del sistema operativo utilizado en cada equipo. GEN-FTP se encarga de generar este tipo de servidores de manera automatizada para así evitar posibles problemas al hacerlo manualmente. 

## ¿Cómo funciona?
GEN-FTP consta de 2 opciones:

* FTP local: Al seleccionar esta opción estamos indicando que queremos generar un servidor FTP que funcione unicamente dentro de nuestra red interna. Al instalarse las dependencias necesarias como primera petición GEN-FTP nos solicitará un usuario y una contraseña con las cuales vamos a accesar a nuestro servidor, posteriormente nos solicitaran un nombre para nuestra carpeta donde serán alojados todos nuestros archivos que deseamos agregar a nuestro servidor y posterior a ello se creará una limitación a esa carpeta para que el usuario FTP no pueda navegar en nuestras carpetas personales o en archivos del propio sistema y así solamente tenga un directorio predeterminado, esto se le conoce como enjaulación. También cabe destacar que es necesario crear una shell especifica para el usuario FTP por medidas de seguridad, el archivo archftp contiene esta shell personalizada y será transferido a su directorio /bin y será sobreescrito el directorio /bin/archftp al archivo /etc/shells para que la shell funcione correctamente. Posteriormente, el archivo vsftpd.conf será transferido al directorio /etc ya que este contiene las configuraciones necesarias de su servidor FTP. Y por ultimo, el servicio vsftpd se pondrá en marcha. Al terminar este proceso GEN-FTP nos cuestionará si deseamos acceder o no a nuestro servidor FTP creado.

* FTP público: Con esta opción estamos indicando que queremos generar un servidor FTP que funcione en cualquier parte del mundo con acceso a internet. GEN-FTP nos cuestiona primero si ya contamos con un FTP local, esto es porque antes de tener un FTP público primero debemos de tener un FTP local para configurar los puertos correspondientes en la configuración de nuestro router y así las peticiones públicas sean redirigidas a nuestro servidor local. En caso de que la respuesta sea negativa se pondrá en marcha la opción numero 1 de FTP local y al final nos volverá a cuestionar la misma pregunta y así seguirá hasta que la respuesta sea positiva. Posteriormente GEN-FTP nos solicitará nuestro gateway que se puede obtener con el siguiente comando:
```bash
route -n 
```
Posteriormente, se nos abrirá automaticamente el login de nuestro router. 
<p align="center"><img src="https://github.com/AdrMXR/GEN-FTP/blob/master/screenshot-1.png" /></p>
Si tienen problemas con el seguimiento de este proceso les recomiendo buscar en internet como abrir puertos en su correspondiente router, ya que el proceso puede variar por los diferentes modelos. 

Posteriormente, ya que hayamos iniciado con nuestro usuario y contraseña de nuestro internet, buscaremos el apartado llamado NAT, para configurar los puertos correspondientes. 

<p align="center"><img src="https://github.com/AdrMXR/GEN-FTP/blob/master/screenshot-2.png" /></p>

Una vez en este apartado, seleccionaremos la opción de servidores y especificaremos que tipo de servidor es con el que queremos trabajar, pondremos una pequeña descripción y seleccionaremos la IP de nuestro servidor local, en PUERTO LAN pondremos el puerto 21 que esta por default y en PUERTO PUBLICO podemos poner el mismo o cualquier otro. 



