# Sistema de Transcripción de Audio

## 📋 Descripción

Se ha implementado un sistema completo de transcripción de audio a texto usando una arquitectura modular con las siguientes características:

### 🏗️ Estructura del Proyecto

```
APP_PARA_SORDOS/
│
├── main.py                 # Aplicación principal con navegación entre pantallas
├── requirements.txt        # Dependencias del proyecto
│
├── models/                 # Estructuras de datos
│   ├── __init__.py
│   └── transcription.py    # Clases Transcription y TranscriptionHistory
│
├── services/               # Lógica de negocio
│   ├── __init__.py
│   └── audio_service.py    # Servicio de captura y transcripción de audio
│
└── ui/                     # Componentes de interfaz
    ├── __init__.py
    └── microphone_screen.py # Pantalla de transcripción con micrófono
```

## 🎯 Funcionalidades Implementadas

### 1. Estructuras de Datos (`models/transcription.py`)

#### **Clase `Transcription`**
- Representa una transcripción individual
- Atributos:
  - `text`: Texto transcrito
  - `confidence`: Nivel de confianza (0-1)
  - `timestamp`: Momento de la transcripción

#### **Clase `TranscriptionHistory`**
- Mantiene un historial de transcripciones usando una lista
- Métodos principales:
  - `add(transcription)`: Agrega una transcripción
  - `get_all()`: Obtiene todas las transcripciones
  - `get_last(n)`: Obtiene las últimas n transcripciones
  - `clear()`: Limpia el historial
  - `get_full_text()`: Obtiene todo el texto concatenado
  - `count()`: Retorna el número de transcripciones

### 2. Servicio de Audio (`services/audio_service.py`)

#### **Clase `AudioTranscriptionService`**
- Maneja la captura de audio y transcripción
- Características:
  - ✅ Escucha continua del micrófono en hilo separado
  - ✅ Ajuste automático de ruido ambiente
  - ✅ Transcripción usando Google Speech Recognition (gratis)
  - ✅ Soporte para idioma español (`es-ES`)
  - ✅ Sistema de callbacks para eventos
  - ✅ Gestión de errores robusta

- Métodos principales:
  - `start_listening()`: Inicia la escucha
  - `stop_listening()`: Detiene la escucha
  - `check_microphone_available()`: Verifica disponibilidad de micrófono
  - `set_on_transcription(callback)`: Callback para nuevas transcripciones
  - `set_on_error(callback)`: Callback para errores
  - `set_on_listening(callback)`: Callback para cambios de estado
  - `get_history()`: Obtiene el historial
  - `clear_history()`: Limpia el historial

### 3. Interfaz de Usuario (`ui/microphone_screen.py`)

#### **Clase `MicrophoneScreen`**
- Pantalla completa de transcripción
- Componentes:
  - 🎤 Botón de iniciar/detener grabación
  - 📝 Área de texto con scroll para transcripciones
  - 🗑️ Botón para limpiar transcripciones
  - ℹ️ Indicador de estado en tiempo real
  - ← Botón para volver al menú principal

- Características de UI:
  - Actualización en tiempo real del texto transcrito
  - Cambio de color del botón según estado (verde/rojo)
  - Mensajes de estado informativos
  - Scroll automático para textos largos

## 📦 Instalación

### 1. Instalar las dependencias:

```bash
pip install -r requirements.txt
```

**Nota sobre PyAudio en Windows:**
Si tienes problemas instalando PyAudio, usa:
```bash
pip install pipwin
pipwin install pyaudio
```

### 2. Ejecutar la aplicación:

```bash
python main.py
```

## 🚀 Uso

1. **Iniciar la aplicación**: Ejecuta `python main.py`
2. **Seleccionar "Entrada de Micrófono"**: Click en el botón rojo
3. **Iniciar grabación**: Click en "🎙️ Iniciar Grabación"
4. **Hablar**: El texto aparecerá automáticamente mientras hablas
5. **Detener**: Click en "⏹️ Detener Grabación"
6. **Limpiar**: Usa el botón "🗑️ Limpiar" para borrar el texto
7. **Volver**: Click en "← Volver" para regresar al menú

## 🔧 Tecnologías Utilizadas

- **Kivy**: Framework de interfaz gráfica
- **SpeechRecognition**: Biblioteca de reconocimiento de voz
- **PyAudio**: Captura de audio del micrófono
- **Google Speech Recognition API**: Servicio de transcripción (gratuito)

## 📝 Notas Técnicas

### Configuración del Reconocedor:
- `energy_threshold`: 4000 (sensibilidad del micrófono)
- `dynamic_energy_threshold`: True (ajuste automático)
- `pause_threshold`: 0.8 segundos (tiempo de silencio antes de finalizar)

### Threading:
- La escucha del micrófono se ejecuta en un hilo separado
- La transcripción se ejecuta en otro hilo para no bloquear la UI
- Los callbacks a Kivy usan `Clock.schedule_once()` para thread-safety

### Manejo de Errores:
- Verificación de disponibilidad de micrófono
- Manejo de timeouts en la escucha
- Detección de audio no comprensible
- Manejo de errores de servicio de reconocimiento

## 🎨 Ventajas de la Arquitectura

1. **Separación de responsabilidades**: 
   - Models: Estructuras de datos
   - Services: Lógica de negocio
   - UI: Presentación

2. **Reutilizable**: Los servicios y modelos pueden usarse en otras pantallas

3. **Testeable**: Cada componente puede probarse independientemente

4. **Mantenible**: Código organizado y fácil de modificar

5. **Escalable**: Fácil agregar nuevas funcionalidades

## 🔮 Posibles Mejoras Futuras

- [ ] Soporte para múltiples idiomas
- [ ] Guardar transcripciones en archivo
- [ ] Compartir transcripciones
- [ ] Usar APIs de reconocimiento más avanzadas (Azure, AWS, etc.)
- [ ] Ajuste de sensibilidad del micrófono desde la UI
- [ ] Modo offline con modelos locales
- [ ] Resaltado de palabras clave
- [ ] Traducción automática
