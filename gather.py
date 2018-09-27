#!/usr/bin/env python3
from core.config import Config
from core.fetcher import Fetcher, CFetcher



cfg = Config()
poroshki = []

if cfg.init:
    for page in cfg.pages:
        poroshki.append(CFetcher(cfg.token, page).run())
else:
    for (page, count) in zip(cfg.pages, cfg.counts):
        poroshki.append(Fetcher(cfg.token, page, count).run())

for p in sum(poroshki, []):
    print(*p.body, sep='\n')
    print(p.date)
    print(p.url)
    if cfg.br:
        print(cfg.br, end='')
