# Debugging, Testing, And Deployment

## Evidence Boundary

This module is scoped to the focused corpus and the NinjaTrader 8.1.8.2 reference build. The corpus contains documentation records for debug/diagnostic APIs, but no authorized NinjaTrader installation or local compiler was available. Treat all code below as guidance to inspect in the NinjaScript Editor, not as compiled or runtime-verified output. [nt-91acd165deabf458 | https://developer.ninjatrader.com/docs/desktop/alert_and_debug_concepts]

Trading examples remain simulation-only. Do not connect generated code to a live account or submit live orders as part of debugging or validation. [nt-75c2b69d3ee38960 | https://developer.ninjatrader.com/docs/desktop/alert_debug_share]

## Debugging Workflow

1. Reproduce the smallest deterministic symptom with a fixed instrument, series, date range, calculation mode, and historical/realtime context.
2. Add narrow diagnostic output around state transitions, bar updates, and any multi-series branch. Include `CurrentBar`, `BarsInProgress`, timestamps, and the values needed to distinguish input, calculation, and rendering issues.
3. Use the documented diagnostic surface deliberately: `Print()` for development output, `Log()` for platform logging, `ClearOutputWindow()` to isolate a run, and `TraceOrders` when the problem is order tracing. Remove or gate noisy diagnostics before distribution.
4. Compare historical and realtime paths separately. `OnStateChange()` can be entered during initialization and compile-time object creation, while `OnBarUpdate()` frequency depends on `Calculate`; do not interpret every state transition as a chart instance restart.

The record indexes the alert/debug concepts and the individual Print, Log, ClearOutputWindow, and TraceOrders references. The focused extraction does not provide a local compiler session or an executed diagnostic transcript. [nt-75c2b69d3ee38960 | https://developer.ninjatrader.com/docs/desktop/alert_debug_share] [nt-91acd165deabf458 | https://developer.ninjatrader.com/docs/desktop/alert_and_debug_concepts] [nt-b87acf9b3c4333b5 | https://docs.ninjatrader.com/ninjascript/onstatechange] [nt-06aeacf1efd95e5d | https://docs.ninjatrader.com/ninjascript/onbarupdate]

## Diagnostic Example

The following is a simulation-only diagnostic pattern. It is intentionally incomplete and must be adapted to the requested script type and lifecycle. It does not place, submit, or modify orders.

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBar < 1)
        return;

    Print($"BIP={BarsInProgress} time={Time[0]} close={Close[0]}");
}
```

The example relies only on the documented bar-update callback and development output surface; it is not evidence that the snippet compiles in the user's installation. [nt-06aeacf1efd95e5d | https://docs.ninjatrader.com/ninjascript/onbarupdate] [nt-e08313567736690f | https://developer.ninjatrader.com/docs/desktop/print]

## Testing Status: Partial

**Partial coverage.** The corpus documents calculation, bar-update, multi-series, session, Tick Replay, and performance-related APIs that can inform a test matrix. It does not provide a local compiler, automated test harness, executed Strategy Analyzer/Playback run, golden output, or evidence that a generated script passed those checks. [nt-06aeacf1efd95e5d | https://docs.ninjatrader.com/ninjascript/onbarupdate] [nt-f37e0ee9034c43a0 | https://docs.ninjatrader.com/ninjascript/developing_for_tick_replay] [nt-1e44819c6bcf02ca | https://developer.ninjatrader.com/docs/desktop/tradesperformance]

Use this evidence-bounded checklist:

- Compile in the user's NinjaScript Editor and resolve errors before any behavioral claim.
- Exercise historical bars, the first realtime update, and the selected `Calculate` mode.
- For multi-series scripts, exercise every intended `BarsInProgress` branch and confirm series alignment.
- If Tick Replay is required, enable it explicitly and compare resource/load behavior with the non-replay path.
- Record observed output, platform version, data provider, instrument, Trading Hours template, and data range.

The checklist is a recommended validation procedure, not a claim that the focused corpus contains those executions. [nt-b87acf9b3c4333b5 | https://docs.ninjatrader.com/ninjascript/onstatechange] [nt-ba525ae7a043c2dd | https://docs.ninjatrader.com/ninjascript/adddataseries] [nt-f37e0ee9034c43a0 | https://docs.ninjatrader.com/ninjascript/developing_for_tick_replay]

## Runtime Verification Status: Uncovered

**Uncovered by corpus evidence.** No local NinjaTrader runtime, authorized installation, provider session, compiled artifact, or runtime log is available here. A response may specify what the user should verify, but must not claim that an indicator loaded, rendered, produced expected values, survived a reconnect, or behaved correctly in historical and realtime execution. [nt-b87acf9b3c4333b5 | https://docs.ninjatrader.com/ninjascript/onstatechange] [nt-f37e0ee9034c43a0 | https://docs.ninjatrader.com/ninjascript/developing_for_tick_replay]

## Deployment Status: Uncovered

**Uncovered by this focused coding corpus.** Do not invent an export format, install path, signing process, version-compatibility guarantee, or distribution checklist. Deployment and import behavior require a separately evidenced official distribution/import record and user-side confirmation. Until then, provide source code only and state that deployment has not been verified. [nt-91acd165deabf458 | https://developer.ninjatrader.com/docs/desktop/alert_and_debug_concepts]
