# Troubleshooting

## The Skill Does Not Load

1. Install the complete `ninjascript-indicators` folder, not a selection of files.
2. Confirm `SKILL.md` is directly inside that folder.
3. Confirm `modules/` and `references/` remain in their original relative locations.
4. Restart or refresh the AI tool's skill discovery after copying the folder.
5. If the tool reports a broken reference, check package-relative links and avoid rewriting the skill root to a machine-specific path.

## The Answer Uses The Wrong API

Provide the exact NinjaTrader version, target script type, calculation mode, primary and added series, Tick Replay setting, and whether the issue is historical or realtime. Ask the skill to cite the relevant source-index record and identify version ambiguity. Do not assume a similarly named API has the same overload or callback timing.

## NinjaScript Does Not Compile

- Copy the complete compiler message, including the file and line number.
- Check namespaces, property types, series indexes, state usage, and generated-code boundaries.
- Verify that the referenced API exists in the installed platform version.
- Reduce the script to a minimal indicator and restore features one at a time.
- Use the NinjaScript editor and the target installation for the final check; the AI skill cannot compile the code here.

## Values Are Missing Or Misaligned

Check `CurrentBar`, `BarsInProgress`, `BarsArray`, `Closes`, `Times`, and the required bars-ago lookback for every series. Confirm that each added series is created in the appropriate lifecycle state and that the chart has enough history. Historical and realtime updates can follow different paths.

## Order Flow Data Is Unavailable

Confirm the selected bar type, required Order Flow + entitlement, provider support, and the data actually supplied by the connection. A correct API call cannot create data that the provider or subscription does not provide.

## Rendering Fails

Check render-target resource ownership and recreation, null or disposed resources, coordinate bounds, and the lifecycle of `OnRender`. Test with rendering disabled to separate calculation errors from drawing errors. Verify against the installed build because runtime rendering behavior is not established by this bundle.

## Live Use Is Requested

Pause and separate the request into code generation, simulation verification, and deployment. Keep indicator examples non-trading by default. Use playback or simulation first, review account and risk settings independently, and require explicit operational controls before considering live deployment.

## Source Pages Differ From The Bundle

The source index is a public locator, not a frozen copy of source content. Pages can move, change, require access, or omit version information. Record the URL and platform version used for the decision, and label any unverified conclusion as uncertain.

## Skill Installation Versus NinjaScript Deployment

Installing this bundle only teaches an AI tool how to assist with NinjaScript. Deploying NinjaScript means importing or compiling code inside NinjaTrader, checking dependencies and entitlements, testing on the intended configuration, and managing backups and distribution. These are separate workflows.
