# Lista de verificación de performance de componentes

1. **Límites declarados.**
   - `performance.max_threads`, `max_requests_per_second` y `max_clients_per_minute` tienen valores basados en pruebas.
   - `performance.resource_budgets.cpu_percent` y `memory_percent` documentan el presupuesto operativo.
2. **Estrategia de overflow.**
   - `performance.overflow_strategy` usa uno de los valores aceptados (`queue`, `reject`, `throttle`).
   - `performance.overflow_messaging` define el código y mensaje visibles para negocio/UX.
3. **Backpressure y dependencia.**
   - Los valores máximos se alinean con la capacidad real de dependencias (referenciado en ADR/runbooks).
   - Se registran los impactos esperados cuando se activa la contención.
4. **Observabilidad de capacidad.**
   - Métricas en `observability.metrics_exposed` cubren límites de recursos, peticiones y clientes.
   - `observability.overload_signal` describe cómo se alerta al ecosistema cuando se alcanza el límite.
5. **Zero Trust en contención.**
   - `zero_trust.input_validation` explica cómo se siguen validando entradas bajo contención.
   - Cualquier ajuste dinámico de límites se vincula a `zero_trust.dependency_assumptions` para evitar abuso.
