# Payments Scenario / Escenario de Pagos

This directory groups every artifact that turns the theoretical ideas of
Wise Tech into a tangible payments product. By keeping code, contracts,
runbooks, and tests together we communicate that this is a complete
business scenario that can be operated, evolved, and audited.

Este directorio reúne cada artefacto que convierte las ideas teóricas de
Wise Tech en un producto de pagos tangible. Al mantener código,
contratos, runbooks y pruebas juntos comunicamos que este es un
escenario de negocio completo que puede operarse, evolucionarse y
auditarse.

## Structure / Estructura

- `service/`: canonical domain components used by the payments service.
  / componentes de dominio canónicos usados por el servicio de pagos.
- `contracts/`: consumer-driven contracts (Pact + schema) published by the
  service. / contratos orientados al consumidor publicados por el
  servicio.
- `knowledge/docs/`: operational runbooks, observability guides and other
  governance assets. / runbooks operativos, guías de observabilidad y
  otros activos de gobernanza.
- `policies/`: resilience policies parametrized for the scenario. / políticas de resiliencia parametrizadas para el escenario.
- `slo/`: service-level objectives and error-budget rules. / objetivos de servicio y reglas de error budget.
- `systems/tests/`: executable evidence that the scenario behaves as expected. /
  evidencia ejecutable de que el escenario se comporta como se espera.

## How it maps to Wise Tech principles / Cómo se alinea con los
principios de Wise Tech

- **Technology with purpose.** Every artifact references a specific need
  from the payments journey (resiliencia ante rechazos, contratos claros
  con checkout, telemetría curada). / Cada artefacto referencia una
  necesidad específica del viaje de pagos.
- **Simplicity.** Contracts, runbooks and code avoid accidental
  complejidad e incluyen ejemplos bilingües listos para adaptar. /
  Contratos, runbooks y código evitan complejidad accidental.
- **Resilience & Observability.** Tests exercise las rutas de error y los
  runbooks detallan cómo responder y qué métricas observar. /
  Las pruebas ejercitan las rutas de error y los runbooks detallan cómo
  responder y qué métricas observar.

## Getting started / Para comenzar

1. Run `python -m unittest discover experience/scenarios/payments/tests` to execute
   the scenario tests. / Ejecuta `python -m unittest discover
   experience/scenarios/payments/tests` para correr las pruebas del escenario.
2. Consume the bilingual runbooks under `knowledge/docs/` to integrate the service
   into your operations. / Usa los runbooks bilingües en `knowledge/docs/` para
   integrar el servicio a tus operaciones.
3. When modifying documentation ensure both languages stay in sync by
   running `python operations/scripts/check_bilingual_parity.py`. / Al modificar
   documentación asegúrate de mantener ambos idiomas en sincronía
   ejecutando `python operations/scripts/check_bilingual_parity.py`.
