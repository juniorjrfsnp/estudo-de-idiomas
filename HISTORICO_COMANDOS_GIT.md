# Histórico de Comandos Git

Este arquivo resume os comandos usados para configurar, verificar e publicar o projeto `estudo-de-idiomas` no GitHub e no GitHub Pages.

## 1. Verificação inicial

Comandos usados para descobrir o estado local, o remoto e o último commit:

```bash
git status --short --branch
git remote -v
git log -1 --oneline
```

Resultado: a branch `main` estava um commit à frente de `origin/main`, então havia um commit local pronto para envio.

## 2. Primeiro envio ao GitHub

```bash
git push origin main
```

Depois, o envio foi confirmado com:

```bash
git status --short --branch
git log -1 --oneline
```

## 3. Verificação antes da automação

```bash
git status --short --branch
git remote -v
git ls-files '.github/*' 'scripts/*' '.gitignore'
git status --short --untracked-files=all
```

Esses comandos confirmaram que o repositório estava limpo e que ainda não havia workflow do GitHub Pages.

## 4. Validação dos arquivos de publicação

Após criar o workflow `.github/workflows/pages.yml` e o script `scripts/publicar.sh`, foram usados:

```bash
chmod +x scripts/publicar.sh
bash -n scripts/publicar.sh
./scripts/publicar.sh --help
git diff --check
git status --short
```

Também foi validado o YAML do workflow com:

```bash
python3 -c 'import yaml; yaml.safe_load(open(".github/workflows/pages.yml")); print("YAML válido")'
```

## 5. Publicação da automação

O script criado para automatizar o processo foi executado com:

```bash
./scripts/publicar.sh "chore: melhora script de publicação"
```

Internamente, quando existem alterações, o script executa:

```bash
git status --porcelain
git add -A
git commit -m "mensagem do commit"
git push origin "branch atual"
```

O script também usa estes comandos para validar o ambiente:

```bash
git remote get-url origin
git branch --show-current
```

## 6. Diagnóstico do endereço do Pages

Para comparar o endereço do site com o remoto Git, foram usados:

```bash
git remote get-url origin
grep -nE 'github\.io|github\.com' README.md .github/workflows/pages.yml
git ls-remote https://github.com/juniorjrfsnp/estudo-de-idiomas.git HEAD
git ls-remote https://github.com/juniorjrfsn/estudo-de-idiomas.git HEAD
```

## 7. Comparação dos históricos

Antes de trocar o repositório remoto, foi baixada apenas a referência `main` do destino correto:

```bash
git fetch https://github.com/juniorjrfsnp/estudo-de-idiomas.git main:refs/remotes/target/main
git log --oneline --decorate --left-right --cherry-pick HEAD...refs/remotes/target/main -8
git merge-base HEAD refs/remotes/target/main
```

Esse passo confirmou que o envio seria compatível com o histórico existente.

## 8. Correção do remoto

O remoto foi alterado para o repositório correto com:

```bash
git remote set-url origin https://github.com/juniorjrfsnp/estudo-de-idiomas.git
git remote get-url origin
```

O primeiro push após essa troca falhou com `403`, porque a autenticação ainda estava na conta `juniorjrfsn`.

## 9. Configuração da autenticação do GitHub

Comandos auxiliares usados para verificar e trocar a conta do GitHub CLI:

```bash
gh auth status
gh auth logout --hostname github.com
gh auth login --hostname github.com
gh auth status
```

Durante o login, foi selecionado o protocolo `HTTPS` e a opção `Login with a web browser`. A conta correta foi `juniorjrfsnp`.

## 10. Envio final para o repositório correto

Antes do envio final:

```bash
git status --short --branch
git log --oneline origin/main..HEAD
```

O envio foi concluído com:

```bash
./scripts/publicar.sh "docs: corrige endereco do GitHub Pages"
```

Confirmação final:

```bash
git status --short --branch
git log -1 --oneline
git remote get-url origin
```

Estado final:

- Branch: `main`
- Remoto: `https://github.com/juniorjrfsnp/estudo-de-idiomas.git`
- Branch local sincronizada com `origin/main`
- GitHub Pages: <https://juniorjrfsnp.github.io/estudo-de-idiomas/>

## 11. Fluxo recomendado para as próximas alterações

Para publicar mudanças futuras:

```bash
./scripts/publicar.sh "tipo: descreve a alteração"
```

Ou manualmente:

```bash
git status
git add -A
git commit -m "tipo: descreve a alteração"
git push origin main
git status --short --branch
```
