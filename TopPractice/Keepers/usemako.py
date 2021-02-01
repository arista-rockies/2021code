from mako.template import Template

SubjectName = "Walter"

ifnums = ['1', '2', '3']

# mytemplate = Template("Your name is ${ThisGuysName}!")
mytemplate = Template(filename='makotest1')

for i in ifnums:
    print(mytemplate.render(x=i))



