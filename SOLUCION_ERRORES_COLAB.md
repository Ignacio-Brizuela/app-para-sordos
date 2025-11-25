# 🔧 Solución de Errores en Google Colab

## ❌ Error: "Command failed: pythonforandroid.toolchain"

### Causa
Este error ocurre cuando hay dependencias incompatibles o problemas en el caché de buildozer.

### Solución 1: Limpiar y Reintentar

En Google Colab, ejecuta:

```python
# Limpiar completamente
!rm -rf .buildozer
!rm -rf bin

# Volver a compilar
!buildozer -v android debug
```

### Solución 2: Verificar buildozer.spec

Asegúrate de que los requirements solo incluyan dependencias compatibles:

```ini
# CORRECTO
requirements = python3,kivy,pyjnius,android

# INCORRECTO (causa errores)
requirements = python3,kivy,pyjnius,android,requests,certifi,...
```

### Solución 3: Usar versión estable de p4a

En `buildozer.spec`, comenta la línea de branch:

```ini
# p4a.branch = develop
```

O usa una versión estable:

```ini
p4a.branch = master
```

## ❌ Error: "No module named 'jnius'"

### Causa
Pyjnius no está en los requirements o no se compiló.

### Solución

Verifica que `buildozer.spec` contenga:

```ini
requirements = python3,kivy,pyjnius,android
```

## ❌ Error: "SDK not found" o "NDK not found"

### Causa
Buildozer no descargó correctamente SDK/NDK.

### Solución

```python
# Limpiar y forzar re-descarga
!buildozer android clean
!rm -rf ~/.buildozer/android/platform/android-sdk
!rm -rf ~/.buildozer/android/platform/android-ndk*

# Volver a compilar
!buildozer -v android debug
```

## ❌ Error de Memoria en Colab

### Causa
Compilación consume mucha RAM.

### Solución

1. En Colab: **Runtime → Factory reset runtime**
2. Volver a ejecutar desde celda 1

## ❌ Error: "Architecture not found"

### Causa
Arquitecturas mal especificadas.

### Solución

En `buildozer.spec`:

```ini
# Usar sin espacios
android.archs = arm64-v8a,armeabi-v7a
```

## 🔍 Ver Logs Detallados

Para ver exactamente dónde falla:

```python
# Ver últimas 100 líneas del log
!tail -n 100 .buildozer/android/platform/build-*/build.log
```

## ✅ Configuración Recomendada

Aquí está la configuración que **SÍ FUNCIONA**:

```ini
[app]
title = App Para Sordos
package.name = appparasordos
package.domain = org.sordos
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.include_patterns = models/*,services/*,ui/*
version = 0.1

android.permissions = RECORD_AUDIO,INTERNET
android.api = 31
android.minapi = 21
android.ndk = 25b

orientation = portrait
fullscreen = 0

# SOLO ESTAS DEPENDENCIAS
requirements = python3,kivy,pyjnius,android

android.presplash_color = #3498DB
p4a.bootstrap = sdl2

android.archs = arm64-v8a,armeabi-v7a

[buildozer]
log_level = 2
```

## 📝 Checklist de Solución

Cuando tengas un error:

- [ ] ¿Los requirements solo tienen: `python3,kivy,pyjnius,android`?
- [ ] ¿Limpiaste con `rm -rf .buildozer bin`?
- [ ] ¿El buildozer.spec tiene `source.include_patterns`?
- [ ] ¿Las arquitecturas están sin espacios?
- [ ] ¿Tienes suficiente RAM en Colab?
- [ ] ¿Revisaste los logs con `tail`?

## 🚀 Comando de Compilación Correcto

```bash
buildozer -v android debug
```

**NO uses:**
- `buildozer android release` (requiere firma)
- Sin `-v` (no verás errores)

## 💡 Tip: Compilación Incremental

Si ya compilaste una vez y solo cambiaste código Python:

```bash
# Más rápido: solo empaqueta
buildozer android deploy
```

## 📱 Probar APK

Después de compilar:

```bash
# Ver APK generado
!ls -lh bin/*.apk

# Información del APK
!aapt dump badging bin/*.apk | grep package
```

## 🆘 Última Opción

Si nada funciona, usa la **versión simple sin Android APIs**:

```ini
# En buildozer.spec, quita pyjnius
requirements = python3,kivy

# En services/__init__.py, fuerza versión desktop
from .audio_service import AudioTranscriptionService
```

El APK compilará pero el micrófono no funcionará en Android (solo la UI).

---

**¿Sigues teniendo problemas?** Revisa los logs completos en `.buildozer/android/platform/build-*/build.log`
