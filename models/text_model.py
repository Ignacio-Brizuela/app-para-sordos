from kivy.utils import platform
from plyer import tts
from gtts import gTTS
import os
import tempfile

try:
    from playsound import playsound
    PLAYSOUND_AVAILABLE = True
except ImportError:
    PLAYSOUND_AVAILABLE = False

class TextModel:
    """
    Clase para manejar las funcionalidades relacionadas con la escritura de texto y la síntesis de voz.
    """

    def __init__(self):
        # Aquí puedes inicializar cualquier variable o configuración necesaria
        self.text_data = ""

    def save_text(self, text):
        """
        Guarda el texto proporcionado en una variable o archivo.
        :param text: Texto a guardar
        """
        self.text_data = text
        print(f"Texto guardado: {self.text_data}")

    def process_text(self):
        """
        Procesa el texto guardado (puedes agregar funcionalidades como análisis, limpieza, etc.).
        :return: Texto procesado
        """
        # Por ahora, simplemente devuelve el texto guardado
        return self.text_data

    def clear_text(self):
        """
        Limpia el texto guardado.
        """
        self.text_data = ""
        print("Texto limpiado.")

    def speak_text(self):
        """
        Utiliza plyer.tts para leer el texto guardado en voz alta.
        """
        if self.text_data.strip():
            try:
                if platform == 'android' or platform == 'ios':
                    # Usar plyer.tts para síntesis de voz en móviles
                    tts.speak(self.text_data)
                    print(f"🔊 Reproduciendo: {self.text_data[:50]}...")
                else:
                    # Para otros sistemas, usar gTTS como alternativa
                    gtts_obj = gTTS(text=self.text_data, lang='es')
                    
                    # Usar tempfile para crear archivo temporal seguro
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as tmp_file:
                        audio_file = tmp_file.name
                    
                    gtts_obj.save(audio_file)
                    
                    if PLAYSOUND_AVAILABLE:
                        playsound(audio_file)
                    else:
                        print(f"⚠️ playsound no disponible. Audio guardado en: {audio_file}")
                        return  # No eliminar si no se puede reproducir
                    
                    # Eliminar el archivo temporal después de reproducirlo
                    try:
                        os.remove(audio_file)
                    except Exception as e:
                        print(f"⚠️ No se pudo eliminar archivo temporal: {e}")
            except Exception as e:
                print(f"Error al reproducir el texto: {e}")
        else:
            print("No hay texto para leer.")