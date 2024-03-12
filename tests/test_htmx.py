from dominix.tags import *

def test_cls():
    tag = html(cls="foo  bar")
    assert tag.render() == '<html class="foo  bar"></html>'
    classes = tag.cls
    tag.cls.remove("foo")
    assert tag.render() == '<html class="bar"></html>'
    classes.remove("bar")
    assert tag.render() == '<html></html>'
    classes.extend(["baz", "qux"])
    assert tag.render() == '<html class="baz qux"></html>'
    tag.cls = "kaz quux "
    assert tag.render() == '<html class="kaz quux "></html>'

def test_style():
    tag = html(style="foo: bar;  baz: qux")
    assert tag.render() == '<html style="foo: bar;  baz: qux"></html>'
    style = tag.style
    del style["foo"]
    assert tag.render() == '<html style="baz:qux"></html>'
    tag.style.update({"foo": "bar", "baz": "zab"})
    assert tag.render() == '<html style="baz:zab; foo:bar"></html>'

def test_hx_on():
    tag = html(hx_on_click="foo()")
    assert tag.render() == '<html hx-on-click="foo()"></html>'
    tag = html(hx_on={"click": "foo()"})
    assert tag.hx_on["click"] == "foo()"
    assert tag.render() == '<html hx-on:click="foo()"></html>'
    tag.hx_on["click"] = "bar()"
    assert tag.render() == '<html hx-on:click="bar()"></html>'
    tag.hx_on.update({"htmx:before-request": "baz()", "htmx:after-request": "qux()"})
    assert tag.render() == '<html hx-on:click="bar()" hx-on:htmx:after-request="qux()" hx-on:htmx:before-request="baz()"></html>'
    assert tag.hx_on == {"click": "bar()", "htmx:before-request": "baz()", "htmx:after-request": "qux()"}
    del tag.hx_on["click"]
    assert tag.render() == '<html hx-on:htmx:after-request="qux()" hx-on:htmx:before-request="baz()"></html>'
    tag.hx_on.update({"htmx:before-request": "foo()", "htmx:after-request": None})
    assert tag.render() == '<html hx-on:htmx:before-request="foo()"></html>'
    tag.hx_on.clear()
    assert tag.render() == '<html></html>'

def test_hx_val():
    tag = html(hx_vals={"foo": "bar", "baz": "qux"})
    assert tag.hx_vals == {"foo": "bar", "baz": "qux"}
    assert tag.hx_vals["foo"] == "bar"
    assert tag.hx_vals.get("bazz", None) == None
    assert tag.render() == '<html hx-vals="{&quot;foo&quot;: &quot;bar&quot;, &quot;baz&quot;: &quot;qux&quot;}"></html>'
    del tag.hx_vals["foo"]
    assert tag.render() == '<html hx-vals="{&quot;baz&quot;: &quot;qux&quot;}"></html>'
    tag.hx_vals.clear()
    assert tag.render() == '<html></html>'

def test_hx_headers():
    tag = html(hx_headers={"foo": "bar", "baz": "qux"})
    assert tag.hx_headers == {"foo": "bar", "baz": "qux"}
    assert tag.hx_headers["foo"] == "bar"
    assert tag.hx_headers.get("bazz", None) == None
    assert tag.render() == '<html hx-headers="{&quot;foo&quot;: &quot;bar&quot;, &quot;baz&quot;: &quot;qux&quot;}"></html>'
    del tag.hx_headers["foo"]
    assert tag.render() == '<html hx-headers="{&quot;baz&quot;: &quot;qux&quot;}"></html>'
    tag.hx_headers.clear()
    assert tag.render() == '<html></html>'

def test_hx_get():
    tag = html()
    tag.hx_get = "bar"
    assert tag.render() == '<html hx-get="bar"></html>'

def test_all_args():
    tag = html(
        hx_get="a",
        hx_post="b",
        hx_push_url="d",
        hx_select="e",
        hx_select_oob="f",
        hx_swap="g",
        hx_swap_oob="h",
        hx_target="i",
        hx_trigger="j",
        hx_vals={"k": "l"},
        hx_boost=True,
        hx_confirm="m",
        hx_delete="n",
        hx_disable="o",
        hx_disable_elt="p",
        hx_disinherit="q",
        hx_encoding="r",
        hx_ext="s",
        hx_headers={"t": "u"},
        hx_history=False,
        hx_history_elt="v",
        hx_include="w",
        hx_indicator="x",
        hx_params="z",
        hx_patch="aa",
        hx_preserve="ab",
        hx_prompt="ac",
        hx_put="ad",
        hx_replace_url="ae",
        hx_request="af",
        hx_sync="ag",
        hx_validate="ah",
    )
    assert tag.render() == '<html hx-boost="true" hx-confirm="m" hx-delete="n" hx-disable="o" hx-disable-elt="p" hx-disinherit="q" hx-encoding="r" hx-ext="s" hx-get="a" hx-headers="{&quot;t&quot;: &quot;u&quot;}" hx-history="false" hx-history-elt="v" hx-include="w" hx-indicator="x" hx-params="z" hx-patch="aa" hx-post="b" hx-preserve="ab" hx-prompt="ac" hx-push-url="d" hx-put="ad" hx-replace-url="ae" hx-request="af" hx-select="e" hx-select-oob="f" hx-swap="g" hx-swap-oob="h" hx-sync="ag" hx-target="i" hx-trigger="j" hx-validate="ah" hx-vals="{&quot;k&quot;: &quot;l&quot;}"></html>'

def test_all_props():
    tag = html()
    tag.hx_get="a"
    tag.hx_post="b"
    tag.hx_push_url="d"
    tag.hx_select="e"
    tag.hx_select_oob="f"
    tag.hx_swap="g"
    tag.hx_swap_oob="h"
    tag.hx_target="i"
    tag.hx_trigger="j"
    tag.hx_vals={"k": "l"}
    tag.hx_boost=True
    tag.hx_confirm="m"
    tag.hx_delete="n"
    tag.hx_disable="o"
    tag.hx_disable_elt="p"
    tag.hx_disinherit="q"
    tag.hx_encoding="r"
    tag.hx_ext="s"
    tag.hx_headers={"t": "u"}
    tag.hx_history=False
    tag.hx_history_elt="v"
    tag.hx_include="w"
    tag.hx_indicator="x"
    tag.hx_params="z"
    tag.hx_patch="aa"
    tag.hx_preserve="ab"
    tag.hx_prompt="ac"
    tag.hx_put="ad"
    tag.hx_replace_url="ae"
    tag.hx_request="af"
    tag.hx_sync="ag"
    tag.hx_validate="ah"
    assert tag.render() == '<html hx-boost="true" hx-confirm="m" hx-delete="n" hx-disable="o" hx-disable-elt="p" hx-disinherit="q" hx-encoding="r" hx-ext="s" hx-get="a" hx-headers="{&quot;t&quot;: &quot;u&quot;}" hx-history="false" hx-history-elt="v" hx-include="w" hx-indicator="x" hx-params="z" hx-patch="aa" hx-post="b" hx-preserve="ab" hx-prompt="ac" hx-push-url="d" hx-put="ad" hx-replace-url="ae" hx-request="af" hx-select="e" hx-select-oob="f" hx-swap="g" hx-swap-oob="h" hx-sync="ag" hx-target="i" hx-trigger="j" hx-validate="ah" hx-vals="{&quot;k&quot;: &quot;l&quot;}"></html>'


def test_attr():
    tag = html()
    tag.attr(href="foo")
    assert tag.render() == '<html href="foo"></html>'
    with tag as t:
        attr(cls="bar")
        t.attr(href="bax")
    assert tag.render() == '<html class="bar" href="bax"></html>'
    tag.attr(cls="baz", href="qux", id="quux")
    assert tag.render() == '<html class="baz" href="qux" id="quux"></html>'
