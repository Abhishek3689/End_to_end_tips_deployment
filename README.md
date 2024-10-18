## Tips Data project    

#### The main Objective of this project is to implement end to end pipeline and deployment in azure web app

### How to run?
### STEPS:

Clone the repository  make some changes for secrets

```bash
https://github.com/Abhishek3689/End_to_end_tips_deployment.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -p venv python=3.10 -y
```

```bash
conda activate venv
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up you local host and port
```
## Steps to follow in azure cloud
1.  Create azure container registry and copy Login server,user name  and password  from Access keys to be needed while login from local vs code 
2.  Create Web app 
 
   


## To build Docker Image and push in azure container Registry
Run from terminal:
```bash
docker build -t tipsregistry.azurecr.io/tipsapp:latest .
```
login to azure registry 
```bash
docker login tipsregistry.azurecr.io
```
push your Docker to azure resitry container
```bash
docker push creditregistry1.azurecr.io/tipsapp:latest
```
