from flask import Flask,request,render_template
import sys
from subprocess import check_output
import subprocess
file_path = "code_input.py"


app = Flask(__name__)

def test():
    command = f'python {file_path}'
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    if error:
        return error
    return output



@app.route('/compiler', methods= ['POST'])
def compiler():
    print(request)
    input = request.form['program']
    with open(file_path , "w") as f:
        f.write(input)		

    output = test()
    return render_template('home.html', input=input, output=output.decode())

@app.route('/')
def home():
    # return render_template('home.html',names=names,rolls=rolls,times=times,l=l,totalreg=totalreg(),datetoday2=datetoday2())
    return render_template('home.html')
if __name__ == '__main__':
    app.run(debug=True)