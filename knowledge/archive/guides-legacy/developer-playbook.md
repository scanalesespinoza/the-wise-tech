# Developer Playbook: Consistencia, Idempotencia y Clocks

## Elegir un perfil de consistencia

1. **Identifica el patrón de acceso**: usa `systems/platform/policies/consistency.yml` para mapear tu servicio a `read_dominant`, `write_conflict` o `session_mutation`.
2. **Selecciona el perfil**:
   - Usa **Strict** si requieres serialización determinista o contención de conflictos de escritura.
   - Usa **Causal** para experiencias multi-dispositivo que necesitan read-your-writes y monotonic reads.
   - Usa **Eventual** cuando la latencia prima sobre la ordenación estricta y puedes reconciliar divergencias.
3. **Documenta la decisión** en la plantilla de PR, incluyendo razones, métricas y trade-offs.

## Diseñar idempotencia

1. **Define idempotency keys** para operaciones que puedan reintentarse (HTTP header, claim JWT o clave en metadata del mensaje).
2. **Persistencia**: guarda el resultado asociado a la clave para detectar replays. Para strict/causal, sincroniza el registro con la transacción principal.
3. **Operaciones no deterministas**: evita leer `now()` o generar UUIDs dentro de la operación; en su lugar, pásalos como parámetros deterministas.
4. **Pruebas**: extiende tus escenarios en `systems/ci/causality-test` con casos de replay y concurrencia para validar la idempotencia declarada.

## Manejo de relojes lógicos/vectoriales

1. **Generación**: incrementa el componente local antes de emitir un evento.
2. **Propagación**: incluye el vector en headers (ej. `x-session-vector`). Los clientes móviles deben reenviar el valor más reciente.
3. **Recepción**: fusiona el vector recibido con tu estado local antes de ejecutar lógica de negocio.
4. **Detección de conflictos**: si los relojes son concurrentes, aplica políticas de reconciliación (p.ej., resolver por prioridad de réplica o timestamp lógico) y registra el caso.
5. **Debug**: anota el vector en tus trazas y logs. Usa las herramientas del equipo de plataforma para visualizar las dependencias.

## Checklist antes de abrir un PR

- [ ] Perfil y patrón actualizados en `consistency.yml`.
- [ ] Estrategia de réplica declarada y compatible.
- [ ] Handlers críticos con claves de idempotencia documentadas.
- [ ] Escenarios de `systems/ci/causality-test` actualizados si cambia el flujo.
- [ ] Sección "lecciones del usuario" completada en la plantilla de PR.
