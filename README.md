# Projeto Integrador de Engenharia 1 2018/2 - Turma C

## Documentação

Documentação disponível em [Wiki](https://github.com/zero101010/PI1_2018_2/wiki).

## Licença

[MIT](https://github.com/zero101010/PI1_2018_2/blob/master/LICENSE)

Copyright (c) 2018 Projeto Integrador de Engenharia 1 2018/2 - Turma C

## Como Contribuir

Para contribuir com a gente, o colaborador deve _fork_ e enviar um [pull request] (https://github.com/zero101010/PI1_2018_2/pulls) com sua contribuição.
O código será analisado por um dos proprietários do projeto e, se aprovado, incluído no núcleo da aplicação.



### Uso do Docker
* Baixe e instale Docker CE no [site oficial](https://docs.docker.com/engine/installation/linux/docker-ce/ubuntu/#install-from-a-package).

* Baixe e instale Docker Compose no [site oficial](https://docs.docker.com/compose/install/#master-builds).

#### Clone o repositório e entre nele
```
git clone https://github.com/zero101010/PI1_2018_2.git && cd PI1_2018_2/
```

#### Levante seu ambiente
```
docker-compose up
```

#### Comandos úteis
#### Como baixar uma imagem do docker
```
docker pull <imagem-desejada>
```

#### Listando imagens locais
```
docker images
```

#### Deletando imagens
```
docker rmi -f <id-da-imagem>
```

#### Listando contêineres em execução
```
docker ps
```

#### Removendo contêineres
```
docker rm [-f] <nome-do-contêiner-ou-id>
```

#### Execução de comandos de fora do contêiner
```
docker exec <nome-do-contêiner> <comando-desejado>
```
