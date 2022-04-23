1. Setup Conda Environment
```bash
$ bash init_setup.sh
```

2. Create a conda environment after opening the repository in VSCODE
```bash
$ conda create --prefix ./env python=3.7 -y
$ conda activate ./env
```

3. Install requirements
```bash
$ pip install -r requirements.txt
```

4. Create conda.yaml file
```bash
$ conda env export > conda.yaml
```

5. MLflow run
```bash
$ mlflow run . --no-conda
```