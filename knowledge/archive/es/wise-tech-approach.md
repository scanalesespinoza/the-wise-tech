# Enfoque The Wise Tech: Un contraste con las prácticas tradicionales de software complejo

## Enfoque tradicional complejo: CICD + DevOps + DevSecOps como cadenas desconectadas

### CICD (Integración y Despliegue Continuos)
- **Enfoque principal:** Automatizar cómo se integra, prueba y despliega el código.
- **Retos clave:**
  - Opera con una visión reducida de la tubería sin alinearse a fondo con seguridad, operaciones o experiencia de usuario.
  - Fomenta liberaciones rápidas que pueden ignorar el contexto organizacional más amplio.
  - Ofrece bucles de retroalimentación limitados para entender la calidad o el impacto.

### DevOps
- **Enfoque principal:** Mejorar la colaboración entre desarrollo y operaciones para incrementar la velocidad de entrega.
- **Retos clave:**
  - Puede convertirse en otro silo donde la velocidad tiene prioridad sobre la calidad sostenible.
  - Seguridad y retroalimentación de usuarios suelen llegar tarde, lo que genera reacción ante incendios.
  - La complejidad del *toolchain* eleva la carga cognitiva de las personas ingenieras y aumenta la fricción.

### DevSecOps
- **Enfoque principal:** Incrustar prácticas de seguridad en los flujos de DevOps.
- **Retos clave:**
  - A menudo se atornilla a procesos existentes, generando responsabilidades fragmentadas.
  - La seguridad se vuelve una lista de cumplimiento en lugar de una mentalidad compartida.
  - Las desconexiones entre desarrollo, operaciones y seguridad crean puntos ciegos e ineficiencias.

## Enfoque The Wise Tech: Integrado y de punta a punta

### Proceso de desarrollo extremo a extremo
- **Enfoque principal:** Las personas desarrolladoras son dueñas del ciclo desde el diseño hasta el despliegue, impulsando calidad, seguridad e impacto en las personas usuarias.
- **Principios clave:**
  - **Mejora de procesos:** Aplicar aprendizajes previos para refinar continuamente cómo construimos y liberamos.
  - **Capitalización del conocimiento:** Colaborar con seguridad, operaciones y producto para construir inteligencia colectiva en lugar de reforzar silos.
  - **Comportamiento resiliente:** Diseñar para la degradación elegante, rutas de recuperación y mantenibilidad a largo plazo.

### Proceso de plataforma extremo a extremo
- **Enfoque principal:** Las personas ingenieras de plataforma crean sistemas resilientes, escalables y conscientes del usuario.
- **Principios clave:**
  - **Resiliencia del sistema:** Diseñar para el fallo, monitorear de forma continua e invertir en mejoras proactivas.
  - **Escalabilidad y eficiencia:** Crecer con la demanda sin sacrificar rendimiento ni sostenibilidad ambiental.
  - **Diseño centrado en el usuario:** Garantizar que los servicios y la arquitectura mejoren la confiabilidad, accesibilidad y simplicidad.

### Proceso de retroalimentación envuelto alrededor de las personas consumidoras de tecnología
- **Enfoque principal:** Cerrar el ciclo con quienes usan el software y permitir que sus experiencias guíen la evolución.
- **Principios clave:**
  - **Tecnología con propósito:** Validar que cada cambio mejore los resultados en lugar de complicar la vida.
  - **Conexión humana:** Medir cómo la tecnología respalda las relaciones y el bienestar comunitario.
  - **Simplicidad:** Reducir fricción, eliminar complejidad innecesaria y clarificar los recorridos de usuario.

## Por qué importa
El enfoque The Wise Tech reemplaza cadenas fragmentadas por un sistema simbiótico. Desarrolladores, personas ingenieras de plataforma y consumidoras de tecnología comparten la responsabilidad por la calidad, la resiliencia y el impacto humano. Cuando la retroalimentación fluye sin obstáculos, creamos productos relevantes, confiables y genuinamente útiles.

## Anexo: Perfiles de Consistencia y Estrategias de Réplica

Este anexo convierte las salvaguardas de sistemas distribuidos en un plan incremental para Wise Tech. Cada servicio declara su **perfil de consistencia** y su **estrategia de réplica** para que la automatización valide la combinación antes de integrar o desplegar código.

### Matriz de decisión

| Perfil / Estrategia | Garantías principales | Estrategias de réplica compatibles | Cuándo elegirlo | Riesgos a vigilar |
| --- | --- | --- | --- | --- |
| **Strict** | Aislamiento cercano a serializable, lecturas linealizables, escrituras deterministas | Primary-backup, Quórums | Flujos financieros, órdenes, cambios de inventario global | Contención de latencia, riesgo de *split-brain* si falla la membresía |
| **Causal** | Respeta dependencias causales, lecturas monotónicas y *read-your-writes* mediante vectores de sesión | Réplica activa, Quórums | Experiencias colaborativas, cronologías de actividad de usuarios | Complejidad al gestionar clocks cuando se pierden metadatos |
| **Eventual** | Convergencia por políticas de reconciliación con latencia mínima | Réplica activa, *fan-out* con cachés TTL | Catálogos, contenido, métricas agregadas | Divergencia visible si no hay idempotencia y reconciliación explícita |

### Guías de implementación

1. **Consistencia declarativa:** Los servicios registran su perfil en `systems/platform/policies/consistency.yml`. El *check* de CI en `systems/ci/consistency-check` contrasta el perfil con los patrones de acceso y con la estrategia de réplica declarada.
2. **Garantías centradas en el cliente:** El middleware de sesión adjunta encabezados con relojes vectoriales para que clientes móviles y web observen *read-your-writes* y lecturas monotónicas aunque roten de réplica.
3. **Consistency vs. coherence:** Las políticas distinguen reglas a nivel de dataset (consistency) de las cachés por ítem (coherence). Las TTL deben alinearse al perfil elegido para evitar lecturas obsoletas.
4. **Migraciones controladas:** Las ADR detallan cómo cambiar de un perfil a otro —por ejemplo, de eventual a causal— mediante despliegues *blue/green* por partición y *checkpoints* de observabilidad.

### Ganchos de resiliencia operativa

- **Catálogo de réplicas:** Las políticas de primary-backup, réplica activa y quórums viven en `experience/scenarios/payments/policies/resilience.yml`, cada una con validaciones automáticas de idempotencia y expectativas de estado compartido.
- **Pruebas de fallos parciales:** Los escenarios en `systems/ci/resilience-lint` y `systems/ci/causality-test` simulan nodos lentos, pérdida de miembros y tormentas de reintentos para asegurar degradaciones controladas.
- **Gestión de membresía:** `guides/platform-playbook.md` mantiene alineados heartbeats, timeouts y el orden de eventos de grupo con la estrategia de réplica declarada.

### Quality Gates y retroalimentación humana

- **Checks automatizados:** Cada Pull Request ejecuta validaciones de consistencia, resiliencia y causalidad para detectar configuraciones incompatibles.
- **Idempotencia por contrato:** Los servicios que optan por réplica activa deben exponer claves de idempotencia o efectos secundarios verificables para sobrevivir a reintentos.
- **Continuidad de sesión:** Soporte y UX consultan vectores de sesión antes de responder cuando una persona usuaria cambia de réplica, garantizando continuidad.
- **Capitalización de conocimiento:** Las plantillas de issues y PR registran decisiones de consistencia y réplica junto con aprendizajes de usuarios, reforzando la memoria organizacional.
