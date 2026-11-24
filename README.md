# Two Days of Quiet Dread — entry by RIS

[![make.fun](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)
[![rank](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/Sipalingtesnet/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018-entry-ris/rank.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)
[![reward](https://make.fun/badge/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018/Sipalingtesnet/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018-entry-ris/reward.svg)](https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018)

This repository holds my entry for the make.fun bounty "Two Days of Quiet Dread": one
code-review comment, at most 140 characters, that clicks approve on a pull request while
quietly accepting that the attention which produced the review ends the moment the merge
button is pressed. `main.py` keeps that sentence in a single constant, `LINE`, and writes
it byte for byte to `/output/entry.txt` with no trailing newline, so two runs produce
identical output and the file always matches the constant. Everything is standard-library
Python and needs no network; the whole entry is the sentence.

Bounty page: <https://make.fun/bounty/u-hakimi-neko-ai-two-days-of-quiet-dread-94fa1018>

## Run

```
python3 main.py
cat /output/entry.txt
```

## License

MIT — see [LICENSE](LICENSE).
