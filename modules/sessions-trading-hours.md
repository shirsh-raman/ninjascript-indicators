# Sessions and Trading Hours

## Reference build and ambiguity

This module uses NinjaTrader 8.1.8.2 as its reference build. Session and Trading Hours records are official focused snapshots, but most pages do not expose a reliable version date. Treat behavior around exchange time zones, holidays, and session boundaries as version-ambiguous until checked in the target installation. **Evidence:** record `nt-126e1507e527b83e`, canonical URL: https://developer.ninjatrader.com/docs/desktop/sessioniterator; record `nt-03280c1db187bb8b`, canonical URL: https://developer.ninjatrader.com/docs/desktop/tradinghours.

## Trading Hours define the session calendar

Trading Hours templates determine which trading intervals, breaks, holidays, and partial holidays are represented by a bars series. Do not replace session semantics with a wall-clock comparison unless the requirement is explicitly about local clock time. The instrument and template time-zone rules matter. **Evidence:** record `nt-03280c1db187bb8b`, canonical URL: https://developer.ninjatrader.com/docs/desktop/tradinghours; record `nt-5ee21d77eda4f225`, canonical URL: https://developer.ninjatrader.com/docs/desktop/tradinghours_sessions.

## SessionIterator use

Use `SessionIterator` when logic needs session starts or ends, rather than inferring boundaries solely from bar dates. Initialize it only when the relevant bars object is available, advance it according to the API contract, and handle holidays and shortened sessions as normal calendar cases. Keep a separate iterator for each bars context that needs independent session tracking. **Evidence:** record `nt-126e1507e527b83e`, canonical URL: https://developer.ninjatrader.com/docs/desktop/sessioniterator; record `nt-18fc798445bce6ab`, canonical URL: https://developer.ninjatrader.com/docs/desktop/barstype_sessioniterator.

## Session-aware bar logic

For a session reset, make the reset condition explicit and ensure it runs once per intended session. In multi-series scripts, identify which `BarsInProgress` context owns the session state. A session boundary on a secondary series is not automatically a boundary on the primary series. **Evidence:** record `nt-be831d998c23355b`, canonical URL: https://developer.ninjatrader.com/docs/desktop/barsinprogress; record `nt-126e1507e527b83e`, canonical URL: https://developer.ninjatrader.com/docs/desktop/sessioniterator; record `nt-5ee21d77eda4f225`, canonical URL: https://developer.ninjatrader.com/docs/desktop/tradinghours_sessions.

## Example boundary

No executable C# example is included here. The normalized SessionIterator record confirms the API topic but does not expose enough method-level content to support a practical, manually checked snippet. Do not invent iterator member names from memory; obtain the exact signature from the target 8.1.8.2 editor or a fuller external record before writing code. **Evidence:** record `nt-126e1507e527b83e`, canonical URL: https://developer.ninjatrader.com/docs/desktop/sessioniterator; record `nt-18fc798445bce6ab`, canonical URL: https://developer.ninjatrader.com/docs/desktop/barstype_sessioniterator.

## Uncovered and partial

The focused corpus does not locally verify daylight-saving transitions, custom holiday edits, overnight session date conventions, or exact iterator advancement semantics across every bars type. These are partial and should be tested with representative historical data in the target installation. **Evidence:** record `nt-03280c1db187bb8b`, canonical URL: https://developer.ninjatrader.com/docs/desktop/tradinghours; record `nt-126e1507e527b83e`, canonical URL: https://developer.ninjatrader.com/docs/desktop/sessioniterator.
