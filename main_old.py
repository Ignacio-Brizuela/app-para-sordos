import os
import sys
import traceback

try:
    from kivy.app import App
    from kivy.uix.boxlayout import BoxLayout
    from kivy.uix.label import Label
    from kivy.core.window import Window
    from kivy.utils import get_color_from_hex, platform
    from kivy.uix.button import Button
    from kivy.uix.textinput import TextInput
    
    print(f"✅ Kivy importado correctamente (Plataforma: {platform})")
    
    # Importar modelos
    from models.text_model import TextModel
    
    # MicrophoneScreen se importará solo cuando se necesite
    MicrophoneScreen = None
    
    print("✅ Módulos de la app importados correctamente")
except Exception as e:
    print(f"❌ ERROR EN IMPORTS: {e}")
    traceback.print_exc()
    sys.exit(1)

# --- CONFIGURACIÓN DE COLORES ---
COLOR_FONDO = '#FAFAFA'
COLOR_TEXTO_PRINCIPAL = '#333333'
COLOR_BTN_TEXTO = '#4A90E2'  # Azul
COLOR_BTN_MIC = '#FF6B6B'    # Rojo

Window.clearcolor = get_color_from_hex(COLOR_FONDO)

class BotonGrande(Button):
    """
    Botón simplificado para evitar problemas de threading en Android
    """
    def __init__(self, texto, color_bg, action, **kwargs):
        super(BotonGrande, self).__init__(**kwargs)
        self.text = texto
        self.font_size = '24sp'
        self.bold = True
        self.size_hint = (0.5, 1)
        self.background_color = get_color_from_hex(color_bg)
        self.bind(on_press=action)

class MainScreen(BoxLayout):
    def __init__(self, **kwargs):
        super(MainScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20
        
        # --- CABECERA ---
        header_layout = BoxLayout(orientation='vertical', size_hint=(1, 0.2))
        
        title = Label(
            text='Asistente',
            font_size='40sp',
            bold=True,
            color=get_color_from_hex(COLOR_TEXTO_PRINCIPAL)
        )
        header_layout.add_widget(title)
        
        subtitle = Label(
            text='Selecciona una opción',
            font_size='18sp',
            color=get_color_from_hex('#7F8C8D')
        )
        header_layout.add_widget(subtitle)
        self.add_widget(header_layout)
        
        # --- BOTONES ---
        botones_layout = BoxLayout(
            orientation='horizontal', 
            spacing=30, 
            size_hint=(1, 0.5)
        )
        
        btn_texto = BotonGrande(
            texto='📝 Escribir',
            color_bg=COLOR_BTN_TEXTO,
            action=self.on_text_input
        )
        
        btn_mic = BotonGrande(
            texto='🎤 Micrófono',
            color_bg=COLOR_BTN_MIC,
            action=self.on_mic_input
        )
        
        botones_layout.add_widget(btn_texto)
        botones_layout.add_widget(btn_mic)
        
        self.add_widget(botones_layout)
        
        # Espacio inferior (vacío y limpio)
        self.add_widget(Label(size_hint=(1, 0.3)))

    def on_text_input(self, instance):
        print("Entrada de texto")
        self.app_reference.switch_to_text_input()
    
    def on_mic_input(self, instance):
        print("Entrada de micrófono")
        if hasattr(self, 'app_reference'):
            self.app_reference.switch_to_microphone()

class TextInputScreen(BoxLayout):
    def __init__(self, on_back=None, **kwargs):
        super(TextInputScreen, self).__init__(**kwargs)
        self.orientation = 'vertical'
        self.padding = 40
        self.spacing = 20
        
        # Callback para volver
        self.on_back = on_back

        # Inicializar el modelo de texto
        self.text_model = TextModel()
        
        # --- HEADER CON BOTÓN VOLVER ---
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
            text='✍️ Entrada de Texto',
            font_size='24sp',
            size_hint=(0.7, 1),
            color=get_color_from_hex('#2C3E50'),
            bold=True
        )
        
        header.add_widget(back_button)
        header.add_widget(title)
        self.add_widget(header)

        # --- ÁREA DE ENTRADA DE TEXTO ---
        self.text_input = TextInput(
            hint_text='Escribe aquí el texto que quieres convertir a voz...',
            multiline=True,
            size_hint=(1, 0.7),
            font_size='18sp',
            background_color=get_color_from_hex('#FFFFFF'),
            foreground_color=get_color_from_hex('#2C3E50')
        )
        self.add_widget(self.text_input)
        
        # --- BOTONES DE CONTROL ---
        controls = BoxLayout(size_hint=(1, 0.15), spacing=10)

        # --- BOTÓN DE REPRODUCIR ---
        speak_button = Button(
            text='🔊 Reproducir Audio',
            font_size='20sp',
            size_hint=(0.7, 1),
            background_color=get_color_from_hex('#27AE60'),
            background_normal='',
            color=(1, 1, 1, 1),
            bold=True
        )
        speak_button.bind(on_press=self.on_speak)
        
        # --- BOTÓN DE LIMPIAR ---
        clear_button = Button(
            text='🗑️',
            font_size='20sp',
            size_hint=(0.3, 1),
            background_color=get_color_from_hex('#E74C3C'),
            background_normal='',
            color=(1, 1, 1, 1),
            bold=True
        )
        clear_button.bind(on_press=self.on_clear)
        
        controls.add_widget(speak_button)
        controls.add_widget(clear_button)
        self.add_widget(controls)
        
        # Información adicional
        info = Label(
            text='Escribe tu texto y presiona "Reproducir Audio" para escucharlo',
            font_size='14sp',
            size_hint=(1, 0.05),
            color=get_color_from_hex('#95A5A6'),
            italic=True
        )
        self.add_widget(info)
    
    def _on_back_pressed(self, instance):
        """Vuelve a la pantalla principal"""
        if self.on_back:
            self.on_back()

    def on_speak(self, instance):
        """Reproduce el texto como audio"""
        text = self.text_input.text
        if text.strip():
            print(f"Texto a reproducir: {text}")
            # Guardar y reproducir el texto usando el modelo
            self.text_model.save_text(text)
            self.text_model.speak_text()
        else:
            print("⚠️ No hay texto para reproducir")
    
    def on_clear(self, instance):
        """Limpia el texto"""
        self.text_input.text = ""
        self.text_model.clear_text()
        print("🗑️ Texto limpiado")

class AppParaSordosApp(App):
    def build(self):
        self.title = 'App Para Sordos'
        self.root_container = BoxLayout()
        
        self.main_screen = MainScreen()
        self.main_screen.app_reference = self
        self.microphone_screen = None
        self.text_input_screen = None
        
        self.root_container.add_widget(self.main_screen)
        return self.root_container
    
    def switch_to_microphone(self):
        self.root_container.clear_widgets()
        if self.microphone_screen is None:
            # Importar solo cuando se necesite (lazy import)
            try:
                from ui.microphone_screen import MicrophoneScreen
                self.microphone_screen = MicrophoneScreen(on_back=self.switch_to_main)
            except Exception as e:
                print(f"❌ Error importando MicrophoneScreen: {e}")
                # Si falla, volver al menú principal
                self.switch_to_main()
                return
        self.root_container.add_widget(self.microphone_screen)
    
    def switch_to_main(self):
        self.root_container.clear_widgets()
        self.root_container.add_widget(self.main_screen)
    
    def switch_to_text_input(self):
        self.root_container.clear_widgets()
        if self.text_input_screen is None:
            self.text_input_screen = TextInputScreen(on_back=self.switch_to_main)
        self.root_container.add_widget(self.text_input_screen)
    
    def on_stop(self):
        if self.microphone_screen:
            self.microphone_screen.on_stop()
        return super().on_stop()

if __name__ == '__main__':
    try:
        print("🚀 Iniciando App Para Sordos...")
        app = AppParaSordosApp()
        app.run()
    except Exception as e:
        print(f"❌ ERROR FATAL: {e}")
        traceback.print_exc()
        import time
        time.sleep(10)  # Dar tiempo para ver el error
        sys.exit(1)