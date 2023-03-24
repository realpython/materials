from dataclasses import dataclass

from maze_solver.graphs.converter import get_edges, get_nodes
from maze_solver.models.maze import Maze
from maze_solver.models.role import Role
from maze_solver.models.solution import Solution
from maze_solver.view.primitives import DisjointLines, Line, Point, tag
from maze_solver.view.renderer import (
    ROLE_EMOJI,
    SVGRenderer,
    arrow_marker,
    background,
    exterior,
    label,
    wall,
)


@dataclass(frozen=True)
class ExtendedSVGRenderer(SVGRenderer):
    square_size: int = 100
    line_width: int = 6
    show_grid: bool = True
    show_obstacles: bool = True
    show_solution: bool = True
    show_roles: bool = True
    show_borders: bool = True
    show_nodes: bool = True
    show_edges: bool = True
    include_corners: bool = True

    def _get_body(self, maze: Maze, solution: Solution | None) -> str:
        tags = [
            arrow_marker(),
            background(),
        ]

        if self.show_grid:
            tags.append(self._render_grid(maze))

        if self.show_obstacles:
            tags.append(self._render_obstacles(maze))

        for square in maze:
            top_left = self._transform(square)
            if self.show_roles:
                if square.role and (emoji := ROLE_EMOJI.get(square.role)):
                    tags.append(label(emoji, top_left, self.square_size // 2))
            if self.show_borders:
                tags.append(self._draw_border(square, top_left))

        if self.show_nodes or self.show_edges:
            tags.append(self._render_nodes_edges(maze))

        if self.show_solution and solution:
            tags.append(self._draw_solution(solution))

        return "".join(tags)

    def _render_grid(self, maze: Maze) -> str:
        horizontal_lines = []
        for y in range(maze.height + 1):
            start = Point(self.offset, self.offset + y * self.square_size)
            end = start.translate(x=self.square_size * maze.width)
            horizontal_lines.append(Line(start, end))

        vertical_lines = []
        for x in range(maze.width + 1):
            start = Point(self.offset + x * self.square_size, self.offset)
            end = start.translate(y=self.square_size * maze.height)
            vertical_lines.append(Line(start, end))

        return DisjointLines(vertical_lines + horizontal_lines).draw(
            stroke_width="6", stroke="gray", stroke_dasharray="5,10"
        )

    def _render_obstacles(self, maze: Maze) -> str:
        rects = []
        for square in maze:
            top_left = self._transform(square)
            if square.role is Role.EXTERIOR:
                rects.append(
                    exterior(top_left, self.square_size, self.line_width)
                )
            elif square.role is Role.WALL:
                rects.append(wall(top_left, self.square_size, self.line_width))
        return "".join(rects)

    def _render_nodes_edges(self, maze: Maze) -> str:
        tags = []

        nodes = get_nodes(maze)

        if self.show_nodes:
            for node in nodes:
                point = self._transform(node)
                tags.append(
                    tag(
                        "circle",
                        cx=point.x + self.square_size // 2,
                        cy=point.y + self.square_size // 2,
                        r=self.square_size // 10,
                        fill="royalblue",
                    )
                )

        if self.show_edges:
            edges = get_edges(maze, nodes)
            for edge in edges:
                point1, point2 = [
                    self._transform(node, extra_offset=self.square_size // 2)
                    for node in [edge.node1, edge.node2]
                ]
                tags.append(
                    Line(point1, point2).draw(
                        stroke_width="6", stroke="royalblue"
                    )
                )

        return "".join(tags)


if __name__ == "__main__":
    from pathlib import Path

    from maze_solver.graphs.solver import solve_all

    renderer = ExtendedSVGRenderer(
        show_grid=True,
        show_obstacles=True,
        show_solution=True,
        show_roles=True,
        show_borders=True,
        show_nodes=False,
        show_edges=False,
    )

    maze = Maze.load(Path("../../../mazes/pacman.maze"))
    for solution in solve_all(maze):
        renderer.render(maze, solution).preview()
