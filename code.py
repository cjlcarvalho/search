#! /usr/bin/python2
#! -*- coding: utf-8 -*-

import web
from web import form
from search import *

render = web.template.render('templates/')

urls = ('/', 'index')
app = web.application(urls, globals())

myform = form.Form(
    form.Textbox('Title: '),
    form.Dropdown('Type: ', ['---','TOPIC', 'PERSON',]),
    form.Dropdown('Action: ', ['Index', 'Search']),
    form.Button('Execute'),)

class index:

    def GET(self):
        form = myform()
        return render.index(form)

    def POST(self):
	form = myform()

        search = Search(form['Title: '].value, form['Type: '].value)

	if not form.validates():
            return render.index(form)
        else:
	    if form['Action: '].value == 'Index':
                search = Search(form['Title: '].value, form['Type: '].value)

                search.add()
	    else:
                search = Search(form['Title: '].value, form['Type: '].value)

                if form['Type: '].value == '---':
                    return search.query()
                else:
                    return search.filter()
                    
if __name__ == '__main__':
    web.internalerror = web.debugerror
    app.run()
