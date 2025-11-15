# Receta: Servicios Observables por Defecto

**Propósito.** Asegurar que cada cambio deje rastros que aceleren la detección, el triage y el aprendizaje.

**Aplica cuando.** Agregas funcionalidad, tocas infraestructura o ajustas configuraciones de logging/métricas/trazas.

**Haz esto.**
1. Define señales de éxito, advertencia y fallo antes de implementar el cambio.
2. Emite logs estructurados con llaves consistentes (nombre del servicio, operación, ID de correlación, contexto de usuario).
3. Publica métricas con nombres claros (`equipo.dominio.metrica`) y adjunta umbrales de SLO/SLA.
4. Instrumenta trazas distribuidas y propaga encabezados de correlación entre servicios.
5. Crea o actualiza tableros y alertas que expongan las nuevas señales.

**Evita esto.**
- Escribir prints/debug ad-hoc que no llegan al sistema centralizado de logs.
- Emitir etiquetas de alta cardinalidad sin justificación.
- Agregar telemetría sin actualizar runbooks o rutas de alerta.

**Ejemplo local.** Revisa `systems/infra/observability/telemetry.json` para los nombres de campos canónicos y el formato de logging.

**Principios relacionados.** [Abraza los comportamientos observables](../principles-essential.md), [Automatiza el aprendizaje repetible](../principles-essential.md).
