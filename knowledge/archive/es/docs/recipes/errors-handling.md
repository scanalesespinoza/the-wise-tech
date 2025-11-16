<!-- metadata
para_quien: Equipos y contribuidores que consultan "Receta: Manejo de Errores Intencional" en The Wise Tech.
objetivo: Proporcionar un contexto accionable sobre receta: manejo de errores intencional.
cuando_usar: Recurre a este documento cuando necesites aplicar o compartir detalles de receta: manejo de errores intencional.
estado: active
-->

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

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
