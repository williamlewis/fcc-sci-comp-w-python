# Python for Everybody - Video Summary Questions

### Introduction

1. Who should learn to program?
    > Everyone

2. Where are your programs stored when they are running?
    > Memory

3. What will print out after running these two lines of code:
x = 6
print(x)
    > 6

4. What will the following program print out:
x = 43
x = x + 1
print(x)
    > 44

5. What is the symbol used in an assignment statement?
    > =

6. What will print out after running this code:
width = 15
height = 12.0
print(height/3)
    > 4.0

7. Which code is indented correctly to print "Yes" if x = 0 and y = 10?
    > if 0 == x:
        if y == 10:
            print("Yes")

8. Given the following code:
    1  temp = "5 degrees"
    2  cel = 0
    3  fahr = float(temp)
    4  cel = (fahr - 32.0) * 5.0 / 9.0
    5  print(cel)
Which line/lines should be surrounded by try block?
    > 3,4

9. What is the purpose of the "def" keyword in Python?
    > It indicates the start of a function, and the following indented section of code is to be stored for later.

10. What will the following Python program print out?:
    def fred():
        print("Zap")
    def jane():
        print("ABC")

    jane()
    fred()
    jane()
    > ABC
    > Zap
    > ABC

11. What will the following code print out?:
    n = 0
    while True:
        if n == 3:
            break
        print(n)
        n = n + 1
    > 0
    > 1
    > 2

12. How many lines will the following code print?:
    for i in [2,1,5]:
        print(i)
    > 3

13. Below is code to find the smallest value from a list of values. One line has an error that will cause the code to not work as expected. Which line is it?:
    smallest = None
    print("Before:", smallest)
    for itervar in [3, 41, 12, 9, 74, 15]:
        if smallest is None or itervar < smallest:
            smallest = itervar
            break
        print("Loop:", itervar, smallest)
    print("Smallest:", smallest)
    > 6

14. Which of these evaluates to False?
    > 0 is 0.0

15. What will the following code print?:
    for n in "banana":
        print(n)
    > b
    > a
    > n
    > a
    > n
    > a

16. What is the value of i in the following code?
    word = "bananana"
    i = word.find("na")
    > 2

17. What is used to indicate a new line in a string?
    > \n

18. What does the word 'continue' do in the middle of a loop?
    > Skips to the next iteration of the loop.

19. What is the value of x after running this code:
    fruit = "banana"
    x = fruit[1]
    > a

20. Which method is used to add an item at the end of a list?
    > append

21. What does n equal in this code?
    > lar@freecodecamp.org

22. What does dict equal after running this code?:
    dict = {"Fri": 20, "Thu": 6, "Sat": 1}
    dict["Thu"] = 13
    dict["Sat"] = 2
    dict["Sun"] = 9
    > {'Fri': 20, 'Thu': 13, 'Sat': 2, 'Sun': 9}

23. What will the following code print?
    counts = { 'quincy' : 1 , 'mrugesh' : 42, 'beau': 100, '0': 10}
    print(counts.get('kris', 0))
    > 0

24. What will the following code print?:
    counts = { 'chuck' : 1 , 'annie' : 42, 'jan': 100}
    for key in counts:
        if counts[key] > 10:
            print(key, counts[key])
    > annie 42
    > jan 100

25. What will the following code print?:
    d = dict()
    d['quincy'] = 1
    d['beau'] = 5
    d['kris'] = 9
    for (k,i) in d.items():
        print(k, i)
    > quincy 1
    > beau 5
    > kris 9

26. Which does the same thing as the following code?:
    lst = []
    for key, val in counts.items():
        newtup = (val, key)
        lst.append(newtup)
    lst = sorted(lst, reverse=True)
    print(lst)
    > print( sorted( [ (v,k) for k,v in counts.items() ], reverse=True ) )

27. Which regex matches only a white space character?
    > \s

28. What will the following program print?:
    import re
    s = 'A message from csev@umich.edu to cwen@iupui.edu about meeting @2PM'
    lst = re.findall('\\S+@\\S+', s)
    print(lst)
    > ['csev@umich.edu', 'cwen@iupui.edu']

29. What will search for a "$" in a regular expression?
    > \$

30. What Python library gives access to TCP Sockets?
    > socket

31. What type of HTTP request is usually used to access a website?
    > GET

32. What does the following code create?:
    import socket

    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)

    while True:
        data = mysock.recv(512)
        if len(data) < 1:
            break
        print(data.decode(),end='')
    mysock.close()
    > A simple web browser.

33. Which type of encoding do most websites use?
    > UTF-8

34. What will the output of the following code be like?:
    import urllib.request
    fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
    for line in fhand:
        print(line.decode().strip())
    > Just contents of "romeo.txt".

35. What Python library is used for parsing HTML documents and extracting data from HTML documents?
    > BeautifulSoup

36. What are the two most common ways to send data over the internet?
    > JSON and XML

37. What is wrong with the following XML?:
    <person>
    <name>Chuck</name>
    <phone type="intl">
        +1 734 303 4456
    <email hide="yes" />
    </person>
    > Phone tag is missing closing tag.

38. What is XSD?
    > The W3C Schema specification for XML.

39. What will the following code print?:
    import json
    data = '''
    [
        { "id" : "001",
        "x" : "2",
        "name" : "Quincy"
        } ,
        { "id" : "009",
        "x" : "7",
        "name" : "Mrugesh"
        }
    ]
    '''
    info = json.loads(data)
    print(info[1]['name'])
    > Mrugesh

40. With a services oriented approach to developing web apps, where is the data located?
    > Spread across many computer systems connected via the internet or internal network.

41. What does API stand for?
    > Application Programming Interface

42. When making a request from the Twitter API, what information must always be sent with the request?
    > key







    

43. a
    > a

44. a
    > a

45. a
    > a

46. a
    > a

47. a
    > a

48. a
    > a

49. a
    > a

50. a
    > a

51. a
    > a

52. a
    > a

53. a
    > a

54. a
    > a

55. a
    > a

56. a
    > a
