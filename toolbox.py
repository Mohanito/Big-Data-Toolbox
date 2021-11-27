import webbrowser

while True:
    print("Welcome to Big data Processing Application")
    print("Please type the number that corresponds to which application you would like to run:")
    print("1. Apache Hadoop")
    print("2. Apache Spark")
    print("3. Jupyter Notebook")
    print("4. SonarQube and SonarScanner")
    print("\nType the number here > ")
    appid = input()
    if appid == 3:
        print("Opening Jupyter Notebook in web browser...\n")
        webbrowser.open("http://34.123.215.223:8888", new = 0, autoraise = True)
