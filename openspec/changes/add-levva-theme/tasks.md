## 1. Paleta e tema

- [x] 1.1 Adicionar o mapa de tokens `levva` ao SCSS com a paleta azul-marinho, laranja e superfícies claras definida no design
- [x] 1.2 Ajustar os tokens e estados específicos necessários para que menus, links, botões, formulários e tabelas usem pares de cores acessíveis
- [x] 1.3 Compilar e versionar os arquivos CSS expandido, minificado e respectivos source maps

## 2. Validação de acessibilidade

- [x] 2.1 Adicionar teste automatizado da matriz de contraste do tema Levva para texto normal, texto grande e componentes essenciais
- [x] 2.2 Executar os testes de contraste e a suíte Python existente, corrigindo eventuais regressões dentro do escopo

## 3. Cobertura visual e documentação

- [x] 3.1 Incluir `levva` na seleção da suíte visual e gerar a baseline representativa da listagem
- [x] 3.2 Auditar visualmente login, índice, listagem, formulário, exclusão e histórico com o tema ativo, incluindo foco, hover e estados ativos
- [x] 3.3 Documentar `levva` entre os valores aceitos por `GARB_CONFIG['THEME']` e atualizar a contagem/descrição da suíte visual

## 4. Verificação final

- [x] 4.1 Executar build limpo, testes automatizados e comparação visual, confirmando que os temas existentes permanecem sem diferenças
- [x] 4.2 Validar os artefatos OpenSpec em modo estrito e registrar o resultado da implementação
