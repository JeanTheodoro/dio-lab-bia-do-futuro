# 🌅 Aurora — Assistente Financeira Inteligente

> Agente financeiro com IA Generativa, desenvolvido como solução ao desafio [DIO Lab: Bia do Futuro](https://github.com/digitalinnovationone/dio-lab-bia-do-futuro).

---

## 💡 Sobre o Projeto

Segundo pesquisa da CNN Brasil, **43% dos brasileiros não têm dinheiro guardado para imprevistos**. A maioria gasta mais do que deveria, não tem hábito de gerir as próprias finanças e não consegue planejar o futuro — falta clareza para tomar boas decisões financeiras.

A **Aurora** é uma assistente financeira educativa e proativa que transforma dados financeiros em decisões simples e acessíveis. O usuário não precisa entender planilhas ou relatórios: ele só precisa perguntar.

> 🎥 **Pitch de apresentação:** [youtu.be/aUGv6n3p3QA](https://youtu.be/aUGv6n3p3QA)

---

## 🤖 Persona

| | |
|---|---|
| **Nome** | Aurora (Educadora Financeira) |
| **Público-alvo** | Iniciantes em finanças pessoais |
| **Tom** | Educado, amigável, claro e objetivo |
| **Regras** | Nunca inventa informações, nunca julga gastos, nunca corrige a escrita do cliente |

**Capacidades:**
- Consulta de saldo, transações, débitos e créditos
- Sugestão de investimentos alinhada ao perfil do cliente (conservador, moderado ou arrojado)
- Apoio ao planejamento de metas financeiras
- Interação por **texto e áudio**

---

## 🎬 Demonstração

![Demonstração da Aurora em funcionamento](https://github.com/JeanTheodoro/dio-lab-bia-do-futuro/raw/main/assets/demostraca-da_aplicacao_aurora.gif)

---

## 🏗️ Arquitetura

![Arquitetura do projeto Aurora](https://github.com/JeanTheodoro/dio-lab-bia-do-futuro/raw/main/assets/aquitetura_chat_bot_aurora.png)

```
Usuário (Streamlit UI)
        ↓
Router FastAPI  →  POST /api/v1/ask_assistent_ia
        ↓
  detectar_intencao()         ← identifica: transação | investimento | meta
        ↓
  ContextBuilder.build()      ← consulta banco via SQLAlchemy (apenas dados relevantes)
        ↓
  Human Prompt enriquecido    ← dados do cliente + transações + metas + produtos
        ↓
  LLM (gemma3 via Ollama)
        ↓
  Resposta contextualizada e segura
```

> Os dados **não** vão no system prompt — são consultados dinamicamente e injetados no `human_prompt`, reduzindo alucinações e melhorando a performance.

---

## 📁 Estrutura do Repositório

```
📁 dio-lab-bia-do-futuro/
├── 📄 README.md
├── 📄 index.html                        # Interface web da Aurora
├── 📁 src/                              # Código-fonte (Python + FastAPI)
│   └── api/llm/services/
│       ├── context_builder.py           # Monta contexto dinâmico para o prompt
│       └── ...
├── 📁 data/
│   ├── base_de_conhecimento/            # CSVs com dados fictícios dos clientes
│   └── sql/
│       ├── criar_tabelas.sql            # Schema do banco de dados
│       └── inserir_dados.sql            # Carga inicial dos dados
├── 📁 docs/                             # Documentação completa do projeto
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
├── 📁 assets/                           # Imagens e diagramas
└── 📁 examples/                         # Referências de implementação
```

---

## 📄 Documentação

### [01 — Documentação do Agente](./docs/01-documentacao-agente.md)
Define o caso de uso, a persona Aurora, a arquitetura do sistema e as regras de segurança anti-alucinação. O agente responde apenas com base nos dados fornecidos, identificando a intenção da pergunta por palavras-chave para buscar somente o contexto necessário.

### [02 — Base de Conhecimento](./docs/02-base-conhecimento.md)
Descreve o banco de dados relacional modelado a partir dos dados mockados originais. Inclui o diagrama entidade-relacionamento com as tabelas `clientes`, `contas_correntes`, `transacoes`, `produtos_financeiros`, `contas_investimento`, `metas` e `historico_atendimentos`, além dos scripts SQL de criação e carga de dados.

### [03 — Prompts do Agente](./docs/03-prompts.md)
Documenta o system prompt completo, exemplos de interação (Few-Shot Prompting) e o tratamento de edge cases como perguntas fora do escopo, solicitações de dados sensíveis e perguntas sem contexto. Registra também os aprendizados sobre redução de contexto para melhorar a precisão das respostas.

### [04 — Métricas de Avaliação](./docs/04-metricas.md)
Define os critérios de qualidade do agente com cenários de teste reais:

| Métrica | O que avalia |
|---|---|
| Assertividade | O agente respondeu o que foi perguntado? |
| Segurança | Evitou inventar informações fora do contexto? |
| Coerência | A resposta faz sentido para o perfil do cliente? |

### [05 — Pitch](./docs/05-pitch.md)
Roteiro do pitch de 3 minutos com o problema, a solução, demonstração prática e diferencial da Aurora. Link do vídeo: [youtu.be/aUGv6n3p3QA](https://youtu.be/aUGv6n3p3QA).

---

## 🗄️ Base de Dados

| Arquivo | Descrição |
|---|---|
| `clientes.csv` | Perfil e dados dos clientes |
| `contas_correntes.csv` | Saldo atual da conta |
| `transacoes.csv` | Histórico de débitos e créditos |
| `produtos_financeiros.csv` | Produtos disponíveis para investimento |

> Todos os dados são **fictícios**, criados exclusivamente para fins didáticos.

---

## 🛠️ Tecnologias

| Camada | Tecnologia |
|---|---|
| Interface | Streamlit + HTML |
| API | FastAPI (Python) |
| LLM | gemma3 via Ollama |
| Banco de Dados | PostgreSQL (SQLAlchemy + PLpgSQL) |
| Orquestração | LangChain |

---

## 👤 Autor

**Jean Theodoro** — Desafio DIO: *Bia do Futuro — Agente Financeiro com IA Generativa*

[![GitHub](https://img.shields.io/badge/GitHub-JeanTheodoro-181717?style=flat&logo=github)](https://github.com/JeanTheodoro)
