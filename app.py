
from flask import Flask, request, jsonify

import language_tool_python
app = Flask(__name__)
@app.route('/spelling', methods=['GET'])
def spelling():
    return "tester"
#     if request.is_json:
#         data = request.get_json()

#         typo = data["sentence"]
#         tool = language_tool_python.LanguageToolPublicAPI('en-US')
#         final = tool.correct(typo)
#         return print(final)
       
#     return {"error": "Request must be JSON"}, 415 
