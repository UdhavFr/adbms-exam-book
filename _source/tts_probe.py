import asyncio, edge_tts

async def main():
    try:
        voices = await edge_tts.list_voices()
        print('voices listed:', len(voices))
        andrew = [v for v in voices if 'Andrew' in v.get('ShortName', '')]
        print('andrew voices:', [v['ShortName'] for v in andrew][:5])
    except Exception as e:
        print('LIST FAIL:', type(e).__name__, str(e)[:200])

asyncio.run(main())
