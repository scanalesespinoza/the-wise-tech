---
title: "Pilar: Resiliencia"
tags: ["developers", "resilience", "principles"]
---

# Pilar: Resiliencia

> Este pilar responde a la visión de Wise Tech de "usar la tecnología correctamente" y se conecta con los principios de Simplicidad, Mejora continua y Responsabilidad. Resiliencia significa que cada componente se recupera con gracia, expone su estado y nunca deja al negocio sin información accionable.

## ¿Qué exige este pilar?
Cada componente **MUST** describir cómo captura errores, limpia su estado y cambia de modo operativo. La evidencia vive en el contrato de comportamiento y en la telemetría adjunta.

### Captura y manejo sistemático de errores
- **MUST** existir bloques funcionales que capturen errores esperados y casos de borde; cada bloque documenta el tipo de error, la salida esperada y el identificador de correlación.
- **MUST** disparar procesos de *clean up* y restauración de estado para evitar fugas de recursos, proteger datos y dejar el sistema en un estado conocido.
- **SHOULD** diferenciar entre errores transitorios y permanentes para activar runbooks distintos (reintentos versus escalamiento manual).
- **MAY** automatizar la clasificación con ML/heurísticas siempre que haya supervisión y registros auditables.

### Visibilidad para negocio y experiencia
- **MUST** registrarse qué actividades de negocio se ejecutaron, cuáles fallaron y cuáles fueron restauradas, usando eventos o logs estructurados.
- **MUST** exponer mensajes claros hacia UX/negocio que expliquen qué sucedió y qué acción se tomó (p. ej., "orden reintentada en modo manual").
- **SHOULD** publicar métricas y eventos que permitan reconstruir el customer journey sin revisar código.

### Modos de operación y degradación controlada
- **MUST** implementarse al menos los modos `in-service`, `degraded` y `out-of-service-controlled`, con criterios de entrada/salida documentados.
- **MUST** intentar recuperar funciones específicas cuando la inicialización falle y, si no es posible, operar en modo degradado pero seguro.
- **SHOULD** exponer tableros o flags que indiquen en qué modo se encuentra la componente y qué restricciones aplican.
- **MAY** añadir modos adicionales (por ejemplo, "manual assist") cuando exista una justificación de negocio.

### Zero Trust transversal
- **MUST** aplicar principios de confianza cero en interacciones y validaciones de entrada. Ningún flujo degradado puede omitir controles de identidad o autorización.
- **SHOULD** registrar qué actor (humano o sistema) habilitó/deshabilitó protecciones para facilitar auditorías.
- **MAY** incorporar señales de postura (riesgo de dispositivo, reputación de cliente) para endurecer o relajar límites dinámicamente.

## Evidencia mínima
1. Contrato de comportamiento actualizado con estrategias de manejo de errores, limpieza y estados declarados.
2. Ejemplos o pruebas (por ejemplo, `examples/service-resilience-basic`) que muestren degradaciones controladas.
3. Checklist de resiliencia en `audit/checklists/component-resilience.md` con evidencias adjuntas.

## Referencias
- [Guía del contrato de comportamiento](../guides/component-behavior-contract.md)
- [Patrón: error handling & cleanup](../patterns/pattern-error-handling-and-cleanup.md)
- [Patrón: modos degradados](../patterns/pattern-degraded-mode.md)
