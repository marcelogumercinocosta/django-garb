## Context

O mecanismo atual resolve mapas parciais de tokens SCSS contra o mapa `default` e publica cada tema como variáveis CSS sob `body.<tema>`. A seleção já chega ao `body` pelo valor de `GARB_CONFIG['THEME']`. A distribuição contém tanto o SCSS-fonte quanto CSS expandido e minificado compilado, e a suíte visual percorre uma lista explícita de temas.

O documento de referência apresenta laranja vivo sobre branco em alguns destaques. Essa combinação é fiel à marca, mas não serve automaticamente para texto pequeno; a implementação precisa separar a cor de destaque decorativa da alternativa escurecida para texto.

## Goals / Non-Goals

**Goals:**

- Integrar `levva` pelo mecanismo de tokens existente, sem criar uma segunda arquitetura de temas.
- Manter a aparência clara, com estrutura azul-marinho e acentos laranja.
- Tornar as razões de contraste reproduzíveis por teste, incluindo estados interativos.
- Entregar CSS-fonte, CSS compilado, documentação e baseline visual coerentes.

**Non-Goals:**

- Incorporar o logotipo, dados pessoais ou conteúdo textual da fatura no Django Garb.
- Alterar estrutura, tipografia global, templates ou comportamento dos temas existentes.
- Buscar fidelidade pixel a pixel com o documento, que é uma fatura e não uma tela administrativa.

## Decisions

### Usar um mapa de tokens `levva`

O tema será acrescentado ao mapa `$themes` e herdará tokens neutros do `default`, sobrescrevendo apenas cores e acabamentos necessários. Isso preserva o contrato atual e reduz o risco de regressão. A alternativa de criar um arquivo CSS independente duplicaria seletores e dificultaria manutenção.

### Separar laranja de marca e laranja para texto

A base planejada é azul-marinho `#052455`, laranja de marca `#FF7A00`, laranja escuro `#C45100`, branco `#FFFFFF`, superfície `#F4F6F8` e texto secundário `#5D6778`. O laranja vivo será usado em preenchimentos, detalhes e estados com texto azul-marinho; o laranja escuro será reservado a links ou texto sobre branco.

As combinações-chave calculadas pela fórmula de luminância relativa WCAG são:

| Primeiro plano | Fundo | Razão |
| --- | --- | ---: |
| `#FFFFFF` | `#052455` | 15,11:1 |
| `#C45100` | `#FFFFFF` | 4,64:1 |
| `#052455` | `#FF7A00` | 5,78:1 |
| `#052455` | `#F4F6F8` | 13,95:1 |
| `#5D6778` | `#FFFFFF` | 5,71:1 |

A alternativa de usar branco sobre `#FF7A00` foi descartada porque não atinge 4,5:1. Os valores finais poderão ser refinados durante a inspeção dos componentes, desde que mantenham a mesma função visual e passem os limites da especificação.

### Automatizar a matriz de contraste

Será criado um teste leve que calcula contraste dos pares sem depender do navegador, cobrindo texto, superfícies, botões e indicadores essenciais. A inspeção visual continuará responsável por composição, hover/foco efetivo e regressões. Apenas uma baseline adicional de listagem será adicionada para `levva`; as existentes não devem mudar.

### Atualizar artefatos compilados versionados

Após modificar o SCSS, o comando de build existente regenerará `style.css`, `style.min.css` e seus source maps. Não haverá dependência de produção nova; as ferramentas Sass e de teste já estão nas dependências de desenvolvimento.

## Risks / Trade-offs

- [A fatura não define estados de UI] → Derivar estados a partir da hierarquia cromática e validar contraste e consistência no navegador.
- [Tokens herdados podem usar uma cor em contextos inesperados] → Auditar login, listagem, formulário, exclusão e histórico, além da captura dedicada do tema.
- [Ajustar o laranja reduz fidelidade literal em texto] → Preservar o laranja vivo em áreas adequadas e usar a variante escura somente onde a acessibilidade exigir.
- [Source maps geram diffs grandes] → Regenerar exclusivamente com o script oficial e revisar que os temas anteriores não tiveram mudanças visuais.

## Migration Plan

Adicionar o novo valor é retrocompatível e opt-in. A publicação inclui SCSS, CSS compilado, documentação e testes no mesmo release. Em caso de rollback, removem-se o mapa `levva`, sua documentação, teste e baseline; aplicações podem voltar a `default` sem migração de dados.
