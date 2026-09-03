## Verificação

- `npm run build:css`: aprovado; CSS expandido, minificado e source maps regenerados.
- `npm run test:contrast`: aprovado; nove pares WCAG verificados, com mínimos de 4,5:1 para texto e 3:1 para componentes.
- `python -W error::DeprecationWarning -m django check --settings=garb.tests.settings`: aprovado, sem alertas.
- `python -W error::DeprecationWarning manage.py test garb.tests`: 33 testes aprovados no Django 5.2.17.
- `npm run test:browser`: 11 capturas e seis temas aprovados, sem erros de JavaScript ou assets.
- Auditoria Levva dedicada: login, índice, listagem, formulário, exclusão e histórico aprovados com foco e hover exercitados.
- `openspec validate add-levva-theme --strict`: aprovado.

O tema é opt-in por meio de `GARB_CONFIG['THEME'] = 'levva'`; os temas existentes e o padrão permanecem inalterados.
