QUERY = 'пальто из натуральной шерсти'

MAX_RETRIES = 12
INITIAL_DELAY = 0.5

VOL_DIVISOR = 100_000
PART_DIVISOR = 1000

CARD_POOL_WORKERS = 50
CARDS_LIMIT = 100  # Set to an integer to limit the number of cards fetched (for testing)

HEADERS = {
    'accept': '*/*',
    'accept-encoding': 'gzip, deflate, zstd',
    'accept-language': 'ru,en;q=0.9',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36',
    'cookie': '_wbauid=5932205761772735099; x_wbaas_token=1.1000.f22e62f0c6fb4022b8bb1006220212e0.MTV8MjEyLjIyNy40OS4xNTN8TW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzE0NS4wLjAuMCBTYWZhcmkvNTM3LjM2fDE3NzM5NDQ5Mjd8cmV1c2FibGV8MnxleUpvWVhOb0lqb2lJbjA9fDB8M3wxNzczMzQwMTI3fDE=.MEUCIQD1N4vrUngId/7xzuF5hTV8zsoS/I3XoCbuHzak5Dc25AIgDRvIPXirab62NuwsbehYWmxpLGlOwTpKlcQJV0m5QwE=; _cp=1; __zzatw-wb=MDA0dBA=Fz2+aQ==; external-locale=ru; cfidsw-wb=t+ZP4worSApwsRlNkIrI5jDXGIqNWJCCp7ylxTlucVmcpPb0CJNGGofQykF7Dy9xgFBS+HzPK54I6k4AM9wLBgGqVf2QzQxh/ZvcPcxY+t3VY9mB0LZbI1KUDGXdtZq4eqqBvBUpWoDjm+jsQmKVR0pTS27QrJvRnzW1'
}