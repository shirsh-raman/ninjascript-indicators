# C# Fundamentals for NinjaScript

## Scope and version posture

Use ordinary C# fundamentals inside NinjaScript, but treat the NinjaTrader object model, lifecycle, and series types as platform APIs rather than standalone .NET code. This module uses NinjaTrader 8.1.8.2 as the reference build. The focused records were retrieved from version-ambiguous documentation pages unless a page explicitly states a version, so verify signatures and generated-code behavior against the installed build before shipping. **Evidence:** record `nt-6c3df90838844e55`, canonical URL: https://developer.ninjatrader.com/docs/desktop/basic_programming_concepts; record `nt-011a0385ee2d7a6a`, canonical URL: https://developer.ninjatrader.com/docs/desktop/c_method_functions_reference.

## Types, state, and references

Prefer explicit types at NinjaScript boundaries: platform enums such as `State` and `Calculate`, platform series such as `ISeries<double>`, and ordinary C# primitives for local calculations. Keep references to platform-owned objects short-lived unless the API documents their lifetime. Do not infer that a property is safe to set in every state; configuration belongs in the state where the platform expects it. **Evidence:** record `nt-6c3df90838844e55`, canonical URL: https://developer.ninjatrader.com/docs/desktop/basic_programming_concepts; record `nt-b4a7af233189d711`, canonical URL: https://developer.ninjatrader.com/docs/desktop/iseriest.

## Collections and null-sensitive code

Use normal C# collection and control-flow practices, but avoid allocating or mutating shared state from a hot callback without a reason. Guard platform series access before indexing; an out-of-range or not-yet-built series is a data-readiness problem, not something to solve with a default value. Treat nullable references, unavailable bars, and missing provider data as explicit cases. **Evidence:** record `nt-04329004876c8e9f`, canonical URL: https://developer.ninjatrader.com/docs/desktop/currentbars; record `nt-37c50fd1f69a2263`, canonical URL: https://developer.ninjatrader.com/docs/desktop/currentbar.

## Supported example

This is a small C# pattern for guarding a one-bar lookback. It is **manually checked, not compiled** because no authorized NinjaTrader installation or compiler was available. It is **simulation-only** and places no orders.

```csharp
protected override void OnBarUpdate()
{
    if (CurrentBar < 1)
        return;

    double change = Close[0] - Close[1];
    Print(change);
}
```

**Evidence:** record `nt-38fad49cb296238f`, canonical URL: https://developer.ninjatrader.com/docs/desktop/onbarupdate; record `nt-37c50fd1f69a2263`, canonical URL: https://developer.ninjatrader.com/docs/desktop/currentbar.

## Uncovered and partial

The focused corpus does not provide local compiler or runtime evidence for language-version settings, nullable-reference configuration, async/threading safety, or the exact generated wrapper code emitted for indicators. Treat those areas as partial and test them in the target 8.1.8.2 installation. **Evidence:** record `nt-6c3df90838844e55`, canonical URL: https://developer.ninjatrader.com/docs/desktop/basic_programming_concepts.
