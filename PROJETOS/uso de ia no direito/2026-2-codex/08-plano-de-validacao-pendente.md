# 08 — Plano de Validação de Itens Pendentes

**Status:** Roteiro de execução
**Base:** 04-matriz-de-afirmacoes-e-validacao.md (A01, A07, A14, A16–A18, A20–A36)
**Data:** 30/08/2026

---

## 1. Objetivo

Validar todas as afirmações marcadas como "Validar externamente", "Revisar
interpretação" ou "Não publicar sem prova" na matriz, para que possam (ou não)
integrar o produto final. Enquanto não validadas, estas afirmações ficam
**fora de todo material publicável**.

## 2. Como usar este documento

Cada item tem o formato:
- **Afirmação** (código A##)
- **Status atual** (da matriz)
- **O que verificar** — pergunta/fonte exata
- **Fonte primária** — URL, documento, base de dados
- **Método de verificação** — como fazer
- **O que fazer se confirmado** / **O que fazer se não confirmado**

---

## 3. Estatísticas de adoção

### A24 — "77% dos advogados usam IA frequentemente"
- **Status:** Validar externamente
- **O que verificar:** Estudo específico: amostra, pergunta, população, data,
  metodologia. Identificar se é pesquisa nacional, seccional da OAB, ou
  instituto privado.
- **Fonte primária:** OAB-PR + Jusbrasil + ITS Rio "O Impacto da IA no Direito
  — edição 2026" (mencionado em anexo da análise crítica)
- **Método:** Extrair o PDF/relatório oficial da pesquisa. Verificar se o
  percentual é exato ou arredondado.
- **Se confirmado:** publicar com "segundo [estudo X, data, metodologia]"
- **Se não confirmado:** remover ou substituir por dado verificado

### A25 — "Adoção saltou de 11% para 30% / 37% para 80%"
- **Status:** Validar externamente / Não publicar sem prova
- **O que verificar:** Duas trajetórias conflitantes no mesmo material.
  Identificar qual estudo gerou 11%→30% e qual gerou 37%→80% (NetDocuments
  e/ou outro). Não apresentar como se fossem complementares.
- **Fonte primária:** NetDocuments "Tendências em tecnologia jurídica para 2026"
  e/ou pesquisa da OAB/Seccional
- **Método:** Extrair os relatórios. Verificar perguntas, amostras, períodos.
- **Se confirmado:** usar UMA trajetória com fonte, ou explicar que são
  estudos diferentes com metodologias distintas.
- **Se não confirmado:** remover completamente.

### A26 — "37% economizam 2–5 dias/mês"
- **Status:** Validar externamente
- **O que verificar:** Estudo de origem — amostra, pergunta exata, período.
- **Fonte primária:** Localizar estudo original citado no material de copy
- **Método:** Busca no Google/estudo referido. Se não encontrar, tratar como
  editorial/não publicado.
- **Se confirmado:** publicar com fonte e metodologia.
- **Se não:** excluir.

---

## 4. Casos de punição

### A27 — "Três advogados oficiados à OAB em 2026"
- **Status:** Não publicar sem prova
- **O que verificar:** Nomes, seções da OAB, processos ético-disciplinares,
  ou ao menos reportagem verificável com processo/número.
- **Fonte primária:** Consulta pública de processos ético-disciplinares nas
  seccionais da OAB; reportagens com número de processo.
- **Método:** Criar ficha individual para cada caso. Sem número de processo
  ou documento oficial, não publicar.
- **Se confirmado:** publicar com número do processo e data.
- **Se não:** excluir.

### A28 — "TRT-2 multou 5% + ofício à OAB"
- **Status:** Não publicar sem prova
- **O que verificar:** Número do processo, vara, data, valor, fundamento legal.
- **Fonte primária:** PJe TRT-2 (consulta pública)
- **Método:** Buscar por palavras-chave "multa 5% IA" + TRT-2. Sem decisão
  identificável, não publicar.
- **Se confirmado:** publicar com número do processo e data.
- **Se não:** excluir.

### A29 — "TST multou 1% por jurisprudência falsa"
- **Status:** Não publicar sem prova
- **O que verificar:** Número do processo, relator, data, percentual.
- **Fonte primária:** PJe TST
- **Método:** Buscar por jurisprudência falsa + TST + IA. Sem decisão, não
  publicar.
- **Se confirmado:** publicar com número do processo.
- **Se não:** excluir.

### A30 — "TJ-PR identificou 43 precedentes fictícios em um recurso"
- **Status:** Não publicar sem prova
- **O que verificar:** Número do recurso, tribunal, data, relator, quantidade
  de precedentes.
- **Fonte primária:** PJe TJ-PR, consulta de jurisprudência
- **Método:** Buscar por "43 precedentes" + TJ-PR + IA. Sem decisão, não
  publicar.
- **Se confirmado:** publicar com número do processo.
- **Se não:** excluir.

### A31 — "Casos em TJSC, TRT-3, 2ª Vara Federal de Londrina"
- **Status:** Não publicar sem prova
- **O que verificar:** Para cada tribunal, número(s) de processo.
- **Fonte primária:** PJe de cada tribunal
- **Método:** Manter como banco de pesquisa, não como prova final. Só publicar
  com processo verificado.
- **Se confirmado:** publicar individualmente com fonte.
- **Se não:** manter como nota interna.

---

## 5. Políticas de fornecedores

### A17 — "ChatGPT Plus é alto risco" (plano/configuração)
- **Status:** Validar externamente
- **O que verificar:** Termos atuais do ChatGPT Plus vs. Enterprise vs. Team.
  Política de treinamento, retenção, criptografia por plano.
- **Fonte primária:** https://openai.com/policies/privacy-policy,
  https://openai.com/enterprise-privacy/
- **Método:** Extrair e comparar por plano. Não tratar ChatGPT Plus como
  "alto risco" sem especificar o que significa — risco de dados, de
  alucinação, de compliance.

### A18 — "Enterprise não treina com dados do cliente"
- **Status:** Validar externamente
- **O que verificar:** Por fornecedor (OpenAI, Anthropic, Google, Microsoft).
  Diferenciar por plano/região/data. Confirmar se há cláusula contratual vs.
  política unilateral.
- **Fonte primária:** Páginas de privacy/enterprise de cada fornecedor.
  Links no doc 05-base-normativa-conferida.md e capítulo 5.
- **Método:** Baixar as políticas atuais e arquivar com data.

### A16 — "Ferramentas gratuitas/públicas usam prompts para treinar por padrão"
- **Status:** Não publicar sem prova
- **O que verificar:** Por ferramenta (ChatGPT free, Claude free, Gemini free,
  Copilot free). Analisar política por plano/configuração/data.
- **Fonte primária:** Políticas de privacidade de cada fornecedor.
- **Método:** Não generalizar. Especificar: "no plano gratuito do ChatGPT, a
  política X afirma que...". Verificar data de vigência.

---

## 6. Afirmações sobre ferramentas específicas

### A21 — "JUIT é a única ferramenta declarada conforme"
- **Status:** Não publicar sem prova
- **O que verificar:** Declaração de conformidade de JUIT. Com o quê? OAB?
  LGPD? ANPD? Qual o escopo? Data de validade?
- **Fonte primária:** Site da JUIT, declaração oficial.
- **Método:** Remover "única" até conseguir documento primário que comprove
  e defina escopo e prazo de validade.

### A20 — "IA local: nada sai do escritório, privacidade máxima"
- **Status:** Revisar interpretação
- **O que verificar:** "Privacidade máxima" é absoluta. Trocar por "pode
  reduzir a exposição externa". Verificar se o modelo local envia telemetria
  ou atualizações.
- **Método:** Reescrever sempre.

---

## 7. Iniciativas do Judiciário

### A22 — "Victor (STF) e Athos (STJ) como exemplos de IA no Judiciário"
- **Status:** Validar externamente
- **O que verificar:** Situação atual de Victor e Athos. Atualizar para
  Resolução CNJ nº 615/2025 como marco regulatório principal.
- **Fonte primária:** https://atos.cnj.jus.br/atos/detalhar/6001
  (CNJ 615/2025); sites do STF e STJ sobre programas de IA.
- **Método:** Verificar se Victor e Athos ainda estão ativos e em que
  estágio. 05 já aponta 615/2025 como atualização.

### A23 — "Pelo menos 13 tribunais usam IA em admissibilidade"
- **Status:** Validar externamente
- **O que verificar:** Universo (13 de quantos?), metodologia, data da
  contagem, fonte (CNJ? reportagem?).
- **Fonte primária:** CNJ — relatório de IA nos tribunais.
- **Método:** Buscar relatório CNJ mais recente. Se não encontrar, não
  publicar.

---

## 8. Promessas de resultado e linguagem comercial

### A34 — "Tarefa de 2h em 15min" / "10 horas semanais economizadas"
- **Status:** Não publicar sem prova
- **O que verificar:** Se há estudo ou caso documentado que comprove.
- **Fonte primária:** Dados do próprio produto ou estudo externo.
- **Método:** Se for hipotético, marcar explicitamente como exemplo. Se for
  promessa, remover.

### A35 — "Material resolve três erros em 1h e coloca leitor à frente de 80%"
- **Status:** Não publicar sem prova
- **O que verificar:** "Três erros" — quais? 80% — com base em quê?
- **Método:** Reescrever como orientação/implementação, não como promessa
  de posicionamento comparativo.

### A36 — "Garantia de 7 dias e entrega imediata por e-mail"
- **Status:** Validar externamente
- **O que verificar:** Se a operação comercial (hospedagem, entrega, suporte)
  suporta a promessa antes de publicar.
- **Método:** Confirmar com operação/plataforma antes de incluir em página
  de vendas.

---

## 9. Prioridade de execução

| Prioridade | Itens | Por quê |
|---|---|---|
| Alta | A24–A26 (estatísticas) | Afetam todo o discurso de mercado |
| Alta | A27–A31 (casos de punição) | Evidência mais forte do risco; sem prova viram alarmismo |
| Alta | A16–A18 (políticas de fornecedores) | Base da Parte 4 e 7 do e-book |
| Média | A21–A23 (ferramentas/Judiciário) | Conteúdo complementar, não central |
| Baixa | A34–A36 (promessas) | Linguagem comercial; remover é mais seguro que validar |

## 10. Regra de bloqueio

Nenhum item com status **Não publicar sem prova** pode aparecer como fato
em: página de vendas, e-book, FAQ, anúncio, post de Instagram, roteiro de
stories, bônus ou qualquer material público. A violação desta regra expõe
o produto a risco jurídico e reputacional.