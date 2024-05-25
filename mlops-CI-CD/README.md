## Installation
### Run service locally

Create a virtual environment

```bash
python3 -m venv venv
```

Activate virtual environment

```bash
source venv/bin/activate
```

Install requirements in virtual environment

```bash
pip3 install -r requirements.txt
```

Move to app subfolder and run below command
```bash
uvicorn app.main:app --host 0.0.0.0 --port 8000 --reload
```

Now you can use the integrated docs at:
[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

docker build -t jyotsana-first .
docker push jyotsana4321/jyotsana-first:latest
docker tag jyotsana-first jyotsana4321/jyotsana-first

ssh -i ~/.ssh/private_key_added_to_server root@161.35.222.117 (IP address of the server to deploy the code on)
apt install docker (ubuntu server should have docker by default before we deploy our image)