# ADR-0001: Perfiles de Consistencia Declarativos

- Fecha: 2024-06-14
- Estado: Propuesto

## Contexto

Los servicios de Wise Tech operan sobre múltiples réplicas y entornos. Sin una taxonomía explícita de consistencia, los equipos mezclaban requisitos (p.ej., transacciones críticas usando cachés eventual) y los despliegues carecían de garantías client-centric como read-your-writes. Necesitamos una forma declarativa de seleccionar garantías por servicio para habilitar automatización en CI/CD y facilitar migraciones controladas.

## Decisión

1. Definimos tres perfiles soportados: **Strict**, **Causal** y **Eventual**.
2. Cada servicio y entorno declara su perfil en `platform/policies/consistency.yml` junto a su patrón de acceso y estrategia de réplica.
3. Documentamos las garantías de cada perfil, incluyendo coherencia client-centric (read-your-writes, monotonic reads) cuando aplique.
4. El middleware de sesión adjunta un vector lógico por usuario para cumplir las garantías client-centric de causalidad.
5. Proveemos guía para distinguir consistencia (dataset) de coherence (ítems/cachés) con ejemplos de TTL.

## Consecuencias

- **Positivas**: decisiones auditables, validaciones automáticas en CI, reducción de incidentes por configuraciones implícitas.
- **Negativas**: sobrecarga inicial para declarar perfiles y mantener metadata; requiere instrumentar headers de sesión en clientes multi-réplica.

## Migración

1. Inventariar servicios críticos y etiquetarlos con el perfil actual implícito.
2. Introducir `consistency.yml` en modo observación (solo lint) para detectar incompatibilidades.
3. Migrar servicios eventual→causal con despliegues blue/green controlados y métricas de latencia.
4. Para strict, introducir bloqueos optimistas/pesimistas según corresponda y validar el impacto en throughput.

## Notas

Las decisiones futuras deben revisar la necesidad de nuevos perfiles (p.ej., strong session) a medida que evolucione la plataforma.
