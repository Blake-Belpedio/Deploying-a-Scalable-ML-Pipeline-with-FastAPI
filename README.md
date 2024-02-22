Reccomended OS: Ubuntu 20.04.6

Environment:
Conda:
name: fastapi
channels:
  - conda-forge
  - defaults
dependencies:
  - python=3.8
  - numpy=1.24.1
  - pandas=1.5.3
  - scikit-learn=1.0.2
  - pytest=7.2.1
  - requests=2.28.2
  - fastapi=0.63.0
  - uvicorn=0.20.0
  - gunicorn=20.1.0
  - pip=20.3.3
  - git=2.30.2

Use:
This project Deploys a RandomForest Classifier to predict income level based on United States Census Data. The model is then deployed via Fast API.

Interaction:
Post and Get methods are integrated in local_api.py. Uvicorn is used to access the API locally with the following command > uvicorn main:app --reload. Once deployed the command Python local_api.py is used to retrive the status codes and results from the API.

Credit:
This project was completed with the help of Udacity and Western Governors University (WGU)

