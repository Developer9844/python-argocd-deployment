from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
<html>
<body>
<center>
<h1>Demo-0025 on GitOps with ArgoCD and Github Actions.</h1> <br>
<br>
<img src="https://github.com/tanmaybhandge/CICD_Application_K8s/blob/main/itsworking.jpeg?raw=true">
<p>In order to speed up recoveries in case of pod failures, you can leverage Flink’s working directory feature <br>
together with local recovery. If the working directory is configured to reside on a persistent volume that gets <br>
remounted to a restarted TaskManager pod, then Flink is able to recover state locally. With the StatefulSet, <br>
Kubernetes gives you the exact tool you need to map a pod to a persistent volume.
</p>
</center>
</body>
</html>
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
