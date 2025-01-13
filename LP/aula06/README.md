<img src="https://www.cesar.school/wp-content/uploads/2019/09/marca_cesar_school.png" alt="drawing" width="200"/>

# NExT 2024.2 **Lógica de Programação** com Python
## Aula 06 - Estruturas de Dados

### Na aula de hoje:
- Tuple
- Set
- Dict

------------------

# Estruturas de Dados

Sempre que precisamos armazenar vários dados em uma única variável se faz necessário usar algum tipo de dado **Container**. Em Python, os principais são:
- `list`;
- `tuple`;
- `set`;
- `dict`;

Cada containers, ou tipos de coleção, tem uma característica específica e um uso diferente. Nesta aula vamos conhecer um pouco mais sobre eles.

## 🪨 `tuple`

Ao usar listas, há bastante liberdade para alterar seus itens. Em determinadas situções, essas listas não deveriam ser alteradas, tais como:
- Dias da semana;
- Coordenadas de um prédio;
- Letras de um alfabeto.

> ### Características:
- Imutáveis;
- Ordenados/indexável;
- Permite elementos duplicados.


```python
t = ('domingo', 'segunda', 'terça', 'quarta', 'quinta', 'sexta', 'sábado')
```

> 💡 Obs.: *O acesso aos elementos de uma tupla é feito da mesma forma que com listas*

```python
# Tópicos a explorar:
# - Criação de uma Tupla
# - Acesso aos elementos de uma Tupla
# - len()
# - tupla.index(item)
# - tupla.count(item)
# - Imutabilidade
```

## 💎 `set`

Tanto em **listas**, quanto em **tuplas**, é possível ter elementos repetidos:

```python
t = (0, 1, 1, 2, 3, 5)
l = [0, 1, 1, 2, 3, 5]
```

Quanto houver uma situação onde você não deva armazenar itens repetidos numa lista, é possível usar um `set`:

```python
s1 = set()
s.add(1)
s.add(2)
s.add(1)

s2 = {'bacon', 'banana', 'spam', 'ovos', 'spam', 'salsicha', 'spam'}
```

> ### Características:
- Imutáveis (mas podem ser adicionados e removidos);
- Não Ordenados/ não indexável;
- Não Permite elementos duplicados.

```python
# Tópicos a explorar:
# - criar um set
# - print(ingredientes[0]) # erro!
# - adicionar elementos
# - remover elementos
```

## 🔑 Dicionários

Para criar estruturas de dados que são mapeados por valores (e não pelo indice, como nas listas) é possível usar um dicionário.

> **Chave** x **Valor**

Obs.: *O mapeamento é feito pela chave (e não pela ordem)*

Exemplos de uso prático:
- Dicionários;
- CEP;

```python
dicionario = {'chave': 'valor1', 'chave2': 'valor2'}
```

> ### Características:
- Mutáveis;
- Ordenados/indexável;
- Permite valores duplicados (mas não a chave).

```python
# Tópicos a explorar
# - Criando um dicionário
# - Acessando elementos de um dicionário
# - Adição de itens por atribuição
# - Adição de itens por update
# - Removendo itens
# - esvaziando um dicionário
```

### 🗝️ Alguns métodos úteis de dicionários

- `dict.keys()` - Apresenta todas as chaves do dicionário
- `dict.values()` - Apresenta todos os valores do dicionário
- `dict.items()` - `dict_keys()` + `dict_values()`

```python
# Tópicos a explorar
# - keys()
# - values()
# - items()
# - for
```

## 📋 Resumão

| Tipo  |Mutável|Ordenado|Indexável|Elementros Duplicados|
|-------| :---: | :----: | :-----: | :-----------------: |
|`list` |   ✅  |   ✅  |   ✅   |          ✅          |
|`tuple`|   ❌  |   ✅  |   ✅   |          ✅          |
| `set` |   ✅  |   ❌  |   ❌   |          ❌          |
|`dict` |   ✅  |   ✅  |   ✅*  |          ✅          |

# 🐝 Exercícios Beecrowd

[1050 - DDD](https://www.beecrowd.com.br/judge/pt/problems/view/1050)

[1168 - LED](https://www.beecrowd.com.br/judge/pt/problems/view/1168)

[1049 - Animal](https://judge.beecrowd.com/pt/problems/view/1049)

[1179 - Preenchimento de Vetor IV*](https://judge.beecrowd.com/pt/problems/view/1179)

[2653 - Dijkstra**](https://www.beecrowd.com.br/judge/pt/problems/view/2653)

\* questão sobre vetor, mas é uma boa oportunidade de usar função

\*\* Essa questão exige os conhecimentos da próxima aula

# 🧱 Exercícios Fundamentais

1. Dada a lista a seguir, crie uma nova lista onde cada um desses elementos aparece apenas uma única vez.
```python
l = [1, 3, 2, 3, 4, 5, 1, 5, 7, 6, 8, 3, 4]
```

2. Crie um programa com duas funções. A primeira deve pedir um CEP e o endereço do usuário e armazena-lo em um dicionário. A segunda deve pesquisar um endereço, buscando pelo CEP informado.

🏆 Desafio: Armazene o dicionário em um arquivo.
