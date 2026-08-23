## Context

O pacote substitui cerca de cinquenta templates do Django Admin e aplica um CSS gerado de SCSS sobre Bootstrap 4.5.2. Os scripts dependem de convenções do Bootstrap 4 e de jQuery, enquanto o backend contém imports, APIs e testes originados na época do Django 3. Ver `proposal.md` para a motivação e `specs/` para o contrato de compatibilidade.

As capturas em `docs/source/_static/` são o registro visual disponível. Elas cobrem cinco temas, páginas administrativas principais e detalhes de busca, paginação, ações, select, checkbox e data/hora, mas não foram produzidas por um teste reproduzível.

Na data da proposta, as referências oficiais indicam Django 5.1, 5.2 LTS e 6.0 como a faixa solicitada, Bootstrap 5.3.8 como release atual, bootstrap-select 1.14.0-beta3 como linha oficial com suporte a Bootstrap 5 e Pace 1.2.4. A versão final de cada asset deverá ser confirmada novamente no início da implementação e fixada no inventário.

## Goals / Non-Goals

**Goals:**

- Manter uma única base de código testada em Django 5.1, 5.2 e 6.0.
- Reduzir dependências de detalhes internos do Admin onde isso não altera o layout.
- Migrar para Bootstrap 5 preservando os tokens e seletores visuais do Garb.
- Tornar as capturas representativas reproduzíveis e comparáveis automaticamente.
- Distribuir assets locais, versionados e auditáveis.

**Non-Goals:**

- Redesenhar a interface, criar novos temas ou modernizar deliberadamente a estética.
- Reescrever a interface como SPA ou remover todos os usos de jQuery nesta mudança.
- Manter suporte a Django anterior a 5.1 ou Python anterior a 3.10.
- Garantir igualdade pixel a pixel entre sistemas operacionais ou motores de fonte distintos.
- Ampliar o escopo para responsividade móvel além de impedir regressões adicionais.

## Decisions

### 1. Suportar explicitamente Django 5.1, 5.2 LTS e 6.0

O metadado do pacote usará `Django>=5.1,<6.1` e `Python>=3.10`. A matriz de testes combinará Django 5.1 e 5.2 com suas versões oficiais do Python e Django 6.0 apenas com Python 3.12 ou posterior. Além de testes unitários, cada combinação executará `django check`, migrações do app de teste e fluxos HTTP do Admin.

Alternativa considerada: suportar apenas Django 5.1 e 5.2. Foi rejeitada porque “5.1 para frente” inclui a versão estável 6.0 disponível na criação desta proposta.

### 2. Reconciliar os overrides com templates upstream antes de adaptar o visual

Cada override será comparado com os templates das três séries suportadas. Templates sem customização necessária serão removidos; os restantes serão reconstruídos a partir do contrato comum mais recente, mantendo blocos públicos, contexto, acessibilidade, formulários de logout, URLs e assets exigidos pelo Admin. Diferenças entre versões deverão ser encapsuladas em pequenos pontos de compatibilidade, não em três árvores completas de templates.

Alternativa considerada: copiar integralmente os templates do Django 6.0. Isso simplificaria a primeira execução, mas aumentaria o risco de incompatibilidade com 5.1 e conservaria o acoplamento que causou a obsolescência atual.

### 3. Separar compatibilidade funcional de restauração visual

A migração ocorrerá em duas passagens. Primeiro, templates e scripts serão ajustados até todos os fluxos funcionarem com HTML semanticamente válido. Depois, o SCSS do Garb será aplicado e ajustado contra as baselines. Essa separação permite distinguir falhas do Django/Bootstrap de diferenças puramente visuais.

Alternativa considerada: trocar vendors e retocar CSS página a página no mesmo passo. Foi rejeitada porque torna difícil localizar a origem de regressões.

### 4. Migrar para Bootstrap 5.3.8 usando o bundle

O CSS reboot e o CSS completo serão substituídos pelos artefatos oficiais correspondentes. O JavaScript passará a usar `bootstrap.bundle.min.js`, que já contém Popper, removendo o Popper vendorizado separadamente. Templates e scripts serão convertidos de atributos Bootstrap 4 como `data-toggle`/`data-parent` para `data-bs-toggle`/`data-bs-parent`, e utilitários direcionais serão atualizados quando necessário.

O SCSS do Garb continuará carregado depois do Bootstrap e preservará seu mapa de temas, dimensões, paletas, bordas e sombras. Overrides serão atualizados para o markup do Bootstrap 5 sem alterar o resultado visual aprovado.

Alternativa considerada: permanecer no Bootstrap 4.6.2 para reduzir mudanças. Foi rejeitada porque Bootstrap 4 está fora de suporte e não atende ao pedido de atualização para a geração atual.

### 5. Tratar bootstrap-select como dependência de compatibilidade controlada

Será usada a release oficial mais nova que declare suporte ao Bootstrap 5; no snapshot atual, `1.14.0-beta3`. Por ser pré-release, ela terá testes dedicados para selects simples, filtros, campos relacionados, inlines dinâmicos, opções vazias e localização. A versão ficará fixa, sem referência `latest` em runtime.

Alternativas consideradas: manter 1.13.x, que não é a linha destinada ao Bootstrap 5, ou substituir o plugin. A primeira mantém incompatibilidade estrutural; a segunda alteraria comportamento e aparência além do escopo.

### 6. Atualizar jQuery com um gate de compatibilidade dos plugins

Bootstrap 5 não exige jQuery, mas bootstrap-select, jQuery Toast Plugin e scripts do Garb exigem. A implementação avaliará primeiro jQuery 4.0.0, atual release upstream, com os testes interativos completos. Se um vendor solicitado não oferecer compatibilidade comprovada, será usada a release 3.x mais nova compatível, com a limitação e a evidência registradas no inventário. O pacote deixará de sobrescrever `admin/js/vendor/jquery/`; seu jQuery será servido por um caminho próprio para evitar colisão com os assets internos do Django Admin.

Alternativa considerada: reutilizar silenciosamente o jQuery interno do Django. Foi rejeitada porque esse caminho não é uma API pública do Django e cria acoplamento entre plugins do Garb e a implementação do Admin.

### 7. Atualizar vendors de forma reproduzível

jQuery Toast Plugin, Pace e demais assets serão obtidos de tags/releases oficiais, mantidos localmente e registrados com nome, versão, URL de origem, licença e checksum. Arquivos antigos serão substituídos em vez de coexistirem sem uso. O procedimento de atualização será documentado para que uma release futura possa repetir a origem dos arquivos.

Alternativa considerada: usar CDN. Foi rejeitada porque prejudica ambientes offline, CSP, reprodutibilidade e controle da ordem de carregamento.

### 8. Criar uma aplicação visual determinística e testes em navegador

O app de testes ganhará dados, permissões e páginas suficientes para reproduzir índice, lista, edição, login, exclusão, histórico e widgets. Um navegador headless capturará viewports fixos para os cinco temas. Comparações visuais usarão tolerância pequena para antialiasing e diferenças de renderização; áreas dinâmicas como datas e tokens serão estabilizadas ou mascaradas.

Os testes de navegador também verificarão ausência de erros no console e os estados aberto/fechado de menu, dropdown, selects, toasts, ações e sidebar. As imagens atuais orientarão a primeira baseline reproduzível; qualquer diferença material precisará de revisão antes de substituir a baseline.

Alternativa considerada: revisar as imagens apenas manualmente. Foi rejeitada porque não protege releases posteriores nem a matriz de versões do Django.

## Risks / Trade-offs

- [bootstrap-select para Bootstrap 5 permanece em pré-release] → Fixar a versão, cobrir os fluxos críticos e bloquear a atualização caso os testes ou a comparação visual falhem.
- [jQuery 4 pode quebrar plugins antigos] → Executar o gate de compatibilidade e manter temporariamente a versão 3.x mais nova compatível quando necessário, documentando o motivo e um caminho de revisão futura.
- [Templates do Admin variam entre Django 5.1 e 6.0] → Reduzir overrides, testar todas as séries e encapsular somente diferenças inevitáveis.
- [Bootstrap 5 altera markup, utilitários e especificidade] → Manter os tokens Garb como fonte do resultado visual e migrar seletores com comparação por componente.
- [Capturas históricas não são baselines reproduzíveis] → Criar fixtures, viewport, fontes e navegador fixos antes de aprovar novas baselines.
- [Testes visuais podem gerar falsos positivos] → Usar ambiente fixo, tolerância controlada e separar snapshots por página/tema em vez de uma única imagem extensa.
- [A matriz completa pode aumentar o tempo de CI] → Executar testes Python em toda a matriz e reservar a regressão visual completa para uma combinação canônica, mantendo smoke tests de renderização nas demais.

## Migration Plan

1. Registrar o inventário atual e produzir baselines reproduzíveis antes de trocar templates ou vendors.
2. Criar ambientes de teste para Django 5.1, 5.2 e 6.0 e tornar o backend compatível sem alterar intencionalmente o visual.
3. Reconciliar os templates com o Admin atual e validar todos os fluxos funcionais.
4. Atualizar Bootstrap, bootstrap-select, jQuery Toast Plugin, Pace e o jQuery compatível, migrando markup e scripts.
5. Recompilar o SCSS e corrigir regressões até as comparações visuais e interativas serem aprovadas.
6. Validar o wheel/sdist em ambiente limpo, atualizar documentação e publicar uma nova versão principal ou outra versão que comunique claramente a quebra da faixa Django/Python antiga.

Para rollback antes da publicação, os assets e templates podem voltar ao último commit conhecido. Após a publicação, consumidores incompatíveis deverão fixar a release antiga; a nova faixa mínima não deverá ser revertida silenciosamente em patch release.
