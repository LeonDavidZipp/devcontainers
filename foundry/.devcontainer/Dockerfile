FROM ghcr.io/foundry-rs/foundry:latest

LABEL maintainer="lzipp"

RUN curl -sL https://deb.nodesource.com/setup_current.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g npm@latest \
# Install nodejs tools
    && npm install -g @web3-storage/w3cli \
    && npm install -g pnpm \
    && npm install -g create-react-app

CMD ["/bin/sh"]
