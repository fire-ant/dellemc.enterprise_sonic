from __future__ import absolute_import, division, print_function
__metaclass__ = type

import traceback
import json

from ansible.module_utils._text import to_native

try:
    import jinja2
    HAS_LIB = True
except Exception as e:
    HAS_LIB = False
    ERR_MSG = to_native(e)
    LIB_IMP_ERR = traceback.format_exc()


# To create Loopback, VLAN interfaces
def build_interfaces_create_request(interface_name):
    url = "data/openconfig-interfaces:interfaces"
    method = "PATCH"
    payload_template = """{"openconfig-interfaces:interfaces": {"interface": [{"name": "{{interface_name}}", "config": {"name": "{{interface_name}}"}}]}}"""
    input_data = {"interface_name": interface_name}
    env = jinja2.Environment(autoescape=select_autoescape())
    t = env.from_string(payload_template)
    intended_payload = t.render(input_data)
    ret_payload = json.loads(intended_payload)
    request = {"path": url,
               "method": method,
               "data": ret_payload}
    return request
