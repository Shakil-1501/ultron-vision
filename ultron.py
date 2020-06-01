import argparse

from agents import *
from inference import *
from utils.config import process_config

def main():
    arg_parser = argparse.ArgumentParser(description="")
    arg_parser.add_argument(
        'config', metavar='config_json_file',
        default=None, help="Configuration file in JSON format."
    )

    args = arg_parser.parse_args()

    # parse config file
    config = process_config(args.config)

    # Create the agent and pass all the configuration to it and run
    agent_class = globals()[config["agent"]]
    agent = agent_class(config)
    
    # train model
    agent.run()
    agent.finalize()
    
    # Create inference agent and pass the configuration to it and interpret
    iagent_class = globals()[config["inference_agent"]]
    iagent = iagent_class(config)
    
    iagent.plot_accuracy_graph()
    iagent.plot_loss_graph()
    iagent.show_misclassified_images()


if __name__=="__main__":
    main()