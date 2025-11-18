# wise-tech-linter (borrador)

Script mínimo para validar que `component-contract.yaml` cumpla con el formato
esperado por las listas de verificación de resiliencia, desempeño y
observabilidad.

## Uso

```bash
python tools/wise-tech-linter/wise_tech_linter.py audit/component-contract.yaml
```

El comando regresa código 0 cuando el contrato es válido. El objetivo es añadirlo
a la canalización de CI en una iteración futura.
