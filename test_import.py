import sys
import os

print("Intentando importar 'app' desde un script normal...")
print(f"Directorio actual: {os.getcwd()}")
print("sys.path:")
for p in sys.path:
    print(f"  - {p}")

try:
    from app.main import app
    print("\n¡ÉXITO! Se pudo importar 'app.main.app'")
    print(f"Ubicación del módulo 'app': {app.__module__}") # O app si es directamente la instancia
except ModuleNotFoundError as e:
    print(f"\nERROR: No se pudo importar. {e}")
except ImportError as e:
    print(f"\nERROR de importación: {e}")
except Exception as e:
    print(f"\nOtro ERROR: {e}")