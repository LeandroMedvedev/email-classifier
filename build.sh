#!/usr/bin/env bash
# exit on error
set -o errexit

# Instala e configura o Rust estável
rustup default stable
rustup update stable

# Por garantia, exporto o PATH padrão para onde o rustup instala os binários.
export PATH="$HOME/.cargo/bin:$PATH"

# Atualiza pip
pip install --upgrade pip

# ETAPA 1: Instala o pacote problemático primeiro, no ambiente principal
# Usamos aspas para garantir que os caracteres especiais sejam lidos corretamente
pip install "tokenizers<0.20,>=0.19"

# ETAPA 2: Instala pacotes restantes. O pip vai ignorar o 'tokenizers' pois já está instalado.
pip install -r requirements.txt