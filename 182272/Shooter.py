from typing import Optional


class Shooter:
    GUNS = {
        # Name: (Range, Power, Bullet size)
        'Submachine Gun': (100, 10, 0.5),
        'Assault Rifle': (200, 20, 1),
        'Pistol': (80, 8, 0.5),
        'Shotgun': (50, 40, 4),
        'Sniper Rifle': (1000, 30, 3)
    }

    BULLETS = {
        # Name: Size, Damage
        'A': (0.5, 1),
        'B': (1, 1.5),
        'C': (3, 3),
        'D': (4, 2),
    }

    def __init__(self) -> None:
        self._selected_gun: Optional[str] = None
        self._selected_bullet: Optional[str] = None
        self._bullets_count: int = 0

    def set_gun_by_name(self, name: str) -> None:
        if name not in self.GUNS:
            raise Exception("Couldn't find selected gun")

        self._selected_gun = name
        self._selected_bullet = None
        self._bullets_count = 0

    def add_bullet_of_given_size_to_gun(self, size: float, count: int) -> None:
        if self._selected_gun is None:
            raise Exception("No gun is selected")

        if self.GUNS[self._selected_gun][2] != size:
            raise Exception("Bullet size and gun size aren't same")

        if count < 0:
            raise Exception("Count should be positive")

        found = list(
            filter(
                lambda x: x[1][0] == size,
                self.BULLETS.items()
            )
        )
        if len(found) == 0:
            raise Exception("Couldn't find bullet with this size")

        name, data = found[0]
        self._selected_bullet = name
        self._bullets_count += count

    def shoot_to_target(self, target_x: int, target_y: int, target_distance: int, aim_x: int, aim_y: int) -> float:
        # Target => 10x10 square
        # target x, y => lower left

        if self._selected_gun is None:
            raise Exception("No gun is selected")

        if self._bullets_count == 0 or self._selected_bullet is None:
            raise Exception("There is no bullet left")

        g_range, power, size = self.GUNS[self._selected_gun]
        b_size, b_dmg = self.BULLETS[self._selected_bullet]

        self._bullets_count -= 1

        if g_range < target_distance:
            return 0

        if target_x < aim_x < target_x + 10 and target_y < aim_y < target_y + 10:
            return power * b_dmg

        return 0
