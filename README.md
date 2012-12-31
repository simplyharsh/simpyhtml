simpyhtml
=========

Creates HTML in very pythonic way

```
>>> from simpyhtml import _
>>> simpy = _('html') [
...         _('body') [
...             _('div') (klass="one") [
...                 _('span') ['Hello World', 'something']
...                 ],
...             _('div') [
...                 'span'
...                 ]
...             ]
...         ]
>>> simpy.generate_html()
'<html>\n  <body>\n    <div class="one">\n      <span>\n        Hello World\n        something\n      <\\span>\n    <\\div>\n    <div>\n      span\n    <\\div>\n  <\\body>\n<\\html>\n'
>>>
>>> print simpy.generate_html()
<html>
  <body>
    <div class="one">
      <span>
        Hello World
        something
      <\span>
    <\div>
    <div>
      span
    <\div>
  <\body>
<\html>

>>>
```