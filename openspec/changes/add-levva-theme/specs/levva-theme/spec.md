## Purpose

Disponibilizar uma identidade visual Levva selecionável e acessível para todas as telas administrativas cobertas pelo Django Garb.

## ADDED Requirements

### Requirement: Seleção do tema Levva
O sistema SHALL aceitar `levva` como valor de `GARB_CONFIG['THEME']` e aplicar a identidade visual correspondente ao corpo das páginas administrativas, sem alterar o tema padrão nem o comportamento dos demais temas.

#### Scenario: Administrador configura o tema Levva
- **WHEN** a aplicação define `GARB_CONFIG['THEME']` como `levva`
- **THEN** as páginas do Django Garb são renderizadas com o tema Levva

#### Scenario: Aplicação não seleciona o tema Levva
- **WHEN** a aplicação mantém outro valor de tema suportado
- **THEN** a aparência desse tema permanece inalterada

### Requirement: Identidade visual baseada na referência Levva
O tema Levva SHALL usar azul-marinho como cor estrutural, laranja como destaque e superfícies brancas ou cinza-claro, de modo consistente nos menus, cabeçalhos, títulos, links, botões, formulários, tabelas e estados interativos do admin.

#### Scenario: Interface administrativa com tema Levva
- **WHEN** um usuário acessa uma tela administrativa com o tema Levva ativo
- **THEN** os principais componentes exibem a paleta e a hierarquia visual inspiradas no documento de referência

### Requirement: Contraste acessível das cores
As combinações de primeiro plano e fundo do tema Levva MUST atender ao nível AA da WCAG 2.1: razão mínima de 4,5:1 para texto normal e 3:1 para texto grande, controles, bordas essenciais, foco e estados interativos. O laranja de marca não SHALL ser usado como texto pequeno sobre branco quando não alcançar 4,5:1.

#### Scenario: Auditoria das combinações de texto
- **WHEN** as combinações de texto e fundo do tema Levva são avaliadas
- **THEN** cada texto normal apresenta contraste de pelo menos 4,5:1 e cada texto grande apresenta contraste de pelo menos 3:1

#### Scenario: Auditoria de componentes interativos
- **WHEN** controles, bordas essenciais, foco, hover, seleção e estados ativos são avaliados
- **THEN** cada indicador visual necessário apresenta contraste de pelo menos 3:1 em relação às cores adjacentes relevantes

### Requirement: Documentação e regressão visual
O sistema SHALL documentar `levva` entre os valores de tema suportados e SHALL incluir uma captura representativa do tema na suíte visual automatizada.

#### Scenario: Consulta à configuração de temas
- **WHEN** um integrador consulta a documentação de `THEME`
- **THEN** encontra `levva` listado como uma opção suportada

#### Scenario: Execução da suíte visual
- **WHEN** a suíte visual é executada com suas baselines aprovadas
- **THEN** uma listagem administrativa com o tema Levva é renderizada e comparada sem erros de assets ou JavaScript
