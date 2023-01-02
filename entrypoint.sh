#!/bin/bash



function connect(){

    pg_isready -U ${POSTGRES_USER} -d ${POSTGRES_DB} -h ${POSTGRES_HOST} -p ${POSTGRES_PORT} 1> /dev/null

    while [ "$?" -ne 0 ]
    do
        echo "Postgres database is not yet ready! Waiting..."
        sleep 4
    done

}


connect

exec "$@"
