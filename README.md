# CS361-Hello-Service

## Description

A minimal API serivice created using python with Flask.

## Installation

1. Clone the code ont your device.

2. Enable WSL2 and install Ubuntu if on windows.

3. Install Git and Docker Desktop or Docker Engine.

4. Install python.

```sh
sudo apt update
sudo apt install -y python3 python3-venv python3-pip
```

5. Create and activate a virtual environment.

```sh
python3 -m venv .venv
source .venv/bin/activate
```

6. build the docker conatiner.

```sh
docker build -t cs361-hello-service:1.0 .
```

## Usage

To run locally:
```sh
python3 app.py
```

To run on a docker container:
```sh
docker run --rm -p 8080:8080 cs361-hello-service:1.0
```

To test the endpoints:
```sh
curl http://localhost:8080/
curl http://localhost:8080/health
```
