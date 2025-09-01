#!/usr/bin/env bash
# exit on error
set -o errexit

# Atualiza pip
pip install --upgrade pip

# ETAPA 2: Instala pacotes restantes. O pip vai ignorar o 'tokenizers' pois já está instalado.
pip install -r requirements.txt