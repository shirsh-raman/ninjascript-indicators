# Data Series

## Reference build and ambiguity

Examples and guidance target NinjaTrader 8.1.8.2. The focused normalized records are official but generally lack reliable publication or update dates, so their API details are version-ambiguous. Confirm overloads, defaults, and generated indicator wrappers in the installed build. **Evidence:** record `nt-b6c1105cda603947`, canonical URL: https://developer.ninjatrader.com/docs/desktop/adddataseries; record `nt-afcc4163d31ad969`, canonical URL: https://developer.ninjatrader.com/docs/desktop/seriest.

## Adding series

Add secondary instruments or periods in `State.Configure` with `AddDataSeries`. Keep the series definition deterministic and avoid making it depend on runtime bar values. The primary series is index `0`; secondary series use their configured index. **Evidence:** record `nt-b6c1105cda603947`, canonical URL: https://developer.ninjatrader.com/docs/desktop/adddataseries; record `nt-04329004876c8e9f`, canonical URL: https://developer.ninjatrader.com/docs/desktop/currentbars.

## Synchronization and guards

NinjaScript invokes `OnBarUpdate` in the context of the series that produced the update. Use `BarsInProgress` to select the work path, and check `CurrentBars[index]` before indexing a secondary series. A guard for the primary series does not establish readiness for every secondary series. **Evidence:** record `nt-be831d998c23355b`, canonical URL: https://developer.ninjatrader.com/docs/desktop/barsinprogress; record `nt-04329004876c8e9f`, canonical URL: https://developer.ninjatrader.com/docs/desktop/currentbars; record `nt-37c50fd1f69a2263`, canonical URL: https://developer.ninjatrader.com/docs/desktop/currentbar.

## Series, price data, and outputs

Use `ISeries<T>` when accepting a bar-synchronized input, `Series<T>` for a custom bar-synchronized calculation series, and plot-backed `Values` or `Value` for indicator outputs. Do not treat a series index as a timestamp or assume that two series have identical bar counts. **Evidence:** record `nt-b4a7af233189d711`, canonical URL: https://developer.ninjatrader.com/docs/desktop/iseriest; record `nt-afcc4163d31ad969`, canonical URL: https://developer.ninjatrader.com/docs/desktop/seriest; record `nt-7b7f63efcf210cc9`, canonical URL: https://developer.ninjatrader.com/docs/desktop/addplot.

## Supported multi-series example

This pattern is **manually checked, not compiled** and **simulation-only**. It demonstrates synchronization and readiness; it does not submit orders. The exact `AddDataSeries` overload should be checked in the target 8.1.8.2 editor.

```csharp
protected override void OnStateChange()
{
    if (State == State.Configure)
        AddDataSeries(BarsPeriodType.Minute, 5);
}

protected override void OnBarUpdate()
{
    if (CurrentBars[0] < 1 || CurrentBars[1] < 1)
        return;

    if (BarsInProgress != 0)
        return;

    double spread = Close[0] - Closes[1][0];
    Print(spread);
}
```

**Evidence:** record `nt-b6c1105cda603947`, canonical URL: https://developer.ninjatrader.com/docs/desktop/adddataseries; record `nt-be831d998c23355b`, canonical URL: https://developer.ninjatrader.com/docs/desktop/barsinprogress; record `nt-04329004876c8e9f`, canonical URL: https://developer.ninjatrader.com/docs/desktop/currentbars.

## Uncovered and partial

Provider-specific bid/ask availability, Tick Replay prerequisites, volumetric series, unusual bar types, and exact multi-series timestamp alignment are only partial in this module. Validate data availability and licensing with the provider before relying on those series. **Evidence:** record `nt-01fbd32a9178a3a0`, canonical URL: https://developer.ninjatrader.com/docs/desktop/developing_for_tick_replay; record `nt-81e86351db9d3a77`, canonical URL: https://developer.ninjatrader.com/docs/desktop/addvolumetric.
