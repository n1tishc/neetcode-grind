class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # sort according to start time 
        meetings.sort()
        # two heaps to keep track of available rooms and roooms being used
        available = [i for i in range(n)] # room numebers from 0 to n-1
        used = [] # Stores rooms being used like (end_time, room_number)

        counts = [0] * n # Trakc of number of meetings happening in each room

        for start, end in meetings:
            # finish all meetngs before the currnet start time 
            while used and start >= used[0][0]:
                _, room = heapq.heappop(used)
                heapq.heappush(available, room)
            
            # No meeting rooms free, then 
            if not available:
                end_time, room = heapq.heappop(used) # room with lowest end time
                # Update the end time
                end = end_time + (end - start)
                heapq.heappush(available, room)
            
            # room(s) is free and schedule the meet
            room = heapq.heappop(available)
            heapq.heappush(used, (end, room))

            counts[room] += 1

        return counts.index(max(counts))