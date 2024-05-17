import heapq
import unittest

def nav(roads, start, end):
    graph = {}
    for city1, city2, time in roads:
        if city1 not in graph:
            graph[city1] = []
        if city2 not in graph:
            graph[city2] = []
        graph[city1].append((time, city2))
        graph[city2].append((time, city1))

    priority = [(0, start, [])]
    visit = set()
    min_times = {start: 0}

    while priority:
        cur_time, cur_city, path = heapq.heappop(priority)

        if cur_city in visit:
            continue
        visit.add(cur_city)
        path = path + [cur_city]
        if cur_city == end:
            return path, cur_time

        for time, neighbour in graph[cur_city]:
            if neighbour in visit:
                continue
            old_time = min_times.get(neighbour, float('inf'))
            new_time = cur_time + time
            if new_time < old_time:
                min_times[neighbour] = new_time
                heapq.heappush(priority, (new_time, neighbour, path))
    return [], None

class TestNavFunction(unittest.TestCase):
    def setUp(self):
        self.roads = [
            ("A", "B", 5),
            ("B", "C", 4),
            ("A", "C", 8),
            ("A", "D", 2),
            ("D", "E", 3),
            ("E", "C", 1),
            ("B", "D", 2)
        ]

    def test_simple_case(self):
        route, total_time = nav(self.roads, "B", "D")
        self.assertEqual(route, ['B', 'D'])
        self.assertEqual(total_time, 2)

    def test_complex_case(self):
        route, total_time = nav(self.roads, "A", "C")
        self.assertEqual(route, ['A', 'D', 'E', 'C'])
        self.assertEqual(total_time, 6)

    def test_no_path(self):
        route, total_time = nav(self.roads, "A", "A")
        self.assertEqual(route, ['A'])
        self.assertEqual(total_time, 0)

    def test_same_start_and_end(self):
        route, total_time = nav(self.roads, "C", "C")
        self.assertEqual(route, ['C'])
        self.assertEqual(total_time, 0)

    def test_nonexistent_points(self):
        with self.assertRaises(KeyError):
            route, total_time = nav(self.roads, "F", "G")

if __name__ == '__main__':
    unittest.main()
