"""
Generate a set of cerberus schemas based on config from kbase.yaml
"""


def generate_validators(config):
    validations = {}
    narrative_methods = config.get('narrative_methods') or {}
    for method_name, method_config in narrative_methods.items():
        val = {}
        validations[method_name] = val
        for param_name, param_config in method_config['input'].items():
            type_str = param_config['type']
            val[param_name] = {'type': type_str}
    return validations
