# Inventario de cadenas y documentación sensibles a i18n

| Ruta | Tipo | Descripción | Prioridad | Complejidad | Riesgo/Notas |
| --- | --- | --- | --- | --- | --- |
| README.md | Documentación | Página raíz con valor narrativo, índice y flujo bilingüe que define cómo sincronizar inglés↔español. | Alta | Traducción directa | Cambiar títulos o pasos puede desalinear la navegación y la cola de traducción. |
| docs/visual-navigation.md | Mensajes UI | Landing de navegación con textos de botones ("Ver índice de valor") y promesas de resultado por rol. | Alta | Traducción directa | Visible en GitHub Pages; los CTA deben conservar emojis/estilos y enlaces. |
| audit/translation-queue.yml | IDs/i18n | Cola de traducciones con waves/batches (`wave-1`, `w1-b1`, P0–P2) y rutas EN/ES. | Alta | Refactor con i18n | No traducir IDs/estados; scripts dependen de claves y prioridades. |
| operations/scripts/audit-evaluator.py | Logs y labels | Criterios de auditoría con etiquetas/sugerencias en español y mensajes de log cuando faltan archivos o Git. | Media | Refactor con i18n | Los labels alimentan reportes; modificar texto o emojis puede romper parsers o expectativas de puntaje. |
| systems/tests/test_audit_evaluator.py | Strings en tests | Casos que validan rutas de API y extraen respuestas con literales `"PASS"/"FAIL"/"UNKNOWN"`. | Alta | Refactor con i18n | Traducir estos tokens rompe las aserciones y el parsing de respuestas del LLM. |
| operations/scripts/validate-resilience.py | Comentarios de código y CLI | Comentarios sobre campos requeridos y mensajes de uso/errores para validar YAML de resiliencia. | Media | Traducción directa | Salida de CLI usada en CI; mantener claves y formatos (`service`, `version`, `Missing required key`). |
