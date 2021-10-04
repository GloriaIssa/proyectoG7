from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html')

if __name__ == '__main__':  #Cuando este corriendo de modo principal debe subir el servidor
    app.run(debug=True)     #Para que cuando haga un cambio y guarde el servidor se actualiza enseguida