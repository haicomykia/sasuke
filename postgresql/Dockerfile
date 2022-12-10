FROM postgres:14

ARG DB_LANG=ja_JP
ARG ENCODE=UTF-8

RUN localedef -i ${DB_LANG} -c -f UTF-8 -A /usr/share/locale/locale.alias ${DB_LANG}.${ENCODE}

COPY ./script/ /docker-entrypoint-initdb.d/
RUN chown 770 ./docker-entrypoint-initdb.d/init_db.sh