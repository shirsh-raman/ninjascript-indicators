# NinjaScript Indicators

Portable AI skill bundle for creating, explaining, and troubleshooting NinjaTrader 8 NinjaScript indicators.

## Install The Skill

Copy the whole `ninjascript-indicators` folder into the skills directory used by your AI tool. Keep `SKILL.md` at the folder root and preserve the `modules/` and `references/` directories. The folder is the installable unit; do not copy only individual Markdown files.

This installs an AI instruction bundle. It does not install NinjaTrader, NinjaScript, a compiler, an indicator, a strategy, a data feed, or a trading license.

### Clone From GitHub

Replace `<owner>/<repository>` with the repository path. For this private repository, use an authenticated HTTPS clone:

```bash
git clone https://github.com/<owner>/<repository>.git
```

Authenticate with GitHub before cloning. Do not put passwords, access tokens, or other credentials in the clone URL. If you do not have access, ask a repository administrator to grant it through GitHub rather than copying credentials from another user.

### Manual Installation

If cloning is not available, download an authorized repository archive or obtain the folder through an approved private-repository channel. Copy the complete `ninjascript-indicators` directory into the skills directory used by your AI tool. Verify that `SKILL.md`, `modules/`, and `references/` are present at the installed folder root.

## Capabilities

- Route indicator questions to focused guidance for lifecycle, data series, plots, sessions, drawing, alerts, order flow, rendering, licensing, and debugging.
- Produce or explain NinjaScript and C# patterns for NinjaTrader 8.
- Identify assumptions involving calculation mode, historical versus realtime processing, Tick Replay, added series, provider data, and platform version.
- Keep indicator examples display-, logging-, or simulation-oriented by default rather than submitting live orders.
- Report evidence limits instead of presenting unsupported runtime behavior as fact.

The skill is not an exhaustive NinjaTrader reference and does not replace the platform documentation or qualified technical advice.

## Invocation Examples

Ask for the task directly, for example:

```text
Create a NinjaTrader 8 indicator with two plots and explain its state transitions.
```

```text
Why does my multi-series NinjaScript calculate on the wrong BarsInProgress value?
```

```text
Help troubleshoot an OnRender SharpDX error. My installed NinjaTrader version is 8.1.8.2.
```

Include the installed NinjaTrader version, target script type, calculation mode, data series, historical/realtime expectations, and provider or licensing assumptions when known.

## NinjaTrader Prerequisites

For generated or deployed code, provide:

- An authorized NinjaTrader Desktop installation and the target platform version.
- Access to the NinjaScript editor and a supported C# development/runtime environment as required by that installation.
- The chart, instrument, Trading Hours template, bar type, and data series configuration used for testing.
- Required market-data, Order Flow +, provider, or other feature entitlements.
- A backup and a simulation or playback workflow before any live use.

The AI skill itself has none of these prerequisites because it does not execute NinjaScript.

## Sources And External Corpus

`references/source-index.jsonl` is a portable index of public source records. It contains record IDs, titles, focused tracks, reference version labels, classifications, and canonical URLs. It is not a bundled copy of the external corpus, and it does not guarantee that a linked page remains available or unchanged.

The focused reference build is NinjaTrader 8.1.8.2, while many source records are version-ambiguous. The skill should identify the relevant record and URL, state uncertainty, and ask for confirmation when an exact overload, callback timing, provider behavior, or runtime detail matters. External retrieval, if available to the AI tool, is for checking current public documentation; it does not turn an unverified claim into a local runtime result.

See [`references/corpus-boundaries.md`](references/corpus-boundaries.md) for provenance, coverage, and known gaps.

## Limitations

- No NinjaTrader installation, compiler, provider session, or authorized runtime harness is bundled.
- The examples are instructional Markdown, not importable NinjaScript files.
- Examples have not been compiled or run against a target installation in this bundle.
- Provider availability, licensing, generated code, platform updates, and runtime behavior can differ from the focused records.
- Strategies, orders, accounts, ATM, custom bar types, chart styles, and Add-Ons are adjacent or partial topics rather than complete coverage.

## Safety

Review generated code before use. Start with simulation, playback, or a test instrument. Confirm data entitlements and session settings. Do not infer live-order safety from an indicator example, and do not connect generated strategies to live accounts without independent testing and operational controls.

## Example Verification

The files in `examples/` are manually checked for clarity and package-local links. They are not compiled or runtime-verified. Treat every code fragment as a starting point and verify it in the exact NinjaTrader build, chart configuration, and provider environment where it will run.

Browse [`examples/README.md`](examples/README.md) for the example map and verification status.

## Troubleshooting

Start with [`TROUBLESHOOTING.md`](TROUBLESHOOTING.md). It separates skill installation problems from NinjaScript compilation, configuration, provider, and runtime problems.

## Contributions And Issues

Use GitHub Issues for reproducible documentation errors, missing guidance, and installation problems. Search existing issues first, include the bundle version and relevant NinjaTrader version when known, and remove credentials or proprietary material. See [`CONTRIBUTING.md`](CONTRIBUTING.md) for change and pull-request guidance. Report suspected security vulnerabilities privately as described in [`SECURITY.md`](SECURITY.md).

## Versioning

The bundle version is recorded in [`VERSION`](VERSION), and release notes are in [`CHANGELOG.md`](CHANGELOG.md). Version changes describe this AI skill bundle and its documentation. They do not identify or promise a NinjaTrader product release.

### Release Note: 1.0.0

The 1.0.0 release provides the initial portable indicator-focused skill bundle, including installation guidance, evidence and provenance boundaries, safety notes, troubleshooting documentation, and focused NinjaScript examples. See [`CHANGELOG.md`](CHANGELOG.md) for the full release history.

## License

Original skill-authored material is available under the MIT License. See [`LICENSE`](LICENSE) and [`NOTICE.md`](NOTICE.md). NinjaTrader and NinjaScript are third-party names and are not claimed by this project.
