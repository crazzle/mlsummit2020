## Start Jupyterlab
### With virtualenv
```bash
virtualenv -p /usr/bin/python3  venv
source venv/usr/local/bin/activate
curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
python3 get-pip.py --force-reinstall
pip install -r requirements.txt
jupyter lab
```

### With docker-compose (recommended, no Docker Toolbox)
```bash
docker-compose up
```

### Without docker-compose
#### Jupyterlab
```bash
docker build . -t mlessentials

# Linux/Mac (Docker version >= 17.06)
docker run -p 8888:8888 --mount type=bind,source=$(pwd)/notebooks,target=/mlessentials/notebooks mlessentials

# Docker for Windows (Docker version >= 17.06)
docker run -p 8888:8888 --mount type=bind,source=%cd%/notebooks,target=/mlessentials/notebooks mlessentials

# Docker for Windows (Docker version < 17.06)
docker run -p 8888:8888 -v %cd%/notebooks:/mlessentials/notebooks mlessentials

# Docker Toolbox (Windows 7, 8 and Windows 10 Home; a separate VM for Docker)
docker run -d -p 8888:8888 mlessentials
# Copy notebooks manually into the container
## get container id
docker ps
## copy into container
docker cp notebooks <container id>:/mlessentials
# After the first day, stop the container
docker stop <container id>
# On the second day, start the container again
docker start <container id>
```

With Docker Toolbox, the JupyterLab instance might be available at `192.168.99.100:8888`, not `localhost:8888`.

#### TensorFlow Serving
```bash
docker run -p 8501:8501 -p 8500:8500 --mount type=bind,source=$(pwd)/notebooks/04-models/iris/,target=/models/iris -e MODEL_NAME=iris codecentric/tensorflow-serving-baseimage
```

#### In general 
- Replace current directory in commands with either `%cd%` (Windows) or `$(pwd)` Mac/Linux
- `--mount` is supported since Docker version 17.06. If you use an older version you have to use `-v` (Volumes). See the Example in the Airflow section above.


## References and Further Information

#### General

- [Cheatsheet for working with IPython/Jupyter](https://ipython.readthedocs.io/en/stable/interactive/python-ipython-diff.html)

- [Cheatsheet for Docker](https://hackernoon.com/docker-commands-the-ultimate-cheat-sheet-994ac78e2888)

- [Free notebooks from the book "Deep Learning with Python"](https://github.com/fchollet/deep-learning-with-python-notebooks)

- [Introduction to Reinforcement Learning (Youtube)](https://www.youtube.com/watch?v=FCyZplb0ul4)

- [Keras examples](https://github.com/keras-team/keras/tree/master/examples)

#### Production-Ready Data Science

- [What’s your ML test score? A rubric for ML production systems](https://ai.google/research/pubs/pub45742)

- [A walkthrough of DVC](https://blog.codecentric.de/en/2019/03/walkthrough-dvc/),
  [DVC dependency management](https://blog.codecentric.de/en/2019/08/dvc-dependency-management/)
