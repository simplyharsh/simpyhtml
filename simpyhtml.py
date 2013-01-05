#!/usr/bin/env python
#
# $Copyright: copyright(c) 2012-2013 Harsh Kohli, all rights reserved. $
# $License: MIT License (http://www.opensource.org/licenses/mit-license.php) $
#
# Permission is hereby granted, free of charge, to any person obtaining
# a copy of this software and associated documentation files (the
# "Software"), to deal in the Software without restriction, including
# without limitation the rights to use, copy, modify, merge, publish,
# distribute, sublicense, and/or sell copies of the Software, and to
# permit persons to whom the Software is furnished to do so, subject to
# the following conditions:
#
# The above copyright notice and this permission notice shall be
# included in all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE
# LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION
# OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION
# WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
#

REGULAR = None
CLOSING = 2

TAGTYPE = {
    'br': CLOSING
}.get

class Tag(object):
    def __init__(self, tagname):
        self.tagname = tagname

        tagtype = TAGTYPE(tagname)
        closing = tagtype == CLOSING
        regular = tagtype == REGULAR

        if closing:
            self.s_tag = '<'+tagname+' />'
            self.e_tag = ''
        else:
            self.s_tag = '<'+tagname+'>'
            self.e_tag = '</'+tagname+'>'

        self.tagtype = tagtype
        self.closing = closing
        self.regular = regular

        self.children = []
        self.children_str = ''

        self.attributes = {}
        self.attributes_str = ''

        self.str = self.s_tag+self.children_str+self.e_tag

    def __getitem__(self, children):
        if not isinstance(children, tuple):
            children = (children,)

        return self(*children)

    def __call__(self, *children, **attributes):
        if children and self.closing:
            raise Exception(self.tagname + ' cannot have children.')

        if children:
            ch = ''
            for child in children:
                ch += str(child)

            self.children_str += ch
            self.children += children

        if attributes:
            if 'klass' in attributes:
                attributes['class'] = attributes.pop('klass')

            attrs = ""
            for k,v in attributes.iteritems():
                attrs += (" "+k+"=\""+str(v)+"\"")

            self.s_tag = '<'+self.tagname+attrs+(' />' if self.closing else '>')

            self.attributes_str = attrs
            self.attributes = attributes

        self.str = self.s_tag+self.children_str+self.e_tag
        return self

    def __repr__(self):
        return self.s_tag

    def __str__(self):
        return self.str

    def __mod__(self, context):
        return self.str % context


class Var(object):
    def __init__(self, context_key):
        self.context_key = context_key
        self.str = "%("+self.context_key+")s"

    def __str__(self):
        return self.str

T = Tag
V = Var
