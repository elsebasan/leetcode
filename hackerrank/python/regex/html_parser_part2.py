from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def handle_comment(self, data):
        if  '\n' in data:
            print(">>> Multi-line Comment")
            print(str(data))
        else:
            print(">>> Single-line Comment")
            print(str(data))

    def handle_data(self, data):
        if data != '\n':
            print(">>> Data")
            print(str(data))




if __name__ == '__main__':
    n = int(input())
    text = ''
    for i in range(n):
        text = text + input()
        text = text + '\n'
    parser = MyHTMLParser()
    parser.feed(text)


#in
#4
#<!--[if IE 9]>IE9-specific content
#<![endif]-->
#<div> Welcome to HackerRank</div>
#<!--[if IE 9]>IE9-specific content<![endif]-->
#
#out
#>>> Multi-line Comment
#[if IE 9]>IE9-specific content
#<![endif]
#>>> Data
# Welcome to HackerRank
#>>> Single-line Comment
#[if IE 9]>IE9-specific content<![endif]



