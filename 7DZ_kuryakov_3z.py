import os
import shutil

temp = 'project_1/templates'

for root, dirs, files in os.walk('project_1'):
  if root.endswith('templates'):
    shutil.copytree(
    os.path.join(root, dirs[0]),
    os.path.join(temp, dirs[0])
    )
