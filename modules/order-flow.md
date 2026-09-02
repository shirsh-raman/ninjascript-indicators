# Order Flow

Use this module when a NinjaScript request needs Order Flow +, volumetric bars, bid/ask classification, delta, or per-price volume. Confirm the NinjaTrader version, instrument type, provider, historical/realtime requirements, and whether the request is for an indicator, strategy, or chart display before choosing an implementation.

## Capability And Prerequisites

Order Flow Volumetric bars classify aggressive buying and selling at price levels and expose bar statistics to custom NinjaScript. They are analysis data, not a trading signal by themselves. Bid/ask delta requires historical bid/ask tick data from the connected provider; when only historical last-tick data is available, the documented alternative is `UpDownTick`. Volumetric bars are not supported for Forex spot data. **Evidence:** record `nt-3cd163c723cc0110`; canonical URL <https://ninjatrader.com/support/helpguides/nt8/order_flow_volumetric_bars.htm>.

Order Flow + availability and data coverage are separate checks. The focused record describes Order Flow + as included for lifetime license users, while provider records show that historical tick, bid/ask, instrument, and Tick Replay support varies by provider and may be subscription- or account-dependent. Do not promise that a named provider supplies a requested field without checking the provider table for the exact instrument and data mode. **Evidence:** records `nt-6c11605f8cbe9427` and `nt-5e4a389414718abc`; canonical URLs <https://ninjatrader.com/support/helpguides/nt8/order_flow_plus.htm>, <https://ninjatrader.com/support/helpguides/nt8/data_by_provider.htm>.

## NinjaScript Access

For a volumetric series, use the documented `VolumetricBarsType` access path and check for null before reading values. The exposed values include total bar delta, cumulative delta, bid/ask volume by price, delta by price, total buying/selling volume, trade count, and maximum volume. Cumulative delta resets at the session break. For an added series, the source example uses `BarsArray[index].BarsType`; use the correct series index and guard the required bars before indexing. **Evidence:** record `nt-c690491cb1323896`; canonical URL <https://docs.ninjatrader.com/ninjascript/order_flow_volumetric_bars>.

### Example: Read A Volumetric Bar

This is a manually checked, not compiled example. It is intentionally read-only and does not submit, modify, or simulate orders.

```csharp
protected override void OnBarUpdate()
{
    if (Bars == null || CurrentBar < 0)
        return;

    var barsType = Bars.BarsSeries.BarsType as
        NinjaTrader.NinjaScript.BarsTypes.VolumetricBarsType;
    if (barsType == null)
        return;

    var volume = barsType.Volumes[CurrentBar];
    long delta = volume.BarDelta;
    long buy = volume.TotalBuyingVolume;
    long sell = volume.TotalSellingVolume;
    Print($"delta={delta}, buy={buy}, sell={sell}");
}
```

The access pattern and property meanings are adapted from the normalized official example; the snippet was not compiled against an authorized NinjaTrader installation. **Evidence:** record `nt-c690491cb1323896`; canonical URL <https://docs.ninjatrader.com/ninjascript/order_flow_volumetric_bars>.

## Conservative Failure Handling

Treat missing bid/ask history, unsupported Forex spot data, a null bars type, and incomplete series data as capability or data-state conditions. Report the condition and the selected fallback; do not silently label `UpDownTick` as true bid/ask aggression. Provider tables are subject to change, so provider-specific conclusions need a fresh check when the connection or instrument changes. **Evidence:** records `nt-3cd163c723cc0110` and `nt-5e4a389414718abc`; canonical URLs <https://ninjatrader.com/support/helpguides/nt8/order_flow_volumetric_bars.htm>, <https://ninjatrader.com/support/helpguides/nt8/data_by_provider.htm>.

## Evidence Gap

The focused corpus does not provide a complete runtime matrix for every provider, account entitlement, instrument, or current NinjaTrader build. The provider record says its limitations are subject to change. The example in this module is not compiled or runtime-verified. **Evidence:** record `nt-5e4a389414718abc`; canonical URL <https://ninjatrader.com/support/helpguides/nt8/data_by_provider.htm>.
