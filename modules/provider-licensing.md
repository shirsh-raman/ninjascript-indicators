# Provider And Licensing

Use this module when a NinjaScript request depends on market-data connectivity, historical bid/ask or Tick Replay, Order Flow +, or distribution licensing. Separate three questions: what the script needs, what the provider supplies for the exact instrument and period, and what the user's account or product entitlement permits.

## Provider Data Gate

NinjaTrader states that it is not a market-data provider and that historical data comes from connectivity providers. The provider table distinguishes real-time data, historical tick data, historical bid/ask tick data, Tick Replay, supported instruments, and other fields. Check those columns directly instead of inferring support from a provider name. **Evidence:** record `nt-5e4a389414718abc`; canonical URL <https://ninjatrader.com/support/helpguides/nt8/data_by_provider.htm>.

For bid/ask volumetric classification, require historical bid/ask tick access from the provider. If the provider supplies only historical last ticks, the documented fallback is `UpDownTick`; it is a different classification method. Tick Replay access also depends on provider data support and the configured connection. **Evidence:** records `nt-3cd163c723cc0110` and `nt-5e4a389414718abc`; canonical URLs <https://ninjatrader.com/support/helpguides/nt8/order_flow_volumetric_bars.htm>, <https://ninjatrader.com/support/helpguides/nt8/data_by_provider.htm>.

When a broker connection lacks historical data, the Help Guide describes using another connection such as Kinetick simultaneously for historical data. Treat this as a configuration option, not a guarantee: verify the connection setup, subscription, instrument mapping, and resulting fields before relying on the data. **Evidence:** record `nt-5e4a389414718abc`; canonical URL <https://ninjatrader.com/support/helpguides/nt8/data_by_provider.htm>.

## Order Flow And Product Entitlement

The focused Order Flow + record says the studies are included for all NinjaTrader lifetime license users. That statement does not establish entitlement for every license type, connection, instrument, or historical field. Present it as a documented product statement and still check the user's current license and provider data coverage. **Evidence:** record `nt-6c11605f8cbe9427`; canonical URL <https://ninjatrader.com/support/helpguides/nt8/order_flow_plus.htm>.

## Vendor Licensing

For a third-party vendor product, NinjaTrader documents a vendor license management service for qualified developers. The record says approval supplies a Vendor ID and a Vendor Licensing Help Guide; it also describes machine-ID/prefix licensing, expiration, trials, and an AddOn for license management. Do not invent approval criteria, API names, or entitlement behavior beyond the supplied vendor documentation. **Evidence:** record `nt-0ea59b1bb7bac6e0`; canonical URL <https://docs.ninjatrader.com/ninjascript/licensing_user_authentication>.

The newer user-based licensing record describes tying a commercial product license to a user's NinjaTrader account rather than a single desktop installation. Select the licensing model from the vendor's approved/current documentation; do not assume machine-ID licensing and user-based licensing are interchangeable. **Evidence:** record `nt-9752bd9d24177504`; canonical URL <https://docs.ninjatrader.com/ninjascript/user_based_licensing>.

### Example: Prerequisite Checklist

This is a manually checked, not compiled checklist example. It is not a licensing bypass and does not make network or account calls.

```text
1. Record NinjaTrader version and script type.
2. Record provider, connection, instrument, and trading-hours template.
3. Identify required fields: real-time, historical tick, bid/ask tick, or Tick Replay.
4. Check the official provider table for that exact requirement.
5. Check the user's product/license entitlement separately.
6. If distributing a product, confirm the approved vendor licensing model and Vendor ID status.
7. State any unsupported or unverified condition before generating code.
```

The checklist is a workflow synthesis, not a claim that any item is automatically verified by NinjaScript. **Evidence:** records `nt-5e4a389414718abc`, `nt-6c11605f8cbe9427`, and `nt-0ea59b1bb7bac6e0`; canonical URLs <https://ninjatrader.com/support/helpguides/nt8/data_by_provider.htm>, <https://ninjatrader.com/support/helpguides/nt8/order_flow_plus.htm>, <https://docs.ninjatrader.com/ninjascript/licensing_user_authentication>.

## Evidence Gap

Provider availability, subscriptions, account entitlements, and licensing workflows can change. The focused provider record says its limitations are subject to change, and the licensing record limits the vendor service to qualified developers and an approval process. The focused corpus does not establish a universal provider/license prerequisite or runtime method for checking entitlement. The example in this module is not compiled or runtime-verified. **Evidence:** records `nt-5e4a389414718abc` and `nt-0ea59b1bb7bac6e0`; canonical URLs <https://ninjatrader.com/support/helpguides/nt8/data_by_provider.htm>, <https://docs.ninjatrader.com/ninjascript/licensing_user_authentication>.
