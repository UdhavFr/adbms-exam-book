import asyncio, edge_tts

async def attempt(label, **kw):
    try:
        comm = edge_tts.Communicate('Hello world.', 'en-US-AndrewMultilingualNeural', **kw)
        n_audio = 0
        async for chunk in comm.stream():
            if chunk['type'] == 'audio':
                n_audio += 1
        print(label, 'OK, audio chunks:', n_audio)
    except Exception as e:
        print(label, 'FAIL:', type(e).__name__, str(e)[:150])

async def main():
    await attempt('no-rate')
    await attempt('rate--4pct', rate='-4%')
    await attempt('rate-+0pct', rate='+0%')

asyncio.run(main())
