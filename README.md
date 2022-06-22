# PamREST

Une simple application de restauration.


## Backend
### Requirements and guides (Environnement Linux et Windows, Version Python 3.10 +)


Pour pouvoir lancer cette application, il faut suivre ces instructions et utiliser les versions indiqués:


Création de l'environnement virtuel dans le dossier Backend

```s
cd Backend

python3 -m venv env

```

Activation de l'environnement virtuel:


```s
# linux

source env/bin/activate

```

```s
# windows

.\env\Scripts\activate

```


Installation des requirements:

```s
pip install -r requirements.txt
```

Renommer le fichier `env_template.conf` par `.env` et completer les valeurs vides par les informations sur la base de données et token:


### Lancement de l'API REST


```s
python3 main.py

```

### Lancement test unitaire


```s
pytest -sv

```

### Lien Swagger UI (Documentations)

```s
http://localhost:1600/docs#/
```

## Frontend

Ouvrir le fichier `index.html` dans un navigateur
