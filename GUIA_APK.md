# 📱 Guía para Compilar APK en Google Colab

## 🚀 Pasos Rápidos

### 1. Preparar el Proyecto

Ejecuta el script para crear el ZIP:
```powershell
.\crear_zip_para_colab.ps1
```

Esto creará un archivo `APP_PARA_SORDOS.zip` con todos los archivos necesarios.

### 2. Abrir Google Colab

1. Ve a [Google Colab](https://colab.research.google.com/)
2. Haz clic en **File → Upload notebook**
3. Sube el archivo `BUILD_APK_COLAB.ipynb`

### 3. Ejecutar las Celdas

**Ejecuta las celdas EN ORDEN:**

#### Celda 1: Instalar dependencias (5-10 min)
- Instala Java, Buildozer, Cython, etc.
- ✅ Espera el mensaje "Dependencias instaladas correctamente"

#### Celda 2 ALTERNATIVA: Subir proyecto como ZIP (RECOMENDADO)
- Haz clic en el botón de subir
- Selecciona `APP_PARA_SORDOS.zip`
- ✅ Verifica que aparezcan `main.py` y `buildozer.spec`

#### Celda 3: Compilar APK (30-40 min) ⏳
- **NO CIERRES LA PESTAÑA**
- Puedes minimizar pero mantén la sesión activa
- ✅ Espera el mensaje "Compilación completada"

#### Celda 4: Descargar APK
- El APK se descargará automáticamente
- Tamaño aproximado: 20-30 MB

### 4. Instalar en Android

1. Transfiere el APK a tu dispositivo Android
2. Habilita **"Orígenes desconocidos"** en Configuración
3. Abre el APK y sigue las instrucciones

## ⚠️ LIMITACIONES IMPORTANTES

### Funcionalidad de Micrófono en Android

**PROBLEMA:** `SpeechRecognition` y `PyAudio` no funcionan en Android.

**RAZÓN:** Estas bibliotecas son para Python de escritorio y no son compatibles con Android.

**SOLUCIÓN ACTUAL:**
- La interfaz de la app funcionará perfectamente ✅
- El botón de micrófono estará visible ✅
- Pero NO capturará audio en Android ❌

### Para Implementar Reconocimiento de Voz en Android:

Necesitarás usar **Java/Kotlin** con las APIs nativas de Android:

```java
// Ejemplo con SpeechRecognizer de Android
SpeechRecognizer speechRecognizer = SpeechRecognizer.createSpeechRecognizer(context);
Intent intent = new Intent(RecognizerIntent.ACTION_RECOGNIZE_SPEECH);
intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE_MODEL, RecognizerIntent.LANGUAGE_MODEL_FREE_FORM);
intent.putExtra(RecognizerIntent.EXTRA_LANGUAGE, "es-ES");
speechRecognizer.startListening(intent);
```

### Alternativas para Android:

1. **Usar Pyjnius** (Python + Java):
   - Permite llamar código Java desde Python
   - Requiere implementación adicional en Buildozer
   - Más complejo pero funcional

2. **Usar KivyMD + Android APIs**:
   - Usar `plyer` para acceder a permisos
   - Implementar servicio de audio nativo
   - Requiere conocimientos de Android

3. **Reescribir en Flutter/React Native**:
   - Más soporte nativo
   - Mejor rendimiento
   - Curva de aprendizaje

## 📊 Comparación de Opciones

| Opción | Dificultad | Tiempo | Funcionalidad |
|--------|-----------|--------|---------------|
| APK actual (Kivy) | ⭐ Fácil | 1 hora | Solo UI ✅ |
| Kivy + Pyjnius | ⭐⭐⭐ Difícil | 1 semana | Todo funcional ✅ |
| Flutter/React Native | ⭐⭐⭐⭐ Muy difícil | 2-3 semanas | Todo + mejor UX ✅ |

## 🎯 Recomendación

### Para Pruebas y Demostración:
✅ Usa el APK actual - la interfaz se verá bien

### Para Producción:
❌ El APK actual no es suficiente
✅ Considera reescribir en Flutter o React Native
✅ O usar Kivy + Pyjnius para Android

## 📝 Notas Adicionales

### Requisitos de Android:
- Android 5.0 (API 21) o superior
- Permisos: RECORD_AUDIO, INTERNET
- ~30 MB de espacio de almacenamiento

### Permisos necesarios:
- `RECORD_AUDIO`: Para capturar audio del micrófono
- `INTERNET`: Para enviar audio a API de reconocimiento

### Próximos Pasos para Funcionalidad Completa:

1. Investigar implementación con Pyjnius
2. Crear servicio de Android para captura de audio
3. Integrar con Google Speech-to-Text API de Android
4. Probar en dispositivos físicos

## 🔗 Enlaces Útiles

- [Buildozer Documentation](https://buildozer.readthedocs.io/)
- [Kivy Android Guide](https://kivy.org/doc/stable/guide/android.html)
- [Pyjnius Documentation](https://pyjnius.readthedocs.io/)
- [Android SpeechRecognizer](https://developer.android.com/reference/android/speech/SpeechRecognizer)

## ❓ Solución de Problemas

### Error: "SDK not found"
```bash
# En Colab, ejecuta:
!buildozer android clean
!rm -rf .buildozer
# Luego vuelve a compilar
```

### Error: "NDK not found"
```bash
# Verifica la versión en buildozer.spec
android.ndk = 25b
```

### Error de memoria en Colab
- Usa Runtime → Factory reset runtime
- Vuelve a ejecutar desde el principio

### APK muy grande
- Normal para apps Kivy (20-30 MB mínimo)
- Incluye Python interpreter + Kivy framework

## 📞 Soporte

Si tienes problemas:
1. Revisa los logs en la celda de "Solución de problemas"
2. Verifica que todos los archivos estén en el ZIP
3. Asegúrate de que buildozer.spec esté actualizado

---

**¡Buena suerte con tu compilación!** 🚀
