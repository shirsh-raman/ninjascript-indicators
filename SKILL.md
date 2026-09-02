---
name: ninjascript-indicators
description: Provisional indicator-focused NinjaTrader 8 NinjaScript documentation skill for indicator coding, lifecycle, data series, plots, sessions, built-in indicators, drawing, alerts, order flow, provider/licensing constraints, rendering, and debugging, with partial adjacent API coverage. Use when a user asks to create, modify, explain, or troubleshoot NinjaScript, especially indicators or chart studies.
---

# NinjaScript Indicators

This is a routed, evidence-bounded skill for NinjaTrader 8. The focused corpus reference build is **8.1.8.2**. Most official records are version-ambiguous, so confirm the user's installed platform version before relying on exact overloads, callback timing, generated code, provider behavior, or runtime details.

See [`README.md`](README.md) for orientation and [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md) for common issues.

## Operating Rules

1. Resolve the request before coding. Ask for the platform version, target script type, calculation mode, primary and added data series, historical/realtime behavior, Tick Replay, rendering needs, provider/licensing assumptions, and safety constraints when they are unclear.
2. Route to the smallest relevant module(s) below. Read the module before making substantive claims or code.
3. Cite claims with record IDs and canonical URLs from `references/source-index.jsonl`. External corpus content is not included.
4. Treat examples as manually checked and not compiled unless the user supplies a verified NinjaTrader build and reports successful compilation. Do not claim runtime behavior without an observed target-installation run.
5. Keep trading examples simulation-only by default. Indicator examples should calculate, display, log, or draw; they should not submit live orders.
6. State partial or uncovered evidence plainly instead of filling gaps from assumptions. The focused corpus is practical, not exhaustive.

## Routing Table

| Request area | Read |
|---|---|
| C# syntax, NinjaScript object model, methods | `modules/csharp-fundamentals.md` |
| State transitions, `OnBarUpdate`, calculation, Tick Replay | `modules/indicator-lifecycle.md` |
| Added series, `BarsInProgress`, synchronization | `modules/data-series.md` |
| Trading Hours, sessions, `SessionIterator` | `modules/sessions-trading-hours.md` |
| Plots, `Values`, `Series<T>`, brushes, user properties | `modules/plots-properties.md` |
| Persistence attributes, serialization, generated wrappers/cache | `modules/serialization-generated-code.md` |
| SMA, EMA, RSI, MACD, Bollinger and system indicator methods | `modules/built-in-indicators.md` |
| `Draw.*`, drawing tools, alerts, debug/share APIs | `modules/drawing-alerts.md` |
| Volumetric bars, delta, Order Flow + | `modules/order-flow.md` |
| Provider data availability, entitlements, licensing | `modules/provider-licensing.md` |
| `OnRender`, SharpDX, render-target resources | `modules/rendering-sharpdx.md` |
| Compile errors, diagnostics, test matrix, deployment limits | `modules/debugging-testing-deployment.md` |
| Strategies/orders/accounts/ATM/Bars Types/chart styles and other adjacent APIs | `modules/supplementary-apis.md` |

## Stage 1 Coverage Map

| Taxonomy area | Destination | Status |
|---|---|---|
| C# fundamentals and NinjaScript object model | `csharp-fundamentals.md` | covered |
| Indicator lifecycle and state transitions | `indicator-lifecycle.md` | covered |
| Bar processing, calculation, historical/realtime, Tick Replay | `indicator-lifecycle.md` | covered, runtime behavior partial |
| Data series and multi-series synchronization | `data-series.md` | covered |
| Sessions and Trading Hours | `sessions-trading-hours.md` | covered, edge cases partial |
| Plots, values, series, brushes, properties | `plots-properties.md` | covered |
| Serialization and generated code | `serialization-generated-code.md` | serialization partial; generated-code behavior uncovered |
| Built-in indicators | `built-in-indicators.md` | covered for the documented catalog |
| Drawing and alerts | `drawing-alerts.md` | covered |
| Order flow and volumetric prerequisites | `order-flow.md` | partial |
| Provider and licensing | `provider-licensing.md` | partial and provider-dependent |
| Rendering and SharpDX | `rendering-sharpdx.md` | covered in documentation; runtime partial |
| Debugging and compile errors | `debugging-testing-deployment.md` | partial |
| Testing, deployment, authorized runtime verification | `debugging-testing-deployment.md` | uncovered in focused evidence |
| Strategies, orders, accounts, ATM, Bars Types, chart styles | `supplementary-apis.md` | supplementary/partial |
| Add-Ons and complete deployment workflow | `supplementary-apis.md` | uncovered where not directly evidenced |

## Evidence And Verification

Read `references/corpus-boundaries.md` for provenance, version, and verification constraints. No NinjaTrader installation was available for compilation or runtime checks. Do not describe generated artifacts as corpus-supported unless the relevant module cites a focused record; generated artifacts without direct evidence must be labeled unsupported.
