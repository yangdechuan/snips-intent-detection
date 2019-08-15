# snips-intent-detection
Please refer to [Snips NLU](https://snips-nlu.readthedocs.io/en/latest/index.html) for more information.

## Usage
* step 1: Install snips-nlu
```bash
pip install snips-nlu
```
* step 2: Download language resources
```bash
snips-nlu download en
```
* step 3: Download some entity if necessary
```bash
# Download snips/city
snips-nlu download-entity snips/city en
```
* step 4: Rewrite the .yaml file based on your demand.
* step 5: Use the yaml file to generate json file.
```bash
snips-nlu generate-dataset en dataset/ticket.yaml > dataset/ticket.json
```
* step 5: Train model.
```bash
python train.py
```
* step 6: Use the model.
  
  Refer demo.py

## Suggestion
1. Maybe more detailed intent should be defined.

    For example, for the sentence "Which city would you like?", the intent should
    be "request-city" not "request". 
    