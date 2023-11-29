class Plugin:
    def __init__(self):
        print("Timer plugin init")

    async def run(self, action, input):
        print("Timer plugin running")
        print(f"Action: {action}")
        print(f"Input: {input}")
        res = await action
        return res
