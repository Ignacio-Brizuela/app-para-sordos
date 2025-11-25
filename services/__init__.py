"""
Servicios de la aplicación
"""
from kivy.utils import platform

# Solo cargar en desktop - Android NO SOPORTADO
if platform != 'android':
    from .audio_service import AudioTranscriptionService
    print("✅ AudioTranscriptionService cargado (Desktop)")
else:
    AudioTranscriptionService = None
    print("ℹ️ AudioTranscriptionService deshabilitado (Android)")

__all__ = ['AudioTranscriptionService']
