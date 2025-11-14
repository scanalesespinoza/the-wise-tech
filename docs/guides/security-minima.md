# Seguridad mínima — Contributors
Esta guía define controles prácticos y reproducibles:
- **Secretos**: nunca en el repo. Usa variables de entorno o secretos en GitHub.
- **Dependencias**: Dependabot abre PRs semanales para Actions y Python.
- **Escaneo de secretos**:
  - Local: `make security-scan` (gitleaks).
  - CI: workflow `gitleaks` se ejecuta en PR/push.
- **Datos sensibles en docs**: usa ejemplos ficticios y elimina PII.
- **PRs**: si tu cambio toca CI/scripts/deps, añade una línea “Security note” en el cuerpo del PR.

## Flujo recomendado
1) Ejecuta `make security-scan` antes del PR.
2) Revisa diffs por si quedaron credenciales o tokens.
3) Acepta PRs de Dependabot (verifica que CI pase).
4) Si detectas un riesgo, usa el canal privado de `SECURITY.md`.

## Próximos pasos
- Añadir SAST/linters específicos cuando el stack lo requiera.
- Firmado de commits y/o provenance de artefactos (release pipeline).
