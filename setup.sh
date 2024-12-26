#!/bin/bash

# Install Rust
curl https://sh.rustup.rs -sSf | sh -s -- -y

# Add Rust to PATH
source $HOME/.cargo/env
