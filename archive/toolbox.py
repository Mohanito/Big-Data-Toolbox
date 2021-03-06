import webbrowser

while True:
    print("Welcome to Big Data Processing Application")
    print("Please type the number that corresponds to which application you would like to run:")
    print("1. Apache Hadoop")
    print("2. Apache Spark")
    print("3. Jupyter Notebook")
    print("4. SonarQube and SonarScanner")
    print("\nType the number here > ")
    appid = input()
    if appid == 1:
        print("Opening Hadoop in web browser...\n")
        webbrowser.open("http://34.85.228.99:9870/", new = 0, autoraise = True)
    if appid == 2:
        print("Opening Apache Spark in web browser...\n")
        webbrowser.open("http://35.224.111.226:8080", new = 0, autoraise = True)
    if appid == 3:
        print("Opening Jupyter Notebook in web browser...\n")
        webbrowser.open("http://34.123.215.223:8888", new = 0, autoraise = True)
    if appid == 4:
        print("Opening SonarQube in web browser...\n")
        webbrowser.open("http://34.74.74.68:9000", new = 0, autoraise = True)
