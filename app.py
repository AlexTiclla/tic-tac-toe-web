from flask import Flask, render_template
from binarytree.ArbolBinario import ArbolBinario
from flask import Flask, request, jsonify


app = Flask(__name__)
arbol = ArbolBinario()
arbol.agregar(10)
arbol.agregar(5)
arbol.agregar(15)

@app.route('/')
def inicio():
    return render_template('inicio.html', arbol=arbol)

@app.route('/update_tree', methods=['POST'])
def update_tree():
    action = request.json['action']
    value = request.json['value']

    if action == 'insert':
        arbol.agregar(value)
        return jsonify({'message': f'Successfully inserted {value} into the tree.'})
    elif action == 'delete':
        arbol.deleteNode(value)
        return jsonify({'message': f'Successfully deleted {value} from the tree.'})
    else:
        return jsonify({'message': 'Invalid action.'}), 400