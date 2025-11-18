# Modelo interno de Pilares de Comportamiento de Componentes (PCC)

## ¿Por qué existen los PCC?
Los PCC son el puente entre la filosofía de The Wise Tech y la ejecución diaria de ingeniería. Formalizan la expectativa de que cada componente entregue valor sin comprometer responsabilidad ni confianza. Al tratar resiliencia, rendimiento, datos/observabilidad y Zero Trust como un único marco, evitamos que los principios queden como slogans y habilitamos decisiones trazables: cada requisito describe el comportamiento observable que se espera.

## Relación con la visión original
- **Uso correcto de la tecnología.** Los PCC fuerzan que cada decisión (limitar carga, limpiar estados, emitir métricas) tenga una justificación auditable. Se evita el “crecimiento accidental” porque los contratos obligan a documentar objetivos y límites.
- **Responsabilidad.** Los modos degradados, las señales de sobredemanda y la captura sistemática de eventos garantizan que podamos explicar qué ocurrió y qué haremos después. La responsabilidad deja de ser reactiva.
- **Calidad.** El contrato PCC ancla la calidad a evidencia: un componente solo “cumple” cuando demuestra que maneja errores, respeta presupuestos de performance y comparte la información mínima viable para aprender.

## Subpilares y forma de uso
- **Resiliencia.** Define cómo una componente captura errores, limpia su estado y pasa entre los modos “en servicio”, “degradado” y “fuera de servicio controlado”.
- **Rendimiento.** Explica los presupuestos máximos (hilos, peticiones, clientes, recursos) y la estrategia de contención cuando se exceden.
- **Datos y Observabilidad.** Asegura que cada componente sepa cuánta carga maneja, pueda diferenciar demanda normal vs. sobredemanda y exponga señales para aprendizaje.
- **Zero Trust transversal.** Se aplica en cada pilar: no se asume que las entradas vienen validadas, que las dependencias son confiables ni que los modos degradados pueden omitir controles.

## Mandatoriedad y lenguaje RFC
- Cada componente **MUST** declarar explícitamente cómo cumple cada subpilar. No existen servicios “opt-out”: si algo no aplica, se documenta el motivo y la compensación.
- Los requisitos se redactan usando RFC 2119 (`MUST`, `SHOULD`, `MAY`) para evitar ambigüedad. Esto aplica al contrato, a las guías y a los linters.
- El PCC **SHOULD** vivir junto al código fuente (por ejemplo, en `docs/` o `runbooks/`).
- Los equipos **MAY** añadir campos adicionales siempre que no eliminen los obligatorios, facilitando extensiones sin fragmentar la validación automática.

## Próximos pasos
1. **Contratos consistentes.** Adoptar el esquema `docs/specs/component-behavior-contract.schema.md` en cada componente, incluyendo los estados operativos y la estrategia de sobredemanda.
2. **Guías y ejemplos.** Ligar cada guía y ejemplo a los PCC para que cualquier lector entienda qué requisito satisface.
3. **Validación automática.** Evolucionar `tools/wise-tech-linter` para detectar incumplimientos temprano y habilitar reportes “OK/nOK” en `audit/`.
4. **Revisión ejecutiva.** Compartir esta síntesis con liderazgo para asegurar que el lenguaje, los campos obligatorios y las expectativas de Zero Trust están alineados antes de publicar cambios visibles.
