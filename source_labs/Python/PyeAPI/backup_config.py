import yaml
import pyeapi
import os

file = open('switches.yml', 'r')
switch_vars = yaml.safe_load(file)
pyeapi.load_config('eapi.conf')

directory = "configs"
exists = os.path.exists(directory)
if not exists:
    os.makedirs(directory)

for switch in switch_vars['switches']:
    connect = pyeapi.connect_to(switch)
    running_config = connect.get_config(as_string='True')
    path = directory+'/'+switch+'.cfg'
    file = open(path,'w')
    file.write(running_config)
    file.close()
    print(f"Backing up {switch}")