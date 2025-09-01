#!/usr/bin/env bash
# exit on error
set -o errexit

# Cria um arquivo 'rust-toolchain' no projeto, forçando o uso da versão stable.
# Isso funciona mesmo em subprocessos isolados.
rustup override set stable

# Por garantia, exporto o PATH padrão para onde o rustup instala os binários.
export PATH="$HOME/.cargo/bin:$PATH"

# Atualiza o pip para a versão mais recente
pip install --upgrade pip

# ETAPA 1: Instala o pacote problemático primeiro, no ambiente principal
# Usamos aspas para garantir que os caracteres especiais sejam lidos corretamente
pip install "tokenizers<0.20,>=0.19"

# ETAPA 2: Instala pacotes restantes. O pip vai ignorar o 'tokenizers' pois já está instalado.
pip install -r requirements.txt