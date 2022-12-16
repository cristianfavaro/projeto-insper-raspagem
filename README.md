# Web Crawler

## Objetico
Monitorando a publicação de notícias em concorrentes é uma atividade comum no meu dia a dia. Por isso, resolvi criar um robô para raspar alguns dos principais portais do país e criar um banco de dados em que eu possa avaliar o conteúdo. Para fins didáticos, neste caso vamos construir um simples aquivo CSV, mas o Scrapy abre uma janela interessante para integrar o sistema com o Django.

O projeto foi desenvolvido durante a aula de Pensamento Computacional, do Master em Jornalismo de Dados do Insper. 

## Critério

- Preciso criar uma raspagem padrão que funcione em vários sites diferentes. 
- Entre as colunas estão título, autor, link, img etc.

# Getting Started

## Adicionar novos sites
O modelo padrão de raspagem está dentro da pasta spiders. Basta criar um novo arquivo com a nova configuração e importar este novo site dentro do arquivo "go-spider.py" (é ele o responsável por chamar todos os portais)

## Install and Run

> Este projeto foi testado apenas no MacOS.

1. [Instalar o Docker para Mac](https://docs.docker.com/docker-for-mac/install/)
1. Clone este projeto para a sua máquina.
1. No terminal, digite `docker-compose up` de dentro do diretório principal do projeto.

O comando `docker-compose up` irá iniciar o `crawler` (veja dentro do Dockerfile) e rodar todos os raspadores que estão no arquivo "go-spider.py".

# Common Practices
[Avoiding getting banned for scraping](https://doc.scrapy.org/en/latest/topics/practices.html#avoiding-getting-banned)

# Referências:
- https://github.com/jiaqi-yin/docker-crawler