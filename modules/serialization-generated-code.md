# Serialization And Generated Code

This module covers only serialization behavior supported by focused records. The external source index's validation report identifies generated-code behavior as a partial track; do not invent or imply the contents, regeneration triggers, cache keys, or editability of NinjaTrader-generated code. The external source index is unavailable locally; canonical NinjaTrader URLs are authoritative.

## XML Persistence

The documented default attempts to serialize public properties when NinjaScript objects are saved to a workspace or template. `[XmlIgnore]` excludes a property from those XML serialization routines, which is useful for values that cannot be serialized or should not be persisted. [Record `nt-230e329a0b9a28a3`, canonical URL](https://docs.ninjatrader.com/ninjascript/xmlignoreattribute)

The `XmlIgnoreAttribute` page is specifically an explanation of NinjaTrader conventions around a general .NET attribute and warns that other .NET methods or properties are not guaranteed to work with NinjaTrader serialization. Treat the cited behavior as scoped to the documented convention, not as a complete serializer specification. [Record `nt-230e329a0b9a28a3`, canonical URL](https://docs.ninjatrader.com/ninjascript/xmlignoreattribute)

## NinjaScript Properties

`[NinjaScriptProperty]` marks a property for inclusion as a NinjaScript object constructor parameter and can make it available for Strategy Analyzer optimization. The same record warns that marked properties must be XML-serializable; use a simple serializable backing input when the desired object type cannot be persisted. [Record `nt-c725ce0ac4c23761`, canonical URL](https://docs.ninjatrader.com/ninjascriptpropertyattribute)

## Generated-Code Boundary

No focused record documents the generated wrapper/cache region, its regeneration lifecycle, safe customization boundary, or exact relationship between generated code and serialized parameters. These are evidence gaps. Keep generated sections untouched unless the target installation and an applicable official record establish the behavior; prefer editing the user-authored NinjaScript region. The external source index's validation and unresolved-item reports are unavailable locally; canonical NinjaTrader URLs are authoritative.

## Example Status

The following minimal pattern is **manually checked, not compiled** and demonstrates only the documented exclusion attribute:

```csharp
[XmlIgnore]
public Brush MyBrush { get; set; }
```

It does not establish that every `Brush` configuration, custom converter, generated wrapper, or workspace round trip will behave identically. [Record `nt-230e329a0b9a28a3`, canonical URL](https://docs.ninjatrader.com/ninjascript/xmlignoreattribute)
