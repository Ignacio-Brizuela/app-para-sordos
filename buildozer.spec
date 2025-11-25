[app]

# (str) Título de tu aplicación
title = App Para Sordos

# (str) Nombre del paquete
package.name = appparasordos

# (str) Dominio del paquete (necesario para android/ios)
package.domain = org.sordos

# (str) Directorio donde está el código fuente
source.dir = .

# (list) Patrones de archivos fuente a incluir
source.include_exts = py,png,jpg,kv,atlas

# (list) Directorios a incluir
source.include_patterns = models/*,services/*,ui/*

# (str) Versión de la aplicación
version = 0.3

# (list) Permisos de la aplicación
android.permissions = INTERNET

# (int) Target Android API
android.api = 33

# (int) Minimum API
android.minapi = 21

# (str) Android NDK version
android.ndk = 25b

# (bool) Indicar si la aplicación está en modo landscape
orientation = portrait

# (bool) Indicar si se activa el modo de pantalla completa
fullscreen = 0

# (list) Requerimientos de la aplicación
requirements = python3==3.10.6,kivy==2.3.0,pyjnius,android,plyer,requests,certifi,charset-normalizer

# (str) Presplash background color
android.presplash_color = #3498DB

# (bool) Indicar si se debe copiar las librerías de Android
p4a.bootstrap = sdl2

# (str) Rama de python-for-android a usar
# p4a.branch = develop

# (str) Ícono de la aplicación (reemplaza con tu propio ícono)
#icon.filename = %(source.dir)s/icon.png

# (str) Arquitecturas soportadas
android.archs = arm64-v8a, armeabi-v7a

[buildozer]

# (int) Log level (0 = error only, 1 = info, 2 = debug)
log_level = 2

# (int) Display warning if buildozer está desactualizado
warn_on_root = 1
