# Application Manager for CariboSystem 6
print()
def app():
    f = open("app.dat", 'r')
    app_installed = f.read()
    print("Installed Applications")
    print("----------------------------")
    print()
    print(app_installed)

app()