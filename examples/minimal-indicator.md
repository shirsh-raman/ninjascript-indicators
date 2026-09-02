# Minimal Indicator

Use this prompt to request a small, non-trading indicator:

```text
Create a NinjaTrader 8 indicator that plots the close price, declares one plot, and explains State.SetDefaults, State.Configure, and OnBarUpdate. Include a CurrentBar guard and state that it is uncompiled.
```

Review points:

- Declare the plot and display metadata in `State.SetDefaults`.
- Calculate only after the required lookback is available.
- Write to `Values[0]` rather than assuming a chart-side data structure.
- Confirm the installed version before relying on exact signatures.

Safety: this example should calculate or display only. It should not submit orders.

Verification status: manually reviewed Markdown; not compiled or runtime-tested.
