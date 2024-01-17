from google.cloud import firestore
from datetime import datetime

# Initialize Firestore client
db = firestore.Client()

class Project:
    def __init__(self, name, project_type, configuration, created_at=None, updated_at=None):
        self.id = db.collection('projects').document().id
        self.name = name
        self.project_type = project_type
        self.configuration = configuration
        self.created_at = created_at or datetime.now()
        self.updated_at = updated_at or datetime.now()

    def save(self):
        # Save the project to Firestore
        project_data = self.to_dict()
        db.collection('projects').document(self.id).set(project_data)

    def update(self, new_configuration):
        # Update the project's configuration
        self.configuration = new_configuration
        self.updated_at = datetime.now()
        project_data = self.to_dict()
        db.collection('projects').document(self.id).update(project_data)

    def delete(self):
        # Delete the project from Firestore
        db.collection('projects').document(self.id).delete()

    @classmethod
    def get(cls, project_id):
        # Retrieve a project by its ID from Firestore
        doc = db.collection('projects').document(project_id).get()
        if doc.exists:
            return cls(**doc.to_dict())
        else:
            return None

    def to_dict(self):
        # Convert the project to a dictionary for serialization
        return {
            'id': self.id,
            'name': self.name,
            'project_type': self.project_type,
            'configuration': self.configuration,
            'created_at': self.created_at.isoformat(),
            'updated_at': self.updated_at.isoformat()
        }

# Example usage:
# project = Project(name='MyProject', project_type='web', configuration={'framework': 'Django'})
# project.save()

