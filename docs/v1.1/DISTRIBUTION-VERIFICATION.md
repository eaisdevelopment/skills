# Linux/macOS Distribution Verification

## Scope and result

2026-10-12: **PASS** for clean portable packaging, repository checks, strict Claude validation, isolated Claude user installation across two projects, and Codex read-only discovery on macOS. Linux-host execution, actual Codex installation, and model invocation remain **NOT VERIFIED**. Windows is out of scope. No GitHub publication or real user installation/configuration change occurred.

The canonical skill remains five Markdown files, 231 lines. Distribution adds four native JSON templates and a small Make/tar build recipe, not an installer/runtime. Generated copies exist only in ignored `build/` artifacts and temporary test workspaces.

## Grounding and requirements

Read the repository instructions, full intent/specification/plan, skill and relevant references, existing tests/docs/license, and actual installed CLI help. Focused vault retrieval covered configuration automation, reproducibility, developer experience, and verifiable acceptance; useful existing concept readings informed a standard build and explicit evidence rather than another framework. Runtime credentials are `N/A`: these local checks install no integration and call no model/provider.

Metadata and discovery conventions were checked against [OpenAI packaging](https://developers.openai.com/plugins/build/plugins), [Codex CLI](https://learn.chatgpt.com/docs/cli/reference), [Claude manifests](https://code.claude.com/docs/en/plugins/manifest-reference), [marketplaces](https://code.claude.com/docs/en/plugin-marketplaces), and [environment isolation](https://code.claude.com/docs/en/env-vars). Installed clients: Codex CLI 0.162.1 and Claude Code 2.1.296. Primary documentation and observed CLI behavior are distinguished in the user guide.

## Dogfood findings and fixes

- Before implementation, five distribution tests errored on missing build/metadata resources. This was missing-interface evidence, not five reproduced runtime defects.
- The first real build failed exact-inventory verification: macOS tar injected AppleDouble/resource-fork files. `COPYFILE_DISABLE=1` removed them; the inventory test was not weakened.
- Strict Claude marketplace validation reported a missing description. Add the description, keep strict validation, and rerun successfully.
- Independent review reproduced writes outside `build/` through a symlinked directory and an `OUT` override; `VERSION` could also mislabel a bundle. Three new regression tests ran red (exit 1, three failures) before the fix. Fixed internal output/canonical version, override refusal, and build-symlink rejection made all eight distribution tests pass.
- Native local Claude installation reads the extracted plugin in place even though it also stores a cache copy. Documentation now requires keeping that source available. Native Git-marketplace refresh is not falsely described as a local-archive updater.

Earlier failed/diagnostic builds were moved to explicitly named `*-before-*-fix.tar.gz`/`*-before-output-guards.tar.gz` files under ignored `build/`; they are not distribution candidates. Nothing in historical `dist/` was changed.

## Package evidence

`make package` — exit 0. Output: `build/ai-native-sdlc-1.1.0.tar.gz`.

Archive SHA-256: `64ac4709ab555616755e7dc5093ba0e3df032feba8afec1bb30f9a4d9ff21a98`. The archive has exactly ten regular files: two native catalogs, two native plugin manifests, the unchanged license, and the canonical five skill files. No private corpus, `.env`, caches, old archives, runtime, hooks, MCP, or symlinks are included.

Tests build disposable source fixtures containing synthetic private chaff and check the exact archive allowlist and source bytes. Additional cases reject existing output, absent references, symlinked sources/build, protected output overrides, and version overrides. Source/manifest version consistency is checked. Tar metadata/timestamps can differ between builds; this is not a byte-for-byte reproducible-build claim.

The final extraction is `/tmp/sdlc-final-native.5Jx1HT/ai-native-sdlc-1.1.0`. `diff -r` versus the independently tested earlier extraction exited 0, binding final payload contents to the native trials without claiming identical compressed bytes.

## Native forward test and reproduction

An independent agent used `/tmp/sdlc-native-forward.xLGfe5/` for temporary Claude config/cache and two empty project directories. Commands used `CLAUDE_CONFIG_DIR`, `CLAUDE_CODE_PLUGIN_CACHE_DIR`, `DISABLE_TELEMETRY=1`, and `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC=1`; HOME/CODEX_HOME and real client settings were not changed.

| Command/check | Observed result |
| --- | --- |
| `claude plugin validate BUNDLE --strict --json` and plugin subdirectory | Both exit 0, no warnings/errors |
| `claude plugin marketplace add BUNDLE --scope user --json` | Exit 0 in isolated config |
| `claude plugin install ai-native-sdlc@sdlc-local --scope user --json` | Exit 0, user installation |
| Fresh `claude plugin list --json` and `details` from two projects | Exit 0, same enabled user plugin, one skill; zero hooks/MCP/agents/LSP |
| Repeat installation from second project | Exit 0, already installed; one registry entry, no duplicate |
| Synthetic unrelated settings marker | Preserved; both projects remained empty |
| `diff -qr` clean plugin versus installed cache; `diff -r` canonical skill versus cache; license `cmp` | Exit 0; exact bytes, no cache symlinks |

The main agent independently reproduced current list/details output, empty-project and cache inventories, and final-payload/cache/skill comparisons. Registration, repeated-install, and marker history are evaluator-reported, not independently captured full transcripts. No paid/model call was used to turn metadata discovery into an activation claim.

Codex discovery was reproduced against the final extracted bundle:

```sh
codex \
  -c 'marketplaces.sdlc-local.source="/tmp/sdlc-final-native.5Jx1HT/ai-native-sdlc-1.1.0"' \
  -c 'marketplaces.sdlc-local.source_type="local"' \
  -c 'cli_auth_credentials_store="ephemeral"' \
  plugin list --marketplace sdlc-local --available --json
```

Exit 0: expected plugin/version, clean local source, `AVAILABLE`, `ON_USE`, `installed=false`. The evaluator also observed the same discovery from both projects. No Codex installation was performed because it would write real user configuration/cache; discovery is not installation.

## Repository checks and preservation

- `python3 -m unittest discover -s tests -t .` — exit 0; 19 tests, `OK`, including eight real distribution contract tests. Independent review also reran the eight distribution tests successfully.
- `uv run --with pyyaml python "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-creator/scripts/quick_validate.py" skills/ai-native-sdlc` — exit 0; `Skill is valid!`.
- A temporary public-only copy ran the same suite without private collections — exit 0; 19 tests, `OK`.
- Shipped-skill before/after aggregate SHA-256 matched: `1257d218ca198a28da934c858464b37fa693b764e533a5f7c101d55cd76a4bef`.
- Private vault/audit/historical archive before/after aggregate SHA-256 matched: `fbf1e5510bc4aa3cad2bfe75e4f7d87900aa277679545eb2e914b0a6a9c08d24`.

Earlier memory/documentation verification records remain dated history, not retroactively relabeled as this run.

## Remaining limits

- Actual Linux execution was unavailable in this macOS workspace; Docker/Podman were not installed. POSIX Make/tar and native Linux/macOS clients are the target, not evidence of a Linux run.
- Actual Codex installation, paid-model invocation, cross-model compliance, and update/rollback of a live installation are not verified by catalog discovery or Claude metadata loading.
- Native host/project policy may restrict a user-scoped plugin. Each project still requires its own vault/specification/configuration evidence and authority.
- Git revision binding, hosted CI, remote acquisition, and GitHub publication remain unverified/deferred. There is no approved remote URL and no Git metadata here.
- Proprietary terms are unchanged. Local packaging does not authorize public distribution of the skill or any private data.
