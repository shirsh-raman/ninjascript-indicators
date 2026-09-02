# Indicator Lifecycle

## Reference build and ambiguity

This module targets NinjaTrader 8.1.8.2 as the reference build. The focused records are official documentation snapshots but are generally version-ambiguous; do not assume a later or earlier NinjaTrader build has identical state timing, generated code, or callback details. **Evidence:** record `nt-40dfe12728325c1d`, canonical URL: https://developer.ninjatrader.com/docs/desktop/understanding_the_lifecycle_of; record `nt-e956a651aeee02e0`, canonical URL: https://developer.ninjatrader.com/docs/desktop/onstatechange.

## State responsibilities

Use `State.SetDefaults` for user-facing defaults and plots, `State.Configure` for additional data series, `State.DataLoaded` for objects that depend on loaded series, and `State.Terminated` for cleanup. Keep `OnBarUpdate` focused on bar-driven calculations rather than configuration. **Evidence:** record `nt-e956a651aeee02e0`, canonical URL: https://developer.ninjatrader.com/docs/desktop/onstatechange; record `nt-40dfe12728325c1d`, canonical URL: https://developer.ninjatrader.com/docs/desktop/understanding_the_lifecycle_of; record `nt-b6c1105cda603947`, canonical URL: https://developer.ninjatrader.com/docs/desktop/adddataseries.

## Bar processing and readiness

`OnBarUpdate` can be called for each configured series. Select `Calculate.OnBarClose`, `Calculate.OnEachTick`, or `Calculate.OnPriceChange` deliberately, then guard lookbacks with `CurrentBar` or each relevant entry in `CurrentBars`. In a multi-series indicator, filter work with `BarsInProgress` before reading the intended series. **Evidence:** record `nt-38fad49cb296238f`, canonical URL: https://developer.ninjatrader.com/docs/desktop/onbarupdate; record `nt-9ebbf8fbd2e2d3d5`, canonical URL: https://developer.ninjatrader.com/docs/desktop/calculate; record `nt-be831d998c23355b`, canonical URL: https://developer.ninjatrader.com/docs/desktop/barsinprogress; record `nt-04329004876c8e9f`, canonical URL: https://developer.ninjatrader.com/docs/desktop/currentbars.

## Historical, realtime, and Tick Replay behavior

Historical processing, realtime processing, and Tick Replay can produce different callback sequences and available event data. Treat first-tick/session transitions and intrabar calculations as explicit design decisions. Require Tick Replay and provider support only when the calculation actually needs historical tick-level behavior; do not claim bar-close results are equivalent to tick-replay results. **Evidence:** record `nt-01fbd32a9178a3a0`, canonical URL: https://developer.ninjatrader.com/docs/desktop/developing_for_tick_replay; record `nt-9ebbf8fbd2e2d3d5`, canonical URL: https://developer.ninjatrader.com/docs/desktop/calculate.

## Supported example

This lifecycle sketch is **manually checked, not compiled**. It is **simulation-only**: it calculates an output and does not submit orders. Add the generated namespace/usings and platform boilerplate required by the NinjaScript Editor.

```csharp
protected override void OnStateChange()
{
    if (State == State.SetDefaults)
    {
        Name = "CloseChange";
        Calculate = Calculate.OnBarClose;
        IsOverlay = false;
        AddPlot(Brushes.DodgerBlue, "Change");
    }
}

protected override void OnBarUpdate()
{
    if (CurrentBar < 1)
        return;

    Value[0] = Close[0] - Close[1];
}
```

**Evidence:** record `nt-e956a651aeee02e0`, canonical URL: https://developer.ninjatrader.com/docs/desktop/onstatechange; record `nt-38fad49cb296238f`, canonical URL: https://developer.ninjatrader.com/docs/desktop/onbarupdate; record `nt-7b7f63efcf210cc9`, canonical URL: https://developer.ninjatrader.com/docs/desktop/addplot.

## Uncovered and partial

The corpus does not include local compile/runtime verification, deterministic callback traces for every calculation mode, or a complete treatment of indicator caching and generated accessors. These remain partial and must be validated in the target installation. **Evidence:** record `nt-81ef52f71e6c0355`, canonical URL: https://developer.ninjatrader.com/docs/desktop/developing_indicators.
