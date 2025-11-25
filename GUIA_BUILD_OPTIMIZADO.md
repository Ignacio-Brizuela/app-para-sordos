# 📚 Guía Rápida - Build APK Optimizado

## 🎯 ¿Qué hay de nuevo?

### ⚡ Build Incremental
Ya no necesitas esperar 40 minutos cada vez que hagas un cambio pequeño. El nuevo sistema de **build incremental** te permite actualizar tu APK en solo 5-10 minutos.

### ✨ Funcionalidades Completas
- ✅ Reconocimiento de voz con micrófono (Android nativo)
- ✅ Texto a voz (TTS nativo de Android)
- ✅ Navegación completa con botones "Volver"
- ✅ UI mejorada y consistente

---

## 🚀 Inicio Rápido

### Primera Vez (Build Completo)

1. **Preparar proyecto en tu PC**
   ```powershell
   # Ejecuta el script para crear ZIP
   .\crear_zip_para_colab.ps1
   ```

2. **Abrir Colab**
   - Sube `BUILD_APK_COLAB_OPTIMIZADO.ipynb` a Google Colab
   - O abre directamente desde Drive

3. **Ejecutar celdas en orden**
   ```
   Celda 1: Instalar dependencias (5-10 min)
   Celda 2A: Subir ZIP completo (2-3 min)
   Celda 3: Verificar configuración (30 seg)
   Celda 4: BUILD COMPLETO (40-50 min) ⏳
   Celda 6: Descargar APK (1 min)
   ```

4. **Tiempo total**: ~50-65 minutos

### Actualización Rápida (Build Incremental)

Cuando solo modifiques archivos Python (`.py`):

1. **Modificar archivos en tu PC**
   - Edita solo los archivos que necesites
   - Por ejemplo: `main.py`, `models/text_model.py`, etc.

2. **Abrir Colab con tu sesión anterior**
   - Usa el mismo notebook
   - Si cerraste Colab, vuelve a ejecutar desde celda 1

3. **Ejecutar celdas seleccionadas**
   ```
   Celda 1: Instalar dependencias (5-10 min)
   Celda 2B: Subir archivos modificados (1 min)
   Celda 5: BUILD INCREMENTAL (5-10 min) ⚡
   Celda 6: Descargar APK (1 min)
   ```

4. **Tiempo total**: ~12-22 minutos 🚀

---

## 📋 Cuándo usar cada build

### Build Completo (Celda 4) 🐢
Úsalo cuando:
- ❗ Es tu primera compilación
- ❗ Modificaste `buildozer.spec`
- ❗ Cambiaste dependencias/requirements
- ❗ Agregaste nuevos permisos
- ❗ El build incremental falló

### Build Incremental (Celda 5) ⚡
Úsalo cuando:
- ✅ Solo modificaste archivos `.py`
- ✅ Cambios en UI (main.py, microphone_screen.py)
- ✅ Cambios en lógica (models, services)
- ✅ Ya hiciste un build completo anteriormente
- ✅ Quieres probar cambios rápidamente

---

## 🛠️ Archivos que puedes modificar

### Actualización rápida (Build Incremental)
Estos archivos se pueden actualizar con build incremental:

| Archivo | Descripción |
|---------|-------------|
| `main.py` | Pantalla principal y navegación |
| `models/text_model.py` | Texto a voz |
| `models/transcription.py` | Modelo de transcripción |
| `services/audio_service_android.py` | Reconocimiento de voz |
| `ui/microphone_screen.py` | Interfaz de micrófono |

### Requiere Build Completo
Si modificas estos, necesitas build completo:

| Archivo | Descripción |
|---------|-------------|
| `buildozer.spec` | Configuración de la app |
| `requirements.txt` | Dependencias Python |
| Permisos Android | Cambios en permissions |
| Recursos nuevos | Imágenes, íconos, etc. |

---

## 🎨 Ejemplos de Uso

### Ejemplo 1: Cambiar color de botones
```python
# Modificar en main.py
COLOR_BTN_TEXTO = '#3498DB'  # Cambiar a azul
COLOR_BTN_MIC = '#E74C3C'    # Cambiar a rojo
```

**Build**: ⚡ Incremental (Celda 5)

### Ejemplo 2: Agregar nuevo permiso
```ini
# Modificar en buildozer.spec
android.permissions = RECORD_AUDIO,INTERNET,CAMERA
```

**Build**: 🐢 Completo (Celda 4)

### Ejemplo 3: Cambiar texto de la UI
```python
# Modificar en ui/microphone_screen.py
title = Label(
    text='🎤 Nueva Transcripción',  # Cambiar texto
    ...
)
```

**Build**: ⚡ Incremental (Celda 5)

### Ejemplo 4: Actualizar versión
```ini
# Modificar en buildozer.spec
version = 0.3
```

**Build**: 🐢 Completo (Celda 4)

---

## ⚠️ Solución de Problemas

### Error: "No existe build anterior"
**Solución**: Ejecuta Build Completo (Celda 4) primero

### Error: "Module not found"
**Solución**: Verifica requirements.txt y ejecuta Build Completo

### Error: "Permission denied"
**Solución**: Agrega permisos en buildozer.spec y Build Completo

### Build tarda más de 1 hora
**Solución**: 
1. Verifica tu conexión a internet
2. Revisa si Colab tiene recursos disponibles
3. Intenta en horario de menor carga

### APK no se descarga
**Solución**: Ejecuta Celda 6 (Verificar y descargar APK)

---

## 💡 Tips Pro

### 1. Mantener sesión de Colab activa
- No cierres la pestaña durante compilación
- Puedes minimizar pero mantén navegador abierto

### 2. Guardar tiempo
- Usa build incremental siempre que sea posible
- Solo usa build completo cuando sea necesario

### 3. Testing
- Prueba cambios en escritorio primero (más rápido)
- Cuando funcione, compila APK

### 4. Versionado
- Cambia version en buildozer.spec antes de cada build
- Te ayuda a identificar qué APK es más reciente

### 5. Backup
- Guarda los APK generados con nombre descriptivo
- Ejemplo: `app_v0.2_cambio_colores.apk`

---

## 📱 Instalar APK en Android

1. **Descargar APK** desde Colab (Celda 6)

2. **Transferir a Android**
   - Email
   - Google Drive
   - Cable USB
   - AirDrop (si tienes iPhone/Mac)

3. **Habilitar instalación**
   - Ajustes → Seguridad
   - "Orígenes desconocidos" → Activar

4. **Instalar**
   - Abrir APK descargado
   - Tocar "Instalar"
   - Aceptar permisos

5. **Permisos requeridos**
   - 🎤 Micrófono
   - 🌐 Internet
   - 💾 Almacenamiento

---

## ✅ Checklist Pre-Build

Antes de compilar, verifica:

- [ ] Modificaste solo archivos necesarios
- [ ] Decidiste qué tipo de build usar (completo/incremental)
- [ ] Tienes los archivos listos para subir
- [ ] Conexión a internet estable
- [ ] Tiempo disponible (12 min o 50 min)
- [ ] Colab tiene recursos disponibles

---

## 📊 Comparación de Tiempos

| Proceso | Build Completo | Build Incremental |
|---------|----------------|-------------------|
| Instalar deps | 5-10 min | 5-10 min |
| Subir archivos | 2-3 min | 1 min |
| Compilación | 40-50 min ⏳ | 5-10 min ⚡ |
| Descarga | 1 min | 1 min |
| **TOTAL** | **~50-65 min** | **~12-22 min** |
| **Ahorro** | - | **~35-45 min** 🎉 |

---

## 🎓 Preguntas Frecuentes

**P: ¿Puedo usar build incremental después de cerrar Colab?**  
R: No, necesitas hacer build completo de nuevo. Mantén la sesión abierta.

**P: ¿Funciona el micrófono en el APK?**  
R: Sí, usa SpeechRecognizer nativo de Android.

**P: ¿Funciona sin internet?**  
R: El micrófono puede requerir internet para algunos servicios de Google.

**P: ¿Puedo cambiar el ícono de la app?**  
R: Sí, pero requiere build completo.

**P: ¿Funciona en todas las versiones de Android?**  
R: Sí, desde Android 5.0 (API 21) en adelante.

---

## 📞 Soporte

Si tienes problemas:
1. Revisa la sección "Solución de problemas" del notebook
2. Ejecuta la celda de "Ver logs" para debugging
3. Verifica la sección de errores comunes

---

**¡Disfruta de tu app actualizada!** 🎉
