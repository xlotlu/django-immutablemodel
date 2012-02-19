import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.dirname(__file__))

os.environ['PYTHONPATH'] = os.pathsep.join([
  ROOT, 
  os.path.join(ROOT, 'samples')
])
    

def django(django_cmd):
    cmd = "django-admin.py %s" % django_cmd
    print cmd
    return subprocess.call([cmd], shell=True, cwd=ROOT)
    
def test(failfast=False):
    django('syncdb  --noinput --verbosty=0')
    cmd = 'test --settings=test_settings'
    if failfast:
        cmd += " --failfast"
    django(cmd)
    
if __name__=="__main__":
    failfast =  "--failfast" in sys.argv
    retval = test(failfast=failfast)
    sys.exit(retval)