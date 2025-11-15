# Receta: Pruebas de Contrato para Integraciones Estables

**Propósito.** Evitar regresiones entre servicios codificando las expectativas entre productores y consumidores.

**Aplica cuando.** Construyes o modificas APIs, esquemas de mensajes o flujos de eventos consumidos por otros equipos o sistemas.

**Haz esto.**
1. Documenta el contrato (campos, tipos, opcionalidad, significado semántico) y enlázalo desde el PR.
2. Implementa pruebas de contrato impulsadas por consumidores que corran en CI y validen cambios del proveedor.
3. Versiona los contratos explícitamente y describe rutas de migración para cambios disruptivos.
4. Automatiza la publicación del esquema (por ejemplo, subir al registro o compartir vía paquete) como parte del pipeline de release.
5. Monitorea el uso del contrato para detectar endpoints sin uso y consumidores obsoletos.

**Evita esto.**
- Confiar solo en ambientes de integración para detectar cambios disruptivos.
- Desplegar sin notificar a las personas consumidoras sobre actualizaciones necesarias.
- Permitir la coexistencia de múltiples variantes de contrato sin documentar.

**Ejemplo local.** Revisa `experience/scenarios/payments/contracts/payments/v2` para ver los archivos Pact y el README que explica los comportamientos esperados.

**Principios relacionados.** [Respeta el contrato del dominio](../principles-essential.md), [Inclínate por la simplicidad mantenible](../principles-essential.md).
