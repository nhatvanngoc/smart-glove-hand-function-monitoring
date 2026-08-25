#!/usr/bin/env python3
"""Offline verifier for mega_link_diagnostics serial logs.
No serial dependency; save raw serial output to a file first."""
from __future__ import annotations
import argparse

def crc16(data: str) -> int:
    crc=0xFFFF
    for ch in data.encode():
        crc ^= ch << 8
        for _ in range(8): crc=((crc << 1)^0x1021) & 0xFFFF if crc & 0x8000 else (crc << 1) & 0xFFFF
    return crc

def main() -> int:
    ap=argparse.ArgumentParser(); ap.add_argument('log'); args=ap.parse_args()
    valid=bad=gap=restarts=0; prev=None; first_us=last_us=None
    for raw in open(args.log,encoding='utf-8',errors='replace'):
        line=raw.strip()
        if not line.startswith('@'): continue
        try:
            payload, given=line.rsplit(',',1); seq=int(payload[1:].split(',',1)[0]); expected=int(given,16)
        except ValueError: bad+=1; continue
        if crc16(payload) != expected: bad+=1; continue
        fields=payload[1:].split(',');
        if len(fields) != 20 or fields[-1] != 'diag': bad+=1; continue
        ts=int(fields[1]); first_us=ts if first_us is None else first_us; last_us=ts
        if prev is not None:
            if seq > prev + 1: gap += seq-prev-1
            elif seq <= prev: restarts += 1
        prev=seq; valid+=1
    duration=(last_us-first_us)/1e6 if valid>1 else 0
    rate=(valid-1)/duration if duration>0 else 0
    print(f'valid_frames={valid} crc_or_format_failures={bad} sequence_gaps={gap} restarts={restarts} duration_s={duration:.3f} achieved_hz={rate:.3f}')
    print('Interpret only with the saved raw log, firmware/configuration manifest and test condition.')
    return 0
if __name__=='__main__': raise SystemExit(main())
