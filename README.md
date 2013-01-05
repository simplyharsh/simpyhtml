simpyhtml
=========

Html-markup in pythonic way.
Can be used to generate markup for widgets, from within the controllers.

Idea is to not-parse the texts, rather generate and pre-cache it, to minimize runtime rendering.

```
>>> from simpyhtml import Tag as T, Var as V
>>> br = T('br')
>>>
>>> html = T('html') [
...     T('body') (klass=V('theme')) [
...         T('div') (klass="container", rel=V('container-rel')) [
...             'Header', br,
...             'by ', V('name'), br,
...             'Footer'
...         ]
...     ]
... ]
>>> print html % {'name': 'Harsh', 'theme': 'a', 'container-rel': 'blue-g'}
<html><body class="a"><div class="container" rel="blue-g">Header<br />by Harsh<br />Footer</div></body></html>
>>>
>>> html = T('html') [
...     T('body') (klass=V('theme')) (
...         T('div') (klass="container", rel=V('container-rel')) (*(
...             T('div')(x, klass=x) for x in ('header', 'body', 'footer')
...         ))
...     )
... ]
>>> print html % {'name': 'Harsh', 'theme': 'a', 'container-rel': 'blue-g'}
<html><body class="a"><div class="container" rel="blue-g"><div class="header">header</div><div class="body">body</div><div class="footer">footer</div></div></body></html>
>>>
```