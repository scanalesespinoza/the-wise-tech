# Pilar: Performance

> El rendimiento se alinea con la visión de priorizar la lógica de negocio descrita en [Vision and purpose](../../README.md#vision-and-purpose) y aplica los principios de Simplicity y Mejora continua para sostener experiencias confiables.

## Contexto estratégico
Optimizar performance significa asegurar que cada interacción sea rápida, predecible y medible. No busca micro-optimizar cada componente sino garantizar que los flujos que entregan valor tengan capacidad y latencia suficientes para cumplir la promesa al usuario y al negocio.

## Requisitos esenciales
### Límites y presupuestos
- **MUST** definir objetivos de latencia, throughput y costo por operación ligados a SLOs revisados con las áreas de producto.
- **SHOULD** documentar los límites junto a su racional en ADRs o en la taxonomía de principios para que nuevos equipos hereden el contexto.
- **MAY** usar escalado automático siempre que exista una política de guardrails que evite gastos inesperados.

### Manejo de carga y degradación
- **MUST** implementar *rate limits* y *backpressure* en cada punto de entrada público.
- **SHOULD** reservar capacidad para operaciones críticas (pagos, registro) antes que para flujos secundarios.
- **MAY** activar rutas alternativas más simples (por ejemplo, solo lectura o colas batch) cuando la demanda supere el presupuesto.

### Observabilidad de performance
- **MUST** recolectar métricas P50/P90/P99, tasa de errores y consumo de recursos por dominio funcional.
- **SHOULD** correlacionar métricas de experiencia (conversiones, órdenes completadas) con la telemetría técnica usando paneles compartidos.
- **MAY** generar experimentos controlados (feature flags + mediciones) para validar mejoras sin afectar la línea base.

### Experimentos y mejora continua
- **MUST** medir impacto antes y después de cada optimización para comprobar que la Simplicity no se sacrificó.
- **SHOULD** mantener *playbooks* que expliquen cómo interpretar resultados para acelerar el aprendizaje colectivo.
- **MAY** automatizar pruebas de carga en la cadena CI/CD cuando el riesgo operacional lo justifique.

## Transversal — Zero Trust
- **MUST** garantizar que las optimizaciones no deshabilitan controles de autenticación o autorización bajo ninguna circunstancia.
- **SHOULD** monitorear que los mecanismos de caching respetan el aislamiento de datos por identidad y región.
- **MAY** usar señales de riesgo para adaptar límites por cliente o dispositivo sin exponer la plataforma a abuso.
