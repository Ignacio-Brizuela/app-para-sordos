"""
Pantalla de transcripción de audio con micrófono
"""
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.utils import get_color_from_hex, platform
from kivy.clock import Clock

# En Android, NO importar services para evitar crashes
AUDIO_AVAILABLE = False
AudioTranscriptionService = None
Transcription = None

if platform != 'android':
    try:
        from services import AudioTranscriptionService
        from models.transcription import Transcription
        AUDIO_AVAILABLE = True
    except Exception as e:
        print(f"⚠️ No se pudo cargar AudioTranscriptionService: {e}")
        AUDIO_AVAILABLE = False


class MicrophoneScreen(BoxLayout):
    """
    Pantalla que muestra la interfaz de transcripción de audio
    """
    
    def __init__(self, on_back=None, **kwargs):
        super(MicrophoneScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 20
        self.spacing = 15
        
        # Callback para volver a la pantalla anterior
        self.on_back = on_back
        
        # Servicio de audio (solo si está disponible)
        if AUDIO_AVAILABLE:
            self.audio_service = AudioTranscriptionService()
            self.audio_service.set_on_transcription(self._on_new_transcription)
            self.audio_service.set_on_error(self._on_error)
            self.audio_service.set_on_listening(self._on_listening_changed)
        else:
            self.audio_service = None
        
        # Estado
        self.is_recording = False
        
        # Variables para animación de texto
        self.animation_event = None
        self.current_text = ""
        self.target_text = ""
        self.char_index = 0
        
        # Construir UI
        self._build_ui()
    
    def _build_ui(self):
        """
        Construye la interfaz de usuario
        """
        # Header con título y botón de volver
        header = BoxLayout(size_hint=(1, 0.1), spacing=10)
        
        back_button = Button(
            text='← Volver',
            font_size='18sp',
            size_hint=(0.3, 1),
            background_color=get_color_from_hex('#95A5A6'),
            background_normal='',
            color=(1, 1, 1, 1)
        )
        back_button.bind(on_press=self._on_back_pressed)
        
        title = Label(
            text='🎤 Transcripción de Audio',
            font_size='24sp',
            size_hint=(0.7, 1),
            color=get_color_from_hex('#2C3E50'),
            bold=True
        )
        
        header.add_widget(back_button)
        header.add_widget(title)
        self.add_widget(header)
        
        # Estado del micrófono
        self.status_label = Label(
            text='Presiona el botón para comenzar',
            font_size='16sp',
            size_hint=(1, 0.08),
            color=get_color_from_hex('#7F8C8D')
        )
        self.add_widget(self.status_label)
        
        # Área de transcripción con scroll
        scroll_view = ScrollView(
            size_hint=(1, 0.6),
            do_scroll_x=False,
            do_scroll_y=True
        )
        
        self.transcription_label = Label(
            text='El texto transcrito aparecerá aquí...',
            font_size='20sp',
            size_hint_y=None,
            color=get_color_from_hex('#2C3E50'),
            padding=(20, 20),
            text_size=(None, None),
            halign='left',
            valign='top'
        )
        self.transcription_label.bind(
            width=lambda *x: setattr(self.transcription_label, 'text_size', (self.transcription_label.width - 40, None)),
            texture_size=lambda *x: setattr(self.transcription_label, 'height', self.transcription_label.texture_size[1])
        )
        
        scroll_view.add_widget(self.transcription_label)
        self.add_widget(scroll_view)
        
        # Botones de control
        controls = BoxLayout(size_hint=(1, 0.15), spacing=10)
        
        # Botón de grabar/detener
        self.record_button = Button(
            text='🎙️ Iniciar Grabación',
            font_size='20sp',
            background_color=get_color_from_hex('#27AE60'),
            background_normal='',
            color=(1, 1, 1, 1),
            bold=True
        )
        self.record_button.bind(on_press=self._toggle_recording)
        
        # Botón de limpiar
        clear_button = Button(
            text='🗑️ Limpiar',
            font_size='20sp',
            size_hint=(0.3, 1),
            background_color=get_color_from_hex('#E67E22'),
            background_normal='',
            color=(1, 1, 1, 1),
            bold=True
        )
        clear_button.bind(on_press=self._clear_transcription)
        
        controls.add_widget(self.record_button)
        controls.add_widget(clear_button)
        self.add_widget(controls)
        
        # Información adicional
        if platform == 'android':
            info_text = 'Función de reconocimiento de voz en desarrollo para Android.\nPor ahora usa la función "Escribir" en el menú principal.'
        else:
            info_text = 'Habla claramente cerca del micrófono'
        
        info = Label(
            text=info_text,
            font_size='14sp',
            size_hint=(1, 0.07),
            color=get_color_from_hex('#95A5A6'),
            italic=True
        )
        self.add_widget(info)
    
    def _toggle_recording(self, instance):
        """
        Alterna entre iniciar y detener la grabación
        """
        if not AUDIO_AVAILABLE or self.audio_service is None:
            self._update_status("❌ Función de micrófono no disponible en esta versión")
            return
            
        if not self.is_recording:
            # Verificar si hay micrófono disponible
            if not self.audio_service.check_microphone_available():
                self._update_status("❌ No se detectó ningún micrófono")
                return
            
            # Iniciar grabación
            self.audio_service.start_listening()
        else:
            # Detener grabación
            self.audio_service.stop_listening()
    
    def _on_listening_changed(self, is_listening):
        """
        Callback cuando cambia el estado de escucha
        """
        def update_ui(dt):
            self.is_recording = is_listening
            if is_listening:
                self.record_button.text = '⏹️ Detener Grabación'
                self.record_button.background_color = get_color_from_hex('#E74C3C')
                self._update_status("🎤 Escuchando... Habla ahora")
            else:
                self.record_button.text = '🎙️ Iniciar Grabación'
                self.record_button.background_color = get_color_from_hex('#27AE60')
                self._update_status("⏸️ Grabación detenida")
        
        Clock.schedule_once(update_ui, 0)
    
    def _on_new_transcription(self, transcription: Transcription):
        """
        Callback cuando hay una nueva transcripción
        """
        def update_text(dt):
            # Obtener todo el texto del historial
            full_text = self.audio_service.get_history().get_full_text(separator="\n\n")
            
            if full_text:
                # Iniciar animación de texto
                self._animate_text(full_text)
                self.transcription_label.color = get_color_from_hex('#2C3E50')
        
        Clock.schedule_once(update_text, 0)
    
    def _animate_text(self, new_text):
        """
        Anima el texto para que aparezca carácter por carácter de forma suave
        """
        # Cancelar animación anterior si existe
        if self.animation_event:
            self.animation_event.cancel()
        
        # Configurar nuevo texto objetivo
        self.target_text = new_text
        
        # Si el nuevo texto comienza con el texto actual, solo agregar lo nuevo
        if new_text.startswith(self.current_text):
            self.char_index = len(self.current_text)
        else:
            # Texto completamente nuevo, empezar desde cero
            self.current_text = ""
            self.char_index = 0
        
        # Iniciar animación (30 caracteres por segundo = ~0.033s por carácter)
        self.animation_event = Clock.schedule_interval(self._update_animated_text, 0.033)
    
    def _update_animated_text(self, dt):
        """
        Actualiza el texto animado carácter por carácter
        """
        if self.char_index < len(self.target_text):
            # Agregar el siguiente carácter
            self.char_index += 1
            self.current_text = self.target_text[:self.char_index]
            self.transcription_label.text = self.current_text
        else:
            # Animación completada
            if self.animation_event:
                self.animation_event.cancel()
                self.animation_event = None
    
    def _on_error(self, error_message: str):
        """
        Callback cuando hay un error
        """
        def update_status(dt):
            self._update_status(f"⚠️ {error_message}")
        
        Clock.schedule_once(update_status, 0)
    
    def _update_status(self, message: str):
        """
        Actualiza el mensaje de estado
        """
        self.status_label.text = message
    
    def _clear_transcription(self, instance):
        """
        Limpia la transcripción actual
        """
        # Cancelar animación si existe
        if self.animation_event:
            self.animation_event.cancel()
            self.animation_event = None
        
        # Resetear variables de animación
        self.current_text = ""
        self.target_text = ""
        self.char_index = 0
        
        # Limpiar servicio y UI
        if AUDIO_AVAILABLE and self.audio_service:
            self.audio_service.clear_history()
        self.transcription_label.text = 'El texto transcrito aparecerá aquí...'
        self.transcription_label.color = get_color_from_hex('#7F8C8D')
        self._update_status("🗑️ Transcripción limpiada")
    
    def _on_back_pressed(self, instance):
        """
        Maneja el evento de volver atrás
        """
        # Cancelar animación si existe
        if self.animation_event:
            self.animation_event.cancel()
            self.animation_event = None
        
        # Detener grabación si está activa
        if self.is_recording and AUDIO_AVAILABLE and self.audio_service:
            self.audio_service.stop_listening()
        
        # Llamar al callback de volver
        if self.on_back:
            self.on_back()
    
    def on_stop(self):
        """
        Limpieza cuando se cierra la pantalla
        """
        # Cancelar animación si existe
        if self.animation_event:
            self.animation_event.cancel()
            self.animation_event = None
        
        # Detener grabación si está activa
        if self.is_recording and AUDIO_AVAILABLE and self.audio_service:
            self.audio_service.stop_listening()
