## Propósito
Enmarca cómo Receta: Manejo de Errores Intencional ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Receta: Manejo de Errores Intencional.

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Receta: Manejo de Errores Intencional o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Receta: Manejo de Errores Intencional dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Receta: Manejo de Errores Intencional.
> **Estado:** Activo.

# Receta: Manejo de Errores Intencional

**Propósito.** Brindar rutas de recuperación consistentes y amigables para las personas usuarias mientras mantenemos telemetría accionable.

**Aplica cuando.** Modificas código que propaga excepciones entre servicios o expone mensajes a usuarias y usuarios finales.

**Haz esto.**
1. Mapea los modos de fallo esperados y decide cuáles requieren manejo explícito vs. propagación.
2. Convierte excepciones genéricas en errores específicos del dominio que incluyan pistas de remediación.
3. Registra el error una sola vez con contexto estructurado (ID de correlación, entradas, dependencias downstream) y emite métricas para alertas.
4. Devuelve respuestas seguras al cliente (status HTTP + código legible por máquina + mensaje humano).
5. Enlaza el PR a runbooks o playbooks operativos si se requiere intervención manual.

**Evita esto.**
- Tragar excepciones en silencio o registrarlas sin contexto.
- Devolver stack traces o detalles de implementación a las personas consumidoras.
- Crear taxonomías de errores divergentes entre servicios.

**Ejemplo local.** Consulta `experience/scenarios/payments/service/errors.py` para ver las excepciones de dominio canónicas y cómo se mapean a respuestas de API.

**Principios relacionados.** [Respeta el contrato del dominio](../principles-essential.md), [Diseña para el fallo elegante](../principles-essential.md).
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

