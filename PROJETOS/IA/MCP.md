---
tags:
  - AI
  - MCP
  - Protocolo
---

# Model Context Protocol (MCP) - Base de Conhecimento

## O que é MCP?

**MCP (Model Context Protocol)** é um padrão open-source que conecta aplicações de IA a sistemas externos. Pense no MCP como uma "porta USB-C para aplicações de IA" - assim como o USB-C fornece uma forma padronizada de conectar dispositivos eletrônicos, o MCP fornece uma forma padronizada de conectar aplicações de IA a sistemas externos.

**Fonte:** [What is the Model Context Protocol?](https://modelcontextprotocol.io/docs/getting-started/intro)

### O que o MCP possibilita?

- Agentes podem acessar seu Google Calendar e Notion, agindo como assistentes de IA mais personalizados
- Claude Code pode gerar um aplicativo web completo usando um design do Figma
- Chatbots corporativos podem conectar-se a múltiplos bancos de dados em uma organização
- Modelos de IA podem criar designs 3D no Blender e imprimi-los usando impressoras 3D

### Por que o MCP é importante?

**Para Desenvolvedores:** Reduz tempo e complexidade de desenvolvimento ao construir ou integrar aplicações de IA
**Para Aplicações de IA:** Acesso a ecossistema de fontes de dados, ferramentas e apps
**Para Usuários Finais:** Aplicações de IA mais capazes que podem acessar seus dados e tomar ações em seu nome

---

## Arquitetura MCP

O MCP segue uma **arquitetura cliente-host-servidor** com quatro componentes principais:

### 1. Aplicação (AI Host)
- Software voltado ao usuário (ex: chatbot, assistente de IA)
- Executa instâncias de clientes MCP
- Interage com usuários e coordena comunicação

### 2. Cliente MCP
- Gerencia conexões com servidores MCP
- Lida com comunicação do protocolo
- Atua como intermediário entre host e servidores

### 3. Servidor MCP
- Fornece acesso a fontes de dados ou ferramentas específicas
- Expõe recursos, prompts e ferramentas através de interfaces padronizadas
- Pode ser hospedado independentemente

### 4. Serviços Externos
- As fontes de dados ou APIs sendo conectadas (bancos de dados, APIs, sistemas de arquivos, etc.)

**Fontes:**
- [Architecture Overview](https://modelcontextprotocol.io/docs/learn/architecture)
- [Architecture Specification](https://modelcontextprotocol.io/specification/2025-06-18/architecture)
- [Understanding MCP Architecture](https://nebius.com/blog/posts/understanding-model-context-protocol-mcp-architecture)

### Como Funciona

1. **Conexão**: O host AI executa instâncias de clientes MCP que conectam a um ou mais servidores MCP
2. **Padronização**: MCP define uma forma padronizada para aplicações exporem contexto para LLMs
3. **Comunicação Bidirecional**: Permite conexões seguras e bidirecionais entre fontes de dados e ferramentas de IA
4. **Design Modular**: Separa o modelo de IA das ferramentas e dados que ele precisa acessar

---

## Status Atual e Evolução (2025)

### Cronologia Importante

- **2024**: Lançamento inicial do MCP pela Anthropic
- **Maio 2025**: Anthropic anuncia grande atualização do Claude com "Integrations" baseadas em MCP
- **Fevereiro 2025**: Artigo "MCP é o que é,现状 e未来" discute:
  - Anthropic suporta atualmente execução de servidor local
  - Planejamento para suporte oficial de implantação remota no primeiro semestre de 2025
  - Cloudflare já introduziu capacidades de implantação de servidor MCP remoto

### Claude Skills vs MCP

Discussões emergentes sugerem que **Claude Skills** podem ser ainda mais importantes que MCP em 2025. Agentes agora dependem de capacidades de execução real em vez de cadeias de prompts.

**Fontes:**
- [Introducing the Model Context Protocol](https://www.anthropic.com/news/model-context-protocol)
- [Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
- [MCP connector - Claude Docs](https://platform.claude.com/docs/en/agents-and-tools/mcp-connector)
- [MCP Status and Future](https://onevcat.com/2025/02/mcp/)
- [Agent Skills Open Standard](https://tonybai.com/2025/12/19/anthropic-agent-skills-open-standard-launch/)

---

## Implementação de Servidores MCP

### Recursos de Implementação

**Documentação Oficial:**
- [Build an MCP server](https://modelcontextprotocol.io/docs/develop/build-server) - Guia oficial para construir servidores

**Tutoriais Completos:**
- [Build an MCP Server: Complete Tutorial for Beginners](https://www.codecademy.com/article/build-an-mcp-server) - Guia para iniciantes cobrindo instalação, estrutura de projeto e código
- [Build Your First MCP Server in 6 Steps](https://towardsdatascience.com/model-context-protocol-mcp-tutorial-build-your-first-mcp-server-in-6-steps/) - Guia passo a passo
- [MCP Server Step-by-Step Guide](https://composio.dev/blog/mcp-server-step-by-step-guide-to-building-from-scrctch) - Foco em Python SDK

**Guias por Plataforma:**
- [OpenAI - Build your MCP server](https://developers.openai.com/apps-sdk/build/mcp-server/) - Guia para conectar com ChatGPT
- [IBM - How to build an MCP Server](https://www.ibm.com/think/tutorials/how-to-build-an-mcp-server) - Tutorial da IBM
- [How to Create an MCP Server in Python](https://gofastmcp.com/tutorials/create-mcp-server) - Guia Python usando FastMCP

**Recursos Adicionais:**
- [Video Tutorial](https://www.youtube.com/watch?v=RhTiAOGwbYE) - "Build Your First MCP Server and Client from Scratch"
- [MCP Server Development Guide](https://github.com/cyanheads/model-context-protocol-resources/blob/main/guides/mcp-server-development-guide.md) - Guia da comunidade
- [AWS Builder Guide](https://builder.aws.com/content/2ygVh3GU4r5UwNlKa9QWwSAsCu9/getting-started-with-mcp-servers-the-beginner-guide)

---

## Implementações e Exemplos Práticos

### Obsidian MCP Server

O [obsidian-mcp](https://github.com/StevenStavrakis/obsidian-mcp) é um servidor MCP que permite assistentes de IA interagirem com vaults do Obsidian.

**Recursos:**
- Ler e pesquisar notas no vault
- Criar novas notas e diretórios
- Editar notas existentes
- Mover e excluir notas
- Gerenciar tags (adicionar, remover, renomear)
- Pesquisar conteúdo do vault

**Instalação:**

Adicionar ao configuration do Claude Desktop:

**macOS:** `~/Library/Application Support/Claude/claude_desktop_config.json`
**Windows:** `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
    "mcpServers": {
        "obsidian": {
            "command": "npx",
            "args": ["-y", "obsidian-mcp", "/caminho/para/seu/vault"]
        }
    }
}
```

**Ferramentas Disponíveis:**
- `read-note` - Ler conteúdo de uma nota
- `create-note` - Criar nova nota
- `edit-note` - Editar nota existente
- `delete-note` - Excluir nota
- `move-note` - Mover nota para local diferente
- `create-directory` - Criar novo diretório
- `search-vault` - Pesquisar notas no vault
- `add-tags` - Adicionar tags a uma nota
- `remove-tags` - Remover tags de uma nota
- `rename-tag` - Renomear tag em todas as notas
- `manage-tags` - Listar e organizar tags
- `list-available-vaults` - Listar todos os vaults disponíveis

---

## Integrações e Ferramentas Relacionadas

### Tavily - Web Access para AI Agents

[Tavily](https://www.tavily.com/) é um mecanismo de busca em tempo real para agentes de IA e workflows RAG.

**Características:**
- APIs de Search, Extract, Map e Crawl
- Otimizado para LLMs e workflows RAG
- Resultados com citações e trechos otimizados para IA
- Alta velocidade e confiabilidade

**Benefícios:**
- Reduz alucinações com dados factualmente corretos
- Acesso a informações em tempo real
- Cobertura de nicho além dos corpora de treinamento
- Melhores decisões com contexto atualizado

**Preços:**
- **Free:** 1,000 créditos API/mês (para novos criadores)
- **Pay As You Go:** $0.008/Crédito
- **Project:** $30/mês para 4,000 créditos
- **Enterprise:** Customizável

### Claude Code Templates

[Claude Code Templates](https://www.aitmpl.com/agents) oferece templates profissionais para Anthropic Claude Code com:
- 100+ agentes
- 159+ comandos
- Configurações, hooks e MCPs
- Transformação do workflow de desenvolvimento com IA

---

## Benefícios Chave do MCP

- **Universal Standard:** Como USB-C, fornece interface comum para integrações de IA
- **Segurança:** Construído com conexões seguras em mente
- **Modularidade:** Separação limpa entre modelos de IA e fontes de dados
- **Extensibilidade:** Fácil adicionar novas fontes de dados e ferramentas
- **Adoção Crescente:** Ecossistema em crescimento com múltiplas implementações

---

## Links Úteis

### Documentação Oficial
- [MCP Documentation](https://modelcontextprotocol.io/)
- [Getting Started](https://modelcontextprotocol.io/docs/getting-started/intro)
- [Architecture](https://modelcontextprotocol.io/docs/learn/architecture)
- [Specification](https://modelcontextprotocol.io/specification/2025-06-18/architecture)

### Tutoriais e Guias
- [Codecademy MCP Tutorial](https://www.codecademy.com/article/build-an-mcp-server)
- [Towards Data Science MCP Guide](https://towardsdatascience.com/model-context-protocol-mcp-tutorial-build-your-first-mcp-server-in-6-steps/)
- [Composio MCP Guide](https://composio.dev/blog/mcp-server-step-by-step-guide-to-building-from-scrctch)

### Ferramentas e Integrações
- [Tavily - Web Search for AI](https://www.tavily.com/)
- [Obsidian MCP Server](https://github.com/StevenStavrakis/obsidian-mcp)
- [Claude Code Templates](https://www.aitmpl.com/agents)

### Artigos e Análises
- [Anthropic Engineering - Code execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp)
- [OneVcat - MCP Status](https://onevcat.com/2025/02/mcp/)
- [Nebius - Understanding MCP Architecture](https://nebius.com/blog/posts/understanding-model-context-protocol-mcp-architecture)
- [CustomGPT - MCP Architecture](https://customgpt.ai/the-model-context-protocol-mcp-architecture/)
- [Momentum AI - MCP Explained](https://www.themomentum.ai/blog/what-is-mcp-understanding-the-model-context-protocol)
