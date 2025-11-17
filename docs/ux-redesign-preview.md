# Vista previa — Rediseño UX simplificado

Este mockup resume onboarding, rutas y primeras victorias usando un lenguaje visual. No reemplaza la documentación técnica: es un adelanto para usuarios no técnicos que necesitan tomar decisiones rápidas.

## Panel de bienvenida

| Perfil | Qué ve primero | Acción en 1 clic |
| --- | --- | --- |
| 👀 Consumidor | Un resumen visual con botones a historias y métricas humanas. | [🍃 Ve al hub visual](visual-navigation.md#consumidor) |
| 💻 Desarrollador | Pasos guiados por comandos con indicadores de estado. | [💡 Explora el hub visual](visual-navigation.md#desarrollador) |
| 🧱 Plataforma | Estado de controles resilientes y alertas mínimas. | [🛡️ Revisa el hub visual](visual-navigation.md#ingeniero-de-plataforma) |

> ℹ️ **Tip**: Todas las tarjetas muestran badges de "Tiempo estimado" (30, 60, 90 min) para reducir la fricción.

## Onboarding express

| Día | Qué ves | Micro-acción |
| --- | --- | --- |
| Día 0 | Video/infografía sobre filosofía Wise Tech. | Guardar 1 aprendizaje en favoritos. |
| Día 1 | Checklist interactivo (7 pasos) + barra de progreso. | Completar mínimo 3 pasos. |
| Día 2 | Botón “Compárteme tu feedback” con estado dinámico. | Abrir issue desde la plantilla UX. |

## Aprende en 30 días (mockup)

```
Semana 1 | 📘 Fundamentos visuales
─────────┼────────────────────────────
Día 1: Card "Start Here" con botón verde.
Día 3: Card "Elegir ruta" con mini badges.

Semana 2 | 🧪 Manos a la obra
─────────┼────────────────────────────
Día 8: Card "Corre make test" con contador ✅/❌.
Día 10: Card "Entrega feedback" con icono de megáfono.

Semana 3 | 🚀 Escala rápido
─────────┼────────────────────────────
Día 15: Card "Fast Track" con fondo naranja.
Día 20: Card "Runbook vivo" con etiqueta LIVE.

Semana 4 | 🔁 Mejora continua
─────────┼────────────────────────────
Día 25: Card "Comparte KPI" con gráfico mini.
Día 30: Card "Plan 60-90" con flecha ➡️.
```

> ℹ️ **Tip**: Cada tarjeta tendría un borde de color (verde = listo, amarillo = en progreso, gris = próximo).

## Cajas de acción rápida

- ✅ **Primer deploy** → Botón grande con texto “Clona + `make install`”. Debajo, un chip que dice “15 min promedio”.
- 🧪 **Primera prueba** → Card con barra de avance que muestra `make test` → `100%` cuando termina.
- 📣 **Primer feedback** → Caja naranja con icono de megáfono y enlace directo al issue template.

## Cómo se conectan las rutas

| Ruta | Visual principal | Fast Track |
| --- | --- | --- |
| Consumers 30/60/90 | Hero con testimonios y contador de historias activas. | [🍃 Explora rutas](es/guides/choose-your-path.md) |
| Developers 30/60/90 | Tablero tipo Kanban (Docs, Código, Feedback). | [⚡ Explora rutas](es/guides/choose-your-path.md) |
| Platform Engineers 30/60/90 | Matriz de controles (Políticas, SLOs, Runbooks). | [🛡️ Explora rutas](es/guides/choose-your-path.md) |

## Próximos pasos visuales

1. Crear componentes reutilizables (tarjetas, badges y barras de progreso).
2. Integrar métricas reales (por ejemplo, porcentaje de guías leídas por perfil).
3. Activar recordatorios “sigamos en contacto” con enlaces a Fast Track y Start Here.

---

🗳️ **¿Te fue útil este documento?**
- [ ] Sí, resolvió mi duda
- [ ] Más o menos, necesito más contexto
- [ ] No me ayudó

📢 [Abre un feedback aquí](https://github.com/scanalesespinoza/the-wise-tech/issues/new?template=feedback.yml)

---
