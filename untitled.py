from urllib.request import urlopen

class htmlp:

    def __init__(self, hstr):

        try:
            self.hstr = hstr.decode("utf-8")
        except UnicodeDecodeError as e:
            self.hstr = str(hstr)
            print(e)

    def __str__(self):
        return str(self.hstr)

    # Method that returns a list of all strings between a begin string and end string
    # doesntbeginwith is an optional parameter that excludes certain  lists that begin with a certian substring
    # eg. all strings between "foo" and "bar" that dont begin with the substring "n"

    def between(self, substring1, substring2, doesntbeginwith=''):

        retval = []

        s = self.hstr.split(substring1)

        for i in s:
            try:
                if i[0] != doesntbeginwith:
                    retval.append(i[0:i.index(substring2)])

            except:
                pass

        if len(retval) == 1:
            return retval[0]
        return retval

def dadjokes():
    url1 = 'http://www.tweeplers.com/hashtags/?cc=WORLD'
    begstr1 = '<div class="col-xs-8 wordwrap" id="item_u_1" name="'
    endstr1 = '" style="font-size:1.5em"><a href='
    doesntbegw1 = "<"

    html1 = htmlp(urlopen(url1).read())
    lst1 = html1.between(begstr1, endstr1, doesntbeginwith=doesntbegw1)
    print(lst1)

dadjokes()