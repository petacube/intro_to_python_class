# hanoi.py
from manim import *

class TowerOfHanoi(Scene):
    N = 5                 # number of disks
    MOVE_SPEED = 2      # animation speed (seconds per mini-move)

    def construct(self):
        # Layout
        peg_x = [-5, 0, 5]
        ground_y = -3
        peg_height = 4
        peg_width = 0.2
        base = Rectangle(width=12, height=0.2).move_to([0, ground_y - 0.2, 0])
        pegs = VGroup(*[
            Rectangle(width=peg_width, height=peg_height).move_to([x, ground_y + peg_height/2, 0])
            for x in peg_x
        ])
        labels = VGroup(
            Text("A").scale(0.7).next_to(pegs[0], DOWN, buff=0.3),
            Text("B").scale(0.7).next_to(pegs[1], DOWN, buff=0.3),
            Text("C").scale(0.7).next_to(pegs[2], DOWN, buff=0.3),
        )

        title = Text(f"Tower of Hanoi — {self.N} disks").to_edge(UP)
        move_text = Integer(0, group_with_commas=False).scale(0.8)
        move_label = VGroup(Text("Moves:"), move_text).arrange(RIGHT, buff=0.3).next_to(title, DOWN)
        self.add(title, move_label, base, pegs, labels)

        # Build disks (largest at bottom)
        disk_height = 0.3
        max_width = 3.8
        min_width = 1.2
        widths = [min_width + (max_width - min_width) * (i / (self.N - 1 or 1))
                  for i in range(self.N)]
        colors = color_gradient([BLUE, PURPLE, ORANGE, YELLOW], self.N)

        # Stacks: each is a list of disks on a peg (top is last)
        stacks = [[], [], []]

        disks = []
        for i in range(self.N):
            w = widths[self.N - 1 - i]  # bottom largest
            disk = RoundedRectangle(corner_radius=0.1, width=w, height=disk_height)
            disk.set_fill(colors[i], opacity=1.0).set_stroke(BLACK, width=1)
            disk.z_index = 10 + i
            # position on peg A (index 0)
            y = ground_y + disk_height/2 + i * disk_height
            disk.move_to([peg_x[0], y, 0])
            disks.append(disk)
            stacks[0].append(disk)

        self.add(*disks)

        # Helper: compute position on peg for next level
        def slot_position(peg_idx, level_idx):
            """level_idx=0 means bottom, so use len(stack) after pushing to place correctly"""
            y = ground_y + disk_height/2 + level_idx * disk_height
            return [peg_x[peg_idx], y, 0]

        # Animate moving one disk A->B (by peg index)
        def move_one(frm, to):
            # pop from source
            disk = stacks[frm].pop()
            # lift
            above = [disk.get_center()[0], ground_y + peg_height + 0.6, 0]
            # travel horizontally over target peg
            over_target = [peg_x[to], above[1], 0]
            # drop to new level
            new_level = len(stacks[to])  # after pop, before push
            target = slot_position(to, new_level)
            # do animations
            self.play(disk.animate.move_to(above), run_time=self.MOVE_SPEED)
            self.play(disk.animate.move_to(over_target), run_time=self.MOVE_SPEED)
            self.play(disk.animate.move_to(target), run_time=self.MOVE_SPEED)
            # push to target
            stacks[to].append(disk)
            # update counter
            move_text.set_value(move_text.get_value() + 1)
            self.wait(0.02)

        # Recursive solver emitting (frm,to) moves
        def solve(n, frm, aux, to):
            if n == 0:
                return
            solve(n - 1, frm, to, aux)
            move_one(frm, to)
            solve(n - 1, aux, frm, to)

        # Optional: highlight source/target pegs as we start
        self.play(pegs[0].animate.set_fill(GREEN, opacity=0.2),
                  pegs[2].animate.set_fill(RED, opacity=0.2),
                  run_time=0.6)

        # Run the solution
        solve(self.N, 0, 1, 2)

        # Wrap-up: show optimal move count = 2^N - 1
        optimal = 2 ** self.N - 1
        box = RoundedRectangle(corner_radius=0.15, width=5.4, height=1.2).set_fill(WHITE, 0.95).set_stroke(BLACK, 1)
        msg = VGroup(
            Text("Done! Optimal moves:").scale(0.6),
            Integer(optimal).scale(0.9)
        ).arrange(RIGHT, buff=0.3)
        wrap = VGroup(box, msg).arrange(buff=0).move_to([0, 2.1, 0])
        self.play(FadeIn(box), Write(msg), run_time=0.8)
        self.wait(1.2)
