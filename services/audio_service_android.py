"""
Servicio de reconocimiento de voz para Android usando APIs nativas
Usa Pyjnius para comunicarse con SpeechRecognizer de Android
"""
import sys
from kivy.utils import platform

# Verificar si estamos en Android
ANDROID = platform == 'android'

if ANDROID:
    try:
        from jnius import autoclass, PythonJavaClass, java_method
        from android.permissions import request_permissions, Permission
        from android.runnable import run_on_ui_thread
        
        # Clases de Android
        PythonActivity = autoclass('org.kivy.android.PythonActivity')
        Intent = autoclass('android.content.Intent')
        RecognizerIntent = autoclass('android.speech.RecognizerIntent')
        SpeechRecognizer = autoclass('android.speech.SpeechRecognizer')
        Bundle = autoclass('android.os.Bundle')
        
        print("✅ Android: Módulos cargados correctamente")
    except Exception as e:
        print(f"❌ Android: Error cargando módulos: {e}")
        ANDROID = False

from threading import Thread
from typing import Callable, Optional
from models.transcription import Transcription, TranscriptionHistory
from kivy.clock import Clock


if ANDROID:
    class AndroidRecognitionListener(PythonJavaClass):
        """
        Listener para eventos de reconocimiento de voz en Android
        """
        __javainterfaces__ = ['android/speech/RecognitionListener']
        __javacontext__ = 'app'
        
        def __init__(self, callback_transcription, callback_error):
            super().__init__()
            self.callback_transcription = callback_transcription
            self.callback_error = callback_error
        
        @java_method('(Landroid/os/Bundle;)V')
        def onReadyForSpeech(self, params):
            print("🎤 Android: Listo para escuchar")
        
        @java_method('()V')
        def onBeginningOfSpeech(self):
            print("🗣️ Android: Comenzó a hablar")
        
        @java_method('(F)V')
        def onRmsChanged(self, rmsdB):
            pass
        
        @java_method('([B)V')
        def onBufferReceived(self, buffer):
            pass
        
        @java_method('()V')
        def onEndOfSpeech(self):
            print("🔇 Android: Terminó de hablar")
        
        @java_method('(I)V')
        def onError(self, error):
            error_messages = {
                1: "Error de red",
                2: "Error del servidor",
                3: "Audio no disponible",
                4: "Servidor ocupado",
                5: "Cliente ocupado",
                6: "Sin coincidencias",
                7: "Sin reconocimiento",
                8: "Permiso insuficiente",
                9: "Servicio no disponible"
            }
            msg = error_messages.get(error, f"Error desconocido: {error}")
            print(f"⚠️ Android: {msg}")
            Clock.schedule_once(lambda dt: self.callback_error(msg), 0)
        
        @java_method('(Landroid/os/Bundle;)V')
        def onResults(self, results):
            try:
                matches = results.getStringArrayList(RecognizerIntent.EXTRA_RESULTS)
                
                if matches and matches.size() > 0:
                    text = str(matches.get(0))
                    print(f"✅ Android: Texto reconocido: {text}")
                    
                    confidence_scores = results.getFloatArray(RecognizerIntent.EXTRA_CONFIDENCE_SCORES)
                    confidence = float(confidence_scores[0]) if confidence_scores else 1.0
                    
                    transcription = Transcription(text=text, confidence=confidence)
                    Clock.schedule_once(lambda dt: self.callback_transcription(transcription), 0)
            except Exception as e:
                print(f"❌ Android: Error en onResults: {e}")
                Clock.schedule_once(lambda dt: self.callback_error(f"Error: {e}"), 0)
        
        @java_method('(Landroid/os/Bundle;)V')
        def onPartialResults(self, partialResults):
            pass
        
        @java_method('(ILandroid/os/Bundle;)V')
        def onEvent(self, eventType, params):
            pass
else:
    class AndroidRecognitionListener:
        """Stub para desarrollo en Desktop"""
        def __init__(self, callback_transcription, callback_error):
            self.callback_transcription = callback_transcription
            self.callback_error = callback_error


class AudioTranscriptionService:
    """
    Servicio de transcripción de audio
    Usa APIs nativas de Android si está disponible, sino usa SpeechRecognition
    """
    
    def __init__(self):
        self.is_listening = False
        self.history = TranscriptionHistory()
        
        # Callbacks
        self.on_transcription_callback: Optional[Callable[[Transcription], None]] = None
        self.on_error_callback: Optional[Callable[[str], None]] = None
        self.on_listening_callback: Optional[Callable[[bool], None]] = None
        
        if ANDROID:
            self._init_android()
        else:
            self._init_desktop()
    
    def _init_android(self):
        """
        Inicializa el reconocedor para Android
        """
        # Solicitar permisos
        request_permissions([Permission.RECORD_AUDIO, Permission.INTERNET])
        
        # Obtener actividad y contexto
        self.activity = PythonActivity.mActivity
        self.context = cast('android.content.Context', self.activity)
        
        # Crear reconocedor de voz
        self.speech_recognizer = SpeechRecognizer.createSpeechRecognizer(self.context)
        
        # Crear intent para reconocimiento
        self.intent = Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH)
        self.intent.putExtra(
            RecognizerIntent.EXTRA_LANGUAGE_MODEL,
            RecognizerIntent.LANGUAGE_MODEL_FREE_FORM
        )
        self.intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "es-ES")
        self.intent.putExtra(RecognizerIntent.EXTRA_PARTIAL_RESULTS, True)
        self.intent.putExtra(RecognizerIntent.EXTRA_MAX_RESULTS, 1)
    
    def _init_desktop(self):
        """
        Inicializa el reconocedor para escritorio (Windows/Linux/Mac)
        """
        self.recognizer = sr.Recognizer()
        self.recognizer.energy_threshold = 4000
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8
    
    def check_microphone_available(self) -> bool:
        """
        Verifica si hay un micrófono disponible
        """
        if ANDROID:
            return SpeechRecognizer.isRecognitionAvailable(self.context)
        else:
            try:
                mic_list = sr.Microphone.list_microphone_names()
                return len(mic_list) > 0
            except Exception:
                return False
    
    @run_on_ui_thread
    def start_listening(self) -> None:
        """
        Inicia la escucha del micrófono
        """
        if self.is_listening:
            return
        
        self.is_listening = True
        
        if ANDROID:
            self._start_listening_android()
        else:
            self._start_listening_desktop()
        
        if self.on_listening_callback:
            self.on_listening_callback(True)
    
    @run_on_ui_thread
    def _start_listening_android(self):
        """
        Inicia escucha en Android
        """
        try:
            print("🎤 Android: Iniciando reconocimiento de voz...")
            
            # Crear listener directamente (ya implementa la interfaz Java)
            listener = AndroidRecognitionListener(
                self._on_transcription_android,
                self._on_error_android
            )
            
            # Establecer listener directamente
            self.speech_recognizer.setRecognitionListener(listener)
            
            # Iniciar reconocimiento
            self.speech_recognizer.startListening(self.intent)
            print("✅ Android: Reconocimiento de voz iniciado")
        except Exception as e:
            print(f"❌ Android: Error al iniciar: {e}")
            import traceback
            traceback.print_exc()
            if self.on_error_callback:
                Clock.schedule_once(
                    lambda dt: self.on_error_callback(f"Error al iniciar: {str(e)}"),
                    0
                )
    
    def _start_listening_desktop(self):
        """
        Inicia escucha en escritorio (versión original)
        """
        thread = Thread(target=self._listen_thread_desktop, daemon=True)
        thread.start()
    
    def _listen_thread_desktop(self):
        """
        Hilo de escucha para escritorio
        """
        try:
            with sr.Microphone() as source:
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                while self.is_listening:
                    try:
                        audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=10)
                        Thread(target=self._transcribe_audio_desktop, args=(audio,), daemon=True).start()
                    except sr.WaitTimeoutError:
                        continue
                    except Exception as e:
                        if self.on_error_callback:
                            Clock.schedule_once(
                                lambda dt: self.on_error_callback(f"Error: {str(e)}"),
                                0
                            )
        except Exception as e:
            self.is_listening = False
            if self.on_error_callback:
                Clock.schedule_once(
                    lambda dt: self.on_error_callback(f"Error de micrófono: {str(e)}"),
                    0
                )
    
    def _transcribe_audio_desktop(self, audio):
        """
        Transcribe audio en escritorio
        """
        try:
            text = self.recognizer.recognize_google(audio, language='es-ES')
            transcription = Transcription(text=text, confidence=1.0)
            self.history.add(transcription)
            
            if self.on_transcription_callback:
                Clock.schedule_once(
                    lambda dt: self.on_transcription_callback(transcription),
                    0
                )
        except sr.UnknownValueError:
            if self.on_error_callback:
                Clock.schedule_once(
                    lambda dt: self.on_error_callback("No se entendió el audio"),
                    0
                )
        except Exception as e:
            if self.on_error_callback:
                Clock.schedule_once(
                    lambda dt: self.on_error_callback(f"Error: {str(e)}"),
                    0
                )
    
    def _on_transcription_android(self, transcription: Transcription):
        """
        Callback para transcripción en Android
        """
        self.history.add(transcription)
        
        if self.on_transcription_callback:
            self.on_transcription_callback(transcription)
        
        # Reiniciar escucha para modo continuo
        if self.is_listening:
            Clock.schedule_once(lambda dt: self._start_listening_android(), 0.5)
    
    def _on_error_android(self, error_msg: str):
        """
        Callback para errores en Android
        """
        if self.on_error_callback:
            self.on_error_callback(error_msg)
        
        # Reintentar en caso de ciertos errores
        if self.is_listening and "Sin coincidencias" in error_msg:
            Clock.schedule_once(lambda dt: self._start_listening_android(), 0.5)
    
    def stop_listening(self) -> None:
        """
        Detiene la escucha del micrófono
        """
        self.is_listening = False
        
        if ANDROID:
            self.speech_recognizer.stopListening()
            self.speech_recognizer.cancel()
        
        if self.on_listening_callback:
            self.on_listening_callback(False)
    
    def set_on_transcription(self, callback: Callable[[Transcription], None]) -> None:
        self.on_transcription_callback = callback
    
    def set_on_error(self, callback: Callable[[str], None]) -> None:
        self.on_error_callback = callback
    
    def set_on_listening(self, callback: Callable[[bool], None]) -> None:
        self.on_listening_callback = callback
    
    def get_history(self) -> TranscriptionHistory:
        return self.history
    
    def clear_history(self) -> None:
        self.history.clear()
    
    def __del__(self):
        """
        Limpieza al destruir el servicio
        """
        if ANDROID and hasattr(self, 'speech_recognizer'):
            self.speech_recognizer.destroy()
