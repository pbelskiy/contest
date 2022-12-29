Task = namedtuple('Task', ['time', 'duration', 'index'])

class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([Task(t[0], t[1], i) for i, t in enumerate(tasks)])
        order, heap, i, time = [], [], 0, tasks[0].time

        while len(order) < len(tasks):
            # append ready tasks
            while i < len(tasks) and tasks[i].time <= time:
                heappush(heap, (tasks[i].duration, tasks[i].index))
                i += 1

            # rewind time to near task
            if not heap:
                time = tasks[i].time
                continue

            # execute tasks from queue
            duration, index = heappop(heap)
            time += duration
            order.append(index)

        return order
