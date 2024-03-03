from scholarly import scholarly
from scholarly import ProxyGenerator

pg = ProxyGenerator()
scholarly.use_proxy(pg)

search_query = scholarly.search_pubs('Perception of physical stability and center of mass of 3D objects')
scholarly.pprint(next(search_query))
