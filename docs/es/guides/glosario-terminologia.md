---
title: "Glosario de terminología (ES)"
tags: ["docs", "i18n", "terminology"]
---
# Glosario de terminología

> Usa estos términos para consistencia. Si falta alguno, proponlo en un PR.

## Términos clave
- **error budget** → **presupuesto de error**
- **retry** → **reintento**
- **exponential backoff** → **retroceso exponencial**
- **correlation id** → **id de correlación**
- **idempotency key** → **clave de idempotencia**
- **observability** → **observabilidad**
- **playbook** → **playbook** (no traducir el término como tag o nombre de archivo)
- **SLO** → **SLO** (sigla en inglés; expandir como “objetivo de nivel de servicio” en el texto cuando sea necesario)
- **latency p95** → **latencia p95**

## Convenciones de estilo
- **Formalidad**: tono profesional y directo, sin tuteo. Prefiere verbos en infinitivo o imperativo neutro ("Configurar el servicio", "Ejecutar el comando").
- **Dialecto**: español neutro con tecnicismos claros. Evita regionalismos y anglicismos innecesarios; usa préstamos aceptados solo cuando no exista traducción estándar.
- **Capitalización**: sigue las reglas de la RAE salvo nombres de productos, API o paquetes que mantienen su capitalización original.
- **Citas de código y comandos**: mantener en inglés y en minúsculas según se usen en consola o archivos de configuración.

## Elementos que deben permanecer en inglés
- **APIs externas y nombres de endpoints**: conservar nombres y rutas exactas (`/healthz`, `POST /v1/metrics`).
- **Nombres de paquetes, librerías y módulos**: no traducir (`OpenTelemetry`, `numpy`, `fastapi`).
- **Contratos legales, SLAs y términos de licencia**: respetar el inglés original salvo notas aclaratorias.
- **Flags, variables de entorno y claves de configuración**: copiar literalmente para evitar confusiones.

## Prioridad de dominios para aplicar la traducción
1. **Documentación visible para usuarios**: guías, tutoriales, landing pages y notas de versión.
2. **Mensajes de interfaz**: textos de UI y notificaciones en productos, siempre que no se rompa un flujo internacionalizado.
3. **Comentarios y nombres de código**: traducir solo si no afecta compatibilidad (por ejemplo, no cambiar nombres públicos de clases o funciones sin control de versión).

## Cómo usar el glosario
- Refuerza las traducciones en reseñas humanas.
- Complementa con notas si la traducción cambia el flujo (por ejemplo, UI en inglés).
- Actualiza el glosario antes de ejecutar un nuevo batch si agregas términos críticos.

## See also
- [Migración a español — Proceso por lotes](migracion-es.md)
- [Content Style Guide](../../guides/content-style-guide.md)
