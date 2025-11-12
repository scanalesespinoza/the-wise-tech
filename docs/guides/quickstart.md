# Quickstart

## 5 pasos para validar tu entorno

1. **Clona el repositorio**
   ```bash
   git clone https://github.com/the-wise-tech/the-wise-tech.git
   cd the-wise-tech
   ```
2. **Instala dependencias de desarrollo**
   ```bash
   make install
   ```
   Esto actualiza `pip` e instala los paquetes declarados en `requirements-dev.txt` para construir documentación y validar escenarios.
3. **Ejecuta pruebas del escenario de pagos**
   ```bash
   make test
   ```
   El comando ejecuta `python -m unittest discover scenarios/payments/tests` y garantiza que el caso de negocio ejemplo sigue funcionando de punta a punta.
4. **Verifica paridad bilingüe y enlaces**
   ```bash
   make parity
   make links
   ```
   Así sabrás si las rutas `en/` y `es/` están alineadas y si la documentación carece de enlaces rotos antes de abrir una PR.
5. **Construye la documentación**
   ```bash
   make docs
   ```
   Para iterar localmente sobre la experiencia completa usa `make docs-serve` y navega en `http://127.0.0.1:8000`.

## See also
- [Contribution guide](contribution-guide.md)
- [Wise Tech principles](../principles/wise-tech-principles.md)
- [Developers overview](../personas/developers-overview.md)
- [Platform playbook](../playbooks/platform-playbook.md)
- [FAQ](../../README.md#faq)
