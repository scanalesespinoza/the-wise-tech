# Service Resilience (Basic)

This sample models a checkout dependency with retries, timeouts, and graceful
fallbacks. Run it locally to see how the component behavior contract maps to
real safeguards.

```bash
python service.py
```

The script simulates calls to an unstable downstream dependency. The retry logic
and fallback response demonstrate the controls listed in
`behavior-contract.yaml`.
