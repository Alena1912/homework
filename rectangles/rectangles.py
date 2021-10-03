#!/usr/bin/env python

"""
Даны два прямоугольника, стороны которых параллельны осям координат. Известны координаты левого нижнего угла x, y, а также ширина и высота прямоугольника w, h.

                w
    ┌───────────────────────┐
    │                       │
    │                       │ h
    │                       │
    └───────────────────────┘
 (x, y)

- определить, принадлежат ли все точки второго прямоугольника первому (`all`).
- определить, пересекаются ли эти прямоугольники (`any`, `all`).
"""

from collections import namedtuple

Rect = namedtuple("Rect", "x y w h".split())


def rect_inside(a: Rect, b: Rect) -> bool:
    """
    Checks if whole rectangle `b` is within rectangle `a`.
    """
    x1 = a.x
    x2 = a.x + a.w
    y1 = a.y
    y2 = a.y + a.h

    xx1 = b.x
    xx2 = b.x + b.w
    yy1 = b.y
    yy2 = b.y + b.h

    if all([x1 <= xx1,
            y1 <= yy1,
            x2 >= xx2,
            y2 >= yy2]) or all([xx1 <= x1,
                                yy1 <= y1,
                                xx2 >= x2,
                                yy2 >= y2]):
        return True
    return False


def rects_intersect(a: Rect, b: Rect) -> bool:
    """
    Checks if 2 rectangles `a` and `b` have at least a single intersection point.
    """
    x1 = a.x
    x2 = a.x + a.w
    y1 = a.y
    y2 = a.y + a.h

    xx1 = b.x
    xx2 = b.x + b.w
    yy1 = b.y
    yy2 = b.y + b.h

    if any([all([x1 <= xx1 <= x2, y1 <= yy1 <= y2]),
            all([x1 <= xx2 <= x2, y1 <= yy1 <= y2]),
            all([xx1 <= x1 <= xx2, yy1 <= y2 <= yy2]),
            all([xx1 <= x2 <= xx2, yy1 <= y2 <= yy2])]):
        return True
    return False
