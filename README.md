# myhome
 This project is created and interpreted on VSCODE.
 models/ directory that contains classes used for this project
 base_model.py - The baseModel class from which furute classes will be derived.
    .def__init__(self, *args, **kwargs) - Initialisation of the base_model
    .def__save__(self) - updates the updated_at attribute to the current date and tyime, reflecting the instances modification stamp.models.storage.new(self)
Registers the instance with the storage engine, which keeps track of objects to be persisted.models.storage.save()
Saves the current state of the storage engine to ensure all changes are persisted (e.g., written to a database or a file).models.storage.save()
Saves the current state of the storage engine to ensure all changes are persisted (e.g., written to a database or a file).
    .def to_dict(self) - 
    
