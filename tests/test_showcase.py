# Copyright 2026 Softwell S.r.l. - SPDX-License-Identifier: Apache-2.0
"""The first showcase delivers one persistent shared Source tree without a DB."""
import inspect
from pathlib import Path
from textwrap import dedent

from fastapi.testclient import TestClient
from genro_bag import Bag
from genro_tytx import from_tytx

from gramlot_fastapi import GramlotApplication


EXAMPLE = Path(__file__).resolve().parents[1] / 'examples' / 'showcase'


def descendants(bag):
    for node in bag.nodes:
        yield node
        if isinstance(node.value, Bag):
            yield from descendants(node.value)


def test_showcase_navigation_sources_and_shared_components():
    app = GramlotApplication(EXAMPLE)
    with TestClient(app) as client:
        assert client.get('/page/index/').status_code == 200
        response = client.get('/page/index/recipe')
        assert response.status_code == 200
        source = from_tytx(response.text, transport='json')
        nodes = list(descendants(source))
        navigation = next(node.attr['value'] for node in nodes
                          if node.attr.get('destination') == 'showcase.navigation')
        assert navigation.keys() == ['welcome', 'counter', 'formula']
        assert any(node.attr.get('selectedPath') == '^showcase.selected' for node in nodes)
        assert sum(node.attr.get('selectedPage') == '^showcase.selected' for node in nodes) == 2
        assert {node.attr.get('region') for node in nodes} >= {'top', 'left', 'center', 'bottom'}
        page_class = app.gramlot_pages.page_classes['index']
        strings = [node.value for node in nodes if isinstance(node.value, str)]
        for _name, _title, method in page_class.examples:
            assert dedent(inspect.getsource(getattr(page_class, method))) in strings
        assert 'Show source' in strings
        assert any(node.attr.get('alt') == 'Gramlot' for node in nodes)


def test_showcase_initial_data_and_request_isolation():
    app = GramlotApplication(EXAMPLE)
    with TestClient(app) as client:
        def initial_data():
            response = client.get('/page/index/recipe')
            nodes = descendants(from_tytx(response.text, transport='json'))
            return {node.attr['destination']: node.attr.get('value') for node in nodes
                    if node.label.startswith('dataSetter_')}
        first = initial_data()
        first['showcase.navigation'].set_item('private', 'mutation')
        second = initial_data()
        assert second['showcase.navigation'].keys() == ['welcome', 'counter', 'formula']
        assert second['welcome.name'] == 'Ada'
        assert second['counter.value'] == 0
        assert second['formula.quantity'] == 3
        assert second['formula.price'] == 12
        assert second['showcase.sourceOpen'] is False
