import json
import yaml

with open('data.json', 'w') as json_file:
    json.dump([], json_file, indent=4)

config_yaml = {
    "logging": {
        "level": "INFO",
        "file": "app.log",
        "format": "%(asctime)s - %(levelname)s - %(message)s"
    },

    "data": {
        "file": "data.json"
    }
}

with open('config.yaml', 'w') as yaml_file:
    yaml.dump(config_yaml, yaml_file, default_flow_style=False, sort_keys=False)

print("Arquivos criados com sucesso")
