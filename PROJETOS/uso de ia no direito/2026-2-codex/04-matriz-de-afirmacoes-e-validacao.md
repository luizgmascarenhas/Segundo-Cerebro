# Matriz de afirmações e validação

## Finalidade

Este documento transforma as afirmações recorrentes dos materiais-base em itens verificáveis antes de qualquer publicação do e-book, landing page, FAQ ou conteúdo social.

**Status usados:**

- **Base primária disponível:** há uma fonte oficial ou normativa na pasta, mas a redação final ainda deve ser conferida.
- **Validar externamente:** depende de consulta à fonte oficial atualizada.
- **Revisar interpretação:** a fonte pode existir, mas a conclusão editorial está mais ampla do que o texto localizado.
- **Não publicar sem prova:** a afirmação é absoluta, comercialmente sensível ou não possui suporte suficiente nos arquivos analisados.

## Matriz principal

| ID | Afirmação recorrente | Onde aparece | Tipo | Fonte prioritária | Status | Tratamento recomendado |
|---|---|---|---|---|---|---|
| A01 | A OAB não proíbe o uso de IA generativa na advocacia | `concepcao-ia-advocacia-oab.md`, `produto-final.md` | normativa | Recomendação OAB 001/2024 e atos oficiais posteriores | Validar externamente | Usar formulação cuidadosa: a recomendação orienta o uso responsável; não transformar ausência de proibição em autorização irrestrita. |
| A02 | O uso de IA deve respeitar Estatuto, Código de Ética, LGPD, CPC e propriedade intelectual | Recomendação, item 1.1 | normativa | Texto oficial da OAB e legislação oficial | Base primária disponível | Manter com citação direta e referência oficial. |
| A03 | O advogado deve proteger a confidencialidade e evitar tornar o cliente identificável | Recomendação, itens 2.1 e 2.5 | normativa | Texto oficial da OAB | Base primária disponível | Manter; explicar que anonimização é medida de redução de risco, não garantia absoluta. |
| A04 | É necessário avaliar fornecedor, segurança, compartilhamento e uso para treinamento | Recomendação, itens 2.2 e 2.3 | normativa | Texto oficial da OAB + termos do fornecedor | Base primária disponível | Manter como dever de diligência; não recomendar ferramenta apenas por marca. |
| A05 | Chatbots não devem executar atividades privativas da advocacia e devem informar que são máquinas | Recomendação, item 2.4 | normativa | Texto oficial da OAB | Base primária disponível | Manter com exemplos e limites operacionais. |
| A06 | A supervisão humana não pode ser delegada à IA | Recomendação, itens 3.1, 3.3 e 3.7 | normativa | Texto oficial da OAB | Base primária disponível | Manter; evitar dizer que a revisão “elimina” qualquer risco. |
| A07 | O advogado responde pela veracidade do que apresenta em juízo | Recomendação, item 3.2 + art. 77 do CPC | normativa | Planalto/CPC e fonte oficial OAB | Validar externamente | Conferir redação integral do art. 77 e não qualificá-lo como “dever absoluto” sem contexto. |
| A08 | A recomendação prevê capacitação e políticas internas para equipes | Recomendação, itens 3.5, 3.6 e 3.8 | normativa | Texto oficial da OAB | Base primária disponível | Manter como orientação de governança para sócios e gestores. |
| A09 | O uso pretendido de IA deve ser comunicado previamente ao cliente por escrito | Recomendação, itens 4.1 a 4.2.1 | normativa | Texto oficial da OAB | Base primária disponível | Reproduzir o alcance exato e diferenciar “recomenda-se” de “deve”. |
| A10 | O documento de comunicação deve explicar finalidade, benefícios, limitações, riscos, segurança e revisão humana | Recomendação, item 4.2.1 | normativa | Texto oficial da OAB | Base primária disponível | Manter em checklist, sem converter o modelo em contrato universal. |
| A11 | O cliente pode não consentir e o advogado deve respeitar a decisão | Recomendação, item 4.3.2 | normativa | Texto oficial da OAB | Base primária disponível | Manter; orientar adaptação ao caso concreto. |
| A12 | A comunicação/consentimento deve ser arquivada até o término da prestação | Recomendação, item 4.3.3 | normativa | Texto oficial da OAB | Base primária disponível | Manter com indicação de controle documental e prazo conforme fonte. |
| A13 | O art. 34 do Estatuto estabelece “sigilo absoluto” | `produto-final.md`, posts, guias | normativa | Texto oficial da Lei 8.906/1994 e Código de Ética | Revisar interpretação | O art. 34, VII, tipifica como infração “violar, sem justa causa, sigilo profissional”; não usar a expressão “sigilo absoluto” como citação literal do artigo. |
| A14 | A LGPD pode gerar multa de até 2% do faturamento, limitada a R$ 50 milhões por infração | Landing page e propostas | normativa | LGPD, art. 52, Planalto/ANPD | Validar externamente | Informar que sanção depende de requisitos, processo e autoridade competente; evitar uso como ameaça genérica. |
| A15 | O escritório atua como controlador ao decidir tratar dados por meio de IA | `ia-no-direito.md`, `produto-final.md` | jurídica/compliance | LGPD, ANPD e contrato do tratamento | Revisar interpretação | Apresentar como hipótese usual a ser analisada, não como classificação automática em todo cenário. |
| A16 | Ferramentas públicas/gratuitas usam prompts para treinamento por padrão | Kit, guias e posts | fornecedor | Política atual de cada serviço/plano | Não publicar sem prova | Substituir generalização por análise plano a plano, data de consulta e configuração. |
| A17 | ChatGPT Plus deve ser tratado como equivalente a ferramenta pública de alto risco | Kit e landing page | fornecedor/jurídica | Política oficial atual da OpenAI + escopo contratual | Validar externamente | Não categorizar automaticamente; separar plano individual, configurações, dados, retenção e DPA. |
| A18 | Planos empresariais não usam dados do cliente para treinamento | Capítulos e guias | fornecedor | Termos oficiais atuais de OpenAI, Anthropic, Google e Microsoft | Validar externamente | Registrar fornecedor, plano, região, exceções, retenção e data de consulta. |
| A19 | DPA torna a ferramenta adequada para qualquer dado jurídico | Vários documentos | compliance | DPA, política, medidas técnicas e análise do caso | Revisar interpretação | Explicar que DPA é apenas um elemento da diligência; anonimização e governança continuam necessárias. |
| A20 | IA local oferece privacidade máxima ou garante que nenhum dado sai do escritório | Guias de ferramentas | técnico | Documentação da ferramenta + arquitetura implantada | Revisar interpretação | Usar “pode reduzir exposição externa”; considerar telemetria, downloads, integrações, logs e segurança local. |
| A21 | JUIT é a única ferramenta declarada conforme à Recomendação OAB 001/2024 | FAQ, kit e posts | comercial | Declaração oficial da OAB e documentação da empresa | Não publicar sem prova | Remover “única” até obter prova primária, escopo da declaração e data de validade. |
| A22 | Victor e Athos são exemplos de IA no STF e STJ | FAQ e pesquisas | institucional | STF, STJ, CNJ | Validar externamente | Conferir descrição e situação atual; para a regulação do Judiciário, considerar também a Resolução CNJ nº 615/2025 e o texto compilado indicado pelo CNJ. |
| A23 | Pelo menos 13 tribunais usam IA na admissibilidade de recursos | FAQ e iniciativas | estatística | Estudo/levantamento original do STJ ou ConJur | Validar externamente | Informar metodologia, universo, data e o que significa “usam IA”. |
| A24 | 77% dos advogados já usam IA | Kit, landing page e PDF | estatística | Pesquisa original citada pela OAB-SP | Validar externamente | Identificar amostra, pergunta, população, data e escopo; não generalizar para todo o Brasil sem base. |
| A25 | A adoção passou de 11% para 30%, ou de 37% para 80% | Fase 3, análise crítica | estatística | Pesquisas originais distintas | Não publicar sem prova | Escolher um único dado auditável ou explicar claramente que são pesquisas diferentes. |
| A26 | 37% dos advogados economizam de 2 a 5 dias de trabalho por mês | FAQ e exemplos | estatística | Pesquisa original | Validar externamente | Não usar até localizar estudo, amostra e definição de “economizar”. |
| A27 | Três advogados foram multados e tiveram ofícios enviados à OAB em 2026 | Landing page e kit | casos judiciais | decisões e notícias oficiais de TST/TRT/TJ | Validar externamente | Criar ficha individual para cada caso, sem agrupar fatos diferentes. |
| A28 | TRT-2 aplicou multa de 5% e encaminhou ofício à OAB | Relatório de multas e landing page | caso judicial | Acórdão/decisão do TRT-2 | Validar externamente | Conferir número do processo, data, fundamento, percentual e conteúdo do ofício. |
| A29 | TST aplicou multa de 1% em caso de jurisprudência falsa | Landing page | caso judicial | Decisão oficial do TST | Validar externamente | Não publicar sem decisão ou reportagem institucional verificável. |
| A30 | TJ-PR identificou 43 jurisprudências fictícias em um recurso | Guias e posts | caso judicial | Decisão oficial TJ-PR ou fonte jornalística primária | Validar externamente | Conferir se o fato, tribunal, quantidade e consequência estão corretos. |
| A31 | Casos de IA geraram punições em TJSC, TRT-3 e 2ª Vara Federal de Londrina | Relatório de multas | caso judicial | Decisões oficiais/notícias dos órgãos | Validar externamente | Manter como banco de pesquisa, não como prova final. |
| A32 | A IA generativa é um motor de previsão e pode produzir referências plausíveis porém falsas | Todos os materiais | técnico | Documentação técnica e literatura especializada | Revisar interpretação | Manter em linguagem didática, sem sugerir que toda saída é falsa ou que uma instrução elimina alucinações. |
| A33 | “Use exclusivamente as fontes fornecidas” impede alucinações | Prompts e kit | produto/metodologia | Teste interno documentado | Não publicar sem ressalva | Descrever como barreira metodológica que reduz risco; sempre exigir conferência independente. |
| A34 | O protocolo faz uma tarefa de duas horas em quinze minutos ou gera dez horas semanais | Kit, posts e landing page | resultado/marketing | Medição própria com método | Não publicar sem prova | Tratar como exemplo hipotético ou registrar estudo de caso com tarefa, usuário e método de medição. |
| A35 | O material resolve os três erros em uma hora e coloca o leitor à frente de 80% dos advogados | Landing page | promessa comercial | Evidência interna e pesquisa | Não publicar sem prova | Reescrever como promessa de orientação e implementação inicial, sem comparação não comprovada. |
| A36 | O produto oferece garantia de sete dias e entrega imediata por e-mail | Landing page | operacional/comercial | Plataforma de venda e política comercial | Validar externamente | Confirmar se a operação realmente suporta essas condições antes de publicar. |

## Pendências bloqueadoras

1. Obter e registrar as fontes oficiais dos casos judiciais.
2. Conferir a versão oficial da Recomendação OAB nº 001/2024 contra a transcrição local.
3. Conferir artigos legais diretamente em fontes oficiais.
4. Substituir estatísticas conflitantes por dados identificados e metodologicamente descritos.
5. Auditar afirmações sobre cada fornecedor por plano, contrato e data.
6. Escolher se o produto será chamado de “e-book”, “kit” ou ambos, evitando promessas divergentes.

## Regra de publicação

Nenhum item com status **Não publicar sem prova** deve aparecer como fato em página de venda, FAQ, anúncio, post ou capítulo normativo. Enquanto não houver validação, ele pode permanecer apenas em documento interno de pesquisa, marcado como hipótese ou exemplo.
