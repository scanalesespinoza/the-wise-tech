## Propósito
Enmarca cómo Runbook de Incidentes de Pagos ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Runbook de Incidentes de Pagos.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Runbook de Incidentes de Pagos o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Runbook de Incidentes de Pagos dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en los escenarios y rutas de experiencia práctica.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Runbook de Incidentes de Pagos.
> **Estado:** Activo.


## Tabla de navegación

- [Alcance](#alcance)
- [Lista de verificación inicial](#lista-de-verificacin-inicial)
- [Triage por tipo de error](#triage-por-tipo-de-error)
- [Recuperación y seguimiento](#recuperacin-y-seguimiento)

# Runbook de Incidentes de Pagos

Este documento muestra cómo los equipos Wise Tech responden a incidentes
de cara a clientes en el escenario de pagos.

## Alcance

- Errores de checkout visibles en `checkout-ui`.
- Rechazos propagados por emisores externos.
- Timeouts o fallos desconocidos al invocar al proveedor adquirente.

## Lista de verificación inicial

1. **Validar telemetría.** Abre el dashboard `payments_authorizations`
   (ver guía de observabilidad) y confirma el pico o degradación.
2. **Reconocer alertas.** La rotación on-call recibe el evento PagerDuty
   `payments-critical`. Reconócelo en menos de 5 minutos.
3. **Comunicar.** Actualiza el canal compartido `#status-payments` y
   etiqueta a soporte al cliente con el estado actual.

## Triage por tipo de error

| Señal | Acción |
| --- | --- |
| `PAYMENT_DECLINED` | Confirma el código de respuesta del emisor, comparte
| la pista de remediación bilingüe con soporte y recopila ejemplos para la
| revisión diaria de tendencias. |
| `PAYMENT_TIMEOUT` | Activa el job automático de reintentos. Si hay más de
| 3 timeouts consecutivos por proveedor, contacta al enlace del proveedor y
| evalúa modular el tráfico. |
| `PAYMENT_UNKNOWN` | Escala a Nivel 2 después de recopilar payloads de
| petición/respuesta e IDs de correlación. |

## Recuperación y seguimiento

- Crea una línea de tiempo del incidente usando la plantilla de
  retrospectiva Wise Tech.
- Regresa los aprendizajes a los archivos `knowledge/docs/es/runbook.md` y
  `knowledge/docs/en/runbook.md` para mantener el conocimiento bilingüe.
- Actualiza las pruebas de contrato si participaron nuevos campos de
  respuesta, preservando la paridad de observabilidad.
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

