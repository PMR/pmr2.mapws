import json

from pmr2.json.mixin import SimpleJsonFormMixin
from pmr2.json.collection.mixin import JsonCollectionFormMixin
from pmr2.json.collection.core import keyvalue_to_itemdata
from pmr2.mapws.ricordo import QueryForm


class SimpleJsonQueryForm(SimpleJsonFormMixin, QueryForm):

    def render(self):
        if self._searched:
            return json.dumps({'results': [{
                'data': v['data'],
                'source': v['source'],
                'obj': {
                    'href': v['source'] or v['obj'].getURL(),
                    'title': v['obj'].Title or v['source'],
                },
            } for v in self.results()]})
        return super(QueryForm, self).render()


class CollectionQueryForm(JsonCollectionFormMixin, QueryForm):

    def update(self):
        super(CollectionQueryForm, self).update()
        if self._searched:
            self._jc_items = []
            for v in self.results():
                item = keyvalue_to_itemdata(v['data'])
                item['data'].append({
                    'name': 'source',
                    'value': v['source'],
                })
                item['links'] = [{
                    'href': v['source'] or v['obj'].getURL(),
                    'prompt': v['obj'].Title or v['source'],
                    'rel': 'bookmark',
                }]
                self._jc_items.append(item)
