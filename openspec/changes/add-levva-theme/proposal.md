## Why

O Django Garb precisa oferecer uma variação visual alinhada à identidade da Levva, tomando como referência a fatura de locação fornecida. O novo tema deve traduzir a combinação de azul-marinho, laranja, branco e cinzas claros sem comprometer legibilidade ou acessibilidade.

## What Changes

- Adiciona o tema selecionável `levva` à coleção de temas do Django Garb.
- Define uma paleta inspirada no documento de referência, com azul-marinho como cor estrutural, laranja como destaque e superfícies claras.
- Garante contraste WCAG 2.1 nível AA para texto, controles, estados interativos e indicadores visuais relevantes.
- Inclui o tema na documentação de configuração e na cobertura visual automatizada.
- Mantém os temas existentes e o valor padrão inalterados.

## Capabilities

### New Capabilities

- `levva-theme`: Aparência, seleção, acessibilidade de cores, documentação e validação visual do tema Levva.

### Modified Capabilities

Nenhuma.

## Impact

- Estilos-fonte SCSS e artefatos CSS compilados distribuídos pelo pacote.
- Configuração pública `GARB_CONFIG['THEME']`, que passa a aceitar `levva`.
- Documentação de configuração e catálogo visual de temas.
- Testes automatizados de interface e contraste; nenhuma dependência de produção nova é prevista.
