# Integração GitHub para GitHub Developer Program

Este projeto contém um exemplo simples de integração com a API do GitHub que pode ser usado como base para construir uma aplicação ou workflow GitHub.

## O que ele faz

- lista repositórios de um usuário GitHub
- cria uma issue em um repositório GitHub
- roda dentro de um workflow GitHub Actions com o token `GITHUB_TOKEN`

## Como usar

1. Crie um token GitHub com permissão `repo`.
2. Defina a variável de ambiente:

```powershell
$env:GITHUB_TOKEN = "seu_token_aqui"
```

3. Liste repositórios:

```powershell
python github_highlight_integration.py list --owner seu-usuario
```

4. Crie uma issue:

```powershell
python github_highlight_integration.py issue --owner seu-usuario --repo seu-repositorio --title "Teste" --body "Issue criada pelo integration demo."
```

## Como faz integração no GitHub

- o arquivo de workflow `./.github/workflows/github-integration.yml` executa o script automaticamente no GitHub Actions
- adicione esse repositório ao GitHub e habilite o Action
- use o token embutido `secrets.GITHUB_TOKEN` para chamar a API de forma segura

## Por que isso ajuda no GitHub Developer Program

- demonstra uso da API GitHub
- mostra um fluxo contínuo de integração com GitHub Actions
- é um bom ponto de partida para criar uma aplicação ou GitHub App mais avançada
