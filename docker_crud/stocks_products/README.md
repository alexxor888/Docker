cd stocks_products
docker build . --tag=crud
docker run -d -e MY_ENV=top_env -p 8081:8000 crud
docker ps