# Supplementary APIs

## Scope And Selection

Use this module for documented APIs adjacent to the core indicator lifecycle. Confirm the requested script type, platform version, calculation mode, primary and secondary series, session template, historical/realtime behavior, Tick Replay requirement, rendering needs, provider/licensing assumptions, and safety constraints before selecting an API. The focused corpus covers these API families unevenly; a reference listing is not runtime validation. [nt-91acd165deabf458 | https://developer.ninjatrader.com/docs/desktop/alert_and_debug_concepts]

## Multi-Series Data

Use `AddDataSeries()` to add Bars objects for multi-time-frame or multi-instrument scripts. Route calculations by the exact `BarsInProgress` value and use the corresponding series rather than assuming that the primary series triggered the callback. Keep series declarations deterministic and aligned with the user's requested data. [nt-ba525ae7a043c2dd | https://docs.ninjatrader.com/ninjascript/adddataseries] [nt-06aeacf1efd95e5d | https://docs.ninjatrader.com/ninjascript/onbarupdate]

Simulation-only shape:

```csharp
protected override void OnStateChange()
{
    if (State == State.Configure)
        AddDataSeries(BarsPeriodType.Minute, 5);
}

protected override void OnBarUpdate()
{
    if (BarsInProgress != 0 || CurrentBars[1] < 1)
        return;

    double secondaryClose = Closes[1][0];
    // Use secondaryClose in an indicator calculation only.
}
```

This is a structural example only. It does not place orders and has not been compiled or run in the focused environment. [nt-ba525ae7a043c2dd | https://docs.ninjatrader.com/ninjascript/adddataseries]

## System Indicators

Prefer the documented system indicator methods when they meet the requested calculation, rather than reimplementing a covered primitive. The corpus index includes common methods such as SMA, EMA, RSI, MACD, and Bollinger; select parameters explicitly and state the input series and warm-up assumptions. [nt-24d4d9e42b35cb28 | https://docs.ninjatrader.com/ninjascript/system_indicator_methods]

Do not treat a system-indicator reference as proof that a particular overload, cache behavior, or generated accessor is available in every platform version. Verify the signature in the user's editor. [nt-24d4d9e42b35cb28 | https://docs.ninjatrader.com/ninjascript/system_indicator_methods]

## Sessions And Trading-Hours Data

Use `SessionIterator` when a calculation needs trading-hours boundaries or trading dates. Construct it from the intended `Bars` object and defer access to its properties until the documented lifecycle permits it, rather than reading session properties prematurely during `OnStateChange()`. [nt-f76301004ee7da42a0 | https://docs.ninjatrader.com/ninjascript/sessioniterator]

Session behavior is data- and template-dependent. Ask for the Trading Hours template and timezone when session boundaries affect signals, plots, or diagnostics; do not silently substitute exchange, local, or UTC assumptions. [nt-f76301004ee7da42a0 | https://docs.ninjatrader.com/ninjascript/sessioniterator]

## Historical Tick Context

Use Tick Replay only when the requested logic needs tick-level historical market-data behavior. The official record says Tick Replay can generate many events per bar and that the script must be designed for that mode; it also identifies `OnMarketData()`, `OnBarUpdate()`, `OnEachTick`, and `OnPriceChange` as relevant paths. [nt-f37e0ee9034c43a0 | https://docs.ninjatrader.com/ninjascript/developing_for_tick_replay]

Keep Tick Replay examples simulation-only and call out the user's responsibility to enable it on the primary data series. The focused corpus provides documentation, not a replay execution or performance measurement. [nt-f37e0ee9034c43a0 | https://docs.ninjatrader.com/ninjascript/developing_for_tick_replay]

## Alerts, Sharing, And Diagnostics

The focused records expose `Alert()`, `RearmAlert()`, `Share()`, `SendMail()`, `PlaySound()`, `Print()`, `Log()`, and `ClearOutputWindow()` as supplementary platform surfaces. Select them only when the user has specified the desired side effect, and keep alert/share/mail examples disabled or simulation-only by default. [nt-75c2b69d3ee38960 | https://developer.ninjatrader.com/docs/desktop/alert_debug_share] [nt-eebe812c2f98d39e | https://developer.ninjatrader.com/docs/desktop/alert]

## Add-Ons: Uncovered

**Uncovered for implementation guidance.** The focused records identify Add-On Development and an Add On reference in the documentation navigation, but they do not provide sufficient normalized API behavior, lifecycle examples, UI-thread guidance, packaging instructions, or runtime evidence for this module. Do not generate an Add-On architecture or claim Add-On compatibility from these index links. [nt-91acd165deabf458 | https://developer.ninjatrader.com/docs/desktop/alert_and_debug_concepts]

## Rendering And SharpDX Boundary

Rendering and SharpDX are separate concerns from supplementary data APIs. Route rendering requests to the rendering module; only use this module to flag that rendering introduces resource-lifecycle and runtime-verification requirements. The focused corpus contains `OnRender()` and SharpDX records, but this module does not claim a complete rendering recipe. [nt-1d5de8957afc4a4c | https://developer.ninjatrader.com/docs/desktop/sharpdx_directwrite_textformat_fontweight] [nt-1cb348ba64969de4 | https://developer.ninjatrader.com/docs/desktop/sharpdx_direct2d1_strokestyle_endcap]

## Evidence Gaps

Add-Ons are uncovered. Runtime verification is uncovered. Testing is partial, because the API records can define cases but no local compiler, harness, or executed run is present. Deployment is uncovered, because this focused coding corpus does not establish distribution, import, signing, or install behavior. These are evidence gaps, not permissions to fill in platform-specific details from memory. [nt-91acd165deabf458 | https://developer.ninjatrader.com/docs/desktop/alert_and_debug_concepts] [nt-f37e0ee9034c43a0 | https://docs.ninjatrader.com/ninjascript/developing_for_tick_replay]
