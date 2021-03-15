```bash
python3 -m venv .venv
source .venv/bin/activate
```

```bash
python -m pip install --upgrade pip
```

```bash
pip install numpy
pip install pandas
pip install scipy
```

```bash
pip check
pip list

pip freeze > requirements.txt
```

```bash
pip install ipykernel

pip freeze > requirements.txt

python -m ipykernel install --user --name=math_statistics

cat ~/.local/share/jupyter/kernels/math_statistics/kernel.json 
```
