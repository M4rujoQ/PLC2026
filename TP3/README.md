# TPC 3: Analisador Léxico

## Autor
* **Nome:** Paulo Gabriel Torres Rodrigues
* **Número de Aluno:** A110640
* **Fotografia:**

<img width="400" alt="IMG_4527" src="https://github.com/user-attachments/assets/b0307bcf-156a-4fc5-8323-9bf98bee752b" />

## Resumo
Construir um analisador léxico em Python para uma linguagem de query semelhante ao SPARQL. 
O programa lê texto do `stdin` e produz a lista de tokens reconhecidos, sem interpretar o seu significado.

**Tokens reconhecidos**

| Token | Descrição | Exemplo |
|---|---|---|
| `COMENT` | `#` até ao fim da linha (ignorado) | `# comentário` |
| `VAR` | `?` seguido de alfanuméricos | `?nome` |
| `LANG` | `@` seguido de 2 letras | `@en` |
| `STRING` | qualquer sequência entre aspas | `"Chuck Berry"` |
| `PR` | palavras reservadas | `select`, `where`, `LIMIT` |
| `DELIM` | delimitadores | `{`, `}`, `.` |
| `NUM` | sequência de dígitos | `1000` |
| `CONC` | conceito: alfanuméricos com `:` opcional | `dbo:MusicalArtist`, `a` |
| `ERRO` | qualquer outro carater que não seja espaço | `%` |

## Lista de Resultados
* [analexico.py](./analexico.py) - Script principal em Python com a implementação do analisador léxico.
* [exemplo.txt](./exemplo.txt) - Ficheiro de teste.
* [res.txt](./res.txt) - Ficheiro gerado com o resultado.
