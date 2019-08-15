import io
import json

from snips_nlu import SnipsNLUEngine
from snips_nlu.default_configs import CONFIG_EN

# snips-nlu generate-dataset en ticket.yaml > ticket.json

# The first step is to understand which intent the sentence is about.
# The second step is to extract the parameters, a.k.a. the slots of the sentence.
if __name__ == "__main__":
    engine = SnipsNLUEngine(config=CONFIG_EN, random_state=233)

    with io.open("dataset/ticket.json") as f:
        dataset = json.load(f)

    # Train model.
    engine.fit(dataset)

    # Save model.
    engine.persist("snips.model")

    # # Test
    # parsing = engine.parse("Can I get 2 tickets for the big short?")
    # print(json.dumps(parsing, indent=2))
