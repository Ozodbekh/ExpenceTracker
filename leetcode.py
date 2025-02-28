from typing import List

async def connect_websocket():
    uri = "ws://10.10.2.133:8000/ws/leaderboard/"
    async with websockets.connect(uri) as websocket:
        print("WebSocket-ga ulandi!")
        while True:
            message = await websocket.recv()
            data = json.loads(message)
            print("Serverdan kelgan ma'lumot:", data)

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        result = []
        c = [0] * n
        result.append(nums[:])

        i = 0
        while i < n:
            if c[i]:
                pass