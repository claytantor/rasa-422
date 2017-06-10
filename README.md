# setup

These steps will install a virtual env, install all the dependencies and install the spacy language files.

```bash
bash install.sh
source ../ve-rasa-422/bin/activate
pip install -r requirements.txt
python -m spacy download en
```

# running the server
Starting the server using rasa.
```bash
python -m rasa_nlu.server -c ./dronzecore/rasa/data/config.json
```
with the curl command:
```bash
curl -X POST \
  http://localhost:5010/parse \
  -H 'cache-control: no-cache' \
  -H 'content-type: application/json' \
  -d '{"q":"aws s3 ls"}'
```

```json
{
  "entities": [
    {
      "end": 9,
      "entity": "command",
      "extractor": "ner_crf",
      "start": 7,
      "value": "ls"
    }
  ],
  "intent": {
    "confidence": 0.70301507838113098,
    "name": "command_awscli_s3"
  },
  "intent_ranking": [
    {
      "confidence": 0.70301507838113098,
      "name": "command_awscli_s3"
    },
    {
      "confidence": 0.29698492161886869,
      "name": "conversation_dronzebot_about"
    }
  ],
  "text": "aws s3 ls"
}
```

# running the embedded client

```bash
python embedded.py --modeldir ./dronzecore/rasa/data/model_20170608-214404 \
   --config ./dronzecore/rasa/data/config.json --text "aws ls s3"
```
produces the response:

```json
{
    "entities": [
        {
            "start": 4,
            "extractor": "ner_crf",
            "end": 9,
            "value": "ls s3",
            "entity": "command"
        }
    ],
    "intent": {
        "confidence": 0.70301507838113098,
        "name": "command_awscli_s3"
    },
    "text": "aws ls s3",
    "intent_ranking": [
        {
            "confidence": 0.70301507838113098,
            "name": "command_awscli_s3"
        },
        {
            "confidence": 0.29698492161886869,
            "name": "conversation_dronzebot_about"
        }
    ]
}
```
