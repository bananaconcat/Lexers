import json

NODE_TYPES = {
    0: "functionDeclaration",
    1: "functionCall",
    2: "returnStatement",
    3: "variableAssignment"
}

class CodeGenerator:
    def __init__(self, ast):
        assembly = self.collectVariables(ast["body"])
        assembly += "section .text\n.global main\n"
        assembly += self.handleBody(ast['body'])

        with open("out.asm", "w") as out:
            out.write(assembly)

    def collectVariables(self, ast, variables=None):
        assembly = "section .data\n"

        if variables == None:
            variables = set()

        for node in ast:
            if node["type"] == NODE_TYPES[0]:
                self.collectVariables(node["body"], variables)
            elif node["type"] == NODE_TYPES[3]:
                variables.add(node["name"])
            elif isinstance(node.get("value"), dict):
                self.collectVariables([node["value"]], variables)

        for var in variables:
            assembly += f"{var} dq 0\n"

        return assembly
    
    def handleValue(self, value):
        if isinstance(value, dict):
            if value["type"] == NODE_TYPES[1]:
                return f"\tcall {value['value']}\n"
        else:
            return f"\tmov rax, {value}\n"

    def handleBody(self, ast):
        assembly_code = ""
    
        for node in ast:
            if node['type'] == NODE_TYPES[0]:
                assembly_code += f"{node['name']}:\n" # name:
                
                assembly_code += self.handleBody(node['body'])
    
                assembly_code += f"\tret\n" # ret
            elif node["type"] == NODE_TYPES[1]:
                assembly_code += f"\tcall {node['value']}\n"
            elif node["type"] == NODE_TYPES[2]:
                assembly_code += f"\tmov rax, {node['value']}\n"
            elif node["type"] == NODE_TYPES[3]:
                assembly_code += self.handleValue(node["value"])
                assembly_code += f"\tmov [{node['name']}], rax\n"
    
        return assembly_code
    
ast = {
	"body": [
        {
            "type": "functionDeclaration",
            "name": "testFunc",
            "params": [],
            "body": [
                {
                    "type": "returnStatement",
                    "value": "7"
                }
            ]
        },
        {
            "type": "functionDeclaration",
            "name": "main",
            "params": [],
            "body": [
                {
                    "type": "variableAssignment",
                    "name": "testVar",
                    "value": {
                        "type": "functionCall",
                        "value": "testFunc"
                    }
                },
                {
                    "type": "variableAssignment",
                    "name": "testVar2",
                    "value": "3"
                },
                {
                    "type": "functionCall",
                    "value": "testFunc"
                }
			]
		}
    ]
}

codeGenerator = CodeGenerator(ast)
