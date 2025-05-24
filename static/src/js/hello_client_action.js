/** @odoo-module **/

import { Component } from "@odoo/owl";
import { registry } from "@web/core/registry";

// Create a simple OWL component
class HelloClientAction extends Component {
    setup() {}

    static template = "my_module.HelloClientActionTemplate";
}

// Register the action
registry.category("actions").add("hello_client_action", HelloClientAction);
