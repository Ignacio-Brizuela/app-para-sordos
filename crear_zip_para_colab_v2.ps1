# Script mejorado para crear ZIP compatible con Linux/Colab
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host "  Creando ZIP para Google Colab - App Para Sordos v0.2" -ForegroundColor Cyan
Write-Host "========================================================" -ForegroundColor Cyan
Write-Host ""

# Configuración
$zipName = "APP_PARA_SORDOS_v0.2.zip"
$projectName = "app"

# Eliminar ZIP anterior si existe
if (Test-Path $zipName) {
    Remove-Item $zipName
    Write-Host "[INFO] ZIP anterior eliminado" -ForegroundColor Yellow
}

# Eliminar directorio temporal si existe
if (Test-Path $projectName) {
    Remove-Item -Recurse -Force $projectName
}

# Crear estructura de proyecto
Write-Host "Creando estructura de proyecto..." -ForegroundColor Green
New-Item -ItemType Directory -Path $projectName | Out-Null

# Archivos a copiar
$files = @("main.py", "buildozer.spec", "requirements.txt")
$folders = @("models", "services", "ui", "imagenes")

Write-Host ""
Write-Host "Copiando archivos..." -ForegroundColor Green

# Copiar archivos principales
foreach ($file in $files) {
    if (Test-Path $file) {
        Copy-Item $file -Destination $projectName
        Write-Host "  [OK] $file" -ForegroundColor Gray
    } else {
        Write-Host "  [WARNING] $file NO encontrado" -ForegroundColor Red
    }
}

# Copiar carpetas (excluyendo __pycache__)
foreach ($folder in $folders) {
    if (Test-Path $folder) {
        $destFolder = Join-Path $projectName $folder
        New-Item -ItemType Directory -Path $destFolder -Force | Out-Null
        
        # Copiar solo archivos .py, .png, etc. (no __pycache__)
        Get-ChildItem -Path $folder -Recurse -File | ForEach-Object {
            if ($_.DirectoryName -notlike "*__pycache__*") {
                $relativePath = $_.FullName.Substring((Get-Item $folder).FullName.Length + 1)
                $destPath = Join-Path $destFolder $relativePath
                $destDir = Split-Path $destPath -Parent
                
                if (-not (Test-Path $destDir)) {
                    New-Item -ItemType Directory -Path $destDir -Force | Out-Null
                }
                
                Copy-Item $_.FullName -Destination $destPath
            }
        }
        
        $fileCount = (Get-ChildItem -Path $destFolder -Recurse -File).Count
        Write-Host "  [OK] $folder/ ($fileCount archivos)" -ForegroundColor Gray
    } else {
        Write-Host "  [WARNING] $folder/ NO encontrado" -ForegroundColor Yellow
    }
}

Write-Host ""
Write-Host "Comprimiendo..." -ForegroundColor Green

# Crear ZIP del directorio completo
Compress-Archive -Path "$projectName\*" -DestinationPath $zipName -Force

# Limpiar directorio temporal
Remove-Item -Recurse -Force $projectName

$size = [math]::Round((Get-Item $zipName).Length / 1KB, 2)

Write-Host ""
Write-Host "========================================================" -ForegroundColor Green
Write-Host "              ZIP CREADO EXITOSAMENTE                  " -ForegroundColor Green
Write-Host "========================================================" -ForegroundColor Green
Write-Host ""
Write-Host "Archivo: $zipName" -ForegroundColor Cyan
Write-Host "Tamano: $size KB" -ForegroundColor Cyan
Write-Host ""
Write-Host "Nuevas caracteristicas incluidas:" -ForegroundColor Yellow
Write-Host "  * Reconocimiento de voz nativo (Android SpeechRecognizer)" -ForegroundColor Gray
Write-Host "  * Texto a voz con TTS nativo (plyer.tts)" -ForegroundColor Gray
Write-Host "  * Navegacion completa con botones 'Volver'" -ForegroundColor Gray
Write-Host "  * UI mejorada en todas las pantallas" -ForegroundColor Gray
Write-Host "  * Manejo robusto de errores" -ForegroundColor Gray
Write-Host "  * Sin archivos __pycache__" -ForegroundColor Gray
Write-Host ""
Write-Host "SIGUIENTES PASOS:" -ForegroundColor Yellow
Write-Host "  1. Abre Google Colab (colab.research.google.com)" -ForegroundColor White
Write-Host "  2. Sube BUILD_APK_COLAB_OPTIMIZADO.ipynb" -ForegroundColor White
Write-Host "  3. Ejecuta Celda 1 (Instalar dependencias)" -ForegroundColor White
Write-Host "  4. Ejecuta Celda 2A y sube este ZIP" -ForegroundColor White
Write-Host "  5. Ejecuta Celda 3 (Verificar)" -ForegroundColor White
Write-Host "  6. Ejecuta Celda 4 (Build completo ~45 min)" -ForegroundColor White
Write-Host "  7. Ejecuta Celda 6 (Descargar APK)" -ForegroundColor White
Write-Host ""
Write-Host "PARA ACTUALIZACIONES FUTURAS:" -ForegroundColor Cyan
Write-Host "  - Solo sube archivos modificados (Celda 2B)" -ForegroundColor White
Write-Host "  - Usa Build Incremental (Celda 5 ~10 min)" -ForegroundColor White
Write-Host ""
Write-Host "Listo para subir a Colab!" -ForegroundColor Green
Write-Host ""
