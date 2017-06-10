# setup

These steps will install a virtual env, install all the dependencies and install the spacy language files.

```bash
bash install.sh
source ../ve-rasa-422/bin/activate
pip install -r requirements.txt
python -m spacy download en
```

# running the server


# running the embedded client

```bash
python embedded.py --modeldir ./dronzecore/rasa/data/model_20170608-214404 --config ./dronzecore/rasa/data/config.json --text "aws ls s3"
```
