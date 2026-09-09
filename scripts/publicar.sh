#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

if [[ ! -f index.html ]]; then
  echo "Erro: index.html não foi encontrado na raiz do projeto." >&2
  exit 1
fi

if ! git remote get-url origin >/dev/null 2>&1; then
  echo "Erro: o remoto 'origin' não está configurado." >&2
  exit 1
fi

BRANCH="$(git branch --show-current)"
if [[ -z "$BRANCH" ]]; then
  echo "Erro: não foi possível identificar a branch atual." >&2
  exit 1
fi

COMMIT_MESSAGE="${1:-publish: atualiza site no GitHub Pages}"

if [[ -n "$(git status --porcelain)" ]]; then
  git add -A
  git commit -m "$COMMIT_MESSAGE"
else
  echo "Nenhuma alteração nova para registrar."
fi

git push origin "$BRANCH"
echo "Publicação enviada. O workflow do GitHub Pages será executado na branch $BRANCH."