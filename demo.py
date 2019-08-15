import json

from snips_nlu import SnipsNLUEngine


if __name__ == "__main__":
    engine = SnipsNLUEngine.from_path("snips.model")

    parsing = engine.parse("Can I get 2 tickets for the big short?")
    print(json.dumps(parsing, indent=2))
