"""
    apps_endpoints.py

CLI integration tests for "apps-*" cli commands.
"""
import json
import os
from flask import jsonify, request
from flask_restful import Resource
from .response_templates import response_template_to_json


# Sample response for "apps-list" cli command.
apps_list_response = response_template_to_json("apps-list.json")


class AgaveApps(Resource):
    """ Test apps-* cli commands
    """

    def get(self):
        """ Test apps-list utility

        This test emulates the Agave API endpoint "/apps/v2/" for GET
        requests. To test it:

        curl -sk -H "Authorization: Bearer xxx" 'https://localhost:5000/apps/v2?pretty=True'
        """
        pretty_print = request.args.get("pretty", "")
        return jsonify(apps_list_response)
