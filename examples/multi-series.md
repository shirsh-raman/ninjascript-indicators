# Multi-Series Indicator

Use this prompt for synchronization guidance:

```text
Create a NinjaTrader 8 multi-series indicator with a primary series and one added series. Explain where AddDataSeries belongs, how BarsInProgress selects the update stream, and how to guard lookbacks for both series. Do not submit orders.
```

Review points:

- Add the secondary series during the configuration lifecycle state.
- Treat each `BarsInProgress` branch as a separate update context.
- Guard each series independently before reading bars-ago values.
- Explain that timestamps, session templates, and historical/realtime sequencing affect alignment.
- Name the exact series and bar type rather than relying on chart defaults.

Verification status: manually reviewed Markdown; not compiled or runtime-tested.
