import typing as tp
from graph import Graph

PairedTeams = tp.List[tp.Tuple[int, int]]
PathToTeams = tp.List[int]


def depth_first_search(g: Graph, start_team: int, end_team: int) -> PathToTeams:
    if start_team == end_team:
        return [start_team]
    for neighbor in g.get_neighbor_teams(start_team):
        path: PathToTeams = depth_first_search(g, neighbor, end_team)
        if len(path) > 0:
            return [neighbor] + path
    return []


"""
def depth_first_search(g: Graph, start_team: int, end_team: int) -> PathToTeams:
    frontier: tp.List[int] = [start_team]
    explored: tp.List[int] = []

    paired_teams: PairedTeams = []

    while end_team not in explored and len(frontier) != 0:
        next_to_explore: int = explored.pop()
        if next_to_explore not in explored:
            explored.append(next_to_explore)
            to_add: tp.List[int] = [n for n in g.get_neighbor_teams(next_to_explore) if n not in explored]
            frontier.extend(to_add)
            paired_teams.extend([(next_to_explore, neighbor) for neighbor in to_add])

    return _create_path(paired_teams, start_team, end_team)
"""
