from dominix.tags import *

def test_x_data():
    tag = div(x_data="{ open: false }")
    assert tag.render() == '<div x-data="{ open: false }"></div>'
    tag = div(x_data={ "open": False, "name": "Foo" })
    assert tag.render() == "<div x-data='{\"open\": false, \"name\": \"Foo\"}'></div>"

def test_x_bind():
    tag = input_(x_bind_placeholder="foo")
    assert tag.render() == '<input x-bind:placeholder="foo">'
    tag = input_(x_bind={"placeholder": "foo", "id": "bar"})
    assert tag.render() == '<input x-bind:id="bar" x-bind:placeholder="foo">'

def test_x_on():
    tag = div(x_on_click="foo()")
    assert tag.render() == '<div x-on:click="foo()"></div>'
    tag = div(x_on={"click": "foo()", "keypress": "bar()"})
    assert tag.render() == '<div x-on:click="foo()" x-on:keypress="bar()"></div>'

def test_x_for():
    tag = template(p("foo"), x_for="bar in baz")
    assert tag.render() == """<template x-for="bar in baz">
  <p>foo</p>
</template>"""


def test_x_model():
    tag = input_(x_model="foo")
    assert tag.render() == '<input x-model="foo">'
    tag = input_(x_model_lazy="foo")
    assert tag.render() == '<input x-model.lazy="foo">'
    tag = input_(x_model_debounce_500ms="foo")
    assert tag.render() == '<input x-model.debounce.500ms="foo">'
    

def test_x_transition():
    tag = div(x_transition="")
    assert tag.render() == '<div x-transition=""></div>'
    tag = div(x_transition_enter_scale_origin_top="")
    assert tag.render() == '<div x-transition:enter.scale.origin.top=""></div>'
    tag = div(x_transition_enter="")
    assert tag.render() == '<div x-transition:enter=""></div>'
    tag = div(x_transition_enter_start="")
    assert tag.render() == '<div x-transition:enter-start=""></div>'
    tag = div(x_transition_enter_end="")
    assert tag.render() == '<div x-transition:enter-end=""></div>'
    tag = div(x_transition_leave="")
    assert tag.render() == '<div x-transition:leave=""></div>'
    tag = div(x_transition_leave_scale_90="")
    assert tag.render() == '<div x-transition:leave.scale.90=""></div>'
    tag = div(x_transition_leave_start="")
    assert tag.render() == '<div x-transition:leave-start=""></div>'
    tag = div(x_transition_leave_end="")
    assert tag.render() == '<div x-transition:leave-end=""></div>'
    tag = div(x_transition_leave_end="opacity-0 scale-90")
    assert tag.render() == '<div x-transition:leave-end="opacity-0 scale-90"></div>'
    