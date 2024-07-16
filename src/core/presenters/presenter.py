from features.pools.extract.models.types import PoolsAndSwimlanes

def place_nodes(num_nodes, max_width, max_height):
    
    positions = []
    cols = 2
    # cols = int(num_nodes ** 0.5)
    rows = (num_nodes + cols - 1) // cols

    for i in range(num_nodes):
        col = i % cols
        row = i // cols
        x = col * max_width
        y = row * max_height
        positions.append((x, y))

    return positions



class NodePresenter():
    def __init__(self):
        pass

    def from_pools(self, model : PoolsAndSwimlanes):
        nodes = []
        max_width = 600
        max_height = 0
        num_nodes = len(model.pools)
        for pool in model.pools:
            max_height = max(len(pool.swimlanes)*200,max_height)

        max_height = max_height + 100
        
        positions = place_nodes(num_nodes, max_width, max_height)
        
        for ind,pool in enumerate(model.pools):
            position  = positions[ind]
            height = max(400*len(pool.swimlanes),400)
            data = {
                "label":pool.name
            }
            node = {
                "id":pool.name,
                "position":{
                    "x":position[0],
                    "y":position[1]
                },
                "data":data,
                "type":"pool",
                "resizable": True,
                "style": {
                    "width": 500,
                    "height": height,
                    "backgroundColor": 'rgba(208, 192, 247, 0.2)',
                    "borderRadius": '3px',
                    "border": '1px solid #1a192b'
                }
            }
            nodes.append(node)
            for j, lane in enumerate(pool.swimlanes):
                h = len(lane.name)*10 + 100
                laneNode = {
                            "id": lane.name,
                            "data": { "label": lane.name },
                            "resizable": True,
                            "type":"swimlane",
                            "style": {
                                "backgroundColor": 'rgba(50, 192, 247, 0.2)',
                                "border": '1px solid #1a192b',
                                "height":h
                            },
                            "parentId":pool.name,
                            "position": { "x": 51, "y": 350*j },
                            "extent": "parent"
                }
                nodes.append(laneNode)
        return nodes