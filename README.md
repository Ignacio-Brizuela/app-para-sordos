# App Para Sordos v0.2

Aplicación móvil desarrollada con Kivy para asistir a personas con discapacidad auditiva mediante reconocimiento de voz y síntesis de voz.

## ✨ Características

- 🎤 **Reconocimiento de Voz**: Convierte voz a texto en tiempo real usando SpeechRecognizer nativo de Android
- 📝 **Texto a Voz**: Escribe texto y escúchalo con TTS nativo de Android
- 🎨 **Interfaz Intuitiva**: Diseño limpio y fácil de usar
- 🔄 **Navegación Completa**: Botones de volver en todas las pantallas
- 📱 **Android Nativo**: Optimizado para dispositivos Android 5.0+

## 🆕 Novedades v0.2

- ⚡ **Build incremental en Colab**: Actualiza el APK en 5-10 minutos (vs 45 minutos)
- ✅ **Funcionalidad completa**: Micrófono y TTS totalmente funcionales en Android
- 🎯 **UI mejorada**: Todas las pantallas con navegación consistente
- 🔧 **Código robusto**: Mejor manejo de errores y logging

## 📋 Requisitos

- Python 3.10+
- Kivy 2.3.0
- Dependencias en `requirements.txt`

## 🚀 Instalación para Desarrollo (Windows)

```powershell
# Clonar o descargar el proyecto
cd APP_PARA_SORDOS_v2.1.1

# Instalar dependencias
pip install -r requirements.txt
```

## ▶️ Ejecutar la Aplicación

```powershell
python main.py
```

## 📱 Compilar para Android (Google Colab)

### Método Recomendado: Build Optimizado

1. **Preparar proyecto**:
   ```powershell
   .\crear_zip_para_colab.ps1
   ```

2. **Abrir Google Colab**:
   - Ve a [colab.research.google.com](https://colab.research.google.com)
   - Sube `BUILD_APK_COLAB_OPTIMIZADO.ipynb`

3. **Build Completo** (primera vez, ~50 min):
   - Celda 1: Instalar dependencias
   - Celda 2A: Subir ZIP
   - Celda 3: Verificar configuración
   - Celda 4: **BUILD COMPLETO**
   - Celda 6: Descargar APK

4. **Build Incremental** (actualizaciones, ~10 min):
   - Celda 1: Instalar dependencias
   - Celda 2B: Subir archivos modificados
   - Celda 5: **BUILD INCREMENTAL** ⚡
   - Celda 6: Descargar APK

### Ventajas del Build Optimizado

| Aspecto | Build Tradicional | Build Optimizado |
|---------|-------------------|------------------|
| Primera compilación | 45 min | 45 min |
| Actualizaciones | 45 min | **10 min** ⚡ |
| Facilidad | Media | Alta |
| Documentación | Básica | Completa |

## 📂 Estructura del Proyecto

```
APP_PARA_SORDOS_v2.1.1/
├── main.py                          # Aplicación principal
├── buildozer.spec                   # Configuración de Android
├── requirements.txt                 # Dependencias Python
├── BUILD_APK_COLAB_OPTIMIZADO.ipynb # Notebook optimizado para Colab
├── crear_zip_para_colab.ps1         # Script para crear ZIP
├── models/
│   ├── text_model.py               # Modelo de texto a voz
│   └── transcription.py            # Modelo de transcripción
├── services/
│   ├── audio_service.py            # Servicio de audio (Desktop)
│   └── audio_service_android.py    # Servicio de audio (Android)
├── ui/
│   └── microphone_screen.py        # Pantalla de micrófono
└── imagenes/                        # Recursos gráficos
    ├── habla.png
    └── microfono.png
```

## 🎯 Uso de la Aplicación

1. **Pantalla Principal**:
   - Botón "Escribir": Entrada de texto
   - Botón "Micrófono": Reconocimiento de voz

2. **Pantalla de Texto**:
   - Escribe tu mensaje
   - Presiona "Reproducir Audio" para escucharlo
   - Usa "Limpiar" para borrar
   - "Volver" regresa al menú

3. **Pantalla de Micrófono**:
   - Presiona "Iniciar Grabación"
   - Habla claramente
   - El texto aparecerá en pantalla
   - "Detener Grabación" para pausar
   - "Limpiar" borra el texto
   - "Volver" regresa al menú

## 📱 Instalación en Android

1. Descarga el APK desde Colab
2. Transfiere a tu teléfono Android
3. Habilita "Orígenes desconocidos" en Ajustes → Seguridad
4. Abre el APK y presiona "Instalar"
5. Acepta los permisos:
   - 🎤 Micrófono
   - 🌐 Internet
   - 💾 Almacenamiento

## 🔧 Tecnologías Utilizadas

- **Kivy**: Framework multiplataforma para UI
- **Plyer**: APIs nativas de Android/iOS
- **Pyjnius**: Bridge Python-Java para Android
- **SpeechRecognizer**: API nativa de reconocimiento de voz (Android)
- **TextToSpeech**: TTS nativo de Android
- **gTTS**: Google Text-to-Speech (Desktop)
- **SpeechRecognition**: Reconocimiento de voz (Desktop)

## 📄 Documentación

- [GUIA_BUILD_OPTIMIZADO.md](GUIA_BUILD_OPTIMIZADO.md) - Guía completa del build optimizado
- [CHANGELOG_v0.2.md](CHANGELOG_v0.2.md) - Cambios en la versión 0.2
- [ARCHITECTURE.md](ARCHITECTURE.md) - Arquitectura del proyecto
- [TRANSCRIPTION_GUIDE.md](TRANSCRIPTION_GUIDE.md) - Guía de transcripción

## 🐛 Solución de Problemas

### El micrófono no funciona
- Verifica que hayas aceptado los permisos de micrófono
- Asegúrate de tener conexión a internet
- Intenta reiniciar la app

### El APK no se instala
- Verifica que "Orígenes desconocidos" esté habilitado
- Asegúrate de tener Android 5.0 o superior
- Verifica que tengas espacio suficiente

### Build en Colab falla
- Revisa la celda de "Solución de problemas" en el notebook
- Ejecuta limpieza completa (OPCIÓN 2)
- Intenta build completo en lugar de incremental

## 🤝 Contribuir

Las contribuciones son bienvenidas. Por favor:

1. Fork el proyecto
2. Crea una rama para tu feature (`git checkout -b feature/AmazingFeature`)
3. Commit tus cambios (`git commit -m 'Add some AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abre un Pull Request

## 📜 Licencia

Este proyecto es de código abierto y está disponible bajo la licencia MIT.

## 👤 Autor

**Ignacio**

## 🙏 Agradecimientos

- Comunidad de Kivy
- Plyer developers
- Google Text-to-Speech
- Todos los que han contribuido con feedback

---

**Versión**: 0.2  
**Última actualización**: Noviembre 2025  
**Estado**: Producción ✅
