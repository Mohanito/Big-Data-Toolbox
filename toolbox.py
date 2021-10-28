print("Welcome to Big data Processing Application")
print("Please type the number that corresponds to which application you would like to run:")
print("1. Apache Hadoop")
print("2. Apache Spark")
print("3. Jupyter Notebook")
print("4. SonarQube and SonarScanner")
print("\nType the number here > ")
appid = 0
try:
    appid = int(input())
except:
    print("Invalid input")

if appid < 1 or appid > 4:
    print("Invalid input value (choose from 1 to 4)")
else:
    print(appid)