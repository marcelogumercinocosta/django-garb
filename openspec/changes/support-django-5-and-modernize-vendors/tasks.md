## 1. Baseline e ferramentas de validação

- [x] 1.1 Registrar as versões, origens, licenças e checksums dos vendors atuais e confirmar nas fontes oficiais as versões-alvo disponíveis no início da implementação.
- [x] 1.2 Preparar ambientes reproduzíveis para Django 5.1, 5.2 e 6.0 nas combinações suportadas do Python, incluindo `django check`, migrações e testes com avisos de depreciação habilitados.
- [x] 1.3 Expandir o app de testes com fixtures determinísticas para índice, lista, busca, filtros, paginação, edição, exclusão, histórico, permissões, inlines e widgets relacionados.
- [x] 1.4 Configurar o teste em navegador com viewport, fontes e dados fixos e produzir as baselines iniciais a partir das capturas documentadas para páginas e componentes representativos.

## 2. Compatibilidade Python e Django

- [x] 2.1 Atualizar os metadados de empacotamento para Python 3.10+, `Django>=5.1,<6.1`, classificadores atuais e inclusão verificável de templates, traduções e arquivos estáticos.
- [x] 2.2 Remover imports de compatibilidade obsoletos e substituir APIs Python/Django removidas, incluindo os caminhos incompatíveis de formulários e testes.
- [x] 2.3 Corrigir a resolução de configuração e os efeitos globais de `ModelAdmin`, preservando os defaults e permitindo overrides válidos por `ModelAdmin` individual.
- [x] 2.4 Corrigir e testar a construção do menu para autenticação, permissões únicas ou múltiplas, modelos, rotas, links externos, submenus e item ativo nas três séries do Django.
- [x] 2.5 Atualizar e testar paginação, busca e transformação de filtros com as estruturas de `ChangeList` das três séries suportadas.
- [x] 2.6 Atualizar `GarbForm`, `GarbModelForm`, fieldsets, atributos de linha e formulários de preview para Python moderno e Django 5.1+.

## 3. Templates do Django Admin

- [x] 3.1 Comparar cada override em `garb/templates/admin/` com Django 5.1, 5.2 e 6.0, documentar diferenças relevantes e remover cópias que não agregam customização visual ou funcional.
- [x] 3.2 Atualizar o shell base, cabeçalho, autenticação, logout, sidebar, breadcrumbs e mensagens preservando os blocos de extensão públicos do Garb.
- [x] 3.3 Atualizar templates de índice, app index, lista, resultados, busca, filtros, ações e paginação e validar operações autorizadas e não autorizadas.
- [x] 3.4 Atualizar templates de formulário, fieldsets, submit line, object tools, inlines e widgets relacionados e validar inclusão, edição e erros de formulário.
- [x] 3.5 Atualizar templates de exclusão, histórico, login, troca/recuperação de senha, erros e e-mails para os contratos das séries suportadas.
- [x] 3.6 Executar validação de HTML e smoke tests de renderização em todas as páginas atualizadas antes da migração visual dos vendors.

## 4. Atualização dos vendors e JavaScript

- [x] 4.1 Substituir Bootstrap 4 por Bootstrap 5.3.8 ou pela release estável oficial mais nova confirmada, usar o bundle com Popper e remover os assets antigos ou duplicados.
- [x] 4.2 Atualizar bootstrap-select para a release oficial mais nova com suporte a Bootstrap 5 e adicionar cobertura para selects simples, filtros, campos relacionados, opções vazias, localização e inlines dinâmicos.
- [x] 4.3 Atualizar jQuery Toast Plugin e Pace para as releases oficiais confirmadas, mantendo mensagens, ícones, posição, transição e indicador de progresso equivalentes.
- [x] 4.4 Testar jQuery 4 com todos os plugins e scripts; fixar jQuery 4 quando compatível ou a release 3.x mais nova compatível quando o gate falhar, registrando a evidência e a limitação.
- [x] 4.5 Mover o jQuery do Garb para um namespace estático próprio e garantir convivência com `django.jQuery` sem sobrescrever `admin/js/vendor/jquery/`.
- [x] 4.6 Migrar markup e scripts de `data-toggle`, `data-parent`, dropdowns, collapse, tooltips e utilitários direcionais para Bootstrap 5.
- [x] 4.7 Atualizar a inicialização de selects e componentes adicionados dinamicamente para eventos atuais do Django Admin, sem timeouts frágeis ou inicialização duplicada.
- [x] 4.8 Criar o inventário final dos vendors com versão fixa, URL oficial, licença e checksum e confirmar que nenhum template usa aliases `latest` ou CDN para esses assets.

## 5. Preservação do CSS e dos temas

- [x] 5.1 Corrigir inconsistências do SCSS, estabilizar o processo de compilação e confirmar que o CSS compilado e seu mapa correspondem às fontes versionadas.
- [x] 5.2 Adaptar seletores afetados pelo markup do Bootstrap 5 mantendo os tokens de dimensão, espaçamento, cor, borda, sombra e tipografia do layout atual.
- [x] 5.3 Validar e ajustar sidebar, cabeçalho, breadcrumbs, cartões, tabelas, toolbar, ações, paginação e formulário de duas colunas contra as baselines desktop.
- [x] 5.4 Validar e ajustar selects, checkboxes, data/hora, widgets relacionados, feedback de erro, toasts e Pace contra as capturas de detalhe.
- [x] 5.5 Executar comparações visuais dos temas `default`, `light`, `hybrid`, `dark` e `alive`, corrigindo toda diferença acima da tolerância antes de aprovar as novas baselines.
- [x] 5.6 Testar menu, dropdown de usuário, selects, toast, ações, inlines e alternância da sidebar em navegador, exigindo ausência de erros JavaScript não tratados.

## 6. Qualidade, distribuição e documentação

- [x] 6.1 Completar testes unitários e funcionais para configuração, menu, formulários, tags, permissões e todos os fluxos administrativos especificados.
- [x] 6.2 Executar a matriz completa Django/Python e o conjunto visual canônico, corrigindo falhas e avisos de depreciação originados no Django Garb.
- [x] 6.3 Construir wheel e sdist e validar em ambiente limpo que templates, traduções, CSS, JavaScript, mapas e assets são instalados e encontrados pelo Django.
- [x] 6.4 Atualizar README e documentação com instalação, ordem de `INSTALLED_APPS`, matriz Django/Python, configuração, vendors, compilação do CSS, testes visuais e `collectstatic`.
- [x] 6.5 Registrar a quebra de compatibilidade, orientar consumidores antigos a fixarem a release anterior e atualizar a versão do pacote conforme o versionamento escolhido.
- [x] 6.6 Executar a validação final do OpenSpec, revisar o diff para confirmar que não houve redesign e registrar os resultados funcionais, visuais e de empacotamento.
