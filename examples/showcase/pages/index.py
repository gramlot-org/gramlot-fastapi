# Copyright 2026 Softwell S.r.l. - SPDX-License-Identifier: Apache-2.0
"""Common Gramlot showcase declarations; no host or database imports."""
import base64
import inspect
from pathlib import Path
from textwrap import dedent

from genro_bag import Bag
from gramlot.page import WebPage


ASSETS = Path(__file__).resolve().parents[1] / 'assets'


class Page(WebPage):
    """One persistent SPA, with small methods for the shell and each example."""

    title = 'gramlot.showcase · FastAPI'
    host_label = 'FastAPI / Python'
    examples = (
        ('welcome', '01 · Welcome', 'welcome_page'),
        ('counter', '02 · Actions', 'counter_page'),
        ('formula', '03 · Formulas', 'formula_page'),
    )

    def main(self, root):
        root.style((ASSETS / 'showcase.css').read_text())
        self.navigation_data(root)
        layout = root.borderContainer(height='100vh', class_='showcase')
        self.header(layout)
        self.navigation(layout)
        self.pages(layout)
        self.footer(layout)
        self.source_palette(root)

    def navigation_data(self, root):
        tree = Bag()
        for name, title, _method in self.examples:
            tree.set_item(name, None, _attributes={'caption': title})
        root.data('showcase.navigation', tree)
        root.data('showcase.selected', 'welcome')
        root.data('showcase.sourceOpen', False)

    def header(self, layout):
        header = layout.contentPane(region='top', height='92px', class_='showcase-header')
        encoded = base64.b64encode((ASSETS / 'gramlot-logo.png').read_bytes()).decode()
        header.img(src=f'data:image/png;base64,{encoded}', alt='Gramlot', class_='showcase-logo')
        brand = header.div(class_='showcase-brand')
        brand.strong('gramlot.showcase')
        brand.span('A single-page application built with Gramlot')
        header.span(self.host_label, class_='host-badge')

    def navigation(self, layout):
        sidebar = layout.contentPane(region='left', width='230px', splitter=True,
                                     class_='showcase-navigation')
        sidebar.div('EXPLORE GRAMLOT', class_='eyebrow')
        sidebar.h2('Showcase')
        sidebar.p('One shared collection. Every host.', class_='muted')
        sidebar.storeTree(store='^showcase.navigation', selectedPath='^showcase.selected',
                          labelAttribute='caption')
        sidebar.div('HOST EXAMPLES', class_='eyebrow host-examples-label')
        sidebar.p('Database and host-specific demos remain separate from this shared collection.',
                  class_='muted')

    def pages(self, layout):
        center = layout.contentPane(region='center', class_='showcase-center', overflow='auto')
        stack = center.stackContainer(selectedPage='^showcase.selected', height='100%')
        for name, title, method in self.examples:
            page = stack.contentPane(pageName=name, title=title, class_='showcase-page', overflow='auto')
            getattr(self, method)(page)

    def footer(self, layout):
        footer = layout.contentPane(region='bottom', height='68px', class_='showcase-footer')
        footer.span('Python declarations. Live Data. Shared components.', class_='muted')
        footer.button('Show source', action="this.SET('showcase.sourceOpen', true);",
                      class_='source-button')

    def source_palette(self, root):
        palette = root.palette(value='^showcase.sourceOpen', title='Show source · Python',
                               width='min(820px, 90vw)', height='min(620px, 80vh)',
                               left='5vw', top='10vh', class_='source-palette')
        stack = palette.stackContainer(selectedPage='^showcase.selected', height='100%')
        for name, title, method in self.examples:
            pane = stack.contentPane(pageName=name, title=title, overflow='auto')
            pane.pre(dedent(inspect.getsource(getattr(type(self), method))), class_='source-code')

    def welcome_page(self, root):
        root.data('welcome.name', 'Ada')
        root.dataFormula('welcome.greeting', "'Hello, ' + (name || 'explorer') + '.'",
                         name='^welcome.name', _on_start=True)
        root.div('01 / LIVE BINDINGS', class_='eyebrow')
        root.h1('Small declarations.\nLiving interfaces.')
        root.p('Explore the same Gramlot ideas across every host. Start with a name: '
               'one Data path connects the input and its greeting.', class_='page-lead')
        card = root.div(class_='demo-card')
        card.div('MAKE IT YOURS', class_='eyebrow')
        card.textBox(value='^welcome.name', lbl='Your name')
        card.h2('^welcome.greeting', class_='live-result')
        card.p('Edit the field. The binding keeps the greeting in sync.', class_='muted')
        root.p('Switch pages and come back: your values stay in the same Data Bag.',
               class_='page-note')

    def counter_page(self, root):
        root.data('counter.value', 0)
        root.div('02 / DECLARATIVE ACTIONS', class_='eyebrow')
        root.h1('A little action.\nAn immediate reaction.')
        root.p('Buttons write to Data through Gramlot actions. Every bound view reacts.',
               class_='page-lead')
        card = root.div(class_='demo-card')
        card.div('^counter.value', class_='counter-value')
        controls = card.div(class_='button-row')
        controls.button('− Decrease', action="this.SET('counter.value', this.GET('counter.value') - 1);")
        controls.button('+ Increase', action="this.SET('counter.value', this.GET('counter.value') + 1);")
        controls.button('Reset', action="this.SET('counter.value', 0);")
        card.p('Open the inspector to see counter.value change.', class_='muted')

    def formula_page(self, root):
        root.data('formula.quantity', 3)
        root.data('formula.price', 12)
        root.dataFormula('formula.total', 'Number(quantity) * Number(price)',
                         quantity='^formula.quantity', price='^formula.price', _on_start=True)
        root.div('03 / REACTIVE FORMULAS', class_='eyebrow')
        root.h1('Change the ingredients.\nWatch the result.')
        root.p('A dataFormula declares its dependencies and updates the total as they change.',
               class_='page-lead')
        card = root.div(class_='demo-card')
        card.numberTextBox(value='^formula.quantity', lbl='Quantity')
        card.numberTextBox(value='^formula.price', lbl='Unit price')
        card.div('TOTAL', class_='eyebrow total-label')
        card.div('^formula.total', class_='counter-value')
        card.p('quantity × price · calculated by Gramlot', class_='muted')
