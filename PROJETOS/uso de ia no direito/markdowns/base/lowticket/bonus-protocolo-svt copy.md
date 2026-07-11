---
tags:
  - ia-advocacia
  - bonus
  - protocolo-svt
  - lowticket
produto: "IA na Advocacia sem Violar a OAB"
metodo: "Protocolo SVT (Sigilo, Veracidade, Transparência)"
stack-valor: "R$ 541"
---

# Bônus do Protocolo SVT

Três bônus que resolvem objeções específicas e aceleram a implementação do Protocolo SVT. Cada um converte um dos três deveres da **Recomendação 001/2024 do Conselho Federal da OAB** — sigilo, veracidade e transparência — em um entregável pronto, ancorado em preço de mercado real.

**Stack de valor:** R$ 541

| Bônus | Ancora no pilar | Resolve a objeção | Valor de mercado |
| --- | --- | --- | --- |
| 01. Pack dos 7 Prompts Anti-Alucinação | **Veracidade** | "IA inventa jurisprudência, não dá pra confiar" | R$ 197 |
| 02. Mapa de Ferramentas Seguras por Perfil | **Sigilo** | "Já uso o ChatGPT do meu jeito / não sei qual ferramenta é segura" | R$ 147 |
| 03. Cláusula de Consentimento + Tabela de Anonimização | **Sigilo + Transparência** | "Tenho medo de a OAB me punir" | R$ 197 |

> Cada bônus é uma peça de implementação, não de teoria. O e-book entrega o método; os bônus entregam o atalho para aplicar o método hoje.

---

# Bônus 01 — Pack dos 7 Prompts Anti-Alucinação

**Valor de mercado: R$ 197**
**Pilar do Protocolo SVT:** Veracidade (Etapa 2)
**Objeção que resolve:** "IA inventa jurisprudência e dados, não dá pra confiar numa peça gerada por ela."

## O que é

Sete prompts prontos para copiar e colar. Todos compartilham a mesma instrução-base de segurança: usar **exclusivamente** as fontes fornecidas pelo advogado e **nunca** gerar citação, lei, súmula ou decisão fora do material colado. Cobrem as tarefas mais comuns da rotina: redação de peça, revisão de contrato, síntese de processo, antecipação de contra-argumentos e mais três.

## Por que funciona

A IA generativa não consulta um banco de tribunais — ela prevê texto provável. Quando se pede a ela que "cite uma decisão", sem fornecer a fonte, ela produz algo que parece real e não é. A causa do erro é o comando, não a ferramenta. O caso _Mata contra Avianca_ (2023), em que um advogado apresentou ao tribunal decisões inteiras que não existiam, virou referência mundial sobre o custo de confiar cegamente na saída.

Todos os prompts deste pack invertem o comando: a IA apenas **organiza, estrutura e redige a partir do material que o advogado forneceu**. Assim, cumpre-se o Art. 77 do CPC (dever de veracidade) e o item 3.2 da Recomendação 001/2024, que exige estrito cumprimento dos deveres de veracidade das informações apresentadas em juízo.

## Como usar (em 3 passos, para todos os prompts)

1. **Pesquise você mesmo** a decisão, a lei ou o documento na fonte original (tribunal, Jusbrasil, base oficial).
2. **Cole o prompt** abaixo e, na área indicada por `[COLAR FONTE]`, insira o material que você pesquisou — já anonimizado.
3. **Confira toda citação** no site do tribunal antes de protocolar (número, ementa, relator). Sempre.

> Regra do pack: se a IA trouxer uma citação que não está no material colado, ela é alucinação. Apague e siga.

---

### Prompt 1 — Redação de peça (estrutura a partir dos fatos)

**Quando usar:** petição inicial, contestação, réplica — qualquer peça em que você já tem os fatos e a tese.

```
Você é um assistente de redação jurídica. Use EXCLUSIVAMENTE o material que eu fornecer abaixo. Regras inegociáveis:
1. Não cite nenhuma lei, súmula, jurisprudência ou artigo que não esteja literalmente no texto colado.
2. Se faltar fundamento legal para algum argumento, indique "[FALTA FONTE]" e pare — não invente.
3. Não complete informações que não estejam no material.
4. Estruture a peça em: (a) dos fatos, (b) do direito, (c) do pedido.

TESE E FATOS DO CASO:
[COLAR: narrativa anonimizada dos fatos e da tese — ex.: "O cliente [CLIENTE] pleiteia [PEDIDO] contra [PARTE CONTRÁRIA] em razão de [FUNDAMENTO DE FATO]"]

FUNDAMENTOS LEGAIS PERMITIDOS (só use estes):
[COLAR: os artigos de lei e/ou decisões reais que você pesquisou e verificou na fonte original]

TAREFA:
Redija a estrutura da peça com base somente no que está acima.
```

---

### Prompt 2 — Revisão de contrato (apontamento de riscos)

**Quando usar:** análise de minuta, cláusula de risco, due diligence contratual.

```
Você é um revisor de contratos. Analise o contrato colado abaixo sob o direito brasileiro, observando estas regras:
1. Não invente nenhuma legislação, súmula ou jurisprudência. Se for citar norma, use somente as que eu listar.
2. Para cada risco apontado, indique se há base no texto fornecido ou se é observação de redação.
3. Aponte: (a) ambiguidades, (b) cláusulas abusivas aparentes, (c) omissões relevantes, (d) inconsistências internas.

NORMAS PERMITIDAS PARA CITAÇÃO (só estas):
[COLAR: ex. "CC Art. 421, 422, 423; CDC Art. 51" — liste apenas as que você confirmou em vigor]

CONTRATO A ANALISAR:
[COLAR: contrato, já anonimizado — trocar razão social, CNPJ, valores por marcadores]
```

---

### Prompt 3 — Síntese de processo (resumo estruturado)

**Quando usar:** processos longos, volume grande de páginas, onboarding de caso novo.

```
Você é um assistente de leitura processual. Resuma o documento abaixo usando SOMENTE o que está no texto. Regras:
1. Não complete, não infira e não cite fora do material colado.
2. Se o texto não trouxer um dos blocos pedidos, escreva "[não consta no material]".
3. Mantenha a exatidão de datas, prazos e valores conforme aparecem no original.

DOCUMENTO:
[COLAR: decisão, petição inteira ou conjunto de manifestações — anonimizado]

ENTREGUE EM TÓPICOS:
- Partes e polo de cada uma
- Fatos relevantes (ordem cronológica)
- Pedidos
- Fundamentos jurídicos alegados
- Pontos controvertidos
- Decisões/providências pendentes
```

---

### Prompt 4 — Antecipação de contra-argumentos

**Quando usar:** preparar a peça para a réplica, prever a tese da parte contrária, blindar a argumentação.

```
Você é um analista de argumentação jurídica. A partir EXCLUSIVAMENTE da decisão e da tese que eu colar abaixo, antecipe os contra-argumentos mais prováveis da parte contrária. Regras:
1. Não cite lei, doutrina ou precedente que não esteja no material colado.
2. Para cada contra-argumento, baseie-se em ponto específico do texto (cite o trecho).
3. Para cada contra-argumento antecipado, sugira uma linha de refutação — também restrita ao material fornecido.

DECISÃO/TESE DE REFERÊNCIA (só use esta):
[COLAR: a decisão real ou a tese que você pesquisou e verificou, anonimizada]

TAREFA:
Liste de 3 a 5 contra-argumentos prováveis e, para cada um, a refutação possível dentro do material.
```

---

### Prompt 5 — Estruturação de recurso

**Quando usar:** apelação, agravo, embargos — organizar a tese recursal a partir da decisão recorrida.

```
Você é um assistente de redação recursal. Trabalhe SOMENTE com a decisão recorrida e os fundamentos que eu fornecer. Regras:
1. Não cite dispositivo legal, súmula ou precedente fora do material colado.
2. Estruture o recurso em: (a) tempestividade, (b) legitimidade/interesse, (c) mérito recursal, (d) pedidos.
3. Para cada erro da decisão recorrida que você apontar, indique o trecho exato que fundamenta a crítica.

DECISÃO RECORRIDA:
[COLAR: a decisão na íntegra, anonimizada]

FUNDAMENTOS LEGAIS PERMITIDOS (só estes):
[COLAR: artigos e decisões reais que você confirmou na fonte original]
```

---

### Prompt 6 — Síntese de jurisprudência (a partir de decisão colada)

**Quando usar:** organizar uma decisão real para uso como precedente, sem que a IA invente outras.

```
Você é um assistente de pesquisa jurisprudencial. Abaixo está UMA decisão real que eu verifiquei na fonte. Regras absolutas:
1. Use SOMENTE esta decisão. Não cite nenhuma outra, mesmo que "relacionada".
2. Não complete dados do acórdão que não estejam no texto.
3. Se eu pedir outros precedentes, sua resposta deve ser: "Forneça as outras decisões uma a uma para eu resumir."

DECISÃO (única fonte):
[COLAR: ementa e/ou trecho relevante, com número, relator e data verificados no tribunal]

ENTREGUE:
- Teses centrais (no máximo 3)
- Trecho-chave de cada tese (citação literal)
- Como essa decisão se aplica a um caso com [NATUREZA DO CASO]
```

---

### Prompt 7 — Checklist de consistência da peça pronta

**Quando usar:** antes de protocolar — última verificação da peça que você já redigiu (com ou sem IA).

```
Você é um revisor de consistência. Analise a peça colada abaixo e aponte SOMENTE inconsistências internas e citations que não têm fonte no próprio texto. Regras:
1. Não proponha nova redação, não invente legislação, não cite fora do texto.
2. Para cada apontamento, indique o trecho exato da peça.
3. Sinalize expressamente qualquer citação de lei, súmula ou precedente que apareça sem a fonte verificável no documento.

PEÇA A REVISAR:
[COLAR: a peça final, anonimizada]

VERIFIQUE E LISTE:
- Citações sem fonte verificável
- Contradições entre seções
- Pedidos sem fundamento correspondente
- Datas/prazos/valores inconsistentes
- Erros de qualificação das partes
```

---

# Bônus 02 — Mapa de Ferramentas Seguras por Perfil de Escritório

**Valor de mercado: R$ 147**
**Pilar do Protocolo SVT:** Sigilo (Etapa 1)
**Objeção que resolve:** "Já uso o ChatGPT do meu jeito, não preciso de material nenhum" e "não sei qual ferramenta é realmente segura."

## O que é

Tabela comparativa das ferramentas de IA divididas em **três níveis de proteção de dados** — gratuito, corporativo com DPA (Acordo de Tratamento de Dados) e local — com orientação direta de qual perfil de escritório serve para cada nível.

## Por que funciona

A maioria dos advogados acha que "ChatGPT é tudo igual". Não é. A versão gratuita e a Plus podem usar suas conversas para treinar o modelo. As versões Team, Business e Enterprise, por padrão, **não** treinam com seus dados. A diferença entre uma e outra é a diferença entre quebra de sigilo e conformidade.

O Art. 34 do Estatuto da Advocacia (Lei 8.906/1994) trata o sigilo como dever absoluto. O item 2.2 da Recomendação 001/2024 exige "diligência na escolha do sistema de IA para garantir que o fornecedor irá proteger as informações". A LGPD (Lei 13.709/2018) prevê multa de até 2% do faturamento (limite de R$ 50 milhões por infração) para tratamento inadequado de dados.

Escolher o nível certo **antes** de colar o primeiro prompt é o que separa o uso seguro do uso que gera processo disciplinar.

---

## Parte 1 — Os três níveis de proteção

### Nível 1 — Gratuito / público ⚠️ Alto risco

| Aspecto | Detalhe |
| --- | --- |
| **Ferramentas** | ChatGPT gratuito, Copilot público, Gemini público, Claude gratuito |
| **Treina com seus dados?** | Sim — por padrão, prompts podem treinar o modelo |
| **Sigilo profissional** | Nenhuma proteção |
| **DPA** | Não existe nesta modalidade |
| **Conformidade LGPD** | Não — dado pessoal sem base legal válida |
| **Risco principal** | Quebra de sigilo (Art. 34), processo disciplinar OAB, multa ANPD |

> **Regra absoluta:** nunca insira dado identificável de cliente — nome, CPF, número de processo, valor, estratégia — em ferramentas de Nível 1.

### Nível 2 — Corporativo com DPA ✅ Segurança média

| Aspecto | Detalhe |
| --- | --- |
| **Ferramentas** | ChatGPT Team/Business/Enterprise, Claude for Work, Gemini Enterprise/Vertex AI, Copilot Microsoft 365 |
| **Treina com seus dados?** | Não — garantia contratual inclusa |
| **Criptografia** | Em trânsito (TLS 1.2+) e em repouso (AES-256) |
| **DPA** | Incluído — proteção jurídica contratual |
| **Conformidade LGPD** | Parcial — melhor que o gratuito, mas não é especializado em Direito brasileiro |
| **Risco remanescente** | Não entende nuances jurídicas; exige anonimização + revisão integral |

### Nível 3 — Local / jurídica especializada ✅✅ Alta segurança

| Aspecto | Detalhe |
| --- | --- |
| **Locais** | LM Studio, Ollama, GPT4All — a IA roda no seu hardware, sem internet |
| **Jurídicas** | JUIT (única declarada conforme OAB), Turivius, Jurídico AI, doc9 |
| **Treina com seus dados?** | Não — dado nunca sai do ambiente do escritório |
| **Conformidade LGPD** | Nativa nas jurídicas; nas locais, por definição |
| **Custo** | Locais: gratuitos (exige hardware ≥ 16 GB RAM). Jurídicas: planos pagos |
| **Indicação** | Dados ultrassensíveis (saúde, sigilo industrial), cliente de alto valor |

---

## Parte 2 — Qual ferramenta usar, por perfil de escritório

| Perfil | Nível recomendado | Ferramenta para começar | Próximo passo |
| --- | --- | --- | --- |
| **Advogado autônomo** | Nível 2 | ChatGPT Team (~R$ 150/mês) + U.Legal (gestão) | Adicionar Turivius para pesquisa jurisprudencial |
| **Pequeno escritório (2–10 advogados)** | Nível 2/3 | JUIT (conforme OAB) + Jurídico AI | Implementar Cognitio para conformidade LGPD |
| **Escritório com dados ultrassensíveis** (saúde, sigilo industrial, cliente de alto valor) | Nível 3 — local | LM Studio ou Ollama | Zero dado sai do hardware do escritório |

### Critérios não-negociáveis para escolher qualquer ferramenta

- [ ] Ela treina com meus dados? (precisa ser **não**)
- [ ] Oferece DPA / Acordo de Tratamento de Dados?
- [ ] A política de privacidade é clara e acessível?
- [ ] Há criptografia e controle de retenção?
- [ ] Onde os dados são processados — Brasil ou exterior?

> _Sempre confirme o DPA e a política de não-treinamento antes de fechar contrato. O que está no site de marketing da ferramenta não substitui o que está no contrato._

---

# Bônus 03 — Cláusula de Consentimento + Tabela de Anonimização

**Valor de mercado: R$ 197**
**Pilar do Protocolo SVT:** Transparência (Etapa 3) + Sigilo (Etapa 1)
**Objeção que resolve:** "Tenho medo de a OAB me punir se eu usar IA, então prefiro nem arriscar."

## O que é

Dois entregáveis num só:

1. **Modelo pronto de cláusula de consentimento informado** para contrato de honorários, redigida para cumprir o item 4 da Recomendação 001/2024.
2. **Tabela completa de anonimização** — quais dados trocar por marcador antes de qualquer prompt, e por quê.

## Por que funciona

O item 4.1.1 da Recomendação 001/2024 estabelece que o advogado que optar por usar IA deve, **previamente ao início da utilização, formalizar tal intenção ao cliente**. O item 4.3.1 exige consentimento informado **explícito**, por assinatura. E o item 4.3.4 diz que a formalização é obrigatória em **qualquer fase** da prestação — petição, pesquisa, análise de documento.

Por outro lado, o item 2.1 manda o advogado ter "especial atenção ao inserir dados que possam inadvertidamente tornar o cliente identificável". Ou seja: transparência sem anonimização não basta; anonimização sem transparência também não. Este bônus entrega os dois lados prontos.

---

## Parte 1 — Modelo de cláusula de consentimento informado

Copie e adapte ao seu contrato de honorários. Colha assinatura e arquive até o fim da prestação do serviço (item 4.3.3).

> **CLÁUSULA — USO DE INTELIGÊNCIA ARTIFICIAL**
>
> O(A) CONTRATADO(A) poderá utilizar ferramentas de Inteligência Artificial como apoio à prestação dos serviços advocatícios objeto deste contrato (pesquisa, organização, síntese e redação), comprometendo-se a:
>
> **(i)** revisar integralmente todo conteúdo gerado antes de qualquer uso;
>
> **(ii)** preservar o sigilo profissional e a proteção de dados nos termos da LGPD (Lei nº 13.709/2018), adotando anonimização prévia dos dados identificáveis;
>
> **(iii)** responder pessoalmente pela qualidade técnica das peças, não havendo delegação de atividade privativa da advocacia a sistema automatizado; e
>
> **(iv)** utilizar exclusivamente ferramentas que não utilizem os dados fornecidos para treinamento de seus modelos, na forma da Recomendação nº 001/2024 do Conselho Federal da OAB.
>
> O(A) CONTRATANTE declara estar ciente do propósito, dos benefícios, das limitações e dos riscos envolvidos, bem como das medidas de segurança adotadas, e **consente, de forma expressa e informada**, com a utilização descrita nesta cláusula. O(A) CONTRATANTE poderá, a qualquer tempo, optar por não consentir com o uso de IA, hipótese em que o serviço será prestado por meio alternativo, sem ônus adicional.

### Observações de uso

- **Linguagem clara:** o item 4.2.1 exige linguagem "clara e acessível". Se o cliente não entender um termo, reescreva — a cláusula não pode ser um obstáculo ao consentimento.
- **Direito de recusa:** o item 4.3.2 garante ao cliente o direito de não consentir. A cláusula acima já prevê o caminho alternativo.
- **Arquivamento:** mantenha o documento assinado acessível até o término da prestação, para consultas e auditorias (item 4.3.3).
- **Em qualquer fase:** vale para pesquisa, redação, análise de documentos — não só para a petição final (item 4.3.4).

---

## Parte 2 — Tabela de anonimização

Troque cada dado real pelo marcador correspondente **antes** de colar o texto em qualquer prompt. Reinsira os dados reais só no documento final, dentro do seu computador — fora da IA.

| Dado real | Marcador | Por que anonimizar |
| --- | --- | --- |
| Nome do cliente | `[CLIENTE]` | Identificação direta — núcleo do sigilo (Art. 34, Lei 8.906/1994) |
| Nome da parte contrária | `[PARTE CONTRÁRIA]` | Evita expor terceiro e contaminação cruzada de bases |
| CPF / RG | `[CPF]` / `[RG]` | Dado pessoal sensível à reidentificação (LGPD Art. 5º, II) |
| CNPJ | `[CNPJ]` | Permite vincular empresa a estratégia processual |
| Número do processo | `[Nº DO PROCESSO]` | Cruzamento público no tribunal reidentifica o caso |
| Valores (causa, honorário, contrato) | `[VALOR]` | Valor exato + localização + tempo reidentifica partes |
| Datas específicas (contratos, fatos) | `[DATA]` | Diminui risco de associação a eventos públicos |
| Endereço | `[ENDEREÇO]` | Dado de localização, especialmente sensível em família/criminal |
| Dados de saúde | `[DADO DE SAÚDE]` | Categoria sensível — LGPD Art. 5º, II e Art. 11 (proteção reforçada) |
| Dados de crianças/adolescentes | `[DADO DE CRIANÇA]` | Proteção absoluta — Art. 14 da LGPD |
| Conta bancária / cartão | `[DADO FINANCEIRO]` | Dado financeiro sensível, alvo direto de vazamento |
| E-mail / telefone do cliente | `[CONTATO]` | Identificação direta via consulta reversa |
| Nome de testemunha | `[TESTEMUNHA X]` | Evita expor terceiro que ainda não foi formalmente arrolada |

### Fluxo de uso

1. **Antes do prompt:** troque todos os dados da tabela acima pelos marcadores.
2. **Durante o prompt:** trabalhe só com a versão anonimizada.
3. **Depois do prompt:** reinsira os dados reais no documento final, no seu computador, fora da IA.
4. **Nunca** reinsira os dados reais no campo de prompt, mesmo em ferramenta de Nível 2.

> O anonimato deve resistir ao cruzamento de dados. Remover só o nome não basta se CPF, número de processo e valor permanecerem juntos — o cliente continua "inadvertidamente identificável" (item 2.1 da Recomendação 001/2024).

---

## Resumo dos três bônus

| Pilar SVT | Bônus | O que entrega | Valor |
| --- | --- | --- | --- |
| **Veracidade** | 01. Pack dos 7 Prompts | 7 prompts com trava anti-alucinação para as tarefas mais comuns | R$ 197 |
| **Sigilo** | 02. Mapa de Ferramentas | Tabela por nível de proteção + indicação por perfil de escritório | R$ 147 |
| **Sigilo + Transparência** | 03. Cláusula + Tabela de Anonimização | Cláusula de consentimento pronta + tabela de dados a anonimizar | R$ 197 |
| | | **Stack de valor** | **R$ 541** |

---

_Material educativo e informativo. Não substitui consulta jurídica específica. Baseado na Recomendação nº 001/2024 do Conselho Federal da OAB, na Lei nº 13.709/2018 (LGPD), na Lei nº 8.906/1994 (Estatuto da Advocacia) e no Art. 77 do Código de Processo Civil, na data de publicação._
