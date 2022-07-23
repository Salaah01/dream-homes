#!/usr/bin/bash

# Sets the environment variable files.

MODE="${1,,}"
ROOT_DIR=$(dirname $(realpath ${BASH_SOURCE[0]}))

if [[ ${MODE} != 'prod' ]] && [[ ${MODE} != 'dev' ]]; then
  echo 'Supply "PROD" or "DEV" as the first argument.'
  exit 1
fi

# If running in PROD, then get the settings from the user, otherwise use
# default details for DEV.
if [[ $MODE == 'prod' ]]; then
  echo -e "\033[92mEnvironment Variables Setup for Dream Homes,\033[0m"
  echo "PostGreSQL Settings:"
  read -p "Database Name: " POSTGRES_DB_NAME
  read -p "User: " POSTGRES_USER
  read -sp "Password: " POSTGRES_PASSWORD

  echo "Website Settings:"
  read -p "Secret Key: " SECRET_KEY
else
  POSTGRES_DB_NAME=postgres
  POSTGRES_USER=postgres
  POSTGRES_PASSWORD=postgres
  SECRET_KEY=jfghfdjgh374y237y7324hjbf732237f
fi

mkdir -p "${ROOT_DIR}/postgres/env"

WEB_ENV_FILE="${ROOT_DIR}/web/.web.env"
POSTGRES_ENV_DIR="${ROOT_DIR}/postgres/env"

# Check if files exist and prompt user if they want to continue.
if [[ "$(ls -A ${POSTGRES_ENV_DIR})" ]]; then
  read -p "Files exist in ${POSTGRES_ENV_DIR}, do you want to continue and override? [Y/n]: " PROCEED

  if [[ "${PROCEED,}" != 'y' ]]; then
    echo "Exiting..."
    exit 0
  fi
fi

if [[ -f "${WEB_ENV_FILE}" ]]; then
  read -p "${WEB_ENV_FILE} already exists, do you want to continue and override? [Y/n]: " PROCEED

  if [[ "${PROCEED,}" != 'y' ]]; then
    echo "Exiting..."
    exit 0
  fi
fi

# DB settings
echo "${POSTGRES_DB_NAME}" >"${POSTGRES_ENV_DIR}/.postgres_db_name.env"
echo "${POSTGRES_USER}" >"${POSTGRES_ENV_DIR}/.postgres_db_user.env"
echo "${POSTGRES_PASSWORD}" >"${POSTGRES_ENV_DIR}/.postgres_db_password.env"

# Web settings
echo DB_ENGINE=django.db.backends.postgresql >$WEB_ENV_FILE
echo "SECRET_KEY=${SECRET_KEY}" >>$WEB_ENV_FILE
echo "DB_HOST=postgres" >>$WEB_ENV_FILE
echo "DB_NAME=${POSTGRES_DB_NAME}" >>$WEB_ENV_FILE
echo "DB_USER=${POSTGRES_USER}" >>$WEB_ENV_FILE
echo "DB_PASSWORD=${POSTGRES_PASSWORD}" >>$WEB_ENV_FILE
echo DB_PORT=5432 >>$WEB_ENV_FILE
if [[ $MODE == 'prod' ]]; then
  echo "ALLOWED_HOSTS=web|iamsalaah.com|www.iamsalaah.com|dream-homes.iamsalaah.com|www.dream-homes.iamsalaah.com|localhost|www.localhost" >>$WEB_ENV_FILE
fi

echo -e "\033[92mEnvironment variables have been set for Dream Homes.\033[0m"
