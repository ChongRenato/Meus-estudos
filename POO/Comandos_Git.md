# Lista de Comandos de Git

Esta lista de exercícios irá ajudá-lo a consolidar os conceitos e comandos básicos do Git abordados na primeira aula. 
Lembre-se de praticar os comandos em um ambiente real, utilizando o terminal ou Git Bash, para uma melhor compreensão.

## Exercício 1: Instalando o Git
1. Baixe e instale o Git a partir de [https://git-scm.com/downloads](https://git-scm.com/downloads).
2. Verifique a instalação com:  
   ```
   git --version
   ```
3. Resposta: A versão instalada será exibida (ex.: `git version 2.x.x`).

## Exercício 2: Criando uma Conta no GitHub
1. Crie uma conta no GitHub em [https://github.com](https://github.com).  
2. Personalize seu perfil com nome, foto, e outras informações.

## Exercício 3: Configuração Inicial do Git
1. Configure seu nome e e-mail para os commits:  
   ```bash
   git config --global user.name "Seu Nome"
   git config --global user.email "seuemail@example.com"
   ```
2. **Por que configurar essas informações?**  
   - Elas são usadas para identificar o autor dos commits no histórico do projeto.

## Exercício 4: Iniciar um Repositório Local
1. Crie uma pasta chamada `meu_projeto` e navegue até ela:  
   ```bash
   mkdir meu_projeto
   cd meu_projeto
   ```
2. Inicialize um repositório Git:  
   ```bash
   git init
   ```
   **Resposta:** O comando usado foi `git init`.  

3. Crie um arquivo README:  
   ```bash
   echo "# Meu Projeto" > README.md
   ```

## Exercício 5: Status do Repositório
1. Crie um arquivo `index.html`:  
   ```bash
   touch index.html
   ```
2. Verifique o status:  
   ```bash
   git status
   ```
   **Resposta:** O arquivo `index.html` estará listado como "Untracked files".

## Exercício 6: Adicionando Arquivos à Staging Area
1. Adicione o arquivo:  
   ```bash
   git add index.html
   ```
   **Resposta:** O comando foi `git add index.html` (ou `git add .` para adicionar todos os arquivos).  

2. Verifique o status novamente:  
   ```bash
   git status
   ```
   **Resposta:** O arquivo agora aparece como "Changes to be committed".

## Exercício 7: Fazendo o Primeiro Commit
1. Realize o commit:  
   ```bash
   git commit -m "Primeiro commit: adiciona index.html"
   ```
   **Resposta:** O comando usado foi `git commit -m "Mensagem do commit"`.  

2. **Por que mensagens claras são importantes?**  
   - Para documentar mudanças, facilitando o entendimento do histórico.

## Exercício 8: Criando um Repositório Remoto no GitHub
1. Crie um repositório no GitHub chamado `meu_projeto_remoto`.  
2. Conecte ao repositório remoto:  
   ```bash
   git remote add origin https://github.com/seu_usuario/meu_projeto_remoto.git
   git branch -M main
   ```

## Exercício 9: Enviando Mudanças para o Repositório Remoto
1. Envie as mudanças:  
   ```bash
   git push -u origin main
   ```
   **Resposta:** O comando usado foi `git push`.  

2. **O que acontece se não houver repositório remoto conectado?**  
   - O Git retornará um erro informando que não há origem remota configurada.

## Exercício 10: Clonando um Repositório
1. Comando para clonar:  
   ```bash
   git clone https://github.com/seu_usuario/meu_projeto_remoto.git
   ```

2. **Diferença entre `git clone` e `git init`:**  
   - `git init` inicializa um repositório vazio localmente.  
   - `git clone` cria uma cópia de um repositório remoto.

## Exercício 11: Criando e Navegando entre Branches
1. Crie uma nova branch:  
   ```bash
   git checkout -b feature_a
   ```
2. Mude para a branch:  
   ```bash
   git checkout feature_a
   ```

## Exercício 12: Mesclando Branches
1. Mescle `feature_a` na `main`:  
   ```bash
   git checkout main
   git merge feature_a
   ```

2. **O que acontece em caso de conflito?**  
   - O Git sinaliza o conflito. Para resolver, edite os arquivos conflitantes, remova as marcações, e finalize o merge:  
     ```bash
     git add .
     git commit
     ```

## Exercício 13: Atualizando o Repositório Local
1. Comando para atualizar:  
   ```bash
   git pull
   ```
2. **Diferença entre `git pull` e `git fetch`:**  
   - `git fetch` baixa as mudanças sem mesclar.  
   - `git pull` baixa e mescla as mudanças automaticamente.

## Exercício 14: Workflow Completo
1. **Fluxo Completo:**  
   - Instalar o Git.  
   - Configurar nome e e-mail.  
   - Inicializar um repositório (`git init`).  
   - Adicionar arquivos (`git add .`).  
   - Realizar commits (`git commit -m "Sua mensagem"`).  
   - Conectar a um repositório remoto (`git remote add`).  
   - Enviar mudanças (`git push -u origin main`).  

2. **Por que seguir um fluxo organizado?**  
   - Para evitar conflitos, manter o histórico claro e facilitar o trabalho em equipe.

## **Exercício 15: Conflito de Código em Alterações Simultâneas**
1. **Simulação do conflito:**
   - Crie uma branch `feature_a` e adicione uma linha no arquivo `colaborativo.txt`:  
     ```bash
     git checkout -b feature_a
     echo "Este é um arquivo colaborativo" > colaborativo.txt
     git add colaborativo.txt
     git commit -m "Adiciona linha inicial em colaborativo.txt"
     ```
   - Volte para a branch `main` e adicione outra linha no mesmo arquivo:  
     ```bash
     git checkout main
     echo "Texto inicial diferente" > colaborativo.txt
     git add colaborativo.txt
     git commit -m "Adiciona linha inicial diferente em colaborativo.txt"
     ```

2. **Tente mesclar `feature_a` na branch `main`:**  
   ```bash
   git merge feature_a
   ```
   **Erro esperado:** O Git exibirá uma mensagem informando um conflito em `colaborativo.txt`.  

3. **Resolvendo o conflito:**
   - Abra o arquivo e escolha como resolver o conflito (manualmente ou usando ferramentas de IDE).  
   - Após resolver, finalize o merge:  
     ```bash
     git add colaborativo.txt
     git commit
     ```

## **Exercício 16: Conflito em Arquivo Já Existente**
1. **Criando o conflito:**
   - Crie uma branch `feature_b` e edite o arquivo `index.html`:  
     ```bash
     git checkout -b feature_b
     echo "<h1>Nova seção no index.html</h1>" >> index.html
     git add index.html
     git commit -m "Adiciona nova seção no index.html"
     ```
   - Na branch `main`, faça outra modificação no mesmo lugar:  
     ```bash
     git checkout main
     echo "<h1>Seção de boas-vindas no index.html</h1>" >> index.html
     git add index.html
     git commit -m "Adiciona seção de boas-vindas no index.html"
     ```

2. **Tentativa de mesclar:**
   ```bash
   git merge feature_b
   ```
   **Erro esperado:** Conflito no arquivo `index.html`.

3. **Opções de resolução:**
   - **Accept Current Change:** Aceita a alteração da branch atual (`main`).  
   - **Accept Incoming Change:** Aceita a alteração da branch mesclada (`feature_b`).  
   - **Accept Both Changes:** Combina ambas as alterações.  
   - Após escolher, finalize o merge:  
     ```bash
     git add index.html
     git commit
     ```

## **Exercício 17: Conflito em Deleção e Modificação**
1. **Simulando o conflito:**
   - Crie a branch `feature_delete` e exclua o arquivo `index.html`:  
     ```bash
     git checkout -b feature_delete
     rm index.html
     git commit -m "Remove index.html"
     ```
   - Volte para a branch `main` e modifique o mesmo arquivo:  
     ```bash
     git checkout main
     echo "<p>Texto de introdução</p>" >> index.html
     git add index.html
     git commit -m "Adiciona texto de introdução no index.html"
     ```

2. **Tentativa de mesclar:**
   ```bash
   git merge feature_delete
   ```
   **Erro esperado:** O Git informará que o arquivo foi modificado e excluído em diferentes branches.

3. **Resolvendo o conflito:**
   - Escolha se deseja manter ou excluir o arquivo.  
   - Finalize o merge conforme a decisão:  
     ```bash
     git add .
     git commit
     ```

## **Exercício 18: Conflito em Arquivo Binário**
1. **Criando o conflito:**
   - Na branch `feature_image`, adicione um arquivo `logo.png`:  
     ```bash
     git checkout -b feature_image
     cp /caminho/para/logo1.png logo.png
     git add logo.png
     git commit -m "Adiciona logo inicial"
     ```
   - Na branch `main`, substitua `logo.png` por outra versão:  
     ```bash
     git checkout main
     cp /caminho/para/logo2.png logo.png
     git add logo.png
     git commit -m "Substitui logo por uma nova versão"
     ```

2. **Tentativa de mesclar:**
   ```bash
   git merge feature_image
   ```
   **Erro esperado:** Conflito em `logo.png`.

3. **Como o Git trata arquivos binários?**
   - O Git não consegue mesclar arquivos binários automaticamente.  
   - **Solução:** Substitua manualmente o arquivo ou use ferramentas de comparação externas.

## **Exercício 19: Conflito na Colaboração em Equipe**
1. **Simulação de conflito colaborativo:**
   - Você cria uma branch `feature_teamwork` e modifica `index.html`:  
     ```bash
     git checkout -b feature_teamwork
     echo "Linha adicionada por você" >> index.html
     git add index.html
     git commit -m "Sua modificação"
     ```
   - Seu colega cria a mesma branch e adiciona outra linha no mesmo arquivo.

2. **Tentativa de mesclar na `main`:**
   - Ambos tentam fazer o merge. O Git detecta o conflito.

3. **Resolvendo conflitos colaborativos:**
   - Combine as alterações em conjunto, resolvendo manualmente.  
   - **Importância da comunicação:** Ela previne conflitos e perdas de dados, garantindo um fluxo organizado.

## **Exercício 20: Conflito por Rebase**
1. **Simulação de rebase com conflito:**
   - Na branch `feature_c`, modifique `index.html`:  
     ```bash
     git checkout -b feature_c
     echo "Alteração na feature_c" >> index.html
     git add index.html
     git commit -m "Modifica index.html na feature_c"
     ```
   - Volte para a branch `main` e faça outra alteração no arquivo:  
     ```bash
     git checkout main
     echo "Alteração na main" >> index.html
     git add index.html
     git commit -m "Modifica index.html na main"
     ```
   - Tente rebasear `feature_c` na `main`:  
     ```bash
     git checkout feature_c
     git rebase main
     ```

2. **Conflitos durante o rebase:**
   - O Git sinaliza o conflito. Resolva manualmente, use `git add` e continue o rebase:  
     ```bash
     git rebase --continue
     ```

## **Exercício 21: Merge vs Rebase em Situação de Conflito**
1. **Comparação prática:**
   - Realize o merge:  
     ```bash
     git checkout main
     git merge feature_merge_vs_rebase
     ```
   - Realize o rebase:  
     ```bash
     git checkout feature_merge_vs_rebase
     git rebase main
     ```

2. **Diferença:**
   - **Merge:** Preserva o histórico original, criando um commit de mesclagem.  
   - **Rebase:** Reescreve o histórico, criando um fluxo linear.  

3. **Quando usar:**
   - **Merge:** Colaboração em equipe ou histórico detalhado.  
   - **Rebase:** Manter o histórico limpo e linear.
