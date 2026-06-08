import math


CENTER_X = 50.0
CENTER_Y = 50.0
SUN_RADIUS = 10.0
SAFETY_MARGIN = 1.5


def _get(obs, key, default=None):
    if isinstance(obs, dict):
        return obs.get(key, default)
    return getattr(obs, key, default)


def _distance(a, b):
    return math.hypot(a["x"] - b["x"], a["y"] - b["y"])


def _angle_between(source, target):
    return math.atan2(target["y"] - source["y"], target["x"] - source["x"])


def _planet(row):
    return {
        "id": int(row[0]),
        "owner": int(row[1]),
        "x": float(row[2]),
        "y": float(row[3]),
        "radius": float(row[4]),
        "ships": int(row[5]),
        "production": int(row[6]),
    }


def _segment_point_distance(ax, ay, bx, by, px, py):
    dx = bx - ax
    dy = by - ay

    if dx == 0 and dy == 0:
        return math.hypot(px - ax, py - ay)

    t = ((px - ax) * dx + (py - ay) * dy) / (dx * dx + dy * dy)
    t = max(0.0, min(1.0, t))
    closest_x = ax + t * dx
    closest_y = ay + t * dy
    return math.hypot(px - closest_x, py - closest_y)


def _crosses_sun(source, target):
    return (
        _segment_point_distance(
            source["x"],
            source["y"],
            target["x"],
            target["y"],
            CENTER_X,
            CENTER_Y,
        )
        <= SUN_RADIUS + SAFETY_MARGIN
    )


def _target_score(source, target):
    distance = max(_distance(source, target), 1.0)
    capture_cost = max(target["ships"] + 1, 1)
    production_value = target["production"] * 12.0

    return production_value / distance - capture_cost * 0.03


def _choose_target(source, targets):
    feasible = []

    for target in targets:
        if _crosses_sun(source, target):
            continue

        ships_needed = target["ships"] + 1
        if source["ships"] <= ships_needed + 5:
            continue

        feasible.append(target)

    if not feasible:
        return None

    return max(feasible, key=lambda target: _target_score(source, target))


def agent(obs):
    player = int(_get(obs, "player", 0))
    planets = [_planet(row) for row in _get(obs, "planets", [])]

    my_planets = [planet for planet in planets if planet["owner"] == player]
    targets = [planet for planet in planets if planet["owner"] != player]

    if not my_planets or not targets:
        return []

    moves = []

    for source in my_planets:
        if source["ships"] < 15:
            continue

        target = _choose_target(source, targets)
        if target is None:
            continue

        ships_needed = target["ships"] + 1
        max_send = max(0, source["ships"] - 8)
        ships_to_send = min(max_send, ships_needed + 3)

        if ships_to_send <= 0:
            continue

        moves.append([
            source["id"],
            _angle_between(source, target),
            int(ships_to_send),
        ])

    return moves
