# Projeto Flask com pipeline DevSecOps

App web simples em Python (Flask) criado para estudar DevSecOps na prática.

## O que o projeto faz

- API em Flask com as rotas: `/` (mensagem), `/saude` (status), `/saudacao/<nome>` e `/mensagem` (POST com JSON).
- Validação da entrada no POST: retorna 400 se faltar o campo `texto` e limita o tamanho a 200 caracteres.
- Resposta padronizada para rotas inexistentes (404).
- Pipeline de segurança automatizado no GitHub Actions, que roda a cada push na branch main e a cada pull request.

## Pipeline de segurança

- **SAST com Bandit:** analisa o código Python em busca de práticas inseguras.
- **SCA com pip-audit:** confere se as dependências do requirements.txt têm vulnerabilidades conhecidas.

Se uma das ferramentas encontrar problema, o pipeline falha e o código é barrado.

## Como rodar

```
pip install -r requirements.txt
python main.py
```

Depois abra http://127.0.0.1:5000

## Testando o POST (Prompt de Comando do Windows)

```
curl -X POST http://127.0.0.1:5000/mensagem -H "Content-Type: application/json" -d "{\"texto\":\"oi\"}"
```

## Aprendizados

- Testei o pipeline de propósito com `debug=True`: o Bandit apontou a falha de gravidade alta (B201) e o pull request foi reprovado.
- Ferramentas de SAST funcionam por padrões: um erro de digitação (`debub=True`) fez o pipeline passar verde sem achar nada. Um resultado verde só vale o quanto o teste realmente testou.
- Quando o passo do Bandit falha, o pip-audit é pulado. Melhoria futura: separar em jobs diferentes para os dois rodarem sempre.

## Autor

renanscarmo - [LinkedIn](https://www.linkedin.com/in/renan-s-do-carmo-b4a936244)