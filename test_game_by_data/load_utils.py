
import yaml

class LoadUtils:
    @classmethod
    def load_yaml(self,yaml_path):
        return yaml.safe_load(open(yaml_path))


