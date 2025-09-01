#!/usr/bin/env bash
# exit on error
set -o errexit

# Instala e configura a versão estável do Rust como padrão
rustup default stable

# Instala as dependências do Python
pip install -r requirements.txt