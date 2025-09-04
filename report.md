
# Report: LoRA Tuning Experiments

## Goal
Try out different **LoRA configs** and training setups to see how they affect results, and write down what I learned. The idea is to save time and money by finding faster/better runs.

---

## Run A
- **LoRA config:** `r=4, alpha=8, dropout=0.05`
- **Training:** learning_rate = 2e-4, batch_size=2, epochs=1
- **Max new tokens:** 50
- **Target modules:** query_key_value

### Notes
- Small rank (r=4) and lower alpha → lighter model update.
- Lower dropout (0.05) → keeps more of the training signal.
- Because tokens were capped at 50, output stayed shorter and safer.
- Training was stable but slower to adapt.

---

## Run B
- **LoRA config:** `r=8, alpha=16, dropout=0.10`
- **Training:** learning_rate = 5e-4, batch_size=2, epochs=1
- **Max new tokens:** 100
- **Target modules:** query_key_value

### Notes
- Bigger rank (r=8) and higher alpha (16) → more capacity to learn.
- Higher dropout (0.10) → more regularization.
- Higher learning rate (5e-4) → faster training, but risk of instability.
- Max tokens = 100 → longer answers, sometimes drifting or adding more text than needed.

---

## Main Differences
| Aspect            | Run A (50 tokens) | Run B (100 tokens) |
|-------------------|------------------|-------------------|
| Rank (r)          | 4                | 8                 |
| Alpha             | 8                | 16                |
| Dropout           | 0.05             | 0.10              |
| Learning rate     | 2e-4             | 5e-4              |
| Max new tokens    | 50 (shorter)     | 100 (longer)      |
| Style of outputs  | More concise     | More verbose, risk of drift |

---

## What I Learned
1. **LoRA config matters** – changing r and alpha directly impacts how expressive the adapter is. Bigger values (Run B) = more learning power, but also more risk of overfitting or instability.
2. **Token limits matter** – smaller max_new_tokens keeps answers tighter (Run A), while bigger values let the model ramble (Run B).
3. **Learning rate trade-off** – too low wastes time, too high risks noise. Run B was faster, but less predictable.
4. **Dropout helps** – higher dropout in Run B may prevent overfitting, but can also remove too much signal if too high.
5. **Balance is key** – there is no one-size-fits-all. The best config depends on whether we want short, stable answers (A) or longer, more detailed ones (B).

---

## TL;DR
- Run A → safer, shorter answers, slower learning.
- Run B → bigger, louder, more flexible, but can get messy.
- Lesson: play with r, alpha, dropout, learning rate, and tokens. Each changes the “personality” of the model.
