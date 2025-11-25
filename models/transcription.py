"""
Estructuras de datos para manejar las transcripciones de audio
"""
from datetime import datetime
from typing import List, Optional


class Transcription:
    """
    Clase que representa una transcripción individual de audio a texto
    """
    def __init__(self, text: str, confidence: float = 0.0, timestamp: Optional[datetime] = None):
        """
        Inicializa una transcripción
        
        Args:
            text: Texto transcrito
            confidence: Nivel de confianza de la transcripción (0-1)
            timestamp: Momento de la transcripción
        """
        self.text = text
        self.confidence = confidence
        self.timestamp = timestamp or datetime.now()
    
    def __str__(self) -> str:
        return f"[{self.timestamp.strftime('%H:%M:%S')}] {self.text}"
    
    def __repr__(self) -> str:
        return f"Transcription(text='{self.text}', confidence={self.confidence})"


class TranscriptionHistory:
    """
    Clase que mantiene un historial de transcripciones usando una lista
    """
    def __init__(self, max_size: int = 100):
        """
        Inicializa el historial de transcripciones
        
        Args:
            max_size: Número máximo de transcripciones a mantener en memoria
        """
        self._history: List[Transcription] = []
        self.max_size = max_size
    
    def add(self, transcription: Transcription) -> None:
        """
        Agrega una nueva transcripción al historial
        
        Args:
            transcription: Objeto Transcription a agregar
        """
        self._history.append(transcription)
        
        # Si excede el tamaño máximo, eliminar la más antigua
        if len(self._history) > self.max_size:
            self._history.pop(0)
    
    def get_all(self) -> List[Transcription]:
        """
        Obtiene todas las transcripciones del historial
        
        Returns:
            Lista de objetos Transcription
        """
        return self._history.copy()
    
    def get_last(self, n: int = 1) -> List[Transcription]:
        """
        Obtiene las últimas n transcripciones
        
        Args:
            n: Número de transcripciones a obtener
            
        Returns:
            Lista con las últimas n transcripciones
        """
        return self._history[-n:] if n <= len(self._history) else self._history.copy()
    
    def clear(self) -> None:
        """
        Limpia todo el historial de transcripciones
        """
        self._history.clear()
    
    def get_full_text(self, separator: str = "\n") -> str:
        """
        Obtiene todo el texto transcrito concatenado
        
        Args:
            separator: Separador entre transcripciones
            
        Returns:
            Texto completo del historial
        """
        return separator.join([t.text for t in self._history])
    
    def count(self) -> int:
        """
        Retorna el número de transcripciones en el historial
        
        Returns:
            Cantidad de transcripciones
        """
        return len(self._history)
    
    def __len__(self) -> int:
        return len(self._history)
    
    def __str__(self) -> str:
        return f"TranscriptionHistory({len(self._history)} transcripciones)"
