ifneq ($(origin VERSION),undefined)
$(error VERSION is derived from SKILL.md and cannot be overridden)
endif
ifneq ($(origin OUT),undefined)
$(error OUT is fixed inside build/ and cannot be overridden)
endif
VERSION := $(shell sed -n 's/^  version: "\([0-9][0-9.]*\)"/\1/p' skills/ai-native-sdlc/SKILL.md)
OUT := build/ai-native-sdlc-$(VERSION).tar.gz

.PHONY: package
package:
	@set -eu; umask 077; \
	test -n "$(VERSION)"; \
	if test -L build; then printf 'Refusing symlinked build directory\n' >&2; exit 1; fi; \
	if test -e "$(OUT)" || test -L "$(OUT)"; then printf 'Refusing existing output: %s\n' "$(OUT)" >&2; exit 1; fi; \
	for sdlc_dir in packaging skills skills/ai-native-sdlc skills/ai-native-sdlc/references; do test -d "$$sdlc_dir"; test ! -L "$$sdlc_dir"; done; \
	for sdlc_file in LICENSE packaging/codex-plugin.json packaging/claude-plugin.json packaging/codex-marketplace.json packaging/claude-marketplace.json skills/ai-native-sdlc/SKILL.md skills/ai-native-sdlc/references/completion-evidence.md skills/ai-native-sdlc/references/knowledge-vault.md skills/ai-native-sdlc/references/project-grounding.md skills/ai-native-sdlc/references/test-integrity.md; do test -f "$$sdlc_file"; test ! -L "$$sdlc_file"; done; \
	sdlc_stage_dir=$$(mktemp -d); sdlc_bundle="$$sdlc_stage_dir/ai-native-sdlc-$(VERSION)"; sdlc_plugin="$$sdlc_bundle/plugins/ai-native-sdlc"; \
	mkdir -p "$$sdlc_bundle/.agents/plugins" "$$sdlc_bundle/.claude-plugin" "$$sdlc_plugin/.codex-plugin" "$$sdlc_plugin/.claude-plugin" "$$sdlc_plugin/skills/ai-native-sdlc/references"; \
	cp packaging/codex-marketplace.json "$$sdlc_bundle/.agents/plugins/marketplace.json"; \
	cp packaging/claude-marketplace.json "$$sdlc_bundle/.claude-plugin/marketplace.json"; \
	cp packaging/codex-plugin.json "$$sdlc_plugin/.codex-plugin/plugin.json"; \
	cp packaging/claude-plugin.json "$$sdlc_plugin/.claude-plugin/plugin.json"; \
	cp LICENSE "$$sdlc_plugin/LICENSE"; cp skills/ai-native-sdlc/SKILL.md "$$sdlc_plugin/skills/ai-native-sdlc/SKILL.md"; \
	for sdlc_ref in completion-evidence knowledge-vault project-grounding test-integrity; do cp "skills/ai-native-sdlc/references/$$sdlc_ref.md" "$$sdlc_plugin/skills/ai-native-sdlc/references/$$sdlc_ref.md"; done; \
	mkdir -p "$$(dirname "$(OUT)")"; \
	COPYFILE_DISABLE=1 tar -czf "$(OUT)" -C "$$sdlc_stage_dir" "ai-native-sdlc-$(VERSION)"; \
	printf 'Built %s\n' "$(OUT)"
