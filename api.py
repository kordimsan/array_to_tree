from app import convert_array_to_dict_tree, rec_get_tree
from fastapi import Body, FastAPI

from models import NodeArray


app = FastAPI()


@app.post("/get_tree")
async def get_tree(array: NodeArray = Body(...)):
    tree_dict = convert_array_to_dict_tree(array.nodes)
    result = []
    for node in tree_dict:
        result.append(rec_get_tree(tree_dict, node))
    return result


@app.post("/get_graph")
async def get_tree(array: NodeArray = Body(...)):
    graph = {}
    for row in array.nodes:
        graph.setdefault(row.pid, []).append(row.id)

    return graph
