from flask import Flask, jsonify, request
from data_models import Project

app = Flask(__name__)

@app.route('/projects', methods=['POST'])
def create_project():
    data = request.json
    project = Project(name=data['name'], project_type=data['type'], configuration=data['configuration'])
    project.save()
    return jsonify({'projectId': project.id, 'status': 'success', 'message': 'Project created successfully.'}), 201

@app.route('/projects/<project_id>', methods=['GET'])
def get_project(project_id):
    project = Project.get(project_id)
    return jsonify(project.to_dict()), 200

@app.route('/projects/<project_id>', methods=['PUT'])
def update_project(project_id):
    data = request.json
    project = Project.get(project_id)
    project.update(data['configuration'])
    return jsonify({'status': 'success', 'message': 'Project updated successfully.'}),200

@app.route('/projects/<project_id>', methods=['DELETE'])
def delete_project(project_id):
    project = Project.get(project_id)
    project.delete()
    return jsonify({'status': 'success', 'message': 'Project deleted successfully.'}),200

if __name__ == '__main__':
    app.run(debug=True)

