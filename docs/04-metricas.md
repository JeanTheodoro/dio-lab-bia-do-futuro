# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação pode ser feita de duas formas complementares:

1. **Testes estruturados:** Você define perguntas e respostas esperadas;
2. **Feedback real:** Pessoas testam o agente e dão notas.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |

> [!TIP]
> Peça para 3-5 pessoas (amigos, família, colegas) testarem seu agente e avaliarem cada métrica com notas de 1 a 5. Isso torna suas métricas mais confiáveis! Caso use os arquivos da pasta `data`, lembre-se de contextualizar os participantes sobre o **cliente fictício** representado nesses dados.

---

## Exemplos de Cenários de Teste

Crie testes simples para validar seu agente:

### Teste 1: Consulta de gastos
- **Teste com o usuario 10000**
- **Pergunta:** "Aurora, Quanto gastei com alimentação ?"
- **Resposta:** João, identifiquei uma transação com a descrição "Supermercado mensal" no valor de 930.00. Este foi o único gasto com alimentação registrado nas suas últimas transações.
- **Resposta esperada:** 
    ```sql
    SELECT 
        t.categoria, 
        t.valor, 
        t.tipo_operacao, 
        t.descricao
    FROM contas_correntes cc
    INNER JOIN transacoes t 
        ON cc.id = t.conta_corrente_id
    WHERE cc.cod_conta_corrente = 10000
    AND t.tipo_operacao = 'debito'
    ORDER BY t.created_at DESC
    LIMIT 10;
    ```

    |Categoria       | Valor   | Tipo Operação | Descrição               |
    |----------------|---------|---------------|-------------------------|
    | lazer          | 650.00  | debito        | Viagem curta            |
    | conta_agua     | 118.00  | debito        | Conta de água           |
    | conta_luz      | 220.00  | debito        | Conta de luz            |
    | farmacia       | 150.00  | debito        | Farmácia                |
    | combustivel    | 610.00  | debito        | Combustível carro       |
    | ipva           | 1600.00 | debito        | Pagamento IPVA          |
    |**supermercado** | **930.00** | **debito** | **Supermercado mensal**|
    | iptu           | 850.00  | debito        | Pagamento IPTU          |
    | aluguel        | 3200.00 | debito        | Aluguel apartamento     |
    | lazer          | 380.00  | debito        | Cinema e jantar         |

**Obs:** Os dados da tabela acima, poder ser acessado no arquivo [dado da tabela de transações](../data/sql/inserir_dados.sql)
na linha 53.

- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 2: Recomendação de produto
- **Teste com o usuario 10002**

- **Pergunta:** "Qual investimento você recomenda para mim?"

- **Resposta esperada:** Carlos Pereira, considerando seu perfil de investidor arrojado e sua tolerância ao risco, sugiro que você avalie o investimento em Ações Tech Brasil, ETF BOVA11 ou ETF IVVB11. Esses investimentos apresentam alto risco, mas também potencial de alta rentabilidade, alinhados com sua disposição para assumir riscos maiores. Caso prefira opções com menor risco, o Tesouro Selic ou o CDB Banco XPTO também são boas alternativas, com rentabilidade atrelada ao CDI. Para mais informações e auxílio na escolha, sugiro consultar um profissional do banco.

- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 3: Pergunta fora do escopo
- **Teste com o usuario 10000**
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** 
    Prezado João Silva,
    Não tenho acesso a informações sobre a previsão do tempo. Sou uma assistente financeira e posso fornecer informações sobre sua conta, metas e investimentos.
    Caso necessite de informações sobre o clima, sugiro consultar um aplicativo ou site de meteorologia.

    Obrigado! 😊
- **Resultado:** [X] Correto  [ ] Incorreto

### Teste 4: Informação inexistente
- **Teste com o usuario 10001**

- **Pergunta:** "Quanto rende o produto XYZ?"

- **Resposta esperada:** Maria Souza, o produto XYZ não possui investimentos cadastrados em sua conta. Além disso, seu perfil investidor é conservador e você não aceita riscos. Por gentileza, entre em contato com um de nossos profissionais na agência mais próxima para que possamos ajudá-lo melhor. 😊

- **Resultado:** [x] Correto  [ ] Incorreto

---

## Resultados

Após os testes, registre suas conclusões:

**O que funcionou bem:**
- [Liste aqui]

**O que pode melhorar:**
- [Liste aqui]

---

## Métricas Avançadas (Opcional)

Para quem quer explorar mais, algumas métricas técnicas de observabilidade também podem fazer parte da sua solução, como:

- Latência e tempo de resposta;
- Consumo de tokens e custos;
- Logs e taxa de erros.

Ferramentas especializadas em LLMs, como [LangWatch](https://langwatch.ai/) e [LangFuse](https://langfuse.com/), são exemplos que podem ajudar nesse monitoramento. Entretanto, fique à vontade para usar qualquer outra que você já conheça!