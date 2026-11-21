# Issues and Fixes

| Day | Issue | Cause | Fix |
|---|---|---|---|
| 1 | Python 3.11.18 page had no Windows installer | 3.11 now gets source-only security releases | Installed Python 3.11.9 (last release with installer) |
| 1 | `git` not recognized in VS Code terminal | VS Code opened before Git install, old PATH | Closed and reopened VS Code |
| 1 | Groq `model_not_found` (llama-3.1-8b-instant) | Model no longer available | Listed models via API, switched to openai/gpt-oss-20b |
| 1 | `.vscode/` showed up in git status | VS Code creates local settings folder | Added `.vscode/` to .gitignore |
| 1 | Hopsworks asked for payment details | (to investigate) | (pending) |