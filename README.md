# cat-detector

## Feature

Show possibiloty of your picture whether a cat by AI.

## Demo

http://52.193.167.222/

## System

- Ubuntu 16.04 LTS
- Python: 3.6.7
- Docker: 19.03.2
    - docker-compose: 3.7.3
- Nginx + uWSGI + Flask
- TensorFlow + Keras

# Installation
```
# Docker installation
$ sudo apt-get update
$ sudo apt-get install -y git apt-transport-https ca-certificates curl software-properties-common
$ curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
$ sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"

$ sudo apt-get update
$ sudo apt-get install -y docker-ce

# Add user to docker group
$ sudo usermod -aG docker ubuntu

# Once exit
$ exit

# docker-compose installation
$ sudo curl -L https://github.com/docker/compose/releases/download/1.24.1/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose
$ sudo chmod +x /usr/local/bin/docker-compose
$ exit
```

# Usage
```
$ docker-compose up -d
```

## License

MIT

##  Author

Kenichi Usami
