"""
Generate a set of cerberus schemas based on config from kbase.yaml
"""


def generate_validators(config):
    validators = {}
    narrative_methods = config.get('narrative_methods') or {}
    for method_name, method_config in narrative_methods.items():
        schema = {}
        validators[method_name] = schema
        for param_name, param_config in method_config['input'].items():
            schema[param_name] = {}
            key = schema[param_name]
            key['type'] = param_config['type']
            key['required'] = not param_config.get('optional')
    return validators
