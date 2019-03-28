from application import app
#import os

#app.logger.addHandler(logging.StreamHandler(sys.stdout))
#app.logger.setLevel(logging.ERROR)

if __name__ == '__main__':
#    port = int(os.environ.get('PORT', 5000))
#    app.run(host='0.0.0.0', port=port)
    
#    app.run(debug=True, port=33507)

    app.run(debug=True)