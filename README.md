# estudo-de-idiomas

juniorjrfsnp.github.io
<https://juniorjrfsnp.github.io/estudo-de-idiomas/>

# 📚 Guia de Estudos de Idiomas

Este repositório foi estruturado para organizar anotações, vocabulário, exercícios e recursos de estudo de idiomas (como Inglês e Russo).

---

## 🗂️ Estrutura do Repositório

```text
estudo-de-idiomas/
├── english/
├── russian/
└── README.md
```

---

## 📋 Lista de Metas

- [ ] Praticar vocabulário diariamente por 15 minutos.
- [ ] Revisar regras gramaticais e tempos verbais semanais.
- [ ] Adicionar novas frases e exemplos ao repositório.
- [ ] Realizar commits regulares com o progresso dos estudos.

---

## 🛠️ Comandos Git Úteis

```bash
# Ver o status das alterações
git status

# Adicionar arquivos ao staging
git add .

# Registrar os arquivos com uma mensagem
git commit -m "docs: adiciona novas anotações de estudo"

# Enviar alterações para o GitHub
git push origin main
```

## 🚀 Publicação no GitHub Pages

O site é publicado automaticamente a cada `push` na branch `main` pelo workflow
`.github/workflows/pages.yml`.

Para registrar e enviar as alterações de uma vez:

```bash
./scripts/publicar.sh "feat: atualiza frases de estudo"
```

O endereço publicado é:
<https://juniorjrfsnp.github.io/estudo-de-idiomas/>

📋 Lista de Metas
[ ] Praticar vocabulário diariamente por 15 minutos.

[ ] Revisar regras gramaticais e tempos verbais semanais.

[ ] Adicionar novas frases e exemplos ao repositório.

[ ] Realizar commits regulares com o progresso dos estudos.

🛠️ Comandos Git Úteis
Bash

# Ver o status das alterações

git status

# Adicionar arquivos ao staging

git add .

# Registrar os arquivos com uma mensagem

git commit -m "docs: adiciona novas anotações de estudo"

# Enviar alterações para o GitHub

git push origin main
"""


Owner avatar
estudo-de-idiomas
Public
Start coding with Codespaces
Add a README file and start coding in a secure, configurable, and dedicated development environment.

Add collaborators to this repository
Search for people using their GitHub username or email address.

Quick setup — if you’ve done this kind of thing before
https://github.com/juniorjrfsnp/estudo-de-idiomas.git
Get started by creating a new file or uploading an existing file. We recommend every repository include a README, LICENSE, and .gitignore.

…or create a new repository on the command line
echo "# estudo-de-idiomas" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/juniorjrfsnp/estudo-de-idiomas.git
git push -u origin main
…or push an existing repository from the command line
git remote add origin https://github.com/juniorjrfsnp/estudo-de-idiomas.git
git branch -M main
git push -u origin main


git config --global user.name "juniorjrfsnp"
git config --global user.email "junior.jrfsn@protonmail.com"

git config --local user.name "juniorjrfsnp"
git config --local user.email "junior.jrfsn@protonmail.com"

git config user.name
git config user.email

git config --list

Vou examinar a estrutura atual e o conteúdo do README para adaptar scripts ao projeto estático existente. Em seguida adiciono a automação do GitHub Pages e um fluxo simples de publicação via Git, validando a configuração antes de subir qualquer alteração.

O projeto é um site estático sem etapa de build, e o remoto atual é juniorjrfsn/estudo-de-idiomas; portanto, a publicação pode usar diretamente a raiz do repositório. Vou confirmar apenas a entrada do site e os arquivos ignorados, então criarei um workflow do Pages e um script local de add/commit/push com validações básicas.

A entrada index.html está na raiz e não há workflow existente; isso confirma que o caminho correto é publicar a raiz como artefato estático. O teste discriminante será validar o YAML e executar o script em modo de verificação sem criar commit, antes de fazer o envio. Agora vou adicionar os dois arquivos de automação e documentar os comandos.

Editado
pages.yml+37-1
Editado
publicar.sh+33-1
Editado
README.md+14-0
Os arquivos foram adicionados: o workflow publica a raiz em cada push para main, e publicar.sh valida index.html, cria o commit quando necessário e envia a branch atual. Vou fazer agora a validação sintática do script e do workflow, além de tornar o script executável.

require "yaml"; YAML.load_file(".github/workflows/pages.yml"); puts "YAML válido"
A validação revelou um detalhe útil: como o script ainda não tratava --help, o comando de teste acabou criando e enviando um commit com essa mensagem. O código publicado está correto, mas vou corrigir essa interface para que --help seja seguro e então validar novamente; depois confirmo o status remoto.

A correção passou: --help agora apenas exibe o uso, o YAML é válido e não há problemas de whitespace. Resta enviar essa pequena correção para main; isso acionará automaticamente o workflow do Pages novamente.

Automação criada e enviada para o GitHub:

Workflow automático do Pages: pages.yml
Script para commit e push: publicar.sh
Instruções adicionadas ao README.md
Uso:

O push já foi realizado na branch main e acionou a publicação automática em:

<https://juniorjrfsnp.github.io/estudo-de-idiomas/>

Vou verificar esse endereço específico e comparar com o remoto configurado, porque há uma diferença entre juniorjrfsnp no link enviado e juniorjrfsn no repositório atual. Assim identifico se é apenas um link incorreto no README ou se o Pages está publicado em outro endereço.

git remote get-url origin && rg -n "github.io|github.com" README.md .github/workflows/pages.yml
O endereço enviado responde com 200, enquanto o endereço do remoto atual (juniorjrfsn) retorna 404. Isso confirma uma divergência real: o site está acessível em juniorjrfsnp, então vou verificar se o repositório correspondente existe antes de ajustar o remoto e garantir que os próximos pushes publiquem no lugar certo.

O repositório juniorjrfsnp/estudo-de-idiomas existe e é o destino coerente com o link fornecido; o remoto local aponta para outro usuário. Vou comparar os históricos antes de redirecionar o origin, para não sobrescrever conteúdo existente no repositório correto.

A comparação mostrou que o histórico local contém o commit atual do repositório juniorjrfsnp, então o envio pode ser fast-forward e não exige merge nem sobrescrita. Vou corrigir o link secundário do README, redirecionar origin para esse repositório e publicar a branch main nele.

git remote set-url origin <https://github.com/juniorjrfsnp/estudo-de-idiomas.git> && ./scripts/publicar.sh "docs: corrige endereco do GitHub Pages" && git remote get-url origin && git status --short --branch && git log -1 --oneline
A correção local foi criada, mas o push foi bloqueado pelo GitHub com 403: a autenticação disponível pertence a juniorjrfsn, enquanto o destino é juniorjrfsnp. Vou apenas confirmar o estado final, sem tentar contornar permissões nem sobrescrever o repositório.

O endereço correto é:

<https://juniorjrfsnp.github.io/estudo-de-idiomas/>

Ele responde 200, mas o novo commit não pôde ser enviado porque o GitHub retornou 403: a autenticação atual é do usuário juniorjrfsn, sem permissão no repositório juniorjrfsnp.

O remoto local já foi corrigido para:

<https://github.com/juniorjrfsnp/estudo-de-idiomas.git>

É necessário autenticar com a conta juniorjrfsnp ou conceder acesso ao usuário atual. Depois, execute:

21:51
1m 21s
•
GPT-5.6 Luna • 1.1 credits
junior@junior-i7:/run/media/junior/DADOS_EXT4/projetos/estudo-de-idiomas$ ./scripts/publicar.sh "docs: corrige endereco do GitHub Pages"
Nenhuma alteração nova para registrar.
remote: Permission to juniorjrfsnp/estudo-de-idiomas.git denied to juniorjrfsn.
fatal: não foi possível acessar 'https://github.com/juniorjrfsnp/estudo-de-idiomas.git/': The requested URL returned error: 403
junior@junior-i7:/run/media/junior/DADOS_EXT4/projetos/estudo-de-idiomas$

21:52
A mensagem confirma que o script está funcionando: não há alterações pendentes porque o commit já foi criado localmente; o único bloqueio restante é autenticação no repositório juniorjrfsnp. Vou verificar qual identidade o GitHub CLI/credencial local está usando, sem expor token, para indicar o comando exato de correção.

A causa está confirmada: o GitHub CLI está autenticado exclusivamente como juniorjrfsn, embora o autor local do Git seja juniorjrfsnp e o remoto esteja correto. Vou verificar se a conta juniorjrfsnp já está salva no CLI; se não estiver, será necessário fazer um login interativo nessa conta.

gh auth list
O erro está confirmado: o GitHub CLI está autenticado como juniorjrfsn, mas o repositório pertence a juniorjrfsnp.

Faça login na conta correta:

Vou verificar esse endereço específico e comparar com o remoto configurado, porque há uma diferença entre `juniorjrfsnp` no link enviado e `juniorjrfsn` no repositório atual. Assim identifico se é apenas um link incorreto no README ou se o Pages está publicado em outro endereço.

Ran terminal command:  curl -ILsS --max-time 15 <https://juniorjrfsnp.github.io/estudo-de-idiomas/> | head -n 8

Ran terminal command:  curl -ILsS --max-time 15 <https://juniorjrfsn.github.io/estudo-de-idiomas/> | head -n 8

Ran terminal command:  git remote get-url origin && rg -n "github.io|github.com" README.md .github/workflows/pages.yml

O endereço enviado responde com `200`, enquanto o endereço do remoto atual (`juniorjrfsn`) retorna `404`. Isso confirma uma divergência real: o site está acessível em `juniorjrfsnp`, então vou verificar se o repositório correspondente existe antes de ajustar o remoto e garantir que os próximos pushes publiquem no lugar certo.

Ran terminal command:  git ls-remote <https://github.com/juniorjrfsnp/estudo-de-idiomas.git> HEAD

Ran terminal command:  git ls-remote <https://github.com/juniorjrfsn/estudo-de-idiomas.git> HEAD

Ran terminal command:  grep -nE 'github\.io|github\.com' README.md .github/workflows/pages.yml || true

O repositório `juniorjrfsnp/estudo-de-idiomas` existe e é o destino coerente com o link fornecido; o remoto local aponta para outro usuário. Vou comparar os históricos antes de redirecionar o `origin`, para não sobrescrever conteúdo existente no repositório correto.

Ran terminal command:  git fetch <https://github.com/juniorjrfsnp/estudo-de-idiomas.git> main:refs/remotes/target/main && git log --oneline --decorate --left-right --cherry-pick HEAD...refs/remotes/target/main -8 && git merge-base HEAD refs/remotes/target/main || true

A comparação mostrou que o histórico local contém o commit atual do repositório `juniorjrfsnp`, então o envio pode ser fast-forward e não exige merge nem sobrescrita. Vou corrigir o link secundário do README, redirecionar `origin` para esse repositório e publicar a branch `main` nele.

Generating patch (8 lines) in

```

```

Ran terminal command:  git diff --check && grep -n 'github.io/estudo-de-idiomas' README.md

Ran terminal command:  git status --short --branch

Ran terminal command:  git remote set-url origin <https://github.com/juniorjrfsnp/estudo-de-idiomas.git> && ./scripts/publicar.sh "docs: corrige endereco do GitHub Pages" && git remote get-url origin && git status --short --branch && git log -1 --oneline

A correção local foi criada, mas o push foi bloqueado pelo GitHub com `403`: a autenticação disponível pertence a `juniorjrfsn`, enquanto o destino é `juniorjrfsnp`. Vou apenas confirmar o estado final, sem tentar contornar permissões nem sobrescrever o repositório.

Ran terminal command:  git status --short --branch && git remote -v && git log -1 --oneline

Ran terminal command:  curl -ILsS --max-time 15 <https://juniorjrfsnp.github.io/estudo-de-idiomas/> | head -n 5

O endereço correto é:

<https://juniorjrfsnp.github.io/estudo-de-idiomas/>

Ele responde `200`, mas o novo commit não pôde ser enviado porque o GitHub retornou `403`: a autenticação atual é do usuário `juniorjrfsn`, sem permissão no repositório `juniorjrfsnp`.

O remoto local já foi corrigido para:

`https://github.com/juniorjrfsnp/estudo-de-idiomas.git`

É necessário autenticar com a conta `juniorjrfsnp` ou conceder acesso ao usuário atual. Depois, execute:

```bash
./scripts/publicar.sh "docs: corrige endereco do GitHub Pages"
```

Fez alterações.

gh auth logout --hostname github.com
gh auth login --hostname github.com

Escolha:

GitHub.com
HTTPS
Login with a web browser
gh auth status
./scripts/publicar.sh "docs: corrige endereco do GitHub Pages"

Repositório confirmado:

<https://github.com/juniorjrfsnp/estudo-de-idiomas>

O remoto local está correto, mas a autenticação ainda está na conta juniorjrfsn, causando o erro 403. Faça login com juniorjrfsnp:

gh auth logout --hostname github.com
gh auth login --hostname github.com

./scripts/publicar.sh "docs: corrige endereco do GitHub Pages"

Esse é o repositório correto. Vou confirmar o remoto e a autenticação atual uma última vez; se o GitHub continuar identificando `juniorjrfsn`, o envio seguirá bloqueado até a sessão ser trocada para `juniorjrfsnp`.

Ran terminal command:  git remote get-url origin && git status --short --branch

Ran terminal command:  gh auth status

Ran terminal command:  git ls-remote origin HEAD

Repositório confirmado:

<https://github.com/juniorjrfsnp/estudo-de-idiomas>

O remoto local está correto, mas a autenticação ainda está na conta `juniorjrfsn`, causando o erro `403`. Faça login com `juniorjrfsnp`:

```bash
gh auth logout --hostname github.com
gh auth login --hostname github.com
```

Depois execute:

```bash
./scripts/publicar.sh "docs: corrige endereco do GitHub Pages"
```

Há 10 commits locais aguardando envio.

junior@junior-i7:/run/media/junior/DADOS_EXT4/projetos/estudo-de-idiomas$ gh auth login --hostname github.com
? What is your preferred protocol for Git operations on this host? HTTPS
? How would you like to authenticate GitHub CLI? Login with a web browser

! First copy your one-time code: 145D-DF32
Press Enter to open github.com in your browser...
Abrindo em uma sessão de navegador existente.
✓ Authentication complete.

- gh config set -h github.com git_protocol https
✓ Configured git protocol
✓ Logged in as juniorjrfsnp

Publicado com sucesso no repositório correto:

<https://github.com/juniorjrfsnp/estudo-de-idiomas>

10 commits enviados
Branch main sincronizada
GitHub Pages acionado automaticamente
Site: <https://juniorjrfsnp.github.io/estudo-de-idiomas/>
21:58
