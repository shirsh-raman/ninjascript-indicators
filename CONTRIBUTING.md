# Contributing

Contributions to the NinjaScript Indicators skill bundle are welcome, especially corrections that improve accuracy, provenance, clarity, or installation guidance.

## Before Opening An Issue

- Search existing issues to avoid duplicates.
- Use a clear title and describe the expected and observed behavior.
- Include the relevant bundle version, file or section, and exact NinjaTrader version when applicable.
- Remove credentials, account information, proprietary code, and other sensitive data.
- Use a private report instead of a public issue for security concerns. See [`SECURITY.md`](SECURITY.md).

## Changes

- Keep changes focused and preserve the existing evidence-bounded style.
- Cite or link authoritative sources when correcting technical claims.
- Mark platform-version assumptions and runtime behavior clearly.
- Keep examples simulation-only and do not add live-order instructions.
- Update documentation links and version-related notes when they are affected.

## Validation

Run the repository validation script before opening a pull request:

```text
python scripts/validate_bundle.py .
```

The examples are Markdown guidance and are not compiled or runtime-verified by this repository. Do not describe them as tested against NinjaTrader unless the target installation and configuration are identified.

## Pull Requests

Open a pull request with a concise summary, the reason for the change, and validation results. Keep unrelated files out of the change. Maintainers may request revisions to improve source support, scope, or safety wording.
