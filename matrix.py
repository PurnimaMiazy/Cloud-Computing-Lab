from flask import Flask


# If `entrypoint` is not defined in app.yaml, App Engine will look for an app
# called `app` in `main.py`.
app = Flask(__name__)


@app.route('/')
def hello():
    """Return a friendly HTTP greeting."""
    
    X = [[12,7,3],
        [4 ,5,6],
        [7 ,8,9]]
  
    Y = [[5,8,1,2],
        [6,7,3,0],
        [4,5,9,1]]
    
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