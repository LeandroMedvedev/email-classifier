#!/usr/bin/env bash
set -o errexit

# Criar arquivo 'rust-toolchain' no projeto, forçando o uso da versão stable
rustup override set stable

# Exportar PATH padrão para onde rustup instala os binários
export PATH="$HOME/.cargo/bin:$PATH"

# Atualizar pip
pip install --upgrade pip

# Instalar tokenizers com versão específica para evitar conflitos
pip install "tokenizers<0.20,>=0.19"

# Instalar pacotes restantes
pip install -r requirements.txt