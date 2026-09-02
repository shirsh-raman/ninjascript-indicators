# Plots And Properties

Use this module for indicator outputs, plot appearance, user-facing parameters, and bar-synchronized custom series. The focused records use NinjaTrader 8.1.8.2 as the reference build, but these pages are classified `ambiguous` because the pages do not expose reliable version dates. Confirm the target installation before relying on version-sensitive behavior. [Record `nt-07aaaaf6aae0725e`, canonical URL](https://docs.ninjatrader.com/ninjascript/addplot); [Record `nt-11bf5a7a3f35f000`, canonical URL](https://docs.ninjatrader.com/ninjascript/plots)

## AddPlot And Values

`AddPlot()` adds a plot and creates an associated series in `Values`. Call it from `State.SetDefaults` when the plot must be available in the indicator property grid. Dynamic plots added in `State.Configure` are documented as a special case: their plot configuration is not exposed through that UI. [Record `nt-07aaaaf6aae0725e`, canonical URL](https://docs.ninjatrader.com/ninjascript/addplot)

`Plots[index]` addresses plot visualization settings, while `Values[index]` addresses the underlying calculated series. The focused `Values` example reads a secondary value with bars-ago indexing and writes the primary `Value[0]`. [Record `nt-11bf5a7a3f35f000`, canonical URL](https://docs.ninjatrader.com/ninjascript/plots); [Record `nt-8b9b3c5a7580ffdd`, canonical URL](https://docs.ninjatrader.com/ninjascript/values)

## Plot Appearance

The documented plot object exposes visualization characteristics. The focused example changes `Plots[0].Brush` and `Plots[0].Width`; use `PlotBrushes` when only selected historical-bar segments need different colors. [Record `nt-11bf5a7a3f35f000`, canonical URL](https://docs.ninjatrader.com/ninjascript/plots); [Record `nt-07aaaaf6aae0725e`, canonical URL](https://docs.ninjatrader.com/ninjascript/addplot)

## Series And Lookback

`Series<T>` is a generic, bar-length data structure and can be used as input data for indicator methods. The focused record says the default storage limit is 256 values from the current bar and points to `MaximumBarsLookBack` when older values are required. Do not generalize that limit to every series-like object without checking the relevant API. [Record `nt-77c7861f815d17fc`, canonical URL](https://docs.ninjatrader.com/ninjascript/seriest)

## User Properties

Use `[NinjaScriptProperty]` for a property that should become a NinjaScript object constructor parameter, be passed from another NinjaScript object, or participate in Strategy Analyzer optimization. The record warns that such properties must be XML-serializable; for non-serializable user inputs, expose a simple serializable type instead. [Record `nt-c725ce0ac4c23761`, canonical URL](https://docs.ninjatrader.com/ninjascriptpropertyattribute)

Use `[Display(Name=..., Description=..., GroupName=..., Order=...)]` for property-grid presentation. `Name` must be unique within the object. Use `[Browsable(false)]` to hide a public property from the property grid, and `[Range(...)]` for bounds checked at `State.Configure`. The range record distinguishes UI clamping from an exception for an invalid hosted NinjaScript parameter. [Record `nt-25437896028c4faa`, canonical URL](https://docs.ninjatrader.com/ninjascript/displayattribute); [Record `nt-130635ac4b46c23d`, canonical URL](https://docs.ninjatrader.com/ninjascript/browsableattribute); [Record `nt-9d1ac2bd715947b0`, canonical URL](https://docs.ninjatrader.com/ninjascript/rangeattribute)

## Example Status

Any code assembled from these records is **manually checked, not compiled**. No authorized NinjaTrader installation was available for compile or runtime verification. The external source index's validation report is unavailable locally; canonical NinjaTrader URLs are authoritative.
