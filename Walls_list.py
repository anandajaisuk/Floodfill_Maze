walls = [
    (0, 0, 1, 0, 1, 0),
    (0, 1, 0, 0, 1, 0),
    (0, 2, 0, 0, 1, 0),
    (0, 3, 0, 0, 1, 1),
    (0, 4, 0, 0, 1, 1),
    (0, 5, 0, 0, 1, 1),
    (0, 6, 0, 0, 1, 0),
    (0, 7, 0, 0, 1, 1),
    (0, 8, 0, 0, 1, 0),
    (0, 9, 0, 0, 1, 1),
    (0, 10, 0, 0, 1, 1),
    (0, 11, 0, 0, 1, 1),
    (0, 12, 0, 0, 1, 1),
    (0, 13, 0, 0, 1, 0),
    (0, 14, 0, 0, 1, 1),
    (0, 15, 0, 1, 1, 0),
    (1, 0, 1, 0, 0, 0),
    (1, 1, 1, 0, 1, 0),
    (1, 2, 0, 0, 1, 1),
    (1, 6, 0, 0, 1, 1),
    (1, 7, 0, 0, 0, 1),
    (1, 8, 0, 0, 1, 1),
    (1, 9, 0, 0, 0, 1),
    (1, 12, 0, 0, 0, 1),
    (1, 13, 0, 0, 1, 1),
    (1, 14, 0, 0, 0, 1),
    (1, 15, 0, 1, 0, 0),
    (2, 0, 1, 0, 0, 0),
    (2, 1, 1, 1, 0, 0),
    (2, 3, 0, 0, 1, 0),
    (2, 4, 0, 0, 1, 0),
    (2, 5, 0, 0, 1, 1),
    (2, 8, 0, 0, 0, 1),
    (2, 9, 1, 0, 0, 0),
    (2, 11, 0, 0, 1, 0),
    (2, 12, 0, 0, 0, 1),
    (2, 14, 0, 1, 0, 0),
    (2, 15, 0, 1, 0, 0),
    (3, 0, 1, 1, 0, 0),
    (3, 1, 1, 0, 0, 0),
    (3, 2, 1, 0, 0, 0),
    (3, 3, 1, 1, 1, 0),
    (3, 4, 0, 0, 1, 0),
    (3, 5, 0, 1, 0, 0),
    (3, 6, 0, 0, 0, 1),
    (3, 7, 0, 0, 1, 1),
    (3, 8, 0, 1, 0, 0),
    (3, 9, 0, 0, 1, 0),
    (3, 10, 1, 0, 1, 0),
    (3, 11, 0, 1, 0, 1),
    (3, 13, 0, 0, 1, 0),
    (3, 14, 0, 1, 0, 0),
    (3, 15, 0, 1, 0, 0),
    (4, 0, 1, 1, 0, 0),
    (4, 1, 0, 1, 0, 0),
    (4, 2, 0, 1, 0, 0),
    (4, 4, 0, 1, 0, 0),
    (4, 5, 0, 1, 0, 0),
    (4, 7, 0, 1, 0, 0),
    (4, 8, 0, 0, 0, 1),
    (4, 9, 0, 1, 0, 0),
    (4, 10, 0, 1, 0, 0),
    (4, 11, 0, 0, 0, 1),
    (4, 12, 0, 0, 0, 1),
    (4, 13, 0, 0, 1, 1),
    (4, 14, 0, 1, 1, 0),
    (4, 15, 0, 1, 0, 0),
    (5, 0, 1, 1, 0, 0),
    (5, 2, 1, 0, 0, 0),
    (5, 3, 1, 0, 0, 0),
    (5, 4, 0, 0, 1, 0),
    (5, 5, 1, 1, 0, 0),
    (5, 7, 1, 0, 0, 0),
    (5, 9, 1, 0, 0, 1),
    (5, 10, 0, 1, 0, 0),
    (5, 14, 0, 1, 0, 0),
    (5, 15, 0, 1, 0, 0),
    (6, 0, 1, 0, 0, 0),
    (6, 1, 1, 0, 0, 0),
    (6, 2, 1, 0, 0, 1),
    (6, 3, 0, 0, 1, 1),
    (6, 4, 0, 1, 0, 1),
    (6, 6, 1, 1, 0, 0),
    (6, 7, 0, 0, 1, 1),
    (6, 8, 0, 0, 0, 1),
    (6, 9, 0, 0, 0, 1),
    (6, 10, 0, 0, 1, 0),
    (6, 11, 1, 0, 0, 0),
    (6, 12, 0, 0, 1, 1),
    (6, 13, 0, 1, 1, 0),
    (6, 14, 0, 1, 1, 0),
    (6, 15, 0, 1, 0, 0),
    (7, 0, 1, 0, 0, 0),
    (7, 1, 1, 0, 0, 0),
    (7, 2, 1, 0, 0, 0),
    (7, 4, 1, 0, 0, 0),
    (7, 5, 0, 1, 0, 0),
    (7, 6, 0, 1, 0, 0),
    (7, 10, 1, 0, 0, 0),
    (7, 11, 0, 0, 1, 1),
    (7, 12, 0, 0, 0, 1),
    (7, 13, 0, 1, 0, 1),
    (7, 14, 0, 1, 0, 0),
    (7, 15, 0, 1, 0, 0),
    (8, 0, 1, 0, 0, 0),
    (8, 1, 1, 1, 0, 0),
    (8, 2, 0, 1, 0, 0),
    (8, 4, 0, 1, 1, 0),
    (8, 5, 0, 1, 0, 0),
    (8, 6, 0, 1, 0, 0),
    (8, 7, 0, 0, 0, 1),
    (8, 9, 1, 0, 0, 1),
    (8, 10, 0, 0, 1, 0),
    (8, 11, 0, 1, 0, 1),
    (8, 14, 0, 1, 0, 0),
    (8, 15, 0, 1, 0, 0),
    (9, 0, 1, 0, 0, 0),
    (9, 1, 1, 1, 0, 0),
    (9, 3, 1, 0, 1, 0),
    (9, 5, 1, 0, 0, 0),
    (9, 6, 0, 1, 0, 1),
    (9, 8, 0, 0, 1, 0),
    (9, 9, 0, 1, 0, 0),
    (9, 10, 0, 0, 0, 1),
    (9, 11, 0, 1, 0, 0),
    (9, 12, 0, 1, 0, 0),
    (9, 13, 0, 1, 0, 1),
    (9, 14, 0, 1, 0, 0),
    (9, 15, 0, 1, 0, 0),
    (10, 0, 1, 0, 0, 0),
    (10, 1, 1, 1, 0, 0),
    (10, 2, 0, 1, 0, 0),
    (10, 4, 0, 0, 1, 1),
    (10, 5, 0, 1, 0, 1),
    (10, 7, 0, 1, 1, 0),
    (10, 9, 1, 0, 0, 1),
    (10, 11, 1, 0, 0, 0),
    (10, 13, 0, 0, 0, 1),
    (10, 14, 0, 1, 0, 0),
    (10, 15, 0, 1, 0, 0),
    (11, 0, 1, 1, 0, 0),
    (11, 2, 1, 0, 0, 0),
    (11, 3, 0, 0, 1, 0),
    (11, 6, 1, 0, 0, 0),
    (11, 7, 0, 1, 0, 0),
    (11, 8, 0, 0, 0, 1),
    (11, 9, 0, 1, 0, 0),
    (11, 10, 0, 0, 0, 1),
    (11, 11, 0, 0, 1, 0),
    (11, 12, 1, 0, 0, 0),
    (11, 13, 0, 1, 0, 0),
    (11, 14, 0, 1, 0, 0),
    (11, 15, 0, 1, 0, 0),
    (12, 0, 1, 0, 0, 0),
    (12, 1, 1, 0, 0, 0),
    (12, 2, 1, 0, 0, 0),
    (12, 4, 0, 0, 0, 1),
    (12, 5, 0, 1, 0, 1),
    (12, 8, 1, 0, 0, 1),
    (12, 10, 0, 1, 0, 0),
    (12, 12, 0, 1, 1, 0),
    (12, 13, 0, 0, 0, 1),
    (12, 14, 0, 1, 0, 0),
    (12, 15, 0, 1, 0, 0),
    (13, 0, 1, 0, 0, 0),
    (13, 1, 0, 1, 0, 0),
    (13, 3, 1, 0, 1, 0),
    (13, 8, 1, 0, 0, 1),
    (13, 9, 0, 0, 1, 1),
    (13, 10, 0, 0, 0, 1),
    (13, 11, 0, 0, 1, 0),
    (13, 12, 1, 0, 0, 1),
    (13, 14, 1, 1, 0, 0),
    (13, 15, 0, 1, 0, 0),
    (14, 0, 1, 1, 0, 0),
    (14, 1, 0, 1, 0, 0),
    (14, 2, 0, 0, 0, 1),
    (14, 3, 0, 0, 1, 1),
    (14, 4, 0, 0, 1, 0),
    (14, 5, 0, 0, 1, 0),
    (14, 6, 0, 1, 0, 0),
    (14, 10, 0, 0, 0, 1),
    (14, 11, 0, 1, 0, 0),
    (14, 13, 0, 0, 0, 1),
    (14, 14, 0, 1, 0, 1),
    (14, 15, 0, 1, 0, 0),
    (15, 0, 1, 0, 0, 1),
    (15, 1, 1, 0, 0, 1),
    (15, 2, 0, 0, 0, 1),
    (15, 3, 0, 0, 0, 1),
    (15, 4, 0, 0, 1, 1),
    (15, 5, 0, 0, 1, 1),
    (15, 6, 0, 0, 1, 1),
    (15, 7, 0, 0, 1, 1),
    (15, 8, 0, 0, 1, 1),
    (15, 9, 0, 0, 1, 1),
    (15, 10, 0, 0, 0, 1),
    (15, 11, 0, 0, 1, 1),
    (15, 12, 0, 0, 1, 1),
    (15, 13, 0, 0, 0, 1),
    (15, 14, 0, 0, 0, 1),
    (15, 15, 0, 1, 0, 1),
]
