# 📱 Guía: Compilar APK con GitHub Actions

## 🎯 Ventajas

- ✅ **Automático:** Solo haces push y GitHub compila
- ✅ **Gratis:** 2000 minutos/mes incluidos
- ✅ **No esperas:** Se compila en segundo plano
- ✅ **APK guardado:** Disponible por 30 días

---

## 📋 Pasos iniciales (solo una vez)

### 1. Crear repositorio en GitHub

1. Ve a [github.com](https://github.com)
2. Clic en **"New repository"** (botón verde)
3. Nombre: `app-para-sordos`
4. Marca: ☑️ Public (o Private si prefieres)
5. Clic en **"Create repository"**

### 2. Subir tu código

Abre PowerShell en la carpeta del proyecto y ejecuta:

```powershell
# Inicializar Git
git init

# Agregar archivos
git add .

# Primer commit
git commit -m "Versión 0.3 - App simplificada"

# Conectar con GitHub (reemplaza TU_USUARIO)
git remote add origin https://github.com/TU_USUARIO/app-para-sordos.git

# Subir código
git branch -M main
git push -u origin main
```

---

## 🚀 Usar GitHub Actions

### Compilar automáticamente

Cada vez que hagas cambios:

```powershell
# 1. Modificas archivos (main.py, etc.)

# 2. Guardas cambios
git add .
git commit -m "Descripción del cambio"

# 3. Subes a GitHub
git push
```

**GitHub compilará automáticamente** en ~40 minutos.

### Ver progreso

1. Ve a tu repositorio en GitHub
2. Clic en pestaña **"Actions"**
3. Verás el workflow ejecutándose (🟡 amarillo = compilando)
4. Cuando termine (✅ verde), el APK estará listo

### Descargar APK

1. En **Actions**, clic en el workflow completado
2. Baja hasta **"Artifacts"**
3. Clic en `app-para-sordos-v0.3` para descargar

---

## 🔧 Compilar manualmente (sin esperar push)

1. Ve a tu repositorio → **Actions**
2. Clic en **"Build Android APK"** (izquierda)
3. Clic en **"Run workflow"** (derecha)
4. Selecciona branch `main`
5. Clic en **"Run workflow"** verde

GitHub compilará inmediatamente.

---

## ⚙️ Configuración avanzada

### Cambiar versión automáticamente

El workflow lee la versión de `buildozer.spec`. Para cambiarla:

```powershell
# Edita buildozer.spec
# Cambia: version = 0.4

git add buildozer.spec
git commit -m "Actualizar a v0.4"
git push
```

### Notificaciones por email

GitHub te enviará un email cuando:
- ✅ La compilación termine exitosamente
- ❌ Falle la compilación

Configúralo en: **Settings → Notifications**

---

## 🆘 Solución de problemas

### "Workflow failed"

1. Ve a Actions → workflow fallido
2. Clic en el job que falló
3. Revisa los logs (texto rojo)
4. El error suele estar al final

### "No se genera el APK"

Verifica que `buildozer.spec` esté en la raíz del proyecto.

### "GitHub Actions no aparece"

Asegúrate de que el archivo `.github/workflows/build-apk.yml` existe.

---

## 📊 Límites de GitHub Actions

- **Gratis:** 2000 minutos/mes
- **Cada compilación:** ~40 minutos
- **Máximo:** ~50 compilaciones/mes gratis

Si necesitas más, puedes:
- Usar Google Colab como respaldo
- Compilar localmente con WSL

---

## ✅ Ventajas vs Colab

| Característica | GitHub Actions | Google Colab |
|----------------|----------------|--------------|
| Automático | ✅ Sí | ❌ Manual |
| Cerrar navegador | ✅ Sí | ❌ Se cancela |
| APK guardado | ✅ 30 días | ❌ Debes descargar |
| Notificaciones | ✅ Email | ❌ No |
| Velocidad | ~40 min | ~40 min |
| Costo | 🆓 Gratis | 🆓 Gratis |

---

**¡Listo!** Ahora cada vez que hagas cambios y los subas a GitHub, tendrás un APK nuevo automáticamente.
