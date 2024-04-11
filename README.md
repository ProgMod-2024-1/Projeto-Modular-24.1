# Projeto em Flask
Este é um projeto em Flask para sei la alguem altera essa parte aqui

## Configuração do Ambiente
Clone o repositório e abra a pasta do projeto na sua IDE.

Crie um ambiente virtual Python (venv) usando o comando:
```bash
python -m venv .venv.
```
ou pelo command pallete (cntrl + shift + p ) '>Python:Create Environment'.

Escolha a versao mais recente de Python (nao esquece de baixar a mais nova se nao tiver). Apos a criacao sera possivel ativa-la.

## Ative a venv:

No Windows:
```bash
.\.venv\Scripts\activate
```
No macOS/Linux:
```bash
source .venv/bin/activate
```
para desativar a venv basta usar o comando:
```bash
deactivate
```

A utilização de uma venv é aconselhável para isolar as dependências do projeto, evitando conflitos entre diferentes projetos e facilitando a distribuição do projeto.

## Instale o gerenciador de pacotes Poetry:

```bash
pip install poetry
```
Instale as dependências do projeto com o comando:

```bash
poetry install
```
O Poetry foi escolhido como gerenciador de pacotes devido à sua facilidade de uso e integração com o Python.

## Executando o Projeto
Com o diretorio do projeto aberto na IDE e a venv ativada, para rodar o projeto utilize o comando:

```bash
python ./project/main.py
```

O acesso a aplicacao estará disponível na porta padrão do Flask: http://127.0.0.1:5000/.

## Adicionando Pacotes
Se for necessário adicionar um novo pacote ao projeto, utilize o comando:

```bash
poetry add nome-do-pacote
```
Isso irá adicionar o pacote ao arquivo pyproject.toml e instalara as dependências necessárias.

## Versionamento

O versionamento é fundamental em projetos com muitos desenvolvedores, pois permite controlar as alterações no código-fonte ao longo do tempo. Usar o Git para versionamento traz várias vantagens, como:

- Rastreamento de alterações: Cada alteração no código é registrada, facilitando a identificação de bugs e a reversão de alterações problemáticas.

- Colaboração: Vários desenvolvedores podem trabalhar no mesmo projeto simultaneamente, cada um em sua própria branch, sem interferir no trabalho dos outros.

- Branches: O Git permite a criação de branches, que são cópias isoladas do código. Isso é útil para desenvolver novas funcionalidades sem afetar o código principal.

## Branches
As branches são usadas para desenvolver funcionalidades isoladas do código principal. Elas podem ser mescladas de volta ao código principal quando estiverem prontas. Existem diferentes estratégias de branching, mas no nosso projeto adotamos as seguintes regras:

A branch de desenvolvimento (development) atua como a nossa principal branch de desenvolvimento. É a partir desta branch que novas funcionalidades serão desenvolvidas e testadas.

A branch main será nossa branch de produção, contendo apenas código estável e pronto para ser implantado em produção.

Essa abordagem foi adotada para evitar conflitos e problemas comuns durante a mesclagem de branches, garantindo que apenas código estável seja enviado para produção.

## Regras de Versionamento

- Não criar branches diretamente da main. Sempre criar branches a partir da branch development.
- Utilizar uma branch separada para cada funcionalidade ou correção de bug. Nomear a branch de forma descritiva, por exemplo, feature/nome-da-funcionalidade ou bugfix/nome-do-bug.
- Antes de mesclar uma branch de volta para development, certifique-se de que o código está devidamente testado e revisado.
- SEMPRE de um pull na branch de development antes de abrir um PR. Se nao fizer isso corremos o risco de perder alguma funcionalidade que foi implementada anterior ao seu commit
- Quando voce finalizar uma funcionalidade ou bug de um pull na branch de development e depois um push para colocar suas alteracoes mais recentes na sua branch depois de resolver qualquer conflito. Em seguida, para mesclar seu codigo a branch de desenvolvimento va no projeto do github e abra um pull request. Esse pull request tera que ser aprovado por pelo menos 3 membros dentre os administradores para seu codigo seja mesclado ao da branch de desenvolvimento.
- Para manter a organização e facilitar o entendimento do propósito de cada branch, adotamos a seguinte convenção para os prefixos de nomeação de branches:

    feature: Para novas funcionalidades. (feature/nome-da-feature)
    hotfix: Para correções rápidas de bugs em produção.(hotfix/nome-do-hotfix)
    refactor: Para refatorações de código. (refactor/nome-do-hotfix)
    bugfix: Para correções de bugs. (bugfix/nome-do-bugfix)
    release: Para preparação de novos releases. (release/nome-do-release)
    Esses prefixos devem ser seguidos por uma barra e o nome descritivo da branch. Por exemplo, feature/nova-funcionalidade ou hotfix/bug-na-prod.

Implementei uma regra no projeto para garantir que os nomes das branches sigam essa convenção. Caso o nome não esteja de acordo, a criação da branch será impedida. Isso ajuda a manter a consistência e facilita a identificação do tipo de alteração que está sendo feita em cada branch.

## Criando Branches
Para criar uma nova branch a partir de development, utilize o comando:

``` bash
git checkout -b feature/nova-funcionalidade development
```
Isso criará uma nova branch chamada feature/nova-funcionalidade e mudará para ela. Após concluir o trabalho na nova funcionalidade, você pode mesclar a branch de volta para development utilizando um pull request.

Lembre-se sempre de manter seu repositório Git atualizado e sincronizado com as últimas alterações antes de criar uma nova branch ou fazer um pull request.

## Sua Branch

O processo de manter uma branch segue algumas etapas importantes, desde a sua criação até a sua integração de volta à branch principal (normalmente development). Aqui está um resumo do processo:

Criação da Branch: Utilize o comando git checkout -b nome-da-branch para criar e mudar para a nova branch. Lembre-se de seguir a convenção de nomes estabelecida.
Exemplo:
```bash
git checkout -b feature/nova-funcionalidade
```

Desenvolvimento e Commits: Faça as alterações necessárias no código e utilize os comandos git add para adicionar os arquivos modificados e git commit -m "mensagem" para commitar as alterações.
Exemplo:
```bash
git add .
git commit -m "Adiciona nova funcionalidade X"
```


Push para o Repositório Remoto: Após commitar suas alterações localmente, é importante enviar a branch para o repositório remoto para compartilhar o progresso com a equipe.
Exemplo:
```bash
git push origin feature/nova-funcionalidade
```
ou se estiver na sua branch apenas
```bash
git push
```

Atualização da Branch de Desenvolvimento: Antes de finalizar sua branch, é importante garantir que ela está atualizada com as últimas alterações da branch de desenvolvimento. Para isso, utilize os comandos git fetch e git rebase ou git merge para integrar as alterações.
Exemplo:
```bash
git fetch origin development
git rebase origin/development
```
Alternativamente, você pode usar git pull, que combina os comandos git fetch e git merge em um único comando. No entanto, ao usar git pull, esteja ciente de que ele pode causar conflitos de mesclagem, especialmente se você fez alterações na mesma parte do código que foi modificada na branch de desenvolvimento. Nesse caso, você precisará resolver esses conflitos manualmente.

Exemplo:
```bash
git pull origin development
```
Lembre-se de resolver quaisquer conflitos que possam surgir durante a atualização da sua branch.
Resolução de Conflitos: Durante o rebase ou merge, podem ocorrer conflitos que precisam ser resolvidos manualmente. O Git irá sinalizar os arquivos com conflitos e você precisa editar esses arquivos para resolver as diferenças.
Finalização da Branch e Abertura de PR: Após resolver os conflitos e garantir que sua branch está atualizada, você pode finalizá-la abrindo um Pull Request (PR) para a branch de desenvolvimento. Isso permite que a equipe revise suas alterações antes de mesclá-las.

Revisão e Mesclagem do PR: Os membros da equipe revisarão suas alterações no PR. Após a aprovação, a branch será mesclada (merge) de volta à branch de desenvolvimento.

Remoção da Branch: Após o merge do PR, você pode excluir a branch remota e localmente para manter o repositório limpo.
Exemplo:
```bash
git branch -d feature/nova-funcionalidade  # local
git push origin --delete feature/nova-funcionalidade  # remota
```
Esse processo garante que as alterações sejam revisadas e integradas de forma controlada, mantendo a qualidade e a estabilidade do código.
Atualização da Branch de Desenvolvimento: Antes de finalizar sua branch, é importante garantir que ela está atualizada com as últimas alterações da branch de desenvolvimento. Para isso, utilize os comandos git fetch e git rebase ou git merge para integrar as alterações.

Exemplo:

bash
Copy code
git fetch origin development
git rebase origin/development
Resolução de Conflitos: Durante o rebase ou merge, podem ocorrer conflitos que precisam ser resolvidos manualmente. O Git irá sinalizar os arquivos com conflitos e você precisa editar esses arquivos para resolver as diferenças.

Finalização da Branch e Abertura de PR: Após resolver os conflitos e garantir que sua branch está atualizada, você pode finalizá-la abrindo um Pull Request (PR) para a branch de desenvolvimento. Isso permite que a equipe revise suas alterações antes de mesclá-las.

Revisão e Mesclagem do PR: Os membros da equipe revisarão suas alterações no PR. Após a aprovação, a branch será mesclada (merge) de volta à branch de desenvolvimento.

Remoção da Branch: Após o merge do PR, você pode excluir a branch remota e localmente para manter o repositório limpo.

Remoção da Branch: Após o merge do PR, você pode excluir a branch remota e localmente para manter o repositório limpo.

Exemplo:

```bash
git branch -d feature/nova-funcionalidade  # local
git push origin --delete feature/nova-funcionalidade  # remota
```
Esse processo garante que as alterações sejam revisadas e integradas de forma controlada, mantendo a qualidade e a estabilidade do código. Tambem e possivel fazer a delecao pela plataforma do github entrando no seu PR e scrollando para baixo

Arquitetura do Projeto
A arquitetura do seu projeto segue um padrão comum em aplicações web Flask, onde cada módulo é um Blueprint acoplado ao Blueprint principal, que por sua vez é acoplado ao programa principal. Vamos explicar cada componente dessa arquitetura:

Blueprints: Os Blueprints são uma forma de organizar rotas, modelos e outros elementos de uma aplicação Flask de forma modular. Cada módulo da sua aplicação, como cursos, por exemplo, teria seu próprio Blueprint. Isso facilita a organização do código e permite que diferentes partes da aplicação sejam desenvolvidas separadamente.

Arquivo Principal de Rotas: Cada módulo tem um arquivo principal (por exemplo, curso.py) que contém as rotas e lógicas simples relacionadas a esse módulo. Isso ajuda a manter o blueprint organizado e separado por rotas e funcionalidade.

Arquivo de Serviço (Service): O arquivo de serviço (por exemplo, cursoService.py) abriga toda a lógica de negócios relacionada ao módulo de cursos. Ele contém funções e classes que lidam com a lógica de negócios da aplicação, por exemplo, no arquivo alunoService.py, uma função pode verificar se um aluno já completou uma certificação. No professoreService.py, outra função pode verificar se um professor tem horários livres para ministrar aulas.

Arquivo de Repositório (Repository): O arquivo de repositório (por exemplo, cursoRepo.py) contém toda a lógica relacionada ao banco de dados. Ele contém funções e classes para interagir com o banco de dados, como buscar cursos do banco de dados, inserir um novo curso, etc.

Arquivos Template e Static: Os arquivos template (HTML) e static (CSS, JS) são armazenados em diretórios separados (templates e static, respectivamente). Eles são usados para renderizar as páginas da web e estilizar a aplicação.

Essa arquitetura foi escolhida por ser uma forma organizada e modular de desenvolver aplicações web Flask. Ela facilita a manutenção do código, permite o desenvolvimento paralelo de diferentes partes da aplicação e torna a aplicação mais fácil de entender e modificar no futuro. Além disso, separar a lógica de negócios do banco de dados e a apresentação da aplicação ajuda a manter um código limpo e fácil de dar manutenção.

## Comunicacao com os bancos

Todos os modulos devem utilizar as funcoes db/database.py para se comunicar com seu json(banco) elas devem ser usadas dentro do repo de cada modulo para criar as funcoes de acesso a banco. Elas sao: read_db , write_db, delete_db e update_db. O codigo e autoexplicativo, mas qualquer duvida fico a disposicao.
