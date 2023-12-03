import numpy as np
import typing as tp


class Graph:
    NOT_CONNECTED: int = -1_000_000_000

    def __init__(self, num_nodes: int):
        # Indices are nodes
        # values are edge weights
        self.points_difference: np.ndarray = np.ones((num_nodes, num_nodes), dtype=int) * Graph.NOT_CONNECTED
        self.have_played: np.ndarray = np.zeros((num_nodes, num_nodes), dtype=np.int8)

    def get_points_difference(self, home_team: int, away_team: int) -> int:
        return self.points_difference[home_team, away_team]

    def add_points_difference(self, home_team: int, away_team: int, delta: int):
        self.points_difference[home_team, away_team] += delta

    def have_played(self, team1: int, team2: int) -> bool:
        return self.have_played[team1, team2] == 1

    def set_played(self, team1: int, team2: int) -> tp.NoReturn:
        if team1 == team2:
            return
        self.have_played[team1, team2] = 1
        self.have_played[team2, team1] = 1

    def get_neighbor_teams(self, team: int) -> tp.List[int]:
        return np.argwhere(self.have_played[team] == 1).tolist()