# Drawing And Alerts

Use this module for chart annotations and NinjaScript alerts. The focused records are official but generally version-ambiguous; the corpus reference build is NinjaTrader 8.1.8.2. [Record `nt-fe13d9205df86b5a`, canonical URL](https://docs.ninjatrader.com/ninjascript/drawing); [Record `nt-a86297e2478571e7`, canonical URL](https://docs.ninjatrader.com/ninjascript/alert)

## Draw Methods

NinjaScript can draw shapes, lines, text, and colors on price and indicator panels from indicators and strategies. Select a documented `Draw.*` method and verify its return type and overload rather than generalizing from one drawing method. [Record `nt-fe13d9205df86b5a`, canonical URL](https://docs.ninjatrader.com/ninjascript/drawing)

For custom drawing tools, the focused records describe chart anchors and shared `IDrawingTool` properties, including panel placement, user interaction, global drawing, and alert support. These are drawing-tool concerns, not a substitute for the simpler `Draw.*` calls used by an indicator. [Record `nt-167680018232ab10`, canonical URL](https://ninjatrader.com/support/helpguides/nt8/idrawingtool.htm); [Record `nt-130ed55f4669ff0e`, canonical URL](https://docs.ninjatrader.com/ninjascript/drawing_tools)

## Alert Runtime Gate

`Alert()` generates a visual/audible alert in the Alerts Log. The focused record states that it can be called only after `State.Realtime`; calls in other states are silently ignored. It documents a unique `id`, priority, message, `.wav` path, rearm seconds, and alert-row brushes as parameters. [Record `nt-a86297e2478571e7`, canonical URL](https://docs.ninjatrader.com/ninjascript/alert)

The same `id` is used for rearm timing: an alert called within the documented rearm window is ignored. Use `RearmAlert()` only for an alert created through the corresponding alert mechanism, and verify add-on-specific behavior separately. [Record `nt-a86297e2478571e7`, canonical URL](https://docs.ninjatrader.com/ninjascript/alert); [Record `nt-917d150c65274e54`, canonical URL](https://docs.ninjatrader.com/ninjascript/alert_rearmalert)

## Add-On Boundary

For custom objects outside ordinary NinjaScript scope, the focused alert/debug record points to `AlertCallback()` and `RearmAlert()` rather than treating `Alert()` as interchangeable across scopes. Confirm the object type before selecting the API. [Record `nt-2795cbee637ce978`, canonical URL](https://docs.ninjatrader.com/ninjascript/alert_and_debug_concepts)

## Example Status

Any drawing or alert snippet is **manually checked, not compiled**. No runtime test establishes chart rendering, sound-file availability, alert timing, or behavior across historical/realtime transitions. The external source index's validation report is unavailable locally; canonical NinjaTrader URLs are authoritative.
