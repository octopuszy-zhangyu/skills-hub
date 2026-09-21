# Git Push Workflow Rule

- **Always Use `gh push`**: When pushing git commits to GitHub in this workspace, always use `gh push` instead of raw `git push`.
- **Proxy Compatibility**: When invoking git or gh commands in PowerShell, route traffic via the HTTP proxy `http://127.0.0.1:1082` (e.g. `$env:HTTP_PROXY="http://127.0.0.1:1082"; $env:HTTPS_PROXY="http://127.0.0.1:1082"`), avoiding `socks5://` proxy schemes that cause Windows .NET `ServicePointManager` failures.
- **Verification**: Ensure `gh auth setup-git` and `gh alias set push '!git push "$@"'` are active if pushing from a fresh environment.
