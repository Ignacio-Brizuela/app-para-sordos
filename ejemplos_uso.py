"""
Ejemplo de uso de las estructuras de datos y servicios
de forma independiente (sin necesidad de la UI de Kivy)
"""
from models.transcription import Transcription, TranscriptionHistory
from services.audio_service import AudioTranscriptionService
import time


def ejemplo_estructuras_datos():
    """
    Demuestra el uso de las estructuras de datos
    """
    print("=" * 60)
    print("EJEMPLO 1: Uso de Estructuras de Datos")
    print("=" * 60)
    
    # Crear historial
    historial = TranscriptionHistory(max_size=5)
    
    # Agregar transcripciones
    transcripciones = [
        Transcription("Hola, ¿cómo estás?", confidence=0.95),
        Transcription("Muy bien, gracias por preguntar", confidence=0.92),
        Transcription("¿Qué tal tu día?", confidence=0.88),
    ]
    
    for t in transcripciones:
        historial.add(t)
        print(f"Agregada: {t}")
    
    print(f"\nTotal de transcripciones: {historial.count()}")
    print(f"\nTexto completo:\n{historial.get_full_text()}")
    
    # Obtener las últimas 2
    print(f"\nÚltimas 2 transcripciones:")
    for t in historial.get_last(2):
        print(f"  - {t.text}")
    
    # Limpiar
    historial.clear()
    print(f"\nDespués de limpiar: {historial.count()} transcripciones")


def ejemplo_servicio_audio():
    """
    Demuestra el uso del servicio de audio
    (Este ejemplo solo muestra la configuración, no ejecuta la grabación)
    """
    print("\n" + "=" * 60)
    print("EJEMPLO 2: Configuración del Servicio de Audio")
    print("=" * 60)
    
    # Crear servicio
    servicio = AudioTranscriptionService()
    
    # Configurar callbacks
    def on_transcription(transcription):
        print(f"\n[TRANSCRIPCIÓN] {transcription.text}")
    
    def on_error(error):
        print(f"\n[ERROR] {error}")
    
    def on_listening(is_listening):
        estado = "ESCUCHANDO" if is_listening else "DETENIDO"
        print(f"\n[ESTADO] {estado}")
    
    servicio.set_on_transcription(on_transcription)
    servicio.set_on_error(on_error)
    servicio.set_on_listening(on_listening)
    
    # Verificar micrófono
    mic_disponible = servicio.check_microphone_available()
    print(f"\nMicrófono disponible: {mic_disponible}")
    
    if mic_disponible:
        print("\nPara usar el servicio en un programa real:")
        print("1. servicio.start_listening()  # Iniciar escucha")
        print("2. ... (hablar al micrófono) ...")
        print("3. servicio.stop_listening()   # Detener escucha")
        print("4. texto = servicio.get_history().get_full_text()")
    else:
        print("\n⚠️ No se detectó micrófono. Conecta uno para usar esta función.")


def ejemplo_integracion():
    """
    Demuestra cómo las estructuras de datos y servicios trabajan juntos
    """
    print("\n" + "=" * 60)
    print("EJEMPLO 3: Integración de Componentes")
    print("=" * 60)
    
    # El servicio internamente usa TranscriptionHistory
    servicio = AudioTranscriptionService()
    
    # Simular transcripciones (sin usar el micrófono real)
    from datetime import datetime
    
    transcripciones_simuladas = [
        "Buenos días",
        "¿Cómo puedo ayudarte?",
        "Estoy aquí para asistirte"
    ]
    
    print("\nSimulando transcripciones:")
    for texto in transcripciones_simuladas:
        t = Transcription(texto, confidence=0.90)
        servicio.history.add(t)
        print(f"  ✓ {t}")
    
    # Obtener historial
    print(f"\nHistorial completo ({servicio.history.count()} elementos):")
    print(servicio.history.get_full_text(separator="\n  → "))
    
    # Estadísticas
    print(f"\nEstadísticas:")
    print(f"  - Total de transcripciones: {len(servicio.history)}")
    print(f"  - Primera transcripción: {servicio.history.get_all()[0].text}")
    print(f"  - Última transcripción: {servicio.history.get_last(1)[0].text}")


def main():
    """
    Función principal que ejecuta todos los ejemplos
    """
    print("\n" + "=" * 60)
    print("EJEMPLOS DE USO - Sistema de Transcripción")
    print("=" * 60)
    
    ejemplo_estructuras_datos()
    ejemplo_servicio_audio()
    ejemplo_integracion()
    
    print("\n" + "=" * 60)
    print("✓ Ejemplos completados")
    print("=" * 60)
    print("\nPara usar la aplicación completa con UI, ejecuta: python main.py")


if __name__ == "__main__":
    main()
