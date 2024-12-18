# Gerador de Mensagens de Commit com FastAPI e OpenAI

Este projeto é uma API desenvolvida com **FastAPI** que gera mensagens de commit baseadas em um _diff_ fornecido e no estilo especificado, utilizando a API da **OpenAI**.

---

## 📋 **Índice**

1. [Sobre o Projeto](#sobre-o-projeto)
2. [Tecnologias Utilizadas](#tecnologias-utilizadas)
3. [Requisitos](#requisitos)
4. [Como Rodar o Projeto](#como-rodar-o-projeto)
5. [Endpoints Disponíveis](#endpoints-disponíveis)
6. [Variáveis de Ambiente](#variáveis-de-ambiente)
7. [Exemplo de Uso](#exemplo-de-uso)

---

## 🚀 **Sobre o Projeto**

A API permite gerar mensagens de commit personalizadas a partir de:

- Um _diff_ de código fornecido.
- Um estilo de mensagem (ex: _conventional commits_).

Ela faz uso da API **GPT-3.5-Turbo** da OpenAI para processar e gerar o texto.

---

## 🛠️ **Tecnologias Utilizadas**

- [Python 3.10+](https://www.python.org/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [Pydantic](https://pydantic.dev/)
- [OpenAI Python SDK](https://platform.openai.com/docs/libraries/python)
- [Python-dotenv](https://pypi.org/project/python-dotenv/)

---

## ✅ **Requisitos**

Antes de iniciar, certifique-se de ter as seguintes ferramentas instaladas:

- **Python 3.10+**
- **pip** (gerenciador de pacotes do Python)
- **OpenAI API Key** (disponível em [OpenAI](https://platform.openai.com/))

---

## ▶️ **Como Rodar o Projeto**

1. Clone este repositório:

   ```bash
   git clone https://github.com/seu-usuario/ai-commitAPI.git
   cd ai-commitAPI
   ```

2. Crie um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate      # Linux/MacOS
   venv\Scripts\activate         # Windows
   ```

3. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ```

4. Crie um arquivo .env na raiz do projeto e adicione a sua chave da API OpenAI:

   ```bash
   OPEN_API_KEY=coloque-sua-chave-aqui
   ```

5. Execute o servidor

   ```bash
   fastapi dev app/main.py
   ```

6. Acesse a documentação interativa do Swagger em:

- http://127.0.0.1:8000/docs

## ▶️ **Endpoints Disponíveis**

1. Gerar mensagem de commit

- Rota: "/generate-commit"
- Método: POST
- Descrição: Gera uma mensagem de commit com base no diff e estilo fornecidos.

### Requisição:

- Body (JSON):

```json
{
  "diff": "Seu diff de código aqui",
  "style": "estilo de mensagem de commit"
}
```

- O parâmetro style é opcional (valor padrão: conventional).

### Exemplo de resposta

```json
{
  "response": "feat: refactor function greet to use f-strings for better readability"
}
```

## Variáveis de ambiente

Você vai precisar da chave de api disponível em https://platform.openai.com/api-keys

No arquivo .env coloque a chave da API dessa forma:

```plaintext
OPEN_API_KEY=sua-chave
```

## Exemplos de uso

Requisição Exemplo com cURL

```bash
curl -X POST "http://127.0.0.1:8000/generate-commit" \
-H "Content-Type: application/json" \
-d '{
    "diff": "diff --git a/main.py b/main.py\nindex abc123..def456 100644\n--- a/main.py\n+++ b/main.py\n@@ -1,2 +1,2 @@\n-print(\"Hello\")\n+print(\"Hello, World!\")",
    "style": "conventional"
}'
```

Resposta

```json
{
  "response": "feat: update print statement to include 'World!' for better clarity"
}
```
