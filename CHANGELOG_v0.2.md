# Changelog - App Para Sordos v0.2

## 🎉 Nuevas Funcionalidades

### 1. ✍️ Entrada de Texto con Voz
- **Nueva pantalla**: TextInputScreen completamente funcional
- **TTS Nativo**: Usa `plyer.tts` en Android para síntesis de voz
- **Interfaz mejorada**: 
  - Botón "Volver" para regresar al menú principal
  - Botón "Reproducir Audio" con ícono 🔊
  - Botón "Limpiar" para borrar el texto
  - Área de texto amplia y legible
- **Compatibilidad**: Funciona en Android y escritorio (usando gTTS + playsound)

### 2. 🚀 Build Incremental en Colab
- **Notebook optimizado**: `BUILD_APK_COLAB_OPTIMIZADO.ipynb`
- **Build completo**: 40-50 minutos (primera vez)
- **Build incremental**: 5-10 minutos (actualizaciones)
- **Dos opciones de carga**:
  - Opción A: ZIP completo (primera vez)
  - Opción B: Solo archivos modificados (actualización)

### 3. 🎤 Mejoras en Reconocimiento de Voz
- **Manejo de errores robusto**: Try-catch en inicialización de Android
- **Mensajes informativos**: Logs detallados para debugging
- **Reintentos automáticos**: En caso de errores recuperables

## 🔧 Correcciones

### models/text_model.py
- ✅ Corregido import de `playsound` (opcional, no rompe si no está)
- ✅ Usa `tempfile` para archivos temporales seguros
- ✅ Detecta plataforma correctamente (Android vs Desktop)
- ✅ Manejo de errores mejorado
- ⚠️ Eliminada importación innecesaria de `filechooser`

### main.py
- ✅ TextInputScreen ahora tiene header con botón "Volver"
- ✅ UI consistente con MicrophoneScreen
- ✅ Callbacks `on_back` implementados correctamente
- ✅ Métodos `on_speak` y `on_clear` para control de audio

### services/audio_service_android.py
- ✅ Try-catch en `_start_listening_android`
- ✅ Mensajes de error informativos
- ✅ Logs de éxito para debugging

### buildozer.spec
- ✅ Versión actualizada a **0.2**
- ✅ Permisos ampliados: `WRITE_EXTERNAL_STORAGE`, `READ_EXTERNAL_STORAGE`
- ✅ Target API actualizado a **33** (Android 13)
- ✅ Requirements actualizados con versiones específicas:
  - `python3==3.10.6`
  - `kivy==2.3.0`
  - `plyer`
  - `requests`, `certifi`, `charset-normalizer`

## 📦 Nuevos Archivos

1. **BUILD_APK_COLAB_OPTIMIZADO.ipynb**
   - Notebook completo con build incremental
   - Documentación detallada
   - Solución de problemas integrada
   - Guía de instalación en Android

2. **CHANGELOG_v0.2.md** (este archivo)
   - Documentación de todos los cambios
   - Guía de migración

## 🐛 Bugs Corregidos

1. **ModuleNotFoundError: playsound**
   - ✅ Agregado a requirements.txt (versión 1.2.2)
   - ✅ Import condicional para evitar crashes

2. **TextInputScreen sin botón volver**
   - ✅ Agregado header con navegación

3. **TTS no funcional en Android**
   - ✅ Implementado con plyer.tts nativo

4. **Archivos temporales no se eliminan**
   - ✅ Uso de tempfile.NamedTemporaryFile

## 📝 Archivos Modificados

| Archivo | Cambios |
|---------|---------|
| `models/text_model.py` | Refactorización completa de TTS |
| `main.py` | TextInputScreen con UI mejorada |
| `services/audio_service_android.py` | Manejo de errores robusto |
| `buildozer.spec` | Versión, permisos y requirements |
| `requirements.txt` | Agregado playsound==1.2.2 |

## 🚀 Instrucciones de Actualización

### Para usuarios existentes:

1. **Descargar archivos actualizados**:
   ```
   - models/text_model.py
   - main.py
   - services/audio_service_android.py
   - buildozer.spec
   - requirements.txt
   - BUILD_APK_COLAB_OPTIMIZADO.ipynb
   ```

2. **Instalar nuevo requirements**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Build en Colab**:
   - Abre `BUILD_APK_COLAB_OPTIMIZADO.ipynb`
   - Primera vez: Ejecuta celdas 1-4 (build completo)
   - Actualizaciones: Ejecuta celdas 1, 2B, 5 (build incremental)

## 🎯 Roadmap v0.3 (Futuro)

- [ ] Historial persistente de transcripciones
- [ ] Guardar/exportar transcripciones a archivo
- [ ] Configuración de idiomas
- [ ] Modo oscuro
- [ ] Widget para acceso rápido
- [ ] Notificaciones de transcripción

## 📱 Compatibilidad

| Plataforma | Estado | Notas |
|------------|--------|-------|
| Android 5.0+ | ✅ Completo | API 21+ |
| Android 13 | ✅ Optimizado | Target API 33 |
| Windows | ✅ Funcional | Requiere PyAudio |
| Linux | ✅ Funcional | Requiere PyAudio |
| macOS | ⚠️ No probado | Debería funcionar |

## 🙏 Créditos

- **Kivy**: Framework UI multiplataforma
- **Plyer**: APIs nativas de Android/iOS
- **gTTS**: Google Text-to-Speech
- **Buildozer**: Empaquetado para Android

---

**Versión**: 0.2  
**Fecha**: Noviembre 2025  
**Desarrollador**: Ignacio
