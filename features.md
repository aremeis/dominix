Dominix features
================

These are features not present in Dominate. See the [main article](//github.com/aremeis/dominix) for 
common features.

All code samples assumes Dominix being imported like this:
```python
from dominix.tags import *
```

HTMX support
------------

The most important difference from Dominate is of course the support for HTMX. All HTMX attributes are 
available as named arguments and properties, including docstrings. This provides code completion and better IDE support.

![Screen shot](//github.org/aremeis/dominix/img/screenshot-1.png)

The attributes are available both as constructor arguments and as tag properties:
```python
tag = div(hx_get="/my/endpoint")
print(tag)

tag = div()
tag.hx_get = "/my/endpoint"
print(tag)
```

Output:
```html
<div hx-get="/my/endpoint"></div>
<div hx-get="/my/endpoint"></div>
```


### Special attributes

The following attributes have special implementation to provide better developer experience.

#### `hx-on`

HTMX [requires](https://htmx.org/attributes/hx-on/) one `hx-on*` attriubute for each event handler:
```html
<div hx-on:click="alert()">Click</div>
```

In Dominix `hx-on` is a property that returns a dictionary:
```python
tag = div()
tag.hx_on["click"] = "alert()"
```

Or it can be set using the constructor:
```python
tag = div(hx_on={"click": "alert('Clicked')"}
```

In both cases the resulting HTMX will be:
```html
<div hx-on:click="alert()"></div>
```

### `hx-val` and `hx-headers`

These HTMX attributes are also available as dictionary properties / constructor arguments.
They will be converted to JSON when the tag is rendered:

```python
tag = div(hx_headers={"foo": "bar", "baz": "qux"})
tag.hx_vals = {"foo": "bar", "baz": "qux"}
```

```html
<div hx-headers='{"foo": "bar", "baz": "qux"}' hx-vals='{"foo": "bar", "baz": "qux"}'></div>
```

### `cls`

The `cls` property can be used for easy manipulation of the HTML `class` attribute using standard Python list operations:

```python
tag = div(cls="a b c")
tag.cls.extend(["d", "e", "f"])
tag.cls.append("g")
tag.cls.remove("b")
```

```html
<div class="a b d e f g"></div>
```

(You can assign lists and strings to `cls` interchangably. Strings will be converted to lists as needed.)


### `style`

The `style` property can be used for easy manipulation of the HTML `style` attribute using standard Python dictionary operations:

```python
tag = div(style="color: red; font-size: 12px")
tag.style["color"] = "blue"
del tag.style["font-size"]
tag.style["font-color"] = "green"
```

```html
<div style="color:blue; font-color:green"></div>
```

(You can assign dictionaries and strings to `style` interchangably. Strings will be converted to dictionaries as needed.)


### Chainable `attr`

Dominate comes with the `attr` function for adding attributes to the current tag (when using `with` syntax). 
Dominix has the same function, with the only change that it will return `self`. In addition, `attr` has also been added as a method.
These two features make your code more efficient in some situations:

```python
# Let's say you have created this component in your design system
def section(title):
    # A very simple example
    return div(h1(title))

# ... and you want to make your own variation of it:
def mysection():
    return section("Chained").attr(hx_get="/my/endpoint")

# ... which is equivalent to:
def mysection():
    tag = section("Chained")
    with tag:
        attr(hx_get="/my/endpoint")
    return tag
```

The result of `mysection().render()`: is the same in both cases:
```html
<div hx-get="/my/endpoint">
    <h1>Chained</h1>
</div>
```