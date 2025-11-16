> **Propósito:** Dar contexto accionable sobre ADR-0003: Instrumentación de Causalidad con Relojes Lógicos dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de ADR-0003: Instrumentación de Causalidad con Relojes Lógicos.
> **Estado:** Activo.

# ADR-0003: Instrumentación de Causalidad con Relojes Lógicos

- Fecha: 2024-06-14
- Estado: Propuesto

## Contexto

La plataforma enfrenta incidentes donde eventos llegan fuera de orden, generando reprocesos no idempotentes y dificultando el debugging. Necesitamos una capa común para representar dependencias causales y habilitar reconciliación entre perfiles eventual y causal.

## Decisión

1. Todas las publicaciones de eventos incluyen encabezados con reloj lógico; por defecto vector clocks con identificadores de réplica.
2. Los servicios que usan réplica activa pueden continuar con orden total, pero deben documentar el costo y límites de escalado en sus ADRs específicos.
3. Se agregan utilidades en la capa de eventos para comparar relojes, detectar conflictos y marcar mensajes potencialmente duplicados.
4. Las trazas distribuidas almacenan el vector de sesión para correlacionar diagnósticos entre equipos de soporte y plataforma.
5. `systems/ci/causality-test` ejecuta simulaciones de entrega fuera de orden para verificar idempotencia y reconciliación.

## Consecuencias

- **Positivas**: mejor trazabilidad, menor reproceso, capacidades de depuración causales mejoradas.
- **Negativas**: overhead en tamaño de mensajes y necesidad de sincronizar relojes vectoriales; clientes deben propagar metadata adicional.

## Migración

1. Generar un ID de réplica estable por servicio y despliegue.
2. Incluir reloj lógico en eventos nuevos, manteniendo compatibilidad con consumidores legados mediante encabezados opcionales.
3. Ampliar gradualmente la obligatoriedad a servicios eventual y causal, luego a strict.
4. Documentar las lecciones aprendidas en los playbooks para reforzar la transferencia de conocimiento.

---

---
¿Te fue útil este documento?
[ ] Sí  [ ] Algo  [ ] No
Deja feedback [aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)
---
