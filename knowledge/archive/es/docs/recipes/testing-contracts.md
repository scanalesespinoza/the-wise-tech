## Propósito
Enmarca cómo Receta: Pruebas de Contrato para Integraciones Estables ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Receta: Pruebas de Contrato para Integraciones Estables.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Receta: Pruebas de Contrato para Integraciones Estables o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Receta: Pruebas de Contrato para Integraciones Estables dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Receta: Pruebas de Contrato para Integraciones Estables.
> **Estado:** Activo.

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
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

