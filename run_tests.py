# run_tests.py
import unittest
import os
import sys

# Asegura que la carpeta raíz del proyecto (donde está app.py y tests/)
# se agregue al PATH de Python.
# Esto permite que los módulos dentro de 'tests' puedan importar 'app'.
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

if __name__ == '__main__':
    loader = unittest.TestLoader()

    # Usamos el path completo de la carpeta tests para asegurar la importación
    # os.path.join(project_root, 'tests') crea la ruta absoluta a la carpeta tests
    suite = loader.discover(start_dir=os.path.join(project_root, 'test'), pattern='test*.py')

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
