import yaml
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
myload = yaml.FullLoader

def loadfile(yml_file):
    with open(yml_file) as f:
        return yaml.load(f, myload)

sports = loadfile('yamltest1.yml')['sports']

print(sports)


