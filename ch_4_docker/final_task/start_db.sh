docker run --name de_db_pg \
--rm \
-it \
-v $(pwd)/DE_course:/var/lib/postgresql/data \
-v $(pwd)/init_db/:/docker-entrypoint-initdb.d \
-p 5436:5432 \
-d \
anton_de_pgimage
