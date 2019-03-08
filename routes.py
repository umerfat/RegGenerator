from flask import Flask, url_for, request, render_template
from app import app
import re
import redis
# connect to redis data store
# r = redis.StrictRedis(host='localhost', port=6379, db=0, charset= "utf-8", decode_responses= True)
# All three lines here are same
# r = redis.StrictRedis()
#r = redis.StrictRedis(host='qanda.redis.cache.windows.net', port=6379, ssl = True, db = 0, password = '', charset= "utf-8", decode_responses= True)

# Server/create
@app.route('/', methods = ['GET', 'POST'])
def hello():
    if request.method == 'GET':
        # send the user form
        return render_template('StringForm.html')
    elif request.method == 'POST':
        # read form data and save it
        if request.form['normal_regex'] == 'normal_regex':
            stringIn = request.form['string']
            numberRep = re.compile('([\d.,]+)')
            result = numberRep.findall(stringIn)
            # define desired replacements here in the dictionary
            dictionary = {" ": "\s*", "/": "\/", "%": "\%", "$": "\$", ":": "\:", "@": "\@", "#": "\#",
                          "&": "\&", "!": "\!", "^": "\^", "\\": "\\\\", ".": "\\."}
            # use these three lines to do the replacement
            dictionary = dict((re.escape(k), v) for k, v in dictionary.items())
            pattern = re.compile("|".join(dictionary.keys()))
            regex = pattern.sub(lambda m: dictionary[re.escape(m.group(0))], stringIn)
            return render_template('StringForm.html', originalString = stringIn, regexGenerated=regex)
        elif request.form['normal_regex'] == 'myra_regex':
            #do some magic here
            stringIn = request.form['string']
            numberRep = re.compile('([\d.,]+)')
            result = numberRep.findall(stringIn)
            # define desired replacements here in the dictionary
            dictionary = {" ": "\s*", "/": "\/", "%": "\%", "$": "\$", ":": "\:", "@": "\@", "#": "\#",
                          "&": "\&", "!": "\!", "^": "\^","\\": "\\\\", ".": "\\."}
            # use these three lines to do the replacement
            dictionary = dict((re.escape(k), v) for k, v in dictionary.items())
            pattern = re.compile("|".join(dictionary.keys()))
            regex = pattern.sub(lambda m: dictionary[re.escape(m.group(0))], stringIn)
            regex = regex.replace("\\", "\\\\")
            return render_template('StringForm.html',originalString = stringIn, regexGenerated=regex)
    else:
        return "<h2>Invalid request</h2>"