from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    
    X = [[15,2,7],
        [6 ,9,6],
        [10 ,8,3]]
  
    Y = [[11,8,8,5],
        [16,5,3,4],
        [2,1,6,4]]
    
    result = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]

  
    for i in range(len(X)):
   
     for j in range(len(Y[0])):
       
       for k in range(len(Y)):
           result[i][j] += X[i][k] * Y[k][j]

    return result


if __name__ == '__main__':
    # This is used when running locally only. When deploying to Google App
    # Engine, a webserver process such as Gunicorn will serve the app. You
    # can configure startup instructions by adding `entrypoint` to app.yaml.
    app.run(host='127.0.0.1', port=8080, debug=True)