---
title: "Pilar transversal: Zero Trust"
tags: ["security", "zero-trust", "principles"]
---

# Pilar transversal: Zero Trust

Zero Trust no es un capítulo aislado: define cómo aplicamos los PCC en cualquier modo operativo. Sus reglas:

1. **Validación continua.** Cada interacción **MUST** validar identidad, contexto y permisos sin asumir confianza previa.
2. **Aislamiento de modos degradados.** Los modos `degraded` o `out-of-service-controlled` **MUST** mantener los mismos controles que el modo normal (auditoría, registro, autenticación).
3. **Dependencias verificadas.** Toda dependencia crítica **SHOULD** describir en el contrato cómo verifica inputs/outputs antes de usarlos. Los linters consumen esta información para detectar huecos.
4. **Visibilidad y trazabilidad.** Los eventos de acceso, bypass o escalamiento temporal **MUST** quedar registrados con quién, cuándo y por qué se realizaron.
5. **Adaptación basada en riesgo.** Los componentes **MAY** ajustar límites o activar degradaciones según señales de postura o reputación siempre que documenten los criterios.

## Cómo se refleja en los PCC
- **Resiliencia:** los flujos de recuperación y las limpiezas verifican identidad antes de ejecutarse.
- **Performance:** las estrategias de contención nunca sacrifican controles de autenticación ni mezclan sesiones.
- **Datos y Observabilidad:** los pipelines de telemetría se protegen con control de acceso, cifrado y verificación de procedencia.

Use este archivo como referencia cuando diseñe nuevos patrones o herramientas.
