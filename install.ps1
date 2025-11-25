# Script de instalación y configuración del proyecto
# Ejecuta este script para instalar todas las dependencias necesarias

Write-Host "=" -NoNewline -ForegroundColor Cyan
Write-Host ("=" * 60) -ForegroundColor Cyan
Write-Host "  Instalación - App Para Sordos" -ForegroundColor Yellow
Write-Host ("=" * 60) -ForegroundColor Cyan
Write-Host ""

# Verificar si Python está instalado
Write-Host "[1/4] Verificando Python..." -ForegroundColor Green
try {
    $pythonVersion = python --version
    Write-Host "  ✓ Python encontrado: $pythonVersion" -ForegroundColor Gray
} catch {
    Write-Host "  ✗ Python no encontrado. Por favor instala Python 3.8 o superior." -ForegroundColor Red
    exit 1
}

# Verificar si pip está instalado
Write-Host "`n[2/4] Verificando pip..." -ForegroundColor Green
try {
    $pipVersion = pip --version
    Write-Host "  ✓ pip encontrado: $pipVersion" -ForegroundColor Gray
} catch {
    Write-Host "  ✗ pip no encontrado. Por favor instala pip." -ForegroundColor Red
    exit 1
}

# Instalar dependencias
Write-Host "`n[3/4] Instalando dependencias..." -ForegroundColor Green
Write-Host "  Esto puede tomar varios minutos..." -ForegroundColor Gray

# Intentar instalar las dependencias
try {
    pip install -r requirements.txt
    Write-Host "  ✓ Dependencias instaladas correctamente" -ForegroundColor Gray
} catch {
    Write-Host "  ⚠ Algunas dependencias pueden haber fallado" -ForegroundColor Yellow
    Write-Host "  Si PyAudio falla en Windows, ejecuta:" -ForegroundColor Yellow
    Write-Host "    pip install pipwin" -ForegroundColor Cyan
    Write-Host "    pipwin install pyaudio" -ForegroundColor Cyan
}

# Verificar instalación
Write-Host "`n[4/4] Verificando instalación..." -ForegroundColor Green

$modulosRequeridos = @("kivy", "speech_recognition")
$todosInstalados = $true

foreach ($modulo in $modulosRequeridos) {
    try {
        python -c "import $modulo" 2>$null
        Write-Host "  ✓ $modulo instalado correctamente" -ForegroundColor Gray
    } catch {
        Write-Host "  ✗ $modulo NO instalado" -ForegroundColor Red
        $todosInstalados = $false
    }
}

# Resultado final
Write-Host "`n" -NoNewline
Write-Host ("=" * 60) -ForegroundColor Cyan

if ($todosInstalados) {
    Write-Host "  ✓ INSTALACIÓN COMPLETA" -ForegroundColor Green
    Write-Host ("=" * 60) -ForegroundColor Cyan
    Write-Host "`nPara ejecutar la aplicación:" -ForegroundColor Yellow
    Write-Host "  python main.py" -ForegroundColor Cyan
    Write-Host "`nPara ver ejemplos de uso:" -ForegroundColor Yellow
    Write-Host "  python ejemplos_uso.py" -ForegroundColor Cyan
} else {
    Write-Host "  ⚠ INSTALACIÓN INCOMPLETA" -ForegroundColor Yellow
    Write-Host ("=" * 60) -ForegroundColor Cyan
    Write-Host "`nAlgunos módulos no se instalaron correctamente." -ForegroundColor Yellow
    Write-Host "Por favor revisa los errores arriba." -ForegroundColor Yellow
}

Write-Host ""
