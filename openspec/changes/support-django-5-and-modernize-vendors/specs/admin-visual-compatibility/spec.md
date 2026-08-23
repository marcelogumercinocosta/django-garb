## Purpose

Garantir que a modernização dos templates e vendors preserve a identidade visual, os temas e as interações que caracterizam o Django Garb na documentação atual.

## ADDED Requirements

### Requirement: Preservação da identidade visual documentada
O pacote SHALL preservar a composição visual apresentada nas capturas de documentação para as páginas de índice, lista de modelos, formulário de edição, login, exclusão e histórico.

#### Scenario: Comparação de página administrativa
- **WHEN** uma página representativa é renderizada no viewport de referência com dados e estado determinísticos
- **THEN** sua estrutura, espaçamento, tipografia, cores, bordas, sombras e alinhamento deverão permanecer dentro da tolerância visual aprovada em relação ao baseline

#### Scenario: Alteração visual intencional
- **WHEN** uma diferença excede a tolerância do baseline
- **THEN** a alteração deverá ser tratada como regressão até que seja corrigida ou explicitamente aprovada e documentada

### Requirement: Temas preservados
O pacote SHALL manter disponíveis os temas públicos `default`, `light`, `hybrid`, `dark` e `alive`, conservando para cada um a paleta e o contraste reconhecíveis nas capturas existentes.

#### Scenario: Seleção de tema
- **WHEN** um tema público é configurado em `GARB_CONFIG`
- **THEN** a classe e os estilos correspondentes deverão ser aplicados consistentemente ao shell, menu, conteúdo, formulários, tabelas e estados interativos

### Requirement: Layout administrativo preservado
O pacote SHALL manter sidebar, cabeçalho, breadcrumbs, cartões de conteúdo, listagens e o formulário de edição em duas colunas nas mesmas relações espaciais documentadas para viewport desktop.

#### Scenario: Formulário de edição desktop
- **WHEN** uma página de inclusão ou edição é aberta no viewport desktop de referência
- **THEN** os campos deverão ocupar a coluna principal e as ações de salvar, voltar, excluir e histórico deverão permanecer agrupadas na coluna lateral

#### Scenario: Lista de modelos desktop
- **WHEN** uma lista de modelos é aberta no viewport desktop de referência
- **THEN** busca, filtros, ação de inclusão, tabela, ações em lote e paginação deverão conservar sua hierarquia e posições relativas

### Requirement: Componentes interativos compatíveis
O pacote SHALL manter funcionais o menu recolhível, dropdown do usuário, selects aprimorados, controles de modelos relacionados, mensagens toast, indicador de progresso, ações em lote e alternância da sidebar após a atualização dos vendors.

#### Scenario: Interações sem erro de navegador
- **WHEN** o usuário aciona cada componente interativo suportado
- **THEN** o componente deverá responder conforme documentado sem erro JavaScript não tratado no console

#### Scenario: Inline adicionado dinamicamente
- **WHEN** o Django Admin adiciona um novo formulário inline contendo um select simples
- **THEN** o select recém-criado deverá receber o mesmo aprimoramento visual e funcional dos selects presentes no carregamento inicial

### Requirement: Assets oficiais e rastreáveis
O pacote SHALL distribuir versões identificáveis dos vendors Bootstrap, bootstrap-select, jQuery Toast Plugin e Pace, obtidas de releases oficiais e acompanhadas de versão, origem e licença.

#### Scenario: Auditoria dos vendors empacotados
- **WHEN** um mantenedor inspeciona o inventário de dependências front-end da release
- **THEN** cada vendor deverá possuir versão fixa, origem oficial, licença e correspondência com o arquivo efetivamente distribuído

### Requirement: Carregamento estável dos estilos
O pacote SHALL carregar o CSS do framework antes do CSS do Garb, garantindo que as regras e tokens do tema Garb continuem sendo a camada visual final.

#### Scenario: Página carregada sem cache
- **WHEN** uma página tematizada é aberta com cache vazio
- **THEN** os estilos finais deverão corresponder ao tema selecionado sem depender da ordem acidental de respostas de rede

