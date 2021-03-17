def gen_dict_extract(var, key, previous_key = None):
    if isinstance(var, dict):
        for k, v in var.items():
            if k == key:
            	if previous_key is None:
                	yield {k : v}
            	elif previous_key is not None:
                	yield {previous_key: {k:v}}
            if isinstance(v, (dict, tuple)):
                yield from gen_dict_extract(v, key, k)
    elif isinstance(var, tuple):
        for d in var:
            yield from gen_dict_extract(d, key, k)