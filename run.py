from notebook import create_app

if __name__ == "__main__":
    app = create_app("/vagrant/local.cfg")
    app.run("0.0.0.0", debug=True)
