# IA na Advocacia Sem Violar a OAB

### O método em 3 passos para usar inteligência artificial com segurança jurídica, proteger o sigilo do cliente e nunca cair na mira da Ordem

**Ao final destas páginas, você vai saber exatamente o que pode e o que não pode fazer com IA — e vai começar a usar a tecnologia hoje, sem medo de representação, vazamento de dados ou jurisprudência inventada.**

---

## O Que Realmente Importa

O medo de usar IA na advocacia quase nunca vem do lugar certo.

A maioria dos advogados acha que o risco é "usar IA". Está errado. A OAB **não proíbe** o uso de inteligência artificial. A Recomendação nº 001/2024 do Conselho Federal autoriza o uso — desde que você respeite três deveres que já existiam antes de qualquer IA: **sigilo, veracidade e transparência.**

A punição nunca vem do fato de você ter usado a ferramenta. Vem de violar um desses três deveres. E dá para violar os três com ou sem tecnologia — num e-mail descuidado, num modelo de petição baixado sem conferir, num dado de cliente jogado em qualquer lugar.

O erro mais comum é o oposto do que você imagina: não é usar IA demais, é usar **sem método**. O advogado que cola um contrato inteiro no ChatGPT grátis e pede "me resume isso" cometeu duas infrações em dez segundos — quebrou sigilo e expôs dado pessoal — e nem percebeu.

A verdade que pouca gente conta: existem **três pontos de risco**, e cada um tem uma solução simples e definitiva. Resolvidos os três, você usa IA com mais segurança do que a maioria dos seus colegas usa o WhatsApp.

Nas próximas páginas você vai dominar:

1. Como **blindar os dados** antes de qualquer prompt (sigilo + LGPD).
2. O **protocolo anti-alucinação** que torna impossível citar jurisprudência falsa.
3. Como **formalizar com o cliente** em uma cláusula pronta para copiar.

Sem teoria. Direto ao que te protege.

---

## Ação #1 — Blinde os Dados Antes do Primeiro Prompt

**Este é o risco mais grave e o mais invisível.** É onde você se expõe sem perceber.

### O que fazer

Nunca insira dado que identifique o cliente em uma IA que usa seus dados para treinamento. Ou você anonimiza o texto, ou você usa uma ferramenta que não treina com o que você digita. De preferência, os dois.

### Como fazer (passo a passo)

1. **Escolha a ferramenta certa.** Pare de usar a versão grátis/Plus para dado real de cliente. Use uma versão empresarial que não treina com seus dados (lista na página de Curadoria).
2. **Anonimize antes de colar.** Troque nomes, CPF, CNPJ, valores exatos e números de processo por marcadores: `[CLIENTE]`, `[PARTE CONTRÁRIA]`, `[VALOR]`, `[DATA]`.
3. **Trabalhe com a versão anonimizada** e só reinsira os dados reais no documento final, dentro do seu computador — fora da IA.
4. **Confira a política de privacidade** da ferramenta: procure por "não usamos seus dados para treinar" e por DPA (Acordo de Tratamento de Dados).

### Exemplo real

Em vez de colar: _"O cliente João da Silva, CPF 123.456.789-00, processo 0801234-55.2025..."_, você escreve: _"O cliente [CLIENTE], no processo [Nº], pleiteia [PEDIDO] contra [PARTE CONTRÁRIA]."_ A IA estrutura o argumento igual — e nenhum dado sensível saiu do seu controle.

### Por que isso importa

O Art. 34 do Estatuto da Advocacia (Lei 8.906/1994) trata o sigilo como dever absoluto. A Recomendação 001/2024 exige diligência na escolha da ferramenta e atenção redobrada para não tornar o cliente identificável. E a LGPD prevê multa de até 2% do faturamento (limite de R$ 50 milhões por infração) para tratamento inadequado de dados.

### Erro comum

Achar que "ChatGPT é tudo igual". **Não é.** A versão gratuita e a Plus podem usar suas conversas para treinar o modelo. As versões Team, Business e Enterprise, por padrão, **não** treinam com seus dados. A diferença entre uma e outra é a diferença entre quebra de sigilo e conformidade.

### Checklist

- [ ] Identifiquei qual ferramenta de IA eu uso hoje e se ela treina com meus dados
- [ ] Criei meus marcadores de anonimização (`[CLIENTE]`, `[VALOR]`, etc.)
- [ ] Verifiquei a política de privacidade da ferramenta
- [ ] Parei de usar versão grátis para dado real de cliente

### Exercício (faça agora)

Pegue a última peça que você redigiu. Reescreva o trecho que você colaria numa IA, já anonimizado. Em 5 minutos você terá seu primeiro "modelo seguro" — e vai reusar esse padrão para sempre.

---

## Ação #2 — Aplique o Protocolo Anti-Alucinação

**Este é o risco mais visível — o que já fez advogados serem multados e ter ofício enviado à OAB.**

### O que fazer

Nunca peça à IA para "citar jurisprudência". A IA generativa não consulta tribunal — ela prevê texto provável. Peça a ela apenas para **organizar e estruturar argumentos a partir de fontes que VOCÊ forneceu.**

### Como fazer (passo a passo)

1. **Pesquise a jurisprudência você mesmo** (nos tribunais, Jusbrasil, bases oficiais).
2. **Cole a decisão real** dentro do prompt e peça: _"Use somente esta decisão. Não invente nenhuma outra."_
3. **Peça à IA para estruturar**, não para descobrir: redação, organização, contra-argumentos.
4. **Confira toda citação** no site do tribunal antes de protocolar. Número, ementa, relator. Sempre.

### Exemplo real

Em março de 2026, a 6ª Turma do TST multou uma empresa **e seu advogado** em 1% sobre o valor da causa por contrarrazões com jurisprudência inexistente — provavelmente gerada por IA. O relator foi direto: a responsabilidade de verificar é **integralmente do advogado.** Foram enviados ofícios à OAB e ao Ministério Público. Em fevereiro de 2026, o TRT-2 aplicou multa de 5% em caso parecido — e o advogado tentou culpar o estagiário. Não colou: o dever de supervisão é dele.

### Por que isso importa

O Art. 77 do CPC impõe o dever de veracidade. A Recomendação 001/2024 exige a **revisão integral** de tudo que a IA gera antes de ir a juízo. Citar precedente falso pode virar litigância de má-fé — e, segundo os tribunais, em casos graves, até comunicação criminal.

### Erro comum

Confiar na IA porque "a resposta parecia perfeita". Alucinação é exatamente isso: a informação inventada vem **convincente**, com número de processo plausível e ementa coerente. Quanto mais bem-feita parece, mais perigosa é se você não conferiu na fonte.

### Checklist

- [ ] Nunca peço jurisprudência "do nada" para a IA
- [ ] Sempre alimento a IA com a decisão real que eu mesmo pesquisei
- [ ] Confiro toda citação no site do tribunal antes de protocolar
- [ ] Reviso integralmente a peça — a IA estrutura, eu respondo por ela

### Exercício (faça agora)

Monte seu prompt-padrão de segurança e salve: _"Use exclusivamente as fontes que eu colar abaixo. Não cite nenhuma lei, súmula ou decisão que não esteja no texto fornecido. Se faltar informação, pergunte — não invente."_ Cole isso no início de toda tarefa jurídica.

---

## Ação #3 — Formalize o Uso com o Cliente

**O passo que quase ninguém dá — e que a Recomendação trata como obrigatório quando você decide usar IA no caso.**

### O que fazer

Antes de usar IA na prestação do serviço, informe o cliente por escrito e obtenha o consentimento dele. Simples assim — e é o que separa o uso transparente do uso que pode ser questionado.

### Como fazer (passo a passo)

1. **Inclua uma cláusula** de uso de IA no contrato de honorários (ou um termo avulso).
2. **Explique em linguagem clara:** propósito, benefícios, limitações, riscos e as medidas de segurança que você adota.
3. **Garanta a revisão humana** e o direito do cliente de falar com você, não só com a máquina.
4. **Colha a assinatura** e arquive o documento até o fim da prestação do serviço.

### Modelo de cláusula (copie e adapte)

> _"O(A) CONTRATADO(A) poderá utilizar ferramentas de Inteligência Artificial como apoio à prestação dos serviços advocatícios (pesquisa, organização e redação), comprometendo-se a: (i) revisar integralmente todo conteúdo antes de qualquer uso; (ii) preservar o sigilo profissional e a proteção de dados nos termos da LGPD (Lei 13.709/2018); e (iii) responder pessoalmente pela qualidade técnica das peças. O(A) CONTRATANTE declara estar ciente e de acordo com tal utilização."_

### Por que isso importa

O item 4 da Recomendação 001/2024 pede transparência e consentimento informado por escrito. O cliente tem direito de saber e de optar por não usar IA. Documentar isso te protege em qualquer auditoria, fiscalização ou questionamento futuro.

### Erro comum

Achar que "é só uma ferramenta, não preciso avisar". A norma é clara: a formalização vale para **qualquer fase** em que você decida usar IA — petição, pesquisa, análise de documentos. Sem o aviso, você perde a camada mais fácil de proteção.

### Checklist

- [ ] Tenho uma cláusula de IA pronta no meu contrato-modelo
- [ ] Explico ao cliente em linguagem acessível
- [ ] Colho assinatura e arquivo o documento
- [ ] Respeito o cliente que não quiser o uso de IA

### Exercício (faça agora)

Copie a cláusula acima para o seu contrato-modelo padrão. Pronto — todo cliente novo já entra coberto.

---

## Curadoria Premium

**Só esta página economiza horas de pesquisa. Use como mapa de decisão.**

### Ferramentas que NÃO treinam com seus dados (uso seguro)

| Ferramenta              | Versão segura              | Observação                                                                                           |
| ----------------------- | -------------------------- | ---------------------------------------------------------------------------------------------------- |
| **ChatGPT (OpenAI)**    | Team, Business, Enterprise | Por padrão não treina; criptografia AES-256, SOC 2. A Plus/grátis **não** serve para dado de cliente |
| **Claude (Anthropic)**  | Claude for Work, API       | Planos comerciais não treinam por padrão; opção de retenção zero                                     |
| **Gemini (Google)**     | Enterprise / Vertex AI     | Não treina com dados do Workspace; protege input e output                                            |
| **Copilot (Microsoft)** | Microsoft 365              | Opera dentro do ambiente seguro da sua organização                                                   |

### Privacidade máxima — IA local (dado nunca sai do seu PC)

- **LM Studio** — grátis, roda no seu computador (mínimo: 16 GB RAM). Interface amigável.
- **Ollama** — grátis, leve, roda modelos abertos (Llama, Mistral, Qwen) localmente.
- _Ideal para escritório boutique e dado ultrassensível: zero risco de vazamento externo._

### Legaltechs brasileiras (já nascem pensando em LGPD)

- **Locus.IA** — arquitetura local/híbrida, processamento no ambiente do cliente.
- **Bits AI** — feita por advogados, promete não armazenar documentos nem treinar com seus dados.
- **Juridico.ai** — foco em pesquisa jurisprudencial.
- _Sempre confirme o DPA e a política de não-treinamento antes de fechar._

### Checklist de escolha de qualquer ferramenta

- [ ] Ela treina com meus dados? (precisa ser NÃO)
- [ ] Oferece DPA / Acordo de Tratamento de Dados?
- [ ] A política de privacidade está clara e acessível?
- [ ] Tem criptografia e controle de retenção?

### Prompts prontos para o dia a dia (já com segurança embutida)

- **Resumo de processo:** _"Resuma o documento abaixo em tópicos: fatos, pedidos, fundamentos e pontos controvertidos. Use só o que está no texto. [colar texto anonimizado]"_
- **Revisão de cláusula:** _"Aponte riscos e ambiguidades nesta cláusula sob o direito brasileiro. Não invente legislação. [colar cláusula]"_
- **Estruturar argumento:** _"Organize um argumento a partir EXCLUSIVAMENTE da decisão que vou colar. Não cite nenhuma outra. [colar decisão real]"_

---

## Plano de Implementação

Você não precisa de meses. Precisa de uma sequência.

### HOJE (próximas 2 horas)

1. Defina **qual ferramenta segura** você vai adotar (escolha uma da Curadoria).
2. Crie seus **marcadores de anonimização** e seu **prompt-padrão de segurança**.
3. Cole a **cláusula de IA** no seu contrato-modelo.

### PRÓXIMOS 7 DIAS

- Use a IA em **uma tarefa de baixo risco por dia** (resumo, organização de pesquisa, revisão de texto sem dado sensível).
- Sempre anonimize. Sempre confira citação na fonte. Sempre revise.
- Anote quanto **tempo** cada tarefa economizou.

### PRÓXIMOS 30 DIAS

- **Meta:** ter as tarefas repetitivas (resumos, modelos, organização) rodando com IA de forma segura e padronizada.
- **Como medir:** compare as horas que você gastava antes com as de agora. A maioria recupera entre 5 e 10 horas por semana.
- Se tiver equipe: estabeleça uma **política interna de uso** (o item 3.6 da Recomendação exige supervisão de quem você gerencia).

### Checklist final — imprima e marque

- [ ] Escolhi uma ferramenta que não treina com meus dados
- [ ] Anonimizo todo dado de cliente antes do prompt
- [ ] Nunca peço jurisprudência "do nada" — só estruturo a partir de fonte que forneço
- [ ] Confiro toda citação no tribunal antes de protocolar
- [ ] Reviso integralmente tudo que a IA gera
- [ ] Tenho cláusula de IA assinada pelo cliente
- [ ] Arquivo o termo de consentimento
- [ ] (Com equipe) Tenho política interna de uso de IA

---

**Você agora sabe onde estão as três linhas. Sigilo, veracidade e transparência. Quem domina essas três usa IA de cabeça erguida — e deixa para trás quem ficou parado por medo.**

_Material educativo e informativo. Não substitui consulta jurídica específica. Baseado na Recomendação nº 001/2024 do Conselho Federal da OAB e na legislação vigente na data de publicação._
