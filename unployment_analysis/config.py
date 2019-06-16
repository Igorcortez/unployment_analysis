from os import path

import unployment_analysis

base_path = path.dirname(path.dirname(unployment_analysis.__file__))
workspace_path = path.join(base_path, 'workspace')
data_path = path.join(workspace_path, 'data')
models_path = path.join(workspace_path, 'models')
