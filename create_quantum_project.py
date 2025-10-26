"""Author: Nihit Choudhary"""

import os

def create_quantum_project_structure(project_name):
    """Generates the recommended folder structure for a quantum computing project."""

    # Define the structure as a dictionary
    structure = {
        'data': {'raw': {}, 'processed': {}},
        'notebooks': {},
        'src': {
            '__init__.py': None,
            'quantum_circuits': {
                '__init__.py': None,
                'algorithms.py': None,
                'gates.py': None,
            },
            'classical_tools': {
                '__init__.py': None,
                'data_processing.py': None,
                'helper_functions.py': None,
            },
            'application': {
                '__init__.py': None,
                'main.py': None,
            }
        },
        'tests': {
            '__init__.py': None,
            'test_algorithms.py': None,
            'test_circuits.py': None,
        },
        'results': {
            'figures': {},
            'logs': {},
            'reports': {}
        },
        'config': {
            'project_settings.ini': None,
            'qiskit_provider.json': None,
        },
        'docs': {
            'README.md': None,
            'setup.md': None,
        },
        'requirements.txt': None,
        '.gitignore': None,
    }

    # Recursively create folders and files
    def create_items(base_path, items):
        for name, content in items.items():
            path = os.path.join(base_path, name)
            if isinstance(content, dict):
                os.makedirs(path, exist_ok=True)
                create_items(path, content)
            elif content is None:
                # Create an empty file
                with open(path, 'w') as f:
                    pass
            else:
                # Create a file with content (if specified)
                with open(path, 'w') as f:
                    f.write(content)

    # Create the top-level project directory
    os.makedirs(project_name, exist_ok=True)

    # Create all subdirectories and files
    create_items(project_name, structure)
    print(f"Project structure for '{project_name}' created successfully.")

if __name__ == "__main__":
    project_name = input("Enter project name: ")
    create_quantum_project_structure(project_name)

