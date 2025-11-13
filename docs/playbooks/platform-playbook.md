# Platform Playbook

## Objetivos del equipo
- Garantizar disponibilidad y tiempos de recuperación acordados.
- Proveer pipelines seguros y reproducibles para cada servicio.
- Facilitar visibilidad operativa unificada para todos los roles.

## Rituales clave
- Revisión semanal de telemetría y incidentes con Developers.
- Ejercicios mensuales de respuesta a incidentes centrados en usuarios.
- Actualización trimestral de políticas de acceso y seguridad.

## Capacidades fundamentales
- Observabilidad end-to-end con métricas, logs y traces accesibles.
- Automación de infraestructura como código con validaciones previas.
- Catálogo de servicios con niveles de servicio y runbooks compartidos.

## Primeros 60 minutos
- Reproduce `make ci` y guarda los tiempos de cada etapa para detectar cuellos de botella.
- Sincroniza runbooks de `scenarios/payments/docs` con los hallazgos del último ejercicio de caos.
- Publica un resumen en el canal de plataforma con acciones concretas para Developers y Consumers.

## Indicadores clave de experimento
- **MTTR simulado**: objetivo ≤ 15 minutos desde el fallo detectado hasta `make ci` exitoso.
- **Cobertura de runbooks**: 100% de procedimientos críticos documentados en EN/ES.
- **Satisfacción de equipos**: incremento mensual del feedback positivo en issues etiquetados como `platform`.

## See also
- [Developer playbook](developer-playbook.md)
- [Wise Tech approach](../principles/wise-tech-approach.md)
- [Platform engineers overview](../personas/platform-engineers-overview.md)
- [Roadmap](../roadmap/roadmap.md)
- [FAQ](../index.md#faq)
