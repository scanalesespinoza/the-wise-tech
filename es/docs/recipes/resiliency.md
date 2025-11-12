# Receta: Patrones de Servicio Resiliente

**Propósito.** Mantener la disponibilidad y una degradación predecible bajo estrés o fallas de dependencias.

**Aplica cuando.** Te integras con servicios de terceros, agregas llamadas de red o modificas configuraciones de resiliencia en infraestructura.

**Haz esto.**
1. Identifica dependencias críticas y clasifícalas (tolerar vs. fallo rápido vs. aislamiento tipo bulkhead).
2. Configura timeouts, reintentos con backoff y circuit breakers por dependencia.
3. Provee fallbacks que entreguen valor mínimo viable (datos en caché, trabajo en cola, respuestas parciales).
4. Realiza pruebas de carga con escenarios de fallo y captura evidencia en la descripción del PR.
5. Documenta procedimientos de recuperación y asegúrate de que las señales de observabilidad cubran las nuevas protecciones.

**Evita esto.**
- Reintentos infinitos o ráfagas de reintentos que amplifican las caídas.
- Tratar todas las dependencias con la misma política de resiliencia.
- Liberar cambios sin validar cómo reaccionan las personas consumidoras ante el comportamiento degradado.

**Ejemplo local.** Examina `infra/resilience/policies.yml` para conocer las configuraciones base de timeouts y reintentos por nivel de dependencia.

**Principios relacionados.** [Diseña para el fallo elegante](../principles-essential.md), [Protege los datos y la confianza humana](../principles-essential.md).
