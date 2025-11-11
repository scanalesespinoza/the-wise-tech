# Guía de Contribución (Español)

Gracias por invertir en la base de conocimiento de The Wise Tech. Este repositorio refleja cada artefacto en inglés y español, así que mantén ambas versiones alineadas.

## Flujo de Trabajo
1. Actualiza primero el documento o recurso en inglés.
2. Replica el cambio en su contraparte en español con la misma estructura e intención.
3. Ejecuta `.github/scripts/generate_module_readmes.py` cuando agregues recetas o guías de onboarding.
4. Abre un pull request usando la plantilla y completa la checklist.
5. Etiqueta a mentorías o personas expertas cuando propongas cambios a los Principios Esenciales.

## Expectativas de Traducción
- Conserva encabezados, llamados y enlaces para que la navegación siga siendo simétrica.
- Usa español neutro, inclusivo y comprensible para Latinoamérica y España.
- Documenta modismos o terminología en `en/docs/glossary.md` y `es/docs/glossary.md`.

## Tipos de Documentación
- **Esencial:** [`es/docs/principles-essential.md`](es/docs/principles-essential.md)
- **Checklists:** [`es/docs/checklist-pr.md`](es/docs/checklist-pr.md)
- **Recetas:** `es/docs/recipes/*.md`
- **Onboarding:** `es/docs/onboarding/*.md`
- **Changelog narrativo:** [`es/docs/changelog-guidelines.md`](es/docs/changelog-guidelines.md)

## Automatización
- GitHub Actions verifican la presencia de la plantilla de PR y preparan resúmenes cuando existe un webhook configurado.
- El workflow `Doc Generation` mantiene actualizados los catálogos de recetas/onboarding.
- Revisa los archivos bajo `.github/workflows/` para adaptar las automatizaciones a tu organización.

## Criterios de Revisión
- Referencias a los Principios Esenciales en la descripción del PR y respeto en el diff.
- Pruebas, observabilidad e implicaciones de seguridad atendidas o justificadas.
- Documentación actualizada o diferida explícitamente con un issue.
- Traducción al inglés revisada por una persona bilingüe cuando sea posible.

Si prefieres orientación en inglés, consulta también la [Contributing Guide](CONTRIBUTING.md).
