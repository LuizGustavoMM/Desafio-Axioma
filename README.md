# Desafio-Axioma
Desafio realizado para submissão de vaga Axioma Tech.

# 🏛️ Eco-System Sentinel: Orquestrador de Dados Legislativos (n8n + AI)

Este projeto foi desenvolvido como demonstração técnica de arquitetura de automação, integrando scripts em Python com **n8n** para coleta e análise de dados públicos legislativos.

## 🎯 O Desafio Resolvido
Construir uma pipeline de dados desacoplada onde um container Python atua como *worker* de extração de dados da API de Transparência, e o n8n atua como *orquestrador*, permitindo integrações futuras com IA (Claude/OpenAI) para análise semântica das leis e gastos.

## 🛠️ Tecnologias Utilizadas
* **Python 3.11** (POO, Requests, BeautifulSoup)
* **n8n** (Workflows de Automação)
* **Docker & Docker Compose** (Isolamento e Service Discovery)
* **Ubuntu** (Ambiente alvo de deploy)

## 🚀 Como Executar o Projeto

1. Clone o repositório e crie o seu arquivo de variáveis de ambiente:
\`\`\`bash
cp .env.example .env
\`\`\`

2. Suba a infraestrutura completa (App + n8n) via Docker Compose:
\`\`\`bash
docker compose up -d --build
\`\`\`

3. Acesse o painel do n8n localmente em \`http://localhost:5678\` para visualizar ou importar o fluxo de recebimento de webhooks.

## 🧠 Arquitetura de Rede
O projeto utiliza a rede interna do Docker (`bridge`). O container Python se comunica com o Webhook do n8n de forma isolada, sem expor portas extras, garantindo segurança na transferência do payload.