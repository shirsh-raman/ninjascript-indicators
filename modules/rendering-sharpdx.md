# Rendering And SharpDX

Use this module only for custom chart rendering with `OnRender()` and SharpDX. Keep calculations and market-data logic in normal script events, and treat rendering as presentation. Confirm the target object and NinjaTrader version before relying on a signature or lifecycle detail.

## Rendering Boundary

`OnRender()` is for custom drawing from indicators, drawing tools, or strategies. NinjaTrader documents that it uses SharpDX for Direct2D text and shapes, can be called in response to market-data updates or chart interaction, and is buffered for performance. It must not be used as historical Strategy Analyzer backtesting logic. **Evidence:** record `nt-7e4b62fcafcbe265`; canonical URL <https://ninjatrader.com/support/helpguides/nt8/onrender.htm>.

Precompute values in `OnBarUpdate()` or another appropriate event, then read stable values while rendering. The documented `OnRender()` guidance warns that `barsAgo` indexing is not guaranteed to be synchronized there; prefer absolute-index access such as `GetValueAt()` when reading series data. Call `base.OnRender()` when standard plots must also be rendered. **Evidence:** record `nt-7e4b62fcafcbe265`; canonical URL <https://ninjatrader.com/support/helpguides/nt8/onrender.htm>.

## Render-Target Resources

Each DirectX render target requires resources belonging to that target. NinjaTrader documents `OnRenderTargetChanged()` as the place to create or clean up device-dependent resources such as SharpDX brushes, because a chart can create and destroy render targets multiple times, including during resize and hit testing. Dispose the old resource before recreating it for the new non-null target. **Evidence:** record `nt-84af9bfb2fa6fcec`; canonical URL <https://ninjatrader.com/support/helpguides/nt8/onrendertargetchanged.htm>.

If a resource is used only inside one render pass, the documented alternative is to create and dispose it in `OnRender()` with a `using` scope. Resources that outlive the pass must have an explicit disposal path; the SharpDX reference warns that NinjaTrader is not guaranteed to dispose unmanaged objects for the script. **Evidence:** records `nt-84af9bfb2fa6fcec`, `nt-7e4b62fcafcbe265`, and `nt-272a26fbcd517aea`; canonical URLs <https://ninjatrader.com/support/helpguides/nt8/onrendertargetchanged.htm>, <https://ninjatrader.com/support/helpguides/nt8/onrender.htm>, <https://ninjatrader.com/support/helpguides/nt8/sharpdx_disposebase_dispose.htm>.

## Coordinate And API Discipline

SharpDX vectors represent chart-panel coordinates. For absolute device coordinates, the educational record says to use `ChartPanel` dimensions because `ChartScale` and `ChartControl` values are WPF units and can differ with display DPI. Use the documented SharpDX namespaces and members for the target build; do not assume arbitrary DirectX or SharpDX APIs are available in NinjaTrader.Custom. **Evidence:** record `nt-71e7eb9d0097809c`; canonical URL <https://ninjatrader.com/support/helpguides/nt8/using_sharpdx_for_custom_chart_rendering.htm>.

### Example: Target-Aware Brush

This is a manually checked, not compiled example. It illustrates ownership and target recreation only; it is not a complete indicator and makes no runtime claim.

```csharp
private SharpDX.Direct2D1.Brush dxBrush;

public override void OnRenderTargetChanged()
{
    dxBrush?.Dispose();
    dxBrush = null;

    if (RenderTarget != null)
        dxBrush = Brushes.Blue.ToDxBrush(RenderTarget);
}

protected override void OnRender(ChartControl chartControl, ChartScale chartScale)
{
    if (dxBrush == null)
        return;

    RenderTarget.FillRectangle(
        new SharpDX.RectangleF(ChartPanel.X, ChartPanel.Y, ChartPanel.W, ChartPanel.H),
        dxBrush);
}
```

The lifecycle pattern follows the normalized official example. The snippet was not compiled, and the exact brush conversion/import context must be checked against the target NinjaTrader build. **Evidence:** records `nt-84af9bfb2fa6fcec` and `nt-7e4b62fcafcbe265`; canonical URLs <https://ninjatrader.com/support/helpguides/nt8/onrendertargetchanged.htm>, <https://ninjatrader.com/support/helpguides/nt8/onrender.htm>.

## Evidence Gap

The rendering records describe render-target ownership and lifecycle, but do not establish a complete thread-safety contract or a universal API-availability matrix across NinjaTrader builds. Treat threading, resource lifetime, and exact signatures as requiring validation in an authorized target installation. The example in this module is not compiled or runtime-verified. **Evidence:** records `nt-84af9bfb2fa6fcec`, `nt-7e4b62fcafcbe265`, and `nt-272a26fbcd517aea`; canonical URLs <https://ninjatrader.com/support/helpguides/nt8/onrendertargetchanged.htm>, <https://ninjatrader.com/support/helpguides/nt8/onrender.htm>, <https://ninjatrader.com/support/helpguides/nt8/sharpdx_disposebase_dispose.htm>.
