# Implementation Roadmap

## Cómo usar este directorio
1. **Siempre lee este roadmap antes de escribir código.** Resume el estado actual del repositorio y la siguiente etapa priorizada para convertirlo en un producto consumible.
2. **Revisa los archivos `implementation/releases/release-XX.md` en orden cronológico.** Cada release documenta qué parte del plan ya está completa.
3. **Cuando termines una etapa, crea un nuevo archivo `release-XX.md`.** Describe qué cambió, cómo se validó y qué queda pendiente antes de pasar a la siguiente fase.
4. **Si el plan necesita ajustes, edita este roadmap primero y explica el cambio en el release que lo introduce.** Esto mantiene la trazabilidad para futuras iteraciones de Codex.

## Estado actual (Release 01)
- El repositorio ya funciona como **hub documental** (ver `README.md` y `knowledge/docs/index.md`), pero aún no existe una experiencia empaquetada para consumo externo más allá de la navegación manual.
- Las automatizaciones (`operations/Makefile`, workflows en `.github/`) cubren calidad documental y paridad bilingüe, lo cual demuestra madurez en procesos, pero no en entrega de producto.
- No hay una **historia de releases** ni artefactos ejecutables que materialicen las guías en un servicio o demostrador.

## Etapas para llegar a un producto consumible
### Etapa 1 — "Discovery operacional" (Release 01 ✅)
Objetivo: Documentar el estado real del repositorio, identificar huecos entre la documentación y una experiencia de producto, y definir criterios de éxito.
Resultados clave:
- Inventario de activos existentes (docs, escenarios, pipelines).
- Definición del backlog mínimo para empaquetar el contenido.
- Instrucciones para futuras iteraciones (este roadmap + `release-01`).

### Etapa 2 — "MVP navegable"
Objetivo: Convertir el hub en una experiencia servible que guíe al usuario paso a paso.
Enfoque:
- Empaquetar un flujo inicial (p. ej., Learning Path 30/60/90) como caso demostrativo dentro de `knowledge/docs/` y exponerlo desde la portada.
- Automatizar la verificación de enlaces críticos (Quick start, Paths, Labs) en `operations/Makefile` para garantizar disponibilidad.
- Preparar un guion de onboarding reproducible (docs + script) en `operations/`.
Criterios de salida:
- README y portada de docs redirigen al flujo MVP.
- Script o comando único que instale dependencias, levante docs y valide enlaces prioritarios.
- Documentación de la etapa en `release-02`.

### Etapa 3 — "Experiencia operacional"
Objetivo: Pasar del MVP documental a un producto que combine documentación con automatización.
Líneas de trabajo sugeridas:
- Integrar un escenario práctico (p. ej., `experience/scenarios/payments/`) con scripts reproducibles.
- Añadir telemetría mínima (referencia `knowledge/docs/guides/telemetry-minima.md`) y tableros compartidos.
- Publicar plantillas de KPIs en `knowledge/docs/playbooks/` vinculadas al flujo ejecutable.
Criterios de salida:
- Release documentado (`release-03`).
- Demostración operativa (comando o pipeline) validada en CI.

### Etapa 4+ — "Producto abierto"
Objetivo: Iterar sobre feedback real para ofrecer una experiencia lista para adopción de equipos.
- Versionar el contenido con etiquetas semánticas.
- Medir satisfacción/uso y ajustar rutas de aprendizaje.
- Establecer ciclos de mentoring documentados en nuevos releases.

## Próximos pasos inmediatos
1. Preparar el diseño del MVP navegable (Etapa 2) priorizando el flujo 30/60/90 de una persona.
2. Definir verificaciones automáticas mínimas que prueben ese flujo.
3. Abrir `release-02.md` cuando se complete el MVP y enlazar cualquier ajuste a este roadmap.
