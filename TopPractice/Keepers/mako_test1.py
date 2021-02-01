from mako.template import Template

from cvprac.cvp_client import CvpClient

mytemplate = Template("hello world!")
print(mytemplate.render())

nutz = 'test1'
print(Template(nutz).render())

# clnt = CvpClient()
# clnt.connect(['192.168.10.100'], 'cvp_user', 'cvp_word')

mytemplate = Template(filename='testmako.mako')


mydict = {'age': '44', 'name': 'jason'}
mylist = ['1', '2']

print(mytemplate.render(test1=dict(mydict), test2=list(mylist)))

# print(test2.render(items=list(mylist)))

