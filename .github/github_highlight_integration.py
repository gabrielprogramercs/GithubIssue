import argparse
import os
import sys
import requests

API_URL = "https://api.github.com"


def get_headers(token: str) -> dict:
    return {
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "GitHub-Developer-Program-Integration"
    }


def list_repos(owner: str, token: str) -> None:
    url = f"{API_URL}/users/{owner}/repos"
    response = requests.get(url, headers=get_headers(token), params={"per_page": 100})
    response.raise_for_status()
    repos = response.json()
    if not repos:
        print(f"Nenhum repositório encontrado para {owner}.")
        return
    print(f"Repositórios de {owner}:")
    for repo in repos:
        print(f"- {repo['full_name']}: {repo['html_url']}")


def create_issue(owner: str, repo: str, title: str, body: str, token: str) -> None:
    url = f"{API_URL}/repos/{owner}/{repo}/issues"
    payload = {"title": title, "body": body}
    response = requests.post(url, headers=get_headers(token), json=payload)
    response.raise_for_status()
    issue = response.json()
    print(f"Issue criada: {issue['html_url']}")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Exemplo de integração com GitHub para Developer Program."
    )
    parser.add_argument("action", choices=["list", "issue"], help="Ação de GitHub a executar.")
    parser.add_argument("--owner", required=True, help="Proprietário do repositório ou usuário GitHub.")
    parser.add_argument("--repo", help="Nome do repositório (necessário para issue).")
    parser.add_argument("--title", help="Título da issue a ser criada.")
    parser.add_argument("--body", default="Criado por integração GitHub Developer Program.", help="Texto da issue.")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Erro: defina a variável de ambiente GITHUB_TOKEN com um token do GitHub.")
        return 1

    try:
        if args.action == "list":
            list_repos(args.owner, token)
        elif args.action == "issue":
            if not args.repo or not args.title:
                print("Para criar uma issue, informe --repo e --title.")
                return 1
            create_issue(args.owner, args.repo, args.title, args.body, token)
        return 0
    except requests.HTTPError as exc:
        response = exc.response
        print(f"Erro HTTP {response.status_code}: {response.text}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
