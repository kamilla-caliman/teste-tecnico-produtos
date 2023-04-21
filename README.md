# Cadastro de Produtos e Categorias - API

O usuário, quando autenticado, tem acesso ao catálogo de produtos e pode cadastrar, atualizar, deletar e listar os produtos e suas categorias. O usuário também tem a possibilidade de buscar produtos e categorias por id e filtrar a busca de produtos por categorias específicas usando queryparams ("/products?category=nome")

# Instruções de uso:

1. Após clonar o repositório, verifique se você tem o Docker instalado em sua máquina. Caso contrário, siga as instruções de instalação da [documentação oficial](https://docs.docker.com/engine/install/)

2. Preencha as variáveis de ambiente seguindo o exemplo de `.env.example`:

```
SECRET_KEY='secret key da sua aplicação'
POSTGRES_DB='teste_tecnico'
POSTGRES_USER='nome do usuário'
POSTGRES_PASSWORD='senha do usuário'
POSTGRES_PORT='porta do servidor'
POSTGRES_DB_HOST='teste_tecnico_db'
DEBUG=True
```

3. Rode o comando de criação dos containers

```
docker compose up
```

# Instruções para rodar os testes

1. Primeiro temos que pegar o id ou nome do nosso container

```
docker ps -a
```

2. Verifique o id ou nome do container e execute o próximo comando para fazer a execução dos testes dentro do container

```
docker exec -it <id ou nome> /bin/sh
```

3. Agora já dentro do container, podemos rodar nossos testes normalmente

```
pytest --testdox -vvs
```

4. Caso queira um log mais resumido, basta executar com os testes sem as flags **verbose**:

```shell
pytest --testdox
```

# Tecnologias Utilizadas:

1. Python
2. Django REST framework
3. PostgreSQL
4. Docker
5. drf-spectacular
6. API Generic Views
7. Model Serializers
8. pytest-testdox
9. dotenv

# Documentação

Para acessar a documentação verifique se o servidor está rodando corretamente e clique [aqui](http://localhost:8000/api/docs/)