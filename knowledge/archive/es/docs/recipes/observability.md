## Propósito
Enmarca cómo Receta: Servicios Observables por Defecto ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Receta: Servicios Observables por Defecto.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Receta: Servicios Observables por Defecto o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Receta: Servicios Observables por Defecto dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Receta: Servicios Observables por Defecto.
> **Estado:** Activo.

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
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

