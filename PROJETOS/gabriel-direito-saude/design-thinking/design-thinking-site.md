# Design Thinking — Site Gabriel Direito & Saúde
## Inspiração: Sinzinger Advocacia (sinzingeradvocacia.com.br)

> **Propósito:** Este documento é o resultado de uma extração completa do site Sinzinger Advocacia (3 landing pages + home + informações técnicas), analisado por 4 subagentes especializados em paralelo. O objetivo não é copiar, mas extrair padrões de conversão, arquitetura de conteúdo e estratégia de marketing que funcionam para um escritório de Direito à Saúde, e adaptá-los ao projeto do Gabriel.

---

## 1. EMPATIA + DEFINIÇÃO

### Personas

**Pai/mãe de criança autista** — recebeu negativa do plano de saúde para terapia ABA (Análise do Comportamento Aplicada, a metodologia padrão ouro). O plano alega carência contratual, clínica distante, lista de espera, ou que a metodologia "não está no contrato". Dores: desespero com o desenvolvimento da criança — "cada dia sem tratamento compromete a neuroplasticidade infantil". Busca: tratamento integral, sem limitação de horas, em clínica próxima de casa, com início imediato. Objeção: medo de processo caro e demorado, de retaliação da operadora.

**Beneficiário de plano com reajuste abusivo** — recebeu reajuste de 29,90%, 35,90% ou até 39,90% em plano coletivo por adesão, enquanto o índice da ANS para 2025 foi de 6,06%. Pode estar em plano empresarial ou falso coletivo. Dores: sensação de injustiça, impotência, perda financeira mês a mês. Busca: reduzir a mensalidade, recuperar valores pagos a mais nos últimos 3 anos (prazo prescricional), proteção contra reajustes futuros. Objeção: "será que compensa contratar advogado?" — o site responde com cases reais numéricos (ex.: 39,9% → 9,63%).

**Beneficiário com coparticipação abusiva** — em tratamento contínuo (terapias para autismo, doenças crônicas), vê a coparticipação superar o valor da própria mensalidade. Dores: dilema financeiro entre manter o tratamento e conseguir pagar o plano. Busca: limite legal da coparticipação ao valor da mensalidade, continuidade do tratamento sem sobressaltos. Objeção: achar que "coparticipação é permitida e não tem o que fazer" — o site quebra isso com a frase "A coparticipação pode existir. O abuso, não."

### Jornada do usuário

1. **Dor/evento gatilho** — Uma carta de negativa do plano, um boleto com reajuste absurdo, ou o susto ao ver que a coparticipação do mês superou a mensalidade. O gatilho é sempre um documento concreto (carta, boleto, fatura) que o usuário tem em mãos.
2. **Pesquisa** — Google, Instagram, YouTube. O usuário digita algo como "plano de saúde negou terapia do meu filho", "reajuste abusivo plano de saúde", "coparticipação acima da mensalidade". O SEO do site (Yoast) captura exatamente essas buscas.
3. **Primeiro contato com o site** — Landing page específica, não página genérica. O herói da página valida a dor: "Seu plano de saúde negou a terapia do seu filho autista?" — o usuário se sente compreendido imediatamente.
4. **Validação e urgência** — O site apresenta jurisprudência, números concretos (ex.: índice ANS 6,06%, reajuste 39,9%), casos reais publicados em portais como Migalhas e CONJUR. O gatilho de urgência emocional aparece: "cada dia sem tratamento compromete o desenvolvimento" (autismo) ou "prazo de prescrição: só 3 anos" (reajuste).
5. **Decisão** — FAQ elimina objeções (tempo, garantia, retaliação, atendimento fora de SP). Depoimentos e resultados comprovados criam confiança.
6. **Conversão** — Clique no CTA (WhatsApp). O WhatsApp 24h remove o atrito de horário comercial.

**Pontos de fricção que o site resolve**: medo de retaliação (respondido explicitamente), dúvida sobre atuação fora de SP (atendimento nacional), receio de processo demorado (pedido de liminar urgente), desconfiança sobre honorários (FAQ e bio do advogado com 15+ anos de experiência).

### Problema que o site resolve

O usuário tem um direito violado por uma operadora de plano de saúde, mas não sabe que esse direito existe, não sabe que é juridicamente exequível, e teme que buscar a justiça seja caro, demorado ou inútil. O site resolve isso provando — com jurisprudência, cases reais e números — que o direito existe, que a justiça já consolidou o entendimento, e que o processo é rápido (liminar) e seguro (sem retaliação).

**Proposta de valor central**: "Você tem o direito. Nós temos a expertise para garantir que ele seja cumprido. Não é concessão da operadora — é direito assegurado."

### Insights acionáveis para o Gabriel

1. **Três landing pages, três dores, uma estrutura.** O modelo de landing page por dor específica (autismo, coparticipação, reajuste) é o ponto mais forte do Sinzinger — cada página fala diretamente com quem está vivendo aquele problema. Gabriel deve criar pelo menos 3 páginas focadas em dores concretas do Direito à Saúde.
2. **Números e casos reais como prova social.** O Sinzinger usa índices da ANS (6,06%), percentuais de reajuste (29,90%, 39,90%) e resultados numéricos (39,9% → 9,63%). Gabriel precisa coletar decisões judiciais favoráveis com dados concretos e publicá-las como cases.
3. **Urgência temporal como gatilho emocional.** "Prazo de prescrição: só 3 anos" no reajuste; "cada dia sem tratamento compromete a neuroplasticidade" no autismo. Gabriel deve identificar os prazos críticos da sua área e transformá-los em argumento de urgência.
4. **FAQ como eliminador de objeções, não como conteúdo.** As FAQ do Sinzinger respondem exatamente: "Tem garantia?", "O plano pode cancelar meu contrato?", "Atendem fora de SP?" — são objeções reais de quem está prestes a contratar mas hesita.
5. **WhatsApp como destino único de conversão.** Todas as páginas convergem para o mesmo WhatsApp, com CTAs diretos ("Solicitar orientação jurídica agora", "Fale agora com um advogado especialista").

---

## 2. ARQUITETURA DA INFORMAÇÃO + CONTEÚDO

### Estrutura de páginas — o mapa do site de referência

O site Sinzinger usa arquitetura de "hub + landing pages por dor". O hub é a Home institucional (bio do Dr., 3 áreas de atuação). A partir dele, cada dor jurídica específica vira uma landing page com URL dedicada e funil de conversão independente: `/autismo/` (negativa de terapia), `/coparticipacao/` (cobrança abusiva), `/reajuste-abusivo/` (reajuste da mensalidade).

A lógica: cada página mira **uma única dor**, uma busca específica (SEO de cauda longa) e um único CTA. Quem cai na página já se reconhece no problema — não há dispersão entre públicos.

### Anatomia de uma landing page eficaz

As três páginas seguem a mesma ordem, do problema → direito → ação:

1. **Hero**: pergunta-retórica que espelha a dor + CTA WhatsApp ("Seu plano de saúde negou a terapia do seu filho autista?").
2. **Problema**: lista de situações reconhecíveis ("Negativas mais frequentes", 5 cards; "Reconhece alguma dessas situações?", com reajustes de 29,90% a 39,90%).
3. **Direitos**: o que a lei assegura, em ícones ("Terapia ABA integral, todas as horas, clínica próxima…").
4. **Frase de impacto** como ponte: "Não se trata de concessão da operadora. Trata-se de um direito assegurado."
5. **Processo jurídico**: etapas numeradas que reduzem a ansiedade ("Análise → Definição → Pedido urgente → Acompanhamento").
6. **Prova social**: jurisprudência, cases reais com números e bio do advogado (OAB, anos, citação).
7. **FAQ**: 4-7 perguntas que quebram objeções.
8. **Urgência**: custo de esperar ("cada dia sem tratamento compromete o desenvolvimento"; "prazo de prescrição: só 3 anos").
9. **CTA final**: "Fale agora com um advogado especialista" + WhatsApp, email, Instagram, endereço.

Propósito de cada bloco: o hero captura; o problema gera identificação ("é comigo"); os direitos dão esperança; a prova desarma o ceticismo; o processo remove o medo de burocracia; a urgência ativa a ação; o CTA fecha o funil.

### Copywriting — técnicas observadas

- **Pergunta-retórica no hero** (espelha a dor): "Seu plano de saúde está cobrando coparticipação acima da mensalidade?"
- **Frase de impacto** (posição de autoridade): "O plano de saúde NÃO PODE decidir o tratamento do seu filho"; "A coparticipação pode existir. O abuso, não."
- **Prova numérica**: "índice 2025: 6,06%"; "reajustes absurdos (29,90%, 35,90%, 39,90%)"; case "Liminar suspende reajuste abusivo (39,9% → 9,63%)".
- **Urgência**: "Cada mês que passa, perde mais dinheiro"; "Prazo de prescrição: só 3 anos".
- **Prova social**: "15 Anos de Experiência em Direito da Saúde", "Casos publicados em portais jurídicos de referência" (Migalhas, CONJUR), "Atendimento em todo o Brasil".
- **Quebra de objeções**: garantia de resultado, "impossibilidade de retaliação", atendimento nacional, WhatsApp 24h.

### Estrutura de FAQ

Os FAQs cobrem sempre os mesmos temas: **prazo/tempo** ("quanto tempo demora?"), **documentos** ("o que preciso levar?"), **garantia de resultado**, **medo de retaliação** ("o plano pode me cancelar?"), **situações em andamento** ("já comecei o tratamento"), **atendimento fora da cidade** e **urgência**. Funcionam porque respondem exatamente às objeções que travam a decisão de contratar um advogado — sobretudo a insegurança ("vou me prejudicar?") e o desconhecimento do processo.

### Recomendações para o Gabriel

**Manter**: a arquitetura hub + landing por dor; a ordem das seções (hero → problema → direitos → processo → prova → FAQ → urgência → CTA); o padrão de FAQ; a urgência e os CTAs repetidos ao longo da página.

**Mudar**: substituir toda a voz pela do Gabriel; trocar casos e índices por dados próprios e verificáveis; reescrever as "dores" para o recorte dele (ex.: negativa de cirurgia, medicamento de alto custo, internação) — usando o que diferencia o escritório, sem reproduzir exemplos alheios; personalizar a prova social com o nº da OAB e cases reais dele; regionalizar a localização e o "atendimento em todo o Brasil" conforme a realidade do Gabriel; e adaptar exemplos numéricos à realidade local dos planos.

---

## 3. CONVERSÃO + MARKETING

### Funil de conversão

O funil adotado pela Sinzinger é de alta pressão digital: o CTA primário (WhatsApp) aparece já no hero, repete-se após cada bloco de autoridade (jurisprudência, bio, FAQ) e retorna no footer e no final das páginas — o usuário nunca está a mais de um scroll de um botão de contato. O link usa tintim.link (link curto com rastreio) e wa.me.

Para o Gabriel, o mesmo modelo funciona: botão flutuante de WhatsApp + CTA inline após cada seção + CTA final. A repetição não é ruído — é conversão em funil.

### Técnicas de persuasão

- **Urgência real**: prazo prescricional de 3 anos (reajustes), neuroplasticidade infantil (autismo — cada dia sem tratamento compromete o desenvolvimento). São gatilhos legítimos, não artificiais.
- **Prova social**: casos publicados em Migalhas e CONJUR (portais jurídicos de referência), cases com números concretos (ex.: reajuste de 39,9% reduzido para 9,63%). O Gabriel deve adaptar com seus próprios resultados e menções na mídia.
- **Autoridade**: 15 anos de experiência, OAB/SP, coautor de obras jurídicas, foto profissional com citação inspiracional. O Gabriel precisa destacar sua especialização em Direito à Saúde e produções acadêmicas.
- **Aversão à perda**: "cada mês que passa, perde mais dinheiro", "prazo de prescrição: só 3 anos", "seu plano pode negar o tratamento". A mensagem é clara: não agir tem custo.

### Diferenciais adaptáveis para o Gabriel

- Compromisso ético com transparência de chances jurídicas (o que a Sinzinger não explicita, mas o Gabriel pode usar como bandeira)
- Promessa de resposta em 24h (Sinzinger usa "atendimento imediato online")
- Atendimento nacional via processos digitais
- Horários amplos (WhatsApp 24h, mesmo que o expediente seja comercial)
- Valor de causa social: direito à saúde como direito fundamental — não é só um serviço, é uma missão

---

## 4. DESIGN + UX

### Técnicas de design observáveis

O site usa WordPress + Elementor com smooth scroll Lenis (efeito fluido e moderno). As landing pages são estruturadas com:

- **Cards e ícones**: blocos de "negativas mais frequentes" (5 cards), "direitos assegurados por lei" (6 ícones). Quebram texto denso em informação escaneável.
- **Seções de imagem + texto**: alternância entre blocos de impacto textual e imagens (Dr. Gustavo, infográficos de processo jurídico). Mantém o olho do usuário em movimento.
- **Contraste emocional**: abertura com problema (ansiedade, negação, dívida) → exposição de direitos → solução (advocacia especializada). O arco emocional vai de tensão para alívio.
- **Exemplo visual concreto**: na página de coparticipação, um mini-infográfico (Mensalidade R$1000 + Coparticipação R$1000 = Total R$2000) — converte abstração jurídica em compreensão imediata.

### Hierarquia visual e ritmo de leitura

O padrão é: headline de impacto → parágrafo curto → CTA → bloco de cards/ícones → prova social (jurisprudência, mídia) → bio do advogado → FAQ → CTA final. O ritmo é rápido: seções curtas, max 4-5 linhas por bloco de texto, títulos em caixa alta ou semi-caixa. O usuário "scannea" a página em 10 segundos e encontra o WhatsApp em pelo menos 3 pontos.

### Recomendações para o Gabriel

- **Manter**: smooth scroll Lenis, estrutura de landing page por dor, cards com ícones, seção de jurisprudência, FAQ conversacional, CTA repetido.
- **Não copiar**: identidade visual azul-marinho e dourada da Sinzinger. O tom deve ser próprio — mais acolhedor e menos institucional, já que Direito à Saúde lida com vulnerabilidade emocional. Evitar fotos genéricas de banco de imagens; usar foto real do Gabriel com ambiente que transmita cuidado.
- **Diferenciar**: inverter a ordem — começar pela missão/valores (não pela bio do advogado), e incluir depoimentos reais de clientes (a Sinzinger não usa, e isso é uma vantagem explorável).

---

## 5. IDEAÇÃO + PRÓXIMOS PASSOS

### 10 ideias de features, conteúdo e estrutura

1. **Landing pages por dor (1 página = 1 problema).** O site de referência converte ao criar uma página dedicada por causa (autismo, coparticipação, reajuste). Para o Gabriel: páginas para *negativa de terapia (ABA)*, *negativa de cirurgia/exame*, *reajuste abusivo* e *internação/custeio*. **Por quê:** permite SEO direcionado e CTA contextual. **Como:** mesma estrutura de hero + problema + direitos + processo em 4 passos + FAQ + CTA.

2. **FAQ de 6-7 perguntas com "escala de urgência".** A referência usa FAQ para vencer objeções (tempo, custo, retaliação, atendimento). **Por quê:** reduz atrito antes do WhatsApp. **Como:** manter as perguntas que funcionam (garantia, retaliação, prazos) adaptadas ao Gabriel.

3. **Cases com números concretos.** A página de reajuste converte com resultados mensuráveis ("39,9% → 9,63%", liminar suspendendo reajuste). **Por quê:** prova social com credibilidade. **Como:** seção "Resultados Reais" com casos anonimizados e valores (reajuste reduzido, terapia garantida, coparticipação limitada).

4. **Urgência temporal real.** Referência usa "prescrição de 3 anos" e "neuroplasticidade infantil". **Por quê:** CTA de urgência acelera decisão. **Como:** bloco "Por que agir agora" por página (prescrição, dano à saúde, perda financeira mensal).

5. **Exemplo visual de cálculo.** A página de coparticipação usa R$1000 mensalidade vs. coparticipação. **Por quê:** transforma abstrato em concreto. **Como:** calculadora simples "quanto paguei a mais?" com reajustes da ANS (índice 2025: 6,06%).

6. **Diferenciais no topo do site.** Referência destaca "atuação exclusiva", "casos na mídia", "atendimento nacional". **Por quê:** diferenciação imediata. **Como:** badge fixo + seção "Por que o Gabriel" (especialização, atendimento digital nacional, resposta em 24h).

7. **Bio com autoridade + citação.** Referência fecha com foto, OAB, bio e frase inspiracional. **Por quê:** autoridade jurídica gera confiança. **Como:** página institucional com bio, formação e canais (WhatsApp, Instagram, e-mail).

8. **WhatsApp como conversão central.** Referência usa WhatsApp em todos os CTAs (wa.me/tintim.link) e horário "atendimento 24h". **Por quê:** canal de menor fricção. **Como:** botões flutuantes, CTAs repetidos a cada rolagem e mensagem pré-preenchida com contexto do problema.

9. **Conteúdo educativo em blog/YouTube.** Referência tem Instagram/YouTube mas pouco conteúdo. **Por quê:** oportunidade de SEO de cauda longa (ex.: "o que é coparticipação abusiva"). **Como:** transformar cada landing em artigo + vídeo curto.

10. **Seção de urgência emocional por página.** Referência usa "cada dia sem tratamento compromete o desenvolvimento". **Por quê:** conecta dor emocional à ação. **Como:** bloco de impacto no final de cada landing, antes do CTA final.

### Roadmap em 3 fases

**Fase 1 — MVP (semanas 1-4):** site estático rápido (não WordPress/Elementor, que ficam lentos) com 1 página institucional + 2 landings (autismo/terapia, reajuste). Hero, problema, direitos, processo em 4 passos, FAQ (6), CTA WhatsApp com wa.me. SEO básico (títulos, meta description, sitemap).

**Fase 2 — Evolução (meses 2-3):** +2 landings (coparticipação, negativa de cirurgia/internação), cases com números, calculadora de reajuste, blog com 4-6 artigos, bio completa, integração WhatsApp Business + Instagram.

**Fase 3 — Escala (meses 4+):** conteúdo contínuo (10+ artigos/ano), funil com e-mail/retargeting, vídeos no YouTube, páginas por cidade/operadora (nicho "negativa SulAmérica/Amil"), monitoramento de métricas e testes A/B de CTAs.

### Métricas para validar

- Taxa de clique no WhatsApp (CTAs: % de visitantes que acionam o botão; meta > 2-3%)
- Tempo médio na página (landing de referência: > 90s)
- Taxa de rejeição (bounce) e scroll depth (até o CTA final)
- Conversão de lead → caso fechado (funil completo)
- Posição orgânica para termos-chave (ex.: "reajuste abusivo plano de saúde")
- Custo por lead em tráfego pago (Google Ads/Meta)

### O que EVITAR copiar

- **Erros de português** identificados na referência ("infncia", "multidiciplinar") — revisão ortográfica obrigatória; um erro destrói a credibilidade jurídica.
- **Páginas duplicadas/sobrepostas** (home "BIO" e landings com o mesmo bio repetido) — evitar conteúdo duplicado que penaliza SEO.
- **Stack pesado** (WordPress + Elementor + Litespeed) — gerar site leve e rápido (Core Web Vitals).
- **Não copiar layout, textos nem estrutura visual** — usar apenas os padrões de conversão; inspiração, não cópia, evita plágio e diferenciação zero.
- **Promessas vazias** ("garantia") sem respaldo — validar juridicamente o que pode ser prometido.
- **Ausência de termos de uso/privacidade e LGPD** — a referência tem, não repetir a lacuna de conformidade digital.

---

## 6. INFORMAÇÕES COMPLEMENTARES DA EXTRAÇÃO

### Stack tecnológico do site de referência
- CMS: WordPress + Elementor (page builder)
- Cache: Litespeed Cache
- SEO: Yoast SEO
- Smooth scroll: Lenis (via unpkg.com)
- Hospedagem: Litespeed

### Redes sociais e contatos
- Instagram: @gustavosinzinger.adv
- YouTube: @gustavosinzinger
- WhatsApp: (11) 9.4234-3328 (via tintim.link e wa.me)
- Email: contato@sinzingeradvocacia.com.br
- Localização: São Paulo/SP, Bairro do Tatuapé
- Créditos design: DannyHana (dannyhana.com.br)

### Observações
- YouTube e Instagram não puderam ser extraídos (exigem login/JS)
- Páginas de Termos de Uso e Política de Privacidade existem no footer
- Atendimento nacional via processos digitais
- Horário: Seg-Sex 8h-18h, WhatsApp 24h

---

*Documento gerado em 31/08/2026. Extração via Hermes Agent com 4 subagentes paralelos. Inspiração: sinzingeradvocacia.com.br.*