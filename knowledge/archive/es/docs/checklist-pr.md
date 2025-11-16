## Propósito
Enmarca cómo Checklist de Pull Request (Esencial + Operativo) ayuda a mantener decisiones alineadas con The Wise Tech.

## Audiencia
Personas y equipos que necesitan una guía rápida sobre Checklist de Pull Request (Esencial + Operativo).

## Cuándo usarlo
Consúltalo cuando requieras referencias inmediatas para Checklist de Pull Request (Esencial + Operativo) o debas compartir el enfoque con otros equipos.

> **Propósito:** Dar contexto accionable sobre Checklist de Pull Request (Esencial + Operativo) dentro de The Wise Tech.
> **Audiencia:** Equipos y perfiles interesados en las bases de conocimiento y lineamientos del programa.
> **Uso recomendado:** Consulta este documento cuando necesites aplicar o compartir detalles de Checklist de Pull Request (Esencial + Operativo).
> **Estado:** Activo.


## Tabla de navegación

- [Alineación Esencial](#alineacin-esencial)
- [Calidad Operativa](#calidad-operativa)
- [Impacto y Compartir Conocimiento](#impacto-y-compartir-conocimiento)

# Checklist de Pull Request (Esencial + Operativo)

Usa esta checklist viva para validar cada cambio antes de solicitar revisión. Complétala junto con la plantilla de PR en `.github/PULL_REQUEST_TEMPLATE.md`.

## Alineación Esencial
- [ ] Vinculado al menos a un [Principio Esencial](principles-essential.md) en la descripción.
- [ ] Se respetan los límites (sin fugas de dominio, contratos explícitos actualizados).
- [ ] Telemetría agregada o confirmada (logs estructurados, métricas, trazas).
- [ ] Modos de fallo controlados (timeouts, reintentos, degradación elegante).
- [ ] Datos sensibles y secretos protegidos (sin credenciales embebidas, almacenamiento seguro verificado).

## Calidad Operativa
- [ ] Pruebas actualizadas (unitarias, integración, contrato según corresponda) con evidencia clara.
- [ ] Señales de observabilidad incluyen identificadores de correlación para depuración.
- [ ] Controles de seguridad (SAST/SCA) pasan localmente o incluyen justificación para seguimiento.
- [ ] Impacto en desempeño revisado para rutas críticas (latencia, uso de recursos).
- [ ] Documentación actualizada (recetas, onboarding, glosario) o confirmado que no es necesario.

## Impacto y Compartir Conocimiento
- [ ] Se agregó nota de changelog/narrativa explicando el valor entregado.
- [ ] Se etiquetó a mentorías o personas expertas del dominio crítico.
- [ ] Se brindaron pistas de onboarding (archivos a leer, comandos a ejecutar) en la descripción del PR.
- [ ] Se capturaron nuevos patrones o anti-patrones en el [catálogo de recetas](recipes/README.md).

Mantén la checklist lo suficientemente corta para seguir siendo accionable. Cuando el equipo detecte nuevos problemas recurrentes, evoluciona la checklist de forma colaborativa y documenta el razonamiento.
---
Última modificación: 2025-11-16

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos
- [ ] No me ayudó

💬 [Deja tu feedback](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---

