# Order Flow

Use this prompt when the requested calculation depends on volumetric data:

```text
Explain how to design a NinjaTrader 8 indicator that reads volumetric bar information for display only. Identify the required bar type, Order Flow + entitlement, provider data assumptions, and what to verify before compilation and simulation.
```

Review points:

- Establish whether the chart uses the required volumetric bar type.
- Check Order Flow + availability and provider-specific data support.
- Treat missing or partial data as an environment issue, not proof that the calculation is wrong.
- Keep the output observational or simulation-only.
- State which behavior remains provider-dependent or unverified.

Verification status: manually reviewed Markdown; not compiled or runtime-tested.
