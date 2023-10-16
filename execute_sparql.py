import os
import glob

import rdflib
from rdflib import RDF, OWL, RDFS
import owlrl

query_file_path = "derive_DSI_from_QUDT.sparql"
cache_dir_path = "onto_cache"
onto_file_paths = glob.glob(os.path.join(cache_dir_path, "*.ttl"))



# load them into rdflib-graph
g = rdflib.Graph()

for file_path in onto_file_paths:
    file_format = os.path.splitext(file_path)[1][1:]
    g.parse(file_path, format=file_format)
    print(f"{file_path}: loaded")

# infer implicit triples by reasoning
#owlrl.DeductiveClosure(owlrl.RDFS_OWLRL_Semantics).expand(g)

## remove owl:sameAs relations, if they only cover identity
#for subj, pred, obj in g.triples((None, RDF.type, None)):
#    print(subj.n3(g.namespace_manager), pred.n3(g.namespace_manager), obj.n3(g.namespace_manager))


query = open(query_file_path, "r").read()

qres = g.query(query)
for row in qres:
    print(f"{row.sub.n3(g.namespace_manager)} --> \"{row.dsiString}\"")