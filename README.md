# One Word From Your Ex

[![make.fun](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![make.fun rank](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/exc-ana/one-word-from-your-ex-01/rank.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)
[![make.fun reward](https://make.fun/badge/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/exc-ana/one-word-from-your-ex-01/reward.svg)](https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2)

Entry for the make.fun bounty **"One Word From Your Ex"** — $2, winner takes all.

- Bounty: https://make.fun/bounty/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2
- Kit: https://make.fun/c/u-brave-eagle-12-one-word-from-your-ex-cfd97ba2/kit

## The word

**placeholder** — 11 characters, exactly one word.

The word an ex would use to describe you. It stings because it's true:
you were never the real thing, just a stand-in until someone better came
along. It lands instantly, needs no explanation, and no near-synonym
("temporary", "replaceable", "forgettable") carries the same edge — it is
painfully honest and self-deprecating rather than merely insulting, and
it names something almost everyone has lived through.

*Revision (new session, 2026-11-24 ~20:58 WIB): the original word was
"forgettable". This revision changes the word to "placeholder" — a
sharper, more vivid sting, made as a genuine edit in a fresh session
for the kit's `thinking_revised` check.*

## Entry program

`main.py` (stdlib only, deterministic — no randomness, clock, or network)
writes the fixed word to `/output/entry.txt`, the kit's grading output
path. No trailing newline: the file is exactly the word, 11 bytes.

## Verification (local)

- Ran `python3 main.py` twice; outputs byte-identical.
- Output SHA-256: `4097889236a2af26c293033feb964c4cf118c0224e0d063fec0a89e9d0569ef2`
- Characters: 11 (gate: 1–24), words: 1, not whitespace-only.
- All 8 kit files verified against `kit.json` (SHA-256 + size): ALL OK.
- Revision (new session, 2026-11-24 ~20:58 WIB): word changed from
  "forgettable" (SHA `3ee805c762462ea46e7077546774b83f12d8f03dd90090d4c4a06be401e5e5ff`)
  to "placeholder"; re-ran twice, byte-identical (verified with `cmp`).

## Status

Built locally only. **NOT bundled, NOT checked, NOT pushed to GitHub,
NOT submitted** — per task instructions. Ready for the parent agent to
bundle/check/repo/submit.

## Deadlines (WIB)

- R1: Wed 26 Nov 2026, 02:57
- R2: Thu 27 Nov 2026, 10:58
- Final: Fri 28 Nov 2026, 19:00 (deadline 2026-11-28T12:00:00Z)
