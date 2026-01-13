from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.get("/")
def root():
    return jsonify(service="cs361-hello-service", status="ok")

@app.get("/health")
def health():
    return jsonify(ok=True)

@app.before_request
def log_request() :
    start = time.time()
    request._start_time = start
    
@app.after_request
def log_response(resp):
    latency_ms = int((time.time() - request._start_time) * 1000)
    print(f'{request.method} {request.path} {resp.status_code} {latency_ms}ms')
    return resp

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
    