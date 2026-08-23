## Purpose

Define a faixa moderna de Django e Python na qual o Django Garb deve instalar, inicializar e executar os fluxos administrativos suportados de forma confiável.

## ADDED Requirements

### Requirement: Matriz suportada de Django e Python
O pacote SHALL suportar Django 5.1, Django 5.2 LTS e Django 6.0 em todas as versões do Python oficialmente aceitas por cada série e SHALL declarar Python 3.10 e Django 5.1 como mínimos gerais.

#### Scenario: Instalação em combinação suportada
- **WHEN** o pacote for instalado com uma combinação de Django e Python pertencente à matriz declarada
- **THEN** a resolução de dependências deverá concluir sem conflito causado pelos metadados do Django Garb

#### Scenario: Verificação da série mais nova
- **WHEN** a suíte for executada com Django 6.0 e uma versão do Python suportada por essa série
- **THEN** todos os testes funcionais e checks do Django deverão concluir com sucesso

### Requirement: Fluxos administrativos funcionais
O pacote SHALL renderizar e processar os fluxos padrão de índice, listagem, busca, filtro, paginação, inclusão, edição, exclusão, histórico, autenticação e recuperação de senha nas séries suportadas do Django.

#### Scenario: Operação CRUD autorizada
- **WHEN** um usuário com permissão acessa e executa uma operação CRUD no Admin tematizado
- **THEN** a página deverá usar o layout Garb e a operação deverá manter a semântica, validação, mensagens e redirecionamento definidos pelo Django Admin

#### Scenario: Operação sem permissão
- **WHEN** um usuário não possui a permissão exigida para uma aplicação, modelo ou operação
- **THEN** o menu e as páginas deverão respeitar as decisões de autorização do Django sem expor ações indevidas

### Requirement: Configuração pública compatível
O pacote SHALL preservar as chaves públicas existentes de `GARB_CONFIG` para nome do projeto, menu, tema, paginação, ações, widgets relacionados e perfil, corrigindo apenas comportamentos inválidos ou incompatíveis com o Django suportado.

#### Scenario: Projeto atualiza sem reconfigurar o tema
- **WHEN** um projeto com uma configuração válida do Django Garb atualiza para uma versão suportada
- **THEN** as mesmas chaves deverão continuar produzindo o nome, menu, tema, paginação e opções de usuário correspondentes

#### Scenario: Chave omitida
- **WHEN** uma chave opcional não está presente em `GARB_CONFIG`
- **THEN** o pacote deverá aplicar o valor padrão documentado sem falhar durante a importação ou renderização

### Requirement: Integração sem APIs removidas
O pacote MUST executar seus caminhos suportados sem depender de APIs removidas do Python ou das séries suportadas do Django.

#### Scenario: Execução com avisos de depreciação visíveis
- **WHEN** a suíte for executada na versão mais nova suportada com avisos de depreciação habilitados
- **THEN** o código do Django Garb não deverá emitir aviso causado por uma API já descontinuada na faixa suportada

### Requirement: Pacote distribuível e documentado
O pacote SHALL incluir templates, traduções e assets necessários e SHALL documentar claramente sua faixa de Django/Python, instalação, configuração e procedimento de coleta de arquivos estáticos.

#### Scenario: Instalação a partir do artefato de distribuição
- **WHEN** um ambiente limpo instala o wheel ou sdist produzido pelo projeto
- **THEN** o Django deverá localizar os templates, traduções, CSS, JavaScript e assets do Garb após a configuração documentada

