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

Três bônus que **avançam sobre o e-book** — não repetem o que você já leu. Onde o guia explica o método, estes bônus entregam o atalho operacional para o passo que normalmente trava o advogado: o prompt blindado que ele não sabe escrever, a configuração de privacidade que ele não sabe onde fica e o documento de consentimento que ele não tem pronto.

Cada um converte um dos três deveres da **Recomendação 001/2024 do Conselho Federal da OAB** — sigilo, veracidade e transparência — em um entregável que você usa ainda hoje.

**Stack de valor:** R$ 541

| Bônus | Pilar SVT | O que o e-book já cobre | O que este bônus ADICIONA | Valor de mercado |
| --- | --- | --- | --- | --- |
| 01. Pack dos 7 Prompts Anti-Alucinação | **Veracidade** | O prompt-padrão de segurança (Cap. 5) | 7 prompts blindados para as tarefas de maior risco, com exemplo aplicado | R$ 197 |
| 02. Kit de Decisão e Configuração Segura | **Sigilo** | _Quais_ ferramentas usar e os 3 níveis (Cap. 5) | _Como_ configurar cada uma e _onde_ você pode colar cada tipo de texto | R$ 147 |
| 03. Kit de Transparência e Anonimização Avançada | **Sigilo + Transparência** | A cláusula curta e os marcadores básicos (Cap. 3) | Cláusula robusta, termo avulso assinável e anonimização que resiste à reidentificação | R$ 197 |

> Regra do pacote: o e-book entrega o **método**; os bônus entregam o **atalho pronto** para aplicar o método sem precisar montar nada do zero.

---

## Como os bônus se encaixam no método

Para não usar os bônus soltos, encaixe cada um na ação correspondente do "Comece Aqui" do e-book:

| Ação do e-book | Pilar SVT | Bônus que aprofunda |
| --- | --- | --- |
| **Ação #1 — Blinde os dados** | Sigilo | Bônus 02 (configurar a ferramenta) + Bônus 03 (anonimizar de verdade) |
| **Ação #2 — Protocolo anti-alucinação** | Veracidade | Bônus 01 (os 7 prompts) |
| **Ação #3 — Formalize com o cliente** | Transparência | Bônus 03 (cláusula + termo avulso) |

A leitura do e-book é o pré-requisito. Os bônus assumem que você já entendeu _por que_ cada passo importa — e cuidam do _como fazer agora_.

---

# Bônus 01 — Pack dos 7 Prompts Anti-Alucinação

**Valor de mercado: R$ 197**
**Pilar do Protocolo SVT:** Veracidade — aprofunda a **Ação #2**
**Objeção que resolve:** "IA inventa jurisprudência e dados, não dá pra confiar numa peça gerada por ela."

## O que é — e o que ele adiciona ao e-book

O Capítulo 5 te deu o **prompt-padrão de segurança** (uma instrução-base para colar no início de qualquer tarefa). Este pack vai além: são **7 prompts completos e blindados**, um para cada tarefa de maior risco da rotina — redação de peça, revisão de contrato, síntese de processo, antecipação de contra-argumentos, recurso, jurisprudência e checagem final. Todos já trazem a trava anti-alucinação embutida e as regras de parada para a IA não preencher o que não sabe.

Você não monta prompt nenhum. Copia, cola na área indicada e usa.

## Por que funciona

A IA generativa não consulta um banco de tribunais — ela prevê texto provável. Quando se pede a ela que "cite uma decisão" sem fornecer a fonte, ela produz algo que parece real e não é. A causa do erro é o comando, não a ferramenta. O caso _Mata contra Avianca_ (EUA, 2023), em que um advogado apresentou ao tribunal decisões inteiras que não existiam, virou referência mundial sobre o custo de confiar cegamente na saída.

Todos os prompts deste pack invertem o comando: a IA apenas **organiza, estrutura e redige a partir do material que o advogado forneceu**. Isso não torna o erro "impossível" — nenhum prompt faz isso sozinho —, mas **fecha a porta de entrada da alucinação** e deixa a verificação humana como única etapa restante. É assim que você passa a cumprir, de fato, o Art. 77 do CPC (dever de veracidade) e o item 3.2 da Recomendação 001/2024.

## Como usar (em 3 passos, para todos os prompts)

1. **Pesquise você mesmo** a decisão, a lei ou o documento na fonte original (tribunal, Jusbrasil, base oficial).
2. **Cole o prompt** abaixo e, na área indicada por `[COLAR: ...]`, insira o material que você pesquisou — já pseudonimizado (ver Bônus 03).
3. **Confira toda citação** no site do tribunal antes de protocolar (número, ementa, relator). Sempre.

> Regra do pack: se a IA trouxer uma citação que não está no material colado, ela é alucinação. Apague e siga.

**Convenção dos prompts:** `[COLAR: ...]` é onde você insere conteúdo; `[CLIENTE]`, `[VALOR]` etc. são os marcadores de anonimização do Bônus 03; campos como `[NATUREZA DO CASO]` você preenche em uma linha.

---

### Prompt 1 — Redação de peça (estrutura a partir dos fatos)

**Quando usar:** petição inicial, contestação, réplica — qualquer peça em que você já tem os fatos e a tese.

```
Você é um assistente de redação jurídica. Use EXCLUSIVAMENTE o material que eu fornecer abaixo. Regras inegociáveis:
1. Não cite nenhuma lei, súmula, jurisprudência ou artigo que não esteja literalmente no texto colado.
2. Se faltar fundamento legal para algum argumento, escreva "[FALTA FONTE]" e pare — não invente.
3. Não complete informações que não estejam no material.
4. Estruture a peça em: (a) dos fatos, (b) do direito, (c) do pedido.

TESE E FATOS DO CASO:
[COLAR: narrativa pseudonimizada dos fatos e da tese — ex.: "O cliente [CLIENTE] pleiteia [PEDIDO] contra [PARTE CONTRÁRIA] em razão de [FUNDAMENTO DE FATO]"]

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
[COLAR: contrato, já pseudonimizado — trocar razão social, CNPJ, valores por marcadores]
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
[COLAR: decisão, petição inteira ou conjunto de manifestações — pseudonimizado]

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
[COLAR: a decisão real ou a tese que você pesquisou e verificou, pseudonimizada]

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
[COLAR: a decisão na íntegra, pseudonimizada]

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
3. Se eu pedir outros precedentes, responda: "Forneça as outras decisões uma a uma para eu resumir."

DECISÃO (única fonte):
[COLAR: ementa e/ou trecho relevante, com número, relator e data verificados no tribunal]

ENTREGUE:
- Teses centrais (no máximo 3)
- Trecho-chave de cada tese (citação literal)
- Como essa decisão se aplica a um caso de [NATUREZA DO CASO]
```

---

### Prompt 7 — Checklist de consistência da peça pronta

**Quando usar:** antes de protocolar — última verificação da peça que você já redigiu (com ou sem IA).

```
Você é um revisor de consistência. Analise a peça colada abaixo e aponte SOMENTE inconsistências internas e citações que não têm fonte no próprio texto. Regras:
1. Não proponha nova redação, não invente legislação, não cite fora do texto.
2. Para cada apontamento, indique o trecho exato da peça.
3. Sinalize expressamente qualquer citação de lei, súmula ou precedente que apareça sem a fonte verificável no documento.

PEÇA A REVISAR:
[COLAR: a peça final, pseudonimizada]

VERIFIQUE E LISTE:
- Citações sem fonte verificável
- Contradições entre seções
- Pedidos sem fundamento correspondente
- Datas/prazos/valores inconsistentes
- Erros de qualificação das partes
```

---

## Exemplo aplicado (Prompt 1, na prática)

Veja o que entra e o que sai — para você reconhecer um bom resultado e uma alucinação.

**O que o advogado cola (já pseudonimizado):**

```
TESE E FATOS: O cliente [CLIENTE] pleiteia indenização por danos morais contra
[PARTE CONTRÁRIA] em razão de negativação indevida após dívida já quitada.
FUNDAMENTOS PERMITIDOS: CDC Art. 43, §1º; Súmula 385 do STJ (verificada no site do STJ).
```

**Saída correta (a IA estrutura, não inventa):**

> **Dos fatos:** narrativa da quitação e da negativação posterior...
> **Do direito:** aplicação do CDC, Art. 43, §1º, quanto à exatidão dos dados em cadastro; análise da Súmula 385 do STJ quanto à preexistência de inscrição legítima... **[FALTA FONTE]** para o valor de referência da indenização — pesquisar precedente do tribunal competente.
> **Do pedido:** ...

O `[FALTA FONTE]` é o pack funcionando: em vez de inventar um precedente sobre valor, a IA **parou e sinalizou**. Esse é o comportamento que você quer — e o sinal de que a trava está ativa.

> ⚡ **Faça agora — 3 minutos:** salve os 7 prompts em uma pasta "Biblioteca de Prompts". Rode o Prompt 3 (síntese) em um processo real ainda hoje e cronometre. É a forma mais rápida de sentir o ganho sem nenhum risco.

## Checklist — Bônus 01

- [ ] Salvei os 7 prompts em local de acesso rápido
- [ ] Em toda tarefa, colei a fonte real que eu mesmo pesquisei
- [ ] Tratei todo `[FALTA FONTE]` como pendência minha, não da IA
- [ ] Conferi cada citação no tribunal antes de protocolar

---

# Bônus 02 — Kit de Decisão e Configuração Segura de Ferramentas

**Valor de mercado: R$ 147**
**Pilar do Protocolo SVT:** Sigilo — aprofunda a **Ação #1**
**Objeção que resolve:** "Já uso o ChatGPT do meu jeito" e "não sei se a ferramenta que uso é realmente segura."

## O que é — e o que ele adiciona ao e-book

O Capítulo 5 do e-book mostra **quais** ferramentas existem e classifica os **três níveis de segurança**. O que ele não resolve — e este kit resolve — é o passo que de fato trava o advogado no dia a dia:

1. **Onde** você pode colar cada tipo de texto (decisão de segundos, sem reler o capítulo).
2. **Como** ativar a proteção de privacidade em cada ferramenta — porque "desative o treinamento nas configurações" não diz onde fica o botão.
3. **O que procurar no contrato/DPA** antes de confiar em qualquer fornecedor.

> Para a tabela completa dos 3 níveis e a recomendação por perfil de escritório, consulte o **Capítulo 5**. Este bônus não repete aquela tabela — ele opera em cima dela.

---

## Parte 1 — Árvore de decisão: "Onde posso colar este texto?"

Antes de qualquer prompt, classifique o conteúdo e siga a seta. Leva 5 segundos.

```
O texto tem nome, CPF/CNPJ, nº de processo, valor exato ou estratégia do cliente?
│
├─ NÃO (lei, doutrina, jurisprudência pública, texto genérico)
│      → Pode usar qualquer ferramenta, inclusive Nível 1 (gratuita).
│
└─ SIM
       │
       ├─ Consigo pseudonimizar e o caso NÃO é ultrassensível?
       │      → Nível 2 (plano empresarial com DPA) + pseudonimização (Bônus 03).
       │
       └─ É dado ultrassensível (saúde, criança, sigilo industrial, criminal)
          ou exijo zero exposição externa?
                 → Nível 3 (IA jurídica especializada) ou IA local (dado não sai do PC).
```

**Regra absoluta:** dado identificável **nunca** entra em ferramenta de Nível 1, mesmo "só para testar".

---

## Parte 2 — Como ativar a proteção em cada ferramenta

A interface **reduz** o risco; só o contrato (DPA) **elimina**. Faça os dois: confirme a configuração e exija o DPA.

| Ferramenta | Onde confirmar a privacidade | O que garantir |
| --- | --- | --- |
| **ChatGPT (Team/Business/Enterprise)** | Não treina por padrão. Ainda assim, abra Configurações → Controles de dados e confirme | Plano com DPA assinado; controle de retenção (Enterprise) |
| **ChatGPT (gratuito/Plus)** | Configurações → Controles de dados → desligar "Melhorar o modelo para todos" | Reduz, mas **não** equivale a DPA — não use com dado de cliente |
| **Claude (for Work / API)** | Planos comerciais não treinam por padrão; confirme nas configurações da organização | Opção de retenção zero; DPA da Anthropic |
| **Gemini (Workspace Enterprise / Vertex AI)** | Não treina com dados do Workspace; confirme no painel de administração | Proteção de input e output; contrato Google Cloud |
| **Copilot (Microsoft 365)** | Opera dentro do tenant da organização; não treina sem permissão | Cobertura pelo DPA da Microsoft 365 |

> O que está no site de marketing não substitui o que está no contrato. Guarde o DPA assinado em pasta segura — ele é a sua prova de diligência (item 2.2 da Recomendação 001/2024).

---

## Parte 3 — Roteiro de leitura do DPA (o que procurar, literalmente)

Antes de fechar com qualquer fornecedor, procure **estas seis cláusulas** no contrato ou na política de privacidade. Se faltar alguma, pergunte por escrito.

- [ ] **Não-treinamento:** declaração expressa de que seus dados (prompts e arquivos) não treinam o modelo
- [ ] **Retenção e eliminação:** por quanto tempo os dados ficam e como são apagados
- [ ] **Localização e transferência internacional:** onde os dados são processados — se saírem do Brasil, há base legal para transferência internacional? (LGPD, Art. 33)
- [ ] **Papel de operador:** o fornecedor se compromete a atuar como operador, seguindo suas instruções (LGPD, Art. 39) — você é o controlador
- [ ] **Subprocessadores:** quem mais acessa os dados (terceiros, outros provedores)
- [ ] **Notificação de incidente:** prazo e forma de aviso em caso de vazamento (LGPD, Art. 48)

> ⚡ **Faça agora — 5 minutos:** abra a ferramenta que você usa hoje, confira em qual plano está e ative a configuração de privacidade da Parte 2. Se for gratuito/Plus com dado de cliente, agende a migração para um plano com DPA esta semana.

## Checklist — Bônus 02

- [ ] Classifiquei meus usos pela árvore de decisão da Parte 1
- [ ] Ativei a configuração de privacidade na minha ferramenta
- [ ] Tenho (ou solicitei) o DPA assinado e arquivado
- [ ] Li as 6 cláusulas do DPA antes de confiar dados ao fornecedor

---

# Bônus 03 — Kit de Transparência e Anonimização Avançada

**Valor de mercado: R$ 197**
**Pilar do Protocolo SVT:** Transparência + Sigilo — aprofunda as **Ações #1 e #3**
**Objeção que resolve:** "Tenho medo de a OAB me punir se eu usar IA, então prefiro nem arriscar."

## O que é — e o que ele adiciona ao e-book

O Capítulo 3 te deu a **cláusula curta** e uma **tabela básica de marcadores**. Este kit entrega as versões completas, que o e-book deliberadamente resumiu:

1. A **cláusula robusta** (quatro compromissos + direito de recusa), pronta para o contrato de honorários.
2. O **termo avulso de consentimento**, assinável, para os clientes que você já atende e que ainda não têm cláusula.
3. O método de **anonimização que resiste à reidentificação** — porque trocar só o nome não basta.

Juntos, cobrem o item 4 da Recomendação 001/2024 (transparência e consentimento) e o item 2.1 (não tornar o cliente identificável).

---

## Parte 1 — Cláusula robusta para o contrato de honorários

Versão completa da cláusula curta do Capítulo 3. Copie, adapte, colha assinatura e arquive até o fim da prestação (item 4.3.3).

> **CLÁUSULA — USO DE INTELIGÊNCIA ARTIFICIAL**
>
> O(A) CONTRATADO(A) poderá utilizar ferramentas de Inteligência Artificial como apoio à prestação dos serviços advocatícios objeto deste contrato (pesquisa, organização, síntese e redação), comprometendo-se a:
>
> **(i)** revisar integralmente todo conteúdo gerado antes de qualquer uso;
>
> **(ii)** preservar o sigilo profissional e a proteção de dados nos termos da LGPD (Lei nº 13.709/2018), adotando pseudonimização prévia dos dados identificáveis;
>
> **(iii)** responder pessoalmente pela qualidade técnica das peças, não havendo delegação de atividade privativa da advocacia a sistema automatizado; e
>
> **(iv)** utilizar exclusivamente ferramentas que não empreguem os dados fornecidos para treinamento de seus modelos, na forma da Recomendação nº 001/2024 do Conselho Federal da OAB.
>
> O(A) CONTRATANTE declara estar ciente do propósito, dos benefícios, das limitações e dos riscos envolvidos, bem como das medidas de segurança adotadas, e **consente, de forma expressa e informada**, com a utilização descrita nesta cláusula. O(A) CONTRATANTE poderá, a qualquer tempo, optar por não consentir com o uso de IA, hipótese em que o serviço será prestado por meio alternativo, sem ônus adicional.

---

## Parte 2 — Termo avulso de consentimento (para clientes ativos)

Para quem você já atende e não tem cláusula no contrato. É um documento independente, assinável, que cumpre o item 4.2.1 (I a V) da Recomendação. Imprima ou envie para assinatura eletrônica.

> **TERMO DE CIÊNCIA E CONSENTIMENTO — USO DE INTELIGÊNCIA ARTIFICIAL**
>
> Eu, **[NOME DO CLIENTE]**, no âmbito da prestação de serviços advocatícios contratada com **[NOME DO ADVOGADO/ESCRITÓRIO]**, declaro estar informado(a) de que o(a) profissional poderá utilizar ferramentas de Inteligência Artificial como apoio às seguintes atividades: **pesquisa, organização, síntese e redação**.
>
> Declaro ter sido esclarecido(a), em linguagem clara e acessível, sobre:
>
> **I.** o **propósito** do uso da IA na defesa dos meus direitos;
> **II.** os **benefícios e limitações** da tecnologia aplicada ao meu caso;
> **III.** os **riscos** envolvidos, como imprecisões nas informações geradas;
> **IV.** as **medidas de segurança e confidencialidade** adotadas, incluindo a pseudonimização dos meus dados e o uso apenas de ferramentas que não os utilizam para treinamento;
> **V.** a garantia de **revisão humana integral** de todo conteúdo antes de qualquer uso.
>
> Estou ciente de que **posso recusar** o uso de IA a qualquer tempo, hipótese em que o serviço será prestado por meio alternativo, sem prejuízo à minha defesa.
>
> ( ) **Consinto** com o uso de IA nos termos acima.
> ( ) **Não consinto** com o uso de IA.
>
> Local e data: ___________________
> Assinatura do(a) cliente: ___________________

**E-mail para acompanhar o termo (clientes ativos):**

> _"[Nome], passamos a utilizar ferramentas de Inteligência Artificial como apoio em tarefas de organização, pesquisa e redação — com revisão humana completa em tudo que é produzido e sem inserir seus dados em ferramentas públicas. Segue em anexo o termo de uso de IA para sua ciência e assinatura. Você pode recusar a qualquer momento. Qualquer dúvida, estou à disposição."_

---

## Parte 3 — Anonimização que resiste à reidentificação

Esta é a diferença entre o e-book e o bônus: o capítulo te deu marcadores; aqui você aprende a **não ser identificável de verdade**.

### Primeiro, o conceito correto: é pseudonimização

Trocar nomes por marcadores e **guardar a correspondência** para reinserir os dados depois é, tecnicamente, **pseudonimização** (reversível — LGPD, Art. 5º, XIII), não anonimização (irreversível — Art. 5º, XI). A distinção importa: como o dado continua reversível, a proteção depende de você manter a chave **fora da IA**, no seu computador. Para o público leigo, "anonimizar" basta; para você, advogado, saber que é pseudonimização é o que sustenta a diligência.

### Fluxo de uso

1. **Antes do prompt:** troque todos os dados identificáveis pelos marcadores da tabela abaixo.
2. **Durante o prompt:** trabalhe só com a versão pseudonimizada.
3. **Depois do prompt:** reinsira os dados reais no documento final, no seu computador, **fora da IA**.
4. **Nunca** reinsira dados reais no campo de prompt, mesmo em ferramenta de Nível 2.

### O teste de reidentificação (faça antes de colar)

Remover o nome não basta. Pergunte-se:

> _Mesmo sem o nome, alguém conseguiria chegar no meu cliente cruzando o que sobrou — número de processo + valor + comarca + data?_

Se a resposta for "sim", **generalize mais**: troque o valor exato por faixa (`[VALOR APROX]`), a data por mês/ano, e remova a comarca. O cliente continua "inadvertidamente identificável" (item 2.1 da Recomendação) enquanto o conjunto permitir o cruzamento — especialmente em processos públicos.

### Tabela-mestre de marcadores

Este é o conjunto canônico do produto. O Capítulo 3 usa um subconjunto reduzido; use **esta** tabela como referência completa.

| Dado real | Marcador | Por que pseudonimizar |
| --- | --- | --- |
| Nome do cliente | `[CLIENTE]` | Identificação direta — núcleo do sigilo (Art. 7º e 34, Lei 8.906/1994) |
| Nome da parte contrária | `[PARTE CONTRÁRIA]` | Evita expor terceiro e contaminação cruzada de bases |
| CPF / RG | `[CPF]` / `[RG]` | Dado pessoal que permite reidentificação (LGPD, Art. 5º, I) |
| CNPJ | `[CNPJ]` | Vincula empresa à estratégia processual |
| Número do processo | `[Nº DO PROCESSO]` | Cruzamento público no tribunal reidentifica o caso |
| Valores (causa, honorário, contrato) | `[VALOR]` / `[VALOR APROX]` | Valor exato + local + tempo reidentifica as partes |
| Datas específicas | `[DATA]` | Diminui a associação a eventos públicos |
| Endereço | `[ENDEREÇO]` | Localização — sensível em família e criminal |
| Comarca / Vara | `[COMARCA]` / `[VARA]` | Estreita o universo de identificação |
| Dados de saúde | `[DADO DE SAÚDE]` | Categoria sensível — LGPD, Art. 5º, II e Art. 11 |
| Dados de crianças/adolescentes | `[DADO DE CRIANÇA]` | Tratamento no melhor interesse — LGPD, Art. 14 |
| Conta bancária / cartão | `[DADO FINANCEIRO]` | Dado financeiro, alvo direto de vazamento |
| E-mail / telefone do cliente | `[CONTATO]` | Identificação por consulta reversa |
| Nome de testemunha | `[TESTEMUNHA X]` | Protege terceiro ainda não arrolado |

### Cuidados extras por área do Direito

O que é "identificável" muda conforme a matéria. Reforce a pseudonimização nestes pontos:

| Área | Atenção redobrada com |
| --- | --- |
| **Família** | Endereço, dados de crianças (Art. 14, LGPD), saúde e relatos de violência |
| **Criminal** | Identidade de vítimas e testemunhas, dados de investigação e antecedentes |
| **Trabalhista** | Dados de saúde (afastamentos), salário e identidade de colegas de trabalho |
| **Empresarial / contratos** | Segredo industrial, faturamento, estratégia comercial e cláusulas confidenciais |

> ⚡ **Faça agora — 10 minutos:** cole a cláusula da Parte 1 no seu contrato-modelo e salve o termo da Parte 2 como arquivo separado para clientes ativos. Todo cliente novo já entra coberto a partir de hoje.

## Checklist — Bônus 03

- [ ] Cláusula robusta no contrato-modelo
- [ ] Termo avulso salvo e enviado aos clientes ativos
- [ ] Aplico o teste de reidentificação antes de colar qualquer texto
- [ ] Mantenho a chave de pseudonimização fora da IA
- [ ] Arquivo o consentimento assinado até o fim da prestação

---

## Resumo dos três bônus

| Pilar SVT | Bônus | O que ADICIONA ao e-book | Valor |
| --- | --- | --- | --- |
| **Veracidade** | 01. Pack dos 7 Prompts | 7 prompts blindados por tarefa + exemplo aplicado | R$ 197 |
| **Sigilo** | 02. Kit de Decisão e Configuração | Árvore de decisão + configuração por ferramenta + leitura do DPA | R$ 147 |
| **Sigilo + Transparência** | 03. Transparência e Anonimização | Cláusula robusta + termo avulso + anonimização anti-reidentificação | R$ 197 |
| | | **Stack de valor** | **R$ 541** |

---

_Material educativo e informativo. Não substitui consulta jurídica específica. Baseado na Recomendação nº 001/2024 do Conselho Federal da OAB, na Lei nº 13.709/2018 (LGPD), na Lei nº 8.906/1994 (Estatuto da Advocacia) e no Art. 77 do Código de Processo Civil, na data de publicação._
