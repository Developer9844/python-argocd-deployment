from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '''
<html>
<body>
<center>
<h1>Demo-1 on GitOps with ArgoCD and Github Actions.</h1> <br>
<br>
<img src="https://github.com/tanmaybhandge/CICD_Application_K8s/blob/main/itsworking.jpeg?raw=true">
<p>Hello My name is Ankush</p>
</center>
</body>
</html>
'''

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
