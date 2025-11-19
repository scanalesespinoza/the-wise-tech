---
title: "Three Context Framework"
tags: ["principles", "resilience", "cloud-native"]
---
## Propósito
Enmarca cómo Three Context Framework ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Three Context Framework.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Three Context Framework o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Three Context Framework dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Three Context Framework.
> **Estado:** Activo.

# Three Context Framework

El Three Context Framework resume los comportamientos mínimos que toda carga cloud-native debe dominar para ser resiliente sin depender únicamente de plataformas externas. A medida que la adopción de Kubernetes y la IA acelera el ritmo de cambio, este enfoque ayuda a reducir la brecha de conocimiento y a devolver la responsabilidad de la calidad al componente de negocio.

Cada contexto representa un conjunto de capacidades observables que puedes mapear a tus aplicaciones. Usa las preguntas de comprobación y los ejemplos para identificar huecos y alinear acciones de mejora en tus playbooks y rutas 30/60/90.

## Contexto 1 — Self-Healing
**Objetivo:** Recuperarse de fallas internas y externas de forma autónoma.

| Capacidad | Qué observar | Prácticas recomendadas |
| --- | --- | --- |
| Detección temprana | ¿La aplicación expone health checks significativos? | Instrumenta liveness/readiness checks y alarmas accionables. |
| Recuperación automática | ¿Existen reintentos inteligentes antes de escalar incidentes? | Aplica reintentos con backoff exponencial y jitter controlado. |
| Contención | ¿Una falla impacta a otros servicios? | Emplea circuit breakers y timeouts consistentes. |

**Ejemplo:** Un deployment en Kubernetes detecta un crash a través de `livenessProbe` y reinicia el contenedor sin afectar la experiencia del usuario.

## Contexto 2 — Remote Connection Self-Management
**Objetivo:** Adaptarse a entornos dinámicos administrando conexiones remotas sin supervisión constante.

| Capacidad | Qué observar | Prácticas recomendadas |
| --- | --- | --- |
| Supervisión continua | ¿Conoces el estado de tus dependencias externas en tiempo real? | Centraliza métricas de conectividad y crea alertas por latencia o errores. |
| Gestión dinámica | ¿La aplicación reacciona a cambios de endpoints o DNS? | Integra service discovery, TTLs cortos y reconexiones graduales. |
| Modos degradados | ¿Hay alternativas cuando la dependencia falla? | Implementa cachés locales, colas persistentes o rutas secundarias. |

**Ejemplo:** Un cliente API cambia automáticamente a un endpoint de respaldo durante una caída y mantiene una copia en caché de los datos críticos para no bloquear al usuario.

## Contexto 3 — Resource and Scaling Management
**Objetivo:** Evitar la saturación gestionando contención, límites y degradaciones controladas.

| Capacidad | Qué observar | Prácticas recomendadas |
| --- | --- | --- |
| Control de entrada | ¿Se moderan los picos de tráfico? | Implementa rate limiting y prioridades por tipo de solicitud. |
| Backpressure | ¿Los productores conocen la presión que generan? | Utiliza colas, `async` y comunicación de capacidad disponible. |
| Escalamiento adaptativo | ¿La plataforma ajusta recursos con base en señales reales? | Activa autoescalado vertical/horizontal y budgets por consumo. |

**Ejemplo:** Un API Gateway regula solicitudes cuando la memoria del backend alcanza el umbral crítico y activa nodos adicionales antes de degradar el servicio.

## Cómo aplicarlo en The Wise Tech
1. **Evalúa tu estado actual.** Usa los tres contextos como checklist en laboratorios o escenarios (`knowledge/docs/labs/` y `knowledge/docs/scenarios/`).
2. **Conecta con tus playbooks.** Documenta brechas en los playbooks de desarrolladores y plataforma para cerrar loops.
3. **Sincroniza con las rutas 30/60/90.** Incluye prácticas de self-healing, gestión remota y escalamiento en cada iteración de aprendizaje.
4. **Expón resultados.** Registra hallazgos en ADRs, postmortems ligeros o la bitácora de auditorías para mantener la trazabilidad.

## See also
- [Wise Tech principles](wise-tech-principles.md)
- [Wise Tech approach](wise-tech-approach.md)
- [Resilience policies guide](../guides/resilience-policies.md)
- [Platform playbook](../playbooks/platform-playbook.md)
- [Lab 01 — Resilience basics](../labs/lab-01-resilience-basics.md)
---
Última modificación: 2025-11-19

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
