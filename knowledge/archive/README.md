# Archive

Este directorio conserva contenido bilingüe y material histórico. Trátalo como una **caja cerrada**: mueve elementos aquí solo cuando ya no participen de los flujos activos.

- `en/` y `es/` mantienen documentación previa en ambos idiomas.
- `guides-legacy/`, `platform-legacy/` e `infra-legacy/` almacenan referencias históricas.
- `legacy-diagrams/` y `config/` resguardan diagramas y configuraciones anteriores.

## Política de archivado
- Documenta en la PR por qué el contenido pasa a `knowledge/archive/` y qué lo reemplaza.
- Añade una nota en `knowledge/docs/audit/content-audit.md` para dejar rastro del movimiento.
- Cuando un activo vuelva a producción, crea un commit separado que lo reubique en la carpeta activa correspondiente y actualiza los enlaces.
