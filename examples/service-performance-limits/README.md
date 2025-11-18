# Service Performance Limits

This sample applies a sliding-window rate limiter to protect upstream systems.
Run it to see how the limiter enforces the objectives declared in the
`behavior-contract.yaml` file.

```bash
python service.py
```

The script issues synthetic requests and prints whether they were accepted or
shed based on the configured throughput limit.
