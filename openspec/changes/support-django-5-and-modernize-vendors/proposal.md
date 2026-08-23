## Why

O Django Garb ainda empacota templates e dependências front-end da geração Django 3/Bootstrap 4, contém APIs incompatíveis com Python moderno e não declara uma faixa suportada do Django. A atualização é necessária para permitir seu uso seguro em projetos Django 5.1 ou posteriores sem perder a identidade visual documentada nas capturas de tela existentes.

## What Changes

- Declarar e validar suporte ao Django 5.1, Django 5.2 LTS e Django 6.0, respeitando a matriz oficial de versões do Python de cada série.
- Atualizar os templates sobrescritos, template tags, formulários, URLs, testes e configuração para as APIs atuais do Django Admin, removendo imports e padrões obsoletos.
- Atualizar os assets vendorizados para as versões oficiais atuais compatíveis: Bootstrap 5.3.8 (CSS e bundle JavaScript), bootstrap-select com suporte a Bootstrap 5, jQuery Toast Plugin e Pace; atualizar também o jQuery necessário aos plugins após validar sua compatibilidade.
- Migrar markup, atributos `data-*` e inicialização JavaScript afetados pela passagem do Bootstrap 4 para o Bootstrap 5.
- Preservar as cinco aparências documentadas (`default`, `light`, `hybrid`, `dark` e `alive`) e os layouts das páginas de lista, edição, login, exclusão, histórico e índice, usando as capturas existentes como baseline visual.
- Criar uma matriz automatizada de compatibilidade para Django/Python e testes de renderização e regressão visual dos principais fluxos do Admin.
- Atualizar metadados de pacote, documentação de instalação, versões suportadas e inventário/licenças dos vendors.
- **BREAKING**: elevar a versão mínima do Python para 3.10 e a versão mínima do Django para 5.1; projetos em Django 3.x/4.x ou Python anterior precisarão permanecer em uma versão antiga do Django Garb.

## Capabilities

### New Capabilities

- `modern-django-support`: instalação, inicialização e fluxos funcionais do Django Admin em Django 5.1, 5.2 LTS e 6.0, com a matriz correspondente de versões do Python.
- `admin-visual-compatibility`: preservação da aparência e interação documentadas enquanto templates, Bootstrap e demais assets front-end são modernizados.

### Modified Capabilities

- Nenhuma; o projeto ainda não possui especificações principais registradas no OpenSpec.

## Impact

- Código Python em `garb/config.py`, `garb/forms.py`, `garb/compat.py`, `garb/urls.py`, `garb/views.py` e `garb/templatetags/`.
- Templates em `garb/templates/admin/`, `garb/templates/registration/` e templates-base do pacote.
- SCSS/CSS, JavaScript e assets em `garb/static/`, incluindo markup e seletores dependentes do Bootstrap 4.
- Empacotamento, declaração de dependências, documentação e suíte de testes.
- Consumidores passam a depender de Python 3.10+ e Django 5.1+; configurações públicas de tema e menu permanecem compatíveis sempre que não dependerem de comportamento inválido ou inseguro.
