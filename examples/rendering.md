# Rendering

Use this prompt for custom chart rendering:

```text
Help design a NinjaTrader 8 indicator that draws a non-trading annotation in OnRender using SharpDX. Explain render-target resource creation, disposal, recreation, null checks, and how to test calculation separately from rendering.
```

Review points:

- Keep calculation and rendering responsibilities distinct.
- Create render-target-dependent resources only when the target is valid.
- Dispose or recreate resources when the render target changes.
- Guard chart coordinates and disposed or unavailable objects.
- Test with rendering disabled to isolate lifecycle and calculation failures.

Verification status: manually reviewed Markdown; not compiled or runtime-tested.
