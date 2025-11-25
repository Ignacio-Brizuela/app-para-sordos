"""
Servicio de transcripción de audio usando speech_recognition
"""
import speech_recognition as sr
from threading import Thread
from typing import Callable, Optional
from models.transcription import Transcription, TranscriptionHistory


class AudioTranscriptionService:
    """
    Servicio que maneja la captura de audio y su transcripción a texto
    """
    
    def __init__(self):
        """
        Inicializa el servicio de transcripción de audio
        """
        self.recognizer = sr.Recognizer()
        self.microphone = None
        self.is_listening = False
        self.history = TranscriptionHistory()
        
        # Callbacks
        self.on_transcription_callback: Optional[Callable[[Transcription], None]] = None
        self.on_error_callback: Optional[Callable[[str], None]] = None
        self.on_listening_callback: Optional[Callable[[bool], None]] = None
        
        # Configuración del reconocedor
        self.recognizer.energy_threshold = 4000  # Ajustar sensibilidad del micrófono
        self.recognizer.dynamic_energy_threshold = True
        self.recognizer.pause_threshold = 0.8  # Segundos de silencio antes de considerar final
        
    def check_microphone_available(self) -> bool:
        """
        Verifica si hay un micrófono disponible
        
        Returns:
            True si hay un micrófono disponible, False en caso contrario
        """
        try:
            mic_list = sr.Microphone.list_microphone_names()
            return len(mic_list) > 0
        except Exception:
            return False
    
    def start_listening(self) -> None:
        """
        Inicia la escucha continua del micrófono en un hilo separado
        """
        if self.is_listening:
            return
        
        self.is_listening = True
        thread = Thread(target=self._listen_thread, daemon=True)
        thread.start()
        
        if self.on_listening_callback:
            self.on_listening_callback(True)
    
    def stop_listening(self) -> None:
        """
        Detiene la escucha del micrófono
        """
        self.is_listening = False
        
        if self.on_listening_callback:
            self.on_listening_callback(False)
    
    def _listen_thread(self) -> None:
        """
        Hilo que escucha continuamente del micrófono
        """
        try:
            with sr.Microphone() as source:
                # Ajustar el ruido ambiente
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                while self.is_listening:
                    try:
                        # Escuchar audio
                        audio = self.recognizer.listen(source, timeout=1, phrase_time_limit=10)
                        
                        # Transcribir en un hilo separado para no bloquear
                        Thread(target=self._transcribe_audio, args=(audio,), daemon=True).start()
                        
                    except sr.WaitTimeoutError:
                        # No se detectó audio en el timeout, continuar escuchando
                        continue
                    except Exception as e:
                        if self.on_error_callback:
                            self.on_error_callback(f"Error al escuchar: {str(e)}")
                        
        except Exception as e:
            self.is_listening = False
            if self.on_error_callback:
                self.on_error_callback(f"Error al inicializar micrófono: {str(e)}")
            if self.on_listening_callback:
                self.on_listening_callback(False)
    
    def _transcribe_audio(self, audio) -> None:
        """
        Transcribe el audio capturado a texto
        
        Args:
            audio: Objeto AudioData de speech_recognition
        """
        try:
            # Usar Google Speech Recognition (gratis)
            text = self.recognizer.recognize_google(audio, language='es-ES')
            
            # Crear objeto Transcription
            transcription = Transcription(text=text, confidence=1.0)
            
            # Agregar al historial
            self.history.add(transcription)
            
            # Llamar al callback si está definido
            if self.on_transcription_callback:
                self.on_transcription_callback(transcription)
                
        except sr.UnknownValueError:
            # No se pudo entender el audio
            if self.on_error_callback:
                self.on_error_callback("No se pudo entender el audio")
        except sr.RequestError as e:
            # Error en el servicio de reconocimiento
            if self.on_error_callback:
                self.on_error_callback(f"Error en el servicio de reconocimiento: {str(e)}")
        except Exception as e:
            if self.on_error_callback:
                self.on_error_callback(f"Error al transcribir: {str(e)}")
    
    def set_on_transcription(self, callback: Callable[[Transcription], None]) -> None:
        """
        Establece el callback que se llamará cuando haya una nueva transcripción
        
        Args:
            callback: Función que recibe un objeto Transcription
        """
        self.on_transcription_callback = callback
    
    def set_on_error(self, callback: Callable[[str], None]) -> None:
        """
        Establece el callback que se llamará cuando haya un error
        
        Args:
            callback: Función que recibe un mensaje de error
        """
        self.on_error_callback = callback
    
    def set_on_listening(self, callback: Callable[[bool], None]) -> None:
        """
        Establece el callback que se llamará cuando cambie el estado de escucha
        
        Args:
            callback: Función que recibe True si está escuchando, False si no
        """
        self.on_listening_callback = callback
    
    def get_history(self) -> TranscriptionHistory:
        """
        Obtiene el historial de transcripciones
        
        Returns:
            Objeto TranscriptionHistory
        """
        return self.history
    
    def clear_history(self) -> None:
        """
        Limpia el historial de transcripciones
        """
        self.history.clear()
