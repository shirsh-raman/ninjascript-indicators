# Built-In Indicators

Use the official system-indicator catalog for built-in indicator definitions, syntax, parameter descriptions, and examples. The focused catalog explicitly includes `SMA`, `EMA`, `RSI`, `MACD`, and Bollinger Bands; this module does not infer undocumented overloads or output members for the other indicators. [Record `nt-24d4d9e42b35cb28`, canonical URL](https://docs.ninjatrader.com/ninjascript/system_indicator_methods)

## Selection And Inputs

Treat the input as a documented `ISeries`/series-compatible source and verify the selected indicator's own syntax before composing calls. The focused `Series<T>` record says series objects can be used as input data for indicator methods. [Record `nt-77c7861f815d17fc`, canonical URL](https://docs.ninjatrader.com/ninjascript/seriest); [Record `nt-24d4d9e42b35cb28`, canonical URL](https://docs.ninjatrader.com/ninjascript/system_indicator_methods)

## Bollinger Bands

The focused Bollinger record documents the three-band description and the syntax `Bollinger(double numStdDev, int period)` plus the `ISeries` overload. It documents `.Upper[barsAgo]` and `.Lower[barsAgo]` accessors; use those members only where the selected API record supports them. [Record `nt-2264c9685815106f`, canonical URL](https://docs.ninjatrader.com/ninjascript/bollinger_bands)

## Calculation And Guards

Before indexing a built-in indicator or its input, establish the required bars-ago history for the target series. The focused corpus guide uses a `CurrentBar` guard in its manually checked indicator template, but no compile or runtime result is available. The external source index's guide and validation report are unavailable locally; canonical NinjaTrader URLs are authoritative.

## Example Status

Examples copied or adapted from these records are **manually checked, not compiled**. Confirm namespaces, overloads, output members, and behavior against the installed NinjaTrader build before shipping. The external source index's validation report is unavailable locally; canonical NinjaTrader URLs are authoritative.
