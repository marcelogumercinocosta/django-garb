# Testes visuais

As capturas usam viewport `1680x984`, locale `pt-BR`, fuso
`America/Sao_Paulo` e as fixtures do comando `seed_visual`. A composição foi
conferida com as imagens históricas em `docs/source/_static/` antes da criação
das baselines.

Com um servidor em `127.0.0.1:8765` usando o banco semeado, execute:

```console
npm run test:browser
```

Somente depois de revisar uma alteração visual intencional, regenere com:

```console
npm run test:visual:update
```

O teste reprova diferenças acima de 1%, ausência de componentes esperados e
erros JavaScript ou de assets locais. A matriz cobre seis temas, incluindo o
tema ``levva``. Capturas e diffs temporários ficam em
`tests/visual/actual/` e `tests/visual/diff/`.
