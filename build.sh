#!/usr/bin/env bash
# exit on error
set -o errexit

# Instala e configura a versão estável do Rust como padrão
rustup default stable

# ATIVA o ambiente do cargo na sessão atual.
export PATH="$CARGO_HOME/bin:$PATH"

# Atualiza o pip para a versão mais recente
pip install --upgrade pip

# Instala as dependências do Python
pip install -r requirements.txt