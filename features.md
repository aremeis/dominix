Dominix features
================

These are features not present in Dominate. See the [main article](//github.com/aremeis/dominix) for 
common features.

All code samples assume Dominix being imported like this:
```python
from dominix.tags import *
```

HTMX support
------------

Dominate introduces support for HTMX. All HTMX attributes are 
available as named arguments and properties, including docstrings. This provides code completion and better IDE support.

![Screen shot](https://raw.githubusercontent.com/aremeis/dominix/master/img/screenshot-1.png)

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

#### Attribute `hx-on`

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

### Attributes `hx-val` and `hx-headers`

These HTMX attributes are also available as dictionary properties / constructor arguments.
They will be converted to JSON when the tag is rendered:

```python
tag = div(hx_headers={"foo": "bar", "baz": "qux"})
tag.hx_vals = {"foo": "bar", "baz": "qux"}
```

```html
<div hx-headers='{"foo": "bar", "baz": "qux"}' hx-vals='{"foo": "bar", "baz": "qux"}'></div>
```

### Attribute `cls`

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


### Attribute `style`

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


### Method chaining

All the special attributes mentioned above have convenience methods for addiing and deleting elements 
with support for _method chaining_:
* `add_class` / `rem_class`
* `upd_style` / `del_style`
* `upd_hx_on` / `del_hx_on`
* `upd_hx_vals` / `del_hx_vals`
* `upd_hx_headers` / `del_hx_headers`

Example:
```python
# Let's say you have created this component in your design system
def component():
    return div("Hello", cls="one two three", hx_on={"click": "alert('click')"})

# ... and you want to make your own variation of it:
def my_component():
    return component().add_class("four").rem_class("one").upd_hx_on("mouseover", "alert('mouseover')").del_hx_on("click")

# Or using with:
def my_component():
    with component() as c:
        add_class("four")
        rem_class("one")
        upd_hx_on("mouseover", "alert('mouseover')")
        del_hx_on("click")
    return c
```

The result of `my_component().render()`is the same in both cases:
```html
<div class="two three four" hx-on:mouseover="alert('mouseover')">Hello</div>
```

Dominate comes with the `attr` function for adding attributes to the current tag (when using `with` syntax). 
Dominix has the same function, with the only change that it will return `self`. In addition, `attr` has also been added as a method.
This allows for using method chaining, which may be more convenient in some situation:

```python
def section(title):
    return div(h1(title))

def my_section():
    return section("Chained").attr(hx_get="/my/endpoint")

# Alternative without method chaining
def my_section():
    tag = section("Chained")
    with tag:
        attr(hx_get="/my/endpoint")
    return tag
```

The result of `my_section().render()`: is the same in both cases:
```html
<div hx-get="/my/endpoint">
    <h1>Chained</h1>
</div>
```


Alpine.js support
------------------

Support for Alpine.js attributes is also available since version 2.0.0 and follows the same pattern as HTMX.
Use the `x_` prefix for all Alpine.js attributes. In cases where an attribute would contain `-`, `.` or `:` in its name, 
the corresponding Pythonargument will have these characters replaced with `_`. Some examples:

* `x-bind:placeholder` -> `x_bind_placeholder`
* `x-model:lazy` -> `x_model_lazy`
* `x-transition:enter-start` -> `x_transition_enter_start`
* `x-transition:enter.scale.80` -> `x_transition_enter_scale_80`


### Special attributes

The fattributes `x-bind` and `x-on` have special implementation to provide better developer experience, similar to `hx-on`.

#### Attribute `x-on`

HTML:
```html
<div x-on:click="alert()">Click</div>
```

Dominix:
```python
# Alternative 1
tag = div(x_on={"click": "alert()"})

# Alternative 2
tag = div()
tag.x_on["click"] = "alert()"

# Alternative 3
tag = div(x_on_click="alert()")
```

#### Attribute `x-bind`

HTML:
```html
<div x-bind:placeholder="foo">Click</div>
```

Dominix:
```python
# Alternative 1
tag = div(x_bind={"placeholder": "foo"})

# Alternative 2
tag = div()
tag.x_bind["placeholder"] = "foo"

# Alternative 3
tag = div(x_bind_placeholder="foo")
```