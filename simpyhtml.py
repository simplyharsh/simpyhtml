#!/usr/bin/env python

class Tag(object):
    def __init__(self, tagname):
        self.tagname = tagname
        self.endtag = "<\%s>\n" % self.tagname
        self.attrs = {}
        self.children = []

    def __getitem__(self, items):
        if not isinstance(items, tuple):
            items = (items,)

        for item in items:
            self.children.append(item)

        return self

    def __call__(self, **kw):
        self.attrs.update(kw)
        return self

    def __str__(self):
        return "<%s>" % self.tagname

    def get_starttag(self):
        if self.attrs:
            if 'klass' in self.attrs:
                self.attrs['class'] = self.attrs.pop('klass')
            attrs = " "+(" ".join(["%s=\"%s\"" % (k,v) for k,v in self.attrs.iteritems()]))
        else:
            attrs = ""

        return "<%s%s>\n" % (self.tagname, attrs)

    def generate_html(self, i=None):
        if not isinstance(i, int):
            i = 0

        ch_str = ''
        for child in self.children:
            if isinstance(child, Tag):
                chs = child.generate_html(i+1)
            elif isinstance(child, basestring):
                chs = ("%s%s\n" % ('  ' * (i+1), child))
            ch_str += chs

        tab = '  ' * i
        st = "%s%s%s%s%s" % (
            tab,
            self.get_starttag(),
            ch_str,
            tab,
            self.endtag
            )

        return st

def _(tagname):
    return Tag(tagname)


if __name__ == '__main__':
    html = _('html') [
        _('body') [
            _('div') (klass="one") [
                _('span') ['Hello World', 'something']
                ],
            _('div') [
                'span'
                ]
            ]
        ]
    print html.generate_html()
