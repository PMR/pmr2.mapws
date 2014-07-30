import json

from pmr2.json.mixin import JsonPage, SimpleJsonFormMixin
from pmr2.mapws.ricordo import QueryForm


class QueryForm(SimpleJsonFormMixin, QueryForm):

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
