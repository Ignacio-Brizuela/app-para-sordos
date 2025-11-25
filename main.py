"""
Versión ULTRA SIMPLIFICADA - Solo para verificar que funciona en Android
"""
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.utils import platform

print(f"Iniciando app en plataforma: {platform}")

class SimpleApp(App):
    def build(self):
        # Layout principal vertical
        layout = BoxLayout(orientation='vertical', padding=20, spacing=10)
        
        # Título
        layout.add_widget(Label(
            text='App Para Sordos v0.3',
            size_hint=(1, 0.1),
            font_size='20sp'
        ))
        
        # Input de texto
        self.text_input = TextInput(
            hint_text='Escribe algo aquí...',
            size_hint=(1, 0.4),
            multiline=True,
            font_size='18sp'
        )
        layout.add_widget(self.text_input)
        
        # Botón TTS
        btn_speak = Button(
            text='🔊 Hablar',
            size_hint=(1, 0.2),
            font_size='18sp'
        )
        btn_speak.bind(on_press=self.speak_text)
        layout.add_widget(btn_speak)
        
        # Label de estado
        self.status = Label(
            text='Lista para usar',
            size_hint=(1, 0.1),
            font_size='14sp'
        )
        layout.add_widget(self.status)
        
        # Botón cerrar
        btn_close = Button(
            text='Cerrar',
            size_hint=(1, 0.1)
        )
        btn_close.bind(on_press=self.stop)
        layout.add_widget(btn_close)
        
        return layout
    
    def speak_text(self, instance):
        texto = self.text_input.text.strip()
        if not texto:
            self.status.text = '⚠️ Escribe algo primero'
            return
        
        try:
            if platform == 'android':
                from plyer import tts
                tts.speak(texto)
                self.status.text = f'✅ Hablando: {texto[:30]}...'
            else:
                from gtts import gTTS
                import tempfile
                import os
                
                tts = gTTS(text=texto, lang='es')
                temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
                tts.save(temp_file.name)
                
                try:
                    from playsound import playsound
                    playsound(temp_file.name)
                except:
                    pass
                
                os.unlink(temp_file.name)
                self.status.text = f'✅ Reproducido: {texto[:30]}...'
        except Exception as e:
            self.status.text = f'❌ Error: {str(e)[:50]}'
            print(f"Error en TTS: {e}")

if __name__ == '__main__':
    SimpleApp().run()
