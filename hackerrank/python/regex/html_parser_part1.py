from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print ("Start :", tag)
        for elem in attrs:
            print ('-> ' + str(elem[0]) + ' > ' + str(elem[1]))

    def handle_endtag(self, tag):
        print ("End   :", tag)

    def handle_startendtag(self, tag, attrs):
        print ("Empty :", tag)
        for elem in attrs:
            print ('-> ' + str(elem[0]) + ' > ' + str(elem[1]))



if __name__ == '__main__':
    n = int(input())
    text = ''
    for i in range(n):
        text = text + input()
    parser = MyHTMLParser()
    parser.feed(text)

