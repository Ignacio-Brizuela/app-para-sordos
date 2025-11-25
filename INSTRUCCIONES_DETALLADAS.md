# 📱 GUÍA PASO A PASO: Compilar APK en Google Colab

## 🎯 OBJETIVO
Crear un archivo APK de Android para tu aplicación "App Para Sordos" que incluye reconocimiento de voz nativo.

---

## 📋 REQUISITOS PREVIOS

### Lo que necesitas:
- ✅ Cuenta de Google (Gmail)
- ✅ Navegador web (Chrome, Firefox, Edge)
- ✅ Conexión a internet estable
- ✅ 1 hora de tiempo disponible
- ✅ Los archivos del proyecto (ya los tienes)

### Archivos importantes:
1. `BUILD_APK_COLAB.ipynb` - El notebook de Colab
2. `APP_PARA_SORDOS.zip` - Tu proyecto comprimido (24.72 KB)

---

## 🚀 PASO 1: ABRIR GOOGLE COLAB

### 1.1 Ir a Google Colab
```
1. Abre tu navegador
2. Ve a: https://colab.research.google.com/
3. Inicia sesión con tu cuenta de Google
```

### 1.2 Subir el Notebook
```
1. En la página principal de Colab, haz clic en "Archivo"
2. Selecciona "Subir notebook"
3. Arrastra BUILD_APK_COLAB.ipynb a la ventana
   O haz clic en "Elegir archivo" y selecciónalo

Deberías ver algo como:
┌─────────────────────────────────────┐
│ 📱 BUILD APK - App Para Sordos      │
│                                     │
│ Este notebook te guiará...          │
└─────────────────────────────────────┘
```

---

## ⚙️ PASO 2: INSTALAR DEPENDENCIAS

### 2.1 Ejecutar Primera Celda

```
1. Ubica la primera celda de código (tiene texto como "!apt-get update")
2. Haz clic en el botón ▶️ a la izquierda de la celda
   O presiona Shift + Enter
3. ESPERA 5-10 minutos
```

**Lo que verás:**
```
Installing...
Reading package lists... Done
Building dependency tree... Done
...
✅ Dependencias instaladas correctamente
```

**⚠️ IMPORTANTE:**
- NO cierres la pestaña
- NO apagues la computadora
- Puedes minimizar el navegador

---

## 📦 PASO 3: SUBIR TU PROYECTO

### 3.1 Opción Recomendada: Subir ZIP

```
1. Desplázate hasta la celda que dice:
   "📦 Sube el archivo ZIP con todo el proyecto"

2. Haz clic en el botón ▶️ para ejecutar la celda

3. Verás un botón "Elegir archivos"

4. Haz clic en "Elegir archivos"

5. Busca y selecciona: APP_PARA_SORDOS.zip

6. Haz clic en "Abrir"

7. Espera a que se suba (unos segundos)
```

**Lo que verás:**
```
📂 Descomprimiendo APP_PARA_SORDOS.zip...

✅ Proyecto descomprimido correctamente

📂 Estructura del proyecto:
main.py
buildozer.spec
requirements.txt
models/
  __init__.py
  transcription.py
services/
  __init__.py
  audio_service.py
  audio_service_android.py
ui/
  __init__.py
  microphone_screen.py

✅ main.py encontrado
✅ buildozer.spec encontrado
```

**✅ TODO BIEN si ves esos dos últimos checks**

---

## 🔨 PASO 4: COMPILAR EL APK (30-40 MINUTOS)

### 4.1 Iniciar Compilación

```
1. Busca la celda que dice:
   "3️⃣ Compilar APK (30-40 minutos) ⏳"

2. Lee el mensaje de advertencia:
   "⚠️ IMPORTANTE: Este proceso tarda 30-40 minutos"

3. Haz clic en el botón ▶️

4. ESPERA PACIENTEMENTE
```

**Lo que verás:**
```
🔨 Iniciando compilación del APK...
⏰ Hora de inicio: 14:23:45

⚠️ IMPORTANTE:
   - Este proceso tarda 30-40 minutos
   - NO cierres esta pestaña
   - Puedes minimizar pero mantén la sesión activa

============================================================

# Buildozer detecta tu proyecto
[INFO]:    Building for armeabi-v7a and arm64-v8a
[INFO]:    Downloading Android SDK...
[INFO]:    Downloading Android NDK...
[INFO]:    Compiling Kivy...
[INFO]:    Compiling Python...
[INFO]:    Packaging application...

... (muchas líneas de texto) ...

[INFO]:    APK created successfully
============================================================

⏰ Hora de finalización: 15:03:12

✅ Compilación completada
```

### 4.2 Durante la Compilación

**PUEDES:**
- ✅ Minimizar la ventana
- ✅ Usar otras pestañas
- ✅ Ver videos (en otra pestaña)
- ✅ Trabajar en otras cosas

**NO PUEDES:**
- ❌ Cerrar la pestaña de Colab
- ❌ Apagar la computadora
- ❌ Quedarte sin internet
- ❌ Dejar que la laptop se suspenda

**💡 TIP:** Configura tu laptop para que no se suspenda:
- Windows: Panel de control → Energía → "Nunca" en suspensión
- Mac: Preferencias → Ahorro de energía → Desactivar suspensión

---

## ⚠️ SI HAY UN ERROR DURANTE LA COMPILACIÓN

### Error Común: "Command failed"

Si ves algo como:
```
# Command failed: ['/usr/bin/python3', '-m', 'pythonforandroid.toolchain'...
# Buildozer failed to execute the last command
```

**SOLUCIÓN:**

```
1. Busca la celda que dice:
   "⚠️ Si hay error en la compilación"

2. Ejecuta esa celda (botón ▶️)

3. Verás:
   🧹 Limpiando builds anteriores...
   ✅ Limpieza completa

4. VUELVE al Paso 4.1 (compilar de nuevo)

5. Esta vez debería funcionar
```

---

## ⬇️ PASO 5: DESCARGAR EL APK

### 5.1 Verificar APK

```
1. Busca la celda que dice:
   "4️⃣ Verificar y descargar APK"

2. Haz clic en el botón ▶️

3. Verás algo como:
```

**Salida esperada:**
```
✅ APK encontrado: appparasordos-0.1-debug.apk
📦 Tamaño: 25.43 MB
📍 Ubicación: bin/appparasordos-0.1-debug.apk

⬇️ Descargando APK...

🎉 ¡APK descargado correctamente!
```

### 5.2 Ubicación del APK

El archivo se descargará a:
- **Windows:** `C:\Users\TuNombre\Downloads\appparasordos-0.1-debug.apk`
- **Mac:** `/Users/TuNombre/Downloads/appparasordos-0.1-debug.apk`

**Tamaño esperado:** 20-30 MB

---

## 📱 PASO 6: INSTALAR EN ANDROID

### 6.1 Transferir APK al Teléfono

**Opción A - Cable USB:**
```
1. Conecta tu Android a la computadora con cable USB
2. En el teléfono, toca la notificación USB
3. Selecciona "Transferencia de archivos"
4. Copia el APK a la carpeta "Downloads" del teléfono
```

**Opción B - Google Drive:**
```
1. Ve a drive.google.com
2. Haz clic en "Nuevo" → "Subir archivo"
3. Selecciona el APK
4. En tu teléfono, abre Google Drive
5. Descarga el APK
```

**Opción C - Email:**
```
1. Envíate el APK por email
2. En tu teléfono, abre el email
3. Descarga el archivo adjunto
```

**Opción D - WhatsApp:**
```
1. Envía el APK a ti mismo o a un contacto
2. Descarga el archivo en el teléfono
```

### 6.2 Habilitar Instalación de Fuentes Desconocidas

```
ANDROID 8.0+ (Oreo y superiores):

1. Abre la aplicación "Archivos" o "Descargas"
2. Busca el APK
3. Toca el APK para instalarlo
4. Verás: "Por tu seguridad, no se permite instalar..."
5. Toca "Configuración"
6. Activa "Permitir de esta fuente"
7. Presiona el botón "Atrás"
8. Toca el APK de nuevo

ANDROID 7.0 y anteriores:

1. Ve a Ajustes
2. Seguridad
3. Activa "Fuentes desconocidas"
4. Toca "Aceptar" en el mensaje de advertencia
```

### 6.3 Instalar APK

```
1. Abre la aplicación "Archivos" o "Mi archivos"
2. Ve a la carpeta "Descargas" o "Downloads"
3. Busca: appparasordos-0.1-debug.apk
4. Toca el archivo
5. Toca "Instalar"
6. Espera 5-10 segundos
7. Toca "Abrir" cuando termine
```

**Pantalla de instalación:**
```
┌─────────────────────────────────────┐
│  ¿Instalar esta app?                │
│                                     │
│  📱 App Para Sordos                 │
│     Versión 0.1                     │
│                                     │
│  Esta app solicitará acceso a:      │
│  • Micrófono                        │
│  • Internet                         │
│                                     │
│  [Cancelar]        [Instalar]       │
└─────────────────────────────────────┘
```

---

## 🎤 PASO 7: USAR LA APLICACIÓN

### 7.1 Primera Vez

```
1. Abre "App Para Sordos" desde el cajón de apps

2. Verás la pantalla principal:
   ┌─────────────────────────────────┐
   │   Asistente para Sordos         │
   │                                 │
   │ Selecciona el método de entrada │
   │                                 │
   │  [📝 Entrada de Texto]          │
   │                                 │
   │  [🎤 Entrada de Micrófono]      │
   └─────────────────────────────────┘

3. Toca "🎤 Entrada de Micrófono"

4. Aparecerá un mensaje:
   "¿Permitir que App Para Sordos grabe audio?"

5. Toca "Permitir" o "Mientras se usa la app"
```

### 7.2 Usar el Reconocimiento de Voz

```
1. Toca el botón "🎙️ Iniciar Grabación"

2. El botón cambiará a "⏹️ Detener Grabación" (rojo)

3. Habla claramente al micrófono:
   "Hola, ¿cómo estás?"

4. El texto aparecerá carácter por carácter:
   ┌─────────────────────────────────┐
   │ H                               │
   │ Ho                              │
   │ Hol                             │
   │ Hola                            │
   │ Hola,                           │
   │ Hola, ¿c                        │
   │ Hola, ¿có                       │
   │ Hola, ¿cómo                     │
   │ Hola, ¿cómo e                   │
   │ Hola, ¿cómo es                  │
   │ Hola, ¿cómo est                 │
   │ Hola, ¿cómo está                │
   │ Hola, ¿cómo estás               │
   │ Hola, ¿cómo estás?              │
   └─────────────────────────────────┘

5. Sigue hablando, el texto se agregará automáticamente

6. Para detener, toca "⏹️ Detener Grabación"

7. Para limpiar el texto, toca "🗑️ Limpiar"

8. Para volver al menú, toca "← Volver"
```

---

## ✅ VERIFICACIÓN FINAL

### ¿Funciona correctamente?

**Prueba esto:**

```
✅ La app se instaló sin errores
✅ La app se abre correctamente
✅ Puedes acceder a "Entrada de Micrófono"
✅ El permiso de micrófono se solicitó
✅ Al hablar, aparece texto
✅ El texto aparece carácter por carácter
✅ Puedes limpiar el texto
✅ Puedes volver al menú principal
```

**Si TODO está ✅ : ¡FELICIDADES! La app funciona perfectamente** 🎉

---

## 🐛 SOLUCIÓN DE PROBLEMAS

### Problema 1: "No se puede instalar la app"

**Causa:** Fuentes desconocidas no habilitadas

**Solución:** Ve al Paso 6.2 de esta guía

---

### Problema 2: "La app se cierra al abrirla"

**Causa:** APK corrupto o mal compilado

**Solución:**
```
1. Desinstala la app del teléfono
2. Vuelve a Google Colab
3. Ejecuta la celda de "Limpiar build"
4. Vuelve a compilar (Paso 4)
5. Descarga el nuevo APK
6. Instala de nuevo
```

---

### Problema 3: "El micrófono no funciona"

**Causa:** Permisos no concedidos

**Solución:**
```
1. Ve a Ajustes del teléfono
2. Apps → App Para Sordos
3. Permisos
4. Activa "Micrófono"
5. Abre la app de nuevo
```

---

### Problema 4: "No aparece texto al hablar"

**Causas posibles:**
- Sin conexión a internet
- Permisos denegados
- Micrófono defectuoso

**Solución:**
```
1. Verifica conexión WiFi/datos
2. Verifica permisos (ver Problema 3)
3. Prueba con otra app de grabación
4. Habla MÁS CERCA del micrófono
5. Habla MÁS CLARO
```

---

### Problema 5: "Compilación falla en Colab"

**Solución:** Lee el archivo `SOLUCION_ERRORES_COLAB.md`

O ejecuta la celda de limpieza (ver Paso 4, sección de errores)

---

## 📊 TIEMPOS ESTIMADOS

| Paso | Tiempo |
|------|--------|
| 1. Abrir Colab | 2 min |
| 2. Instalar dependencias | 5-10 min |
| 3. Subir proyecto | 1 min |
| 4. Compilar APK | 30-40 min |
| 5. Descargar APK | 1 min |
| 6. Instalar en Android | 5 min |
| 7. Probar app | 2 min |
| **TOTAL** | **46-61 min** |

---

## 💡 CONSEJOS IMPORTANTES

### Durante la Compilación:
1. **NO cierres la pestaña de Colab**
2. **Mantén conexión a internet estable**
3. **No dejes que la laptop se suspenda**
4. **Ten paciencia** - 30-40 minutos es normal

### Al Instalar en Android:
1. **Habilita fuentes desconocidas ANTES de instalar**
2. **Concede TODOS los permisos que pida la app**
3. **Ten conexión a internet** (para el reconocimiento de voz)

### Al Usar la App:
1. **Habla CLARO y DESPACIO**
2. **Acércate al micrófono**
3. **Evita ruido de fondo**
4. **Usa conexión WiFi estable**

---

## 🎯 RESUMEN EJECUTIVO

```
1. Abre Google Colab
2. Sube BUILD_APK_COLAB.ipynb
3. Ejecuta celda 1 (instalar dependencias) ⏱️ 10 min
4. Ejecuta celda 2 (subir ZIP) ⏱️ 1 min
5. Ejecuta celda 3 (compilar) ⏱️ 40 min
6. Ejecuta celda 4 (descargar) ⏱️ 1 min
7. Transfiere APK a Android
8. Instala APK
9. Abre app y concede permisos
10. ¡Usa la app! 🎉
```

---

## 📞 AYUDA ADICIONAL

Si tienes problemas:

1. Lee `SOLUCION_ERRORES_COLAB.md`
2. Lee `GUIA_APK.md`
3. Lee `IMPLEMENTACION_ANDROID.md`

---

## ✨ ¡FELICIDADES!

Si llegaste hasta aquí y todo funcionó:

**¡HAS CREADO EXITOSAMENTE UNA APP DE ANDROID PARA AYUDAR A PERSONAS SORDAS!** 🎉📱💙

La aplicación puede:
- ✅ Capturar audio del micrófono
- ✅ Transcribir voz a texto en tiempo real
- ✅ Mostrar el texto con animación suave
- ✅ Funcionar en dispositivos Android reales

**¡Excelente trabajo!** 👏

---

**Fecha de esta guía:** Noviembre 22, 2025
**Versión:** 1.0
