import typing
import logging
import os

import yaml
import yaml.parser

import super_prompt.types

K8S_SYMBOL = "\u2388"
K8S_CONFIG_LOCATION = os.path.expanduser("~/.kube/config")

logger = logging.getLogger("super_prompt_plugin_kubernetes")


def main(config: dict) -> typing.Optional[super_prompt.types.PluginResponse]:
    if not os.path.exists(K8S_CONFIG_LOCATION):
        return
    
    try:
        with open(K8S_CONFIG_LOCATION, mode="r") as config_fd:
            current_context = yaml.safe_load(config_fd).get("current-context", None)
    except yaml.parser.ParserError:
        return
    
    return super_prompt.types.PluginResponse(
        K8S_SYMBOL,
        current_context,
        [0x32, 0x6D, 0xE5]
    )


if __name__ == "__main__":
    print(main({}))

