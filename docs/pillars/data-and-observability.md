---
title: "Pilar: Datos y Observabilidad"
tags: ["developers", "observability", "data"]
---

# Pilar: Datos y Observabilidad

> Este pilar materializa la visión de "Information → Knowledge → Behavior → Real Value" descrita en [Vision and purpose](https://github.com/scanalesespinoza/the-wise-tech/blob/main/README.md#vision-and-purpose) y refuerza los principios de Capitalización del conocimiento y Resiliencia.

## Contexto estratégico
Los datos son el puente entre experiencia y acción. Sin telemetría confiable no hay aprendizaje ni automatización segura. La observabilidad debe exponer cómo cada decisión afecta a las personas y a los sistemas, habilitando ajustes guiados por evidencia.

## Requisitos esenciales
### Modelado y gobierno de datos
- **MUST** definir propietarios funcionales para cada dominio de datos y registrar sus contratos en el catálogo de conocimiento.
- **SHOULD** mapear los datos críticos a los principios relevantes (por ejemplo, resiliencia para métricas de disponibilidad, human connection para feedback cualitativo).
- **MAY** usar ontologías o *schemas* compartidos para que los equipos consuman datos sin reinterpretaciones ad hoc.

### Calidad y manejo de errores
- **MUST** establecer validaciones en origen y destino para detectar datos fuera de rango antes de que lleguen a consumidores sensibles.
- **SHOULD** etiquetar los eventos con la versión del esquema y la fuente de verdad para facilitar depuración.
- **MAY** habilitar colas de cuarentena o *dead-letter* con runbooks que especifiquen cómo limpiar o reprocesar la información.

### Señales de observabilidad
- **MUST** capturar métricas, logs y trazas con la granularidad mínima para reconstruir cada flujo crítico de negocio.
- **SHOULD** publicar paneles compartidos que conecten señales técnicas con indicadores de valor (ingresos, satisfacción, reducción de retrabajo).
- **MAY** enriquecer la telemetría con contexto humano (feedback, etiquetas de usabilidad) siempre que se cumplan las políticas de privacidad.

### Operación y mejora continua
- **MUST** versionar dashboards y alertas igual que el código para preservar la trazabilidad de decisiones.
- **SHOULD** alinear revisiones de telemetría con las cadencias de retrospectives para reforzar el aprendizaje colectivo.
- **MAY** automatizar experimentos de hipótesis (por ejemplo, cambios de UX) conectando métricas de experiencia con los principios.

## Transversal — Zero Trust
- **MUST** aplicar control de acceso basado en roles a cada flujo de datos y mantener evidencia de quién consultó qué información.
- **SHOULD** cifrar datos en tránsito y reposo incluidos los pipelines de observabilidad para evitar filtraciones durante incidentes.
- **MAY** integrar verificaciones de postura (estado del agente, integridad del host) antes de permitir acceso a paneles sensibles.

## See also
- [Vision and purpose](https://github.com/scanalesespinoza/the-wise-tech/blob/main/README.md#vision-and-purpose)
- [Knowledge capitalization](https://github.com/scanalesespinoza/the-wise-tech/blob/main/knowledge/docs/principles/wise-tech-principles.md#capitalizacin-del-conocimiento)
- [Telemetry minima](https://github.com/scanalesespinoza/the-wise-tech/blob/main/knowledge/docs/guides/telemetry-minima.md)
