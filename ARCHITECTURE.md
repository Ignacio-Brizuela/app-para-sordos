# Arquitectura del Sistema de Transcripción

## 📊 Diagrama de Componentes

```
┌─────────────────────────────────────────────────────────────────┐
│                         main.py                                  │
│                    (Aplicación Principal)                        │
│  ┌──────────────────────────────────────────────────────────┐   │
│  │  AppParaSordosApp                                        │   │
│  │  - build()                                               │   │
│  │  - switch_to_microphone()                                │   │
│  │  - switch_to_main()                                      │   │
│  └────────────┬────────────────────────────┬────────────────┘   │
│               │                            │                     │
│         MainScreen                  MicrophoneScreen             │
│         (UI Principal)              (UI Micrófono)               │
└───────────────┼────────────────────────────┼─────────────────────┘
                │                            │
                │                            │
                ▼                            ▼
    ┌─────────────────────┐      ┌──────────────────────────┐
    │   ui/               │      │  services/               │
    │   microphone_       │◄─────┤  audio_service.py        │
    │   screen.py         │      │                          │
    │                     │      │  AudioTranscription      │
    │  - _build_ui()      │      │  Service                 │
    │  - _toggle_         │      │  - start_listening()     │
    │    recording()      │      │  - stop_listening()      │
    │  - _on_new_         │      │  - _listen_thread()      │
    │    transcription()  │      │  - _transcribe_audio()   │
    └─────────────────────┘      └──────────┬───────────────┘
                │                           │
                │                           │
                └───────────┬───────────────┘
                            │
                            │ usa
                            ▼
                ┌────────────────────────┐
                │  models/               │
                │  transcription.py      │
                │                        │
                │  ┌──────────────────┐  │
                │  │  Transcription   │  │
                │  │  - text          │  │
                │  │  - confidence    │  │
                │  │  - timestamp     │  │
                │  └──────────────────┘  │
                │                        │
                │  ┌──────────────────┐  │
                │  │  Transcription   │  │
                │  │  History         │  │
                │  │  - _history      │  │
                │  │  - add()         │  │
                │  │  - get_all()     │  │
                │  │  - get_last()    │  │
                │  │  - clear()       │  │
                │  └──────────────────┘  │
                └────────────────────────┘
```

## 🔄 Flujo de Datos

```
1. Usuario presiona "Entrada de Micrófono"
                │
                ▼
2. main.py cambia a MicrophoneScreen
                │
                ▼
3. Usuario presiona "Iniciar Grabación"
                │
                ▼
4. MicrophoneScreen llama a audio_service.start_listening()
                │
                ▼
5. AudioTranscriptionService inicia hilo de escucha
                │
                ├─► Captura audio del micrófono (PyAudio)
                │
                ├─► Envía audio a Google Speech Recognition API
                │
                └─► Recibe texto transcrito
                │
                ▼
6. Crea objeto Transcription(text, confidence, timestamp)
                │
                ▼
7. Agrega a TranscriptionHistory usando history.add()
                │
                ▼
8. Ejecuta callback on_transcription_callback
                │
                ▼
9. MicrophoneScreen._on_new_transcription() actualiza UI
                │
                ▼
10. Usuario ve el texto transcrito en pantalla
```

## 🎯 Patrón de Diseño: Observer

El sistema usa el patrón Observer para la comunicación entre componentes:

```
AudioTranscriptionService (Subject)
        │
        ├─► on_transcription_callback ──► MicrophoneScreen._on_new_transcription()
        ├─► on_error_callback ──────────► MicrophoneScreen._on_error()
        └─► on_listening_callback ──────► MicrophoneScreen._on_listening_changed()
```

## 🧵 Threading Model

```
Main Thread (Kivy UI)
    │
    ├─► MicrophoneScreen (UI updates via Clock.schedule_once)
    │
    └─► AudioTranscriptionService
        │
        ├─► Listen Thread (daemon)
        │   └─► Captura continua de audio
        │
        └─► Transcription Threads (daemon, múltiples)
            └─► Envío a API y procesamiento de respuesta
```

## 📦 Estructuras de Datos

### Lista (List) - TranscriptionHistory._history
```python
# Estructura interna
[
    Transcription("Hola", 0.95, datetime(2025, 11, 22, 10, 30, 0)),
    Transcription("¿Cómo estás?", 0.92, datetime(2025, 11, 22, 10, 30, 5)),
    Transcription("Muy bien", 0.88, datetime(2025, 11, 22, 10, 30, 10)),
]

# Operaciones: O(1) append, O(1) pop(0), O(n) acceso
```

### Callbacks (Dict-like)
```python
# AudioTranscriptionService mantiene referencias a funciones
{
    'on_transcription': function_reference,
    'on_error': function_reference,
    'on_listening': function_reference
}
```

## 🔐 Gestión de Recursos

```
┌──────────────────────────────────────┐
│  Lifecycle Management               │
├──────────────────────────────────────┤
│                                      │
│  App Start                           │
│    ├─► Create AudioService           │
│    └─► Initialize Microphone         │
│                                      │
│  Recording Start                     │
│    ├─► Start daemon threads          │
│    └─► Acquire microphone resource   │
│                                      │
│  Recording Stop                      │
│    ├─► Set is_listening = False      │
│    ├─► Threads auto-terminate        │
│    └─► Release microphone            │
│                                      │
│  App Stop                            │
│    ├─► Call on_stop()                │
│    ├─► Stop all recordings           │
│    └─► Cleanup resources             │
│                                      │
└──────────────────────────────────────┘
```

## 🔧 Dependencias Externas

```
┌────────────────────┐
│  speech_recognition│  ──► Google Speech Recognition API
└────────────────────┘       (Conexión a Internet requerida)
           │
           ▼
    ┌─────────────┐
    │   PyAudio   │  ──► Sistema de audio del SO
    └─────────────┘       (Driver de micrófono)
           │
           ▼
    ┌─────────────┐
    │    Kivy     │  ──► Framework de UI multiplataforma
    └─────────────┘
```

## 📈 Complejidad

### Operaciones Comunes

| Operación | Complejidad | Descripción |
|-----------|-------------|-------------|
| `add(transcription)` | O(1) | Agregar al final de la lista |
| `get_last(n)` | O(n) | Slice de últimos n elementos |
| `get_all()` | O(n) | Copiar toda la lista |
| `clear()` | O(1) | Limpiar lista |
| `get_full_text()` | O(n) | Concatenar n strings |
| `start_listening()` | O(1) | Iniciar hilo |
| `_transcribe_audio()` | O(network) | API call |

### Memoria

- Cada `Transcription`: ~100-500 bytes (depende del texto)
- `TranscriptionHistory(max_size=100)`: ~10-50 KB máximo
- Total memoria del servicio: < 1 MB
