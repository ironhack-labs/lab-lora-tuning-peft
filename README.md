# LoRA Fine-Tuning with PEFT

Fine-tuning a language model using Low-Rank Adaptation (LoRA) — training less than 0.3% of parameters to meaningfully shift model behavior.

**Notebook:** [lab-lora-tuning-peft.ipynb](lab-lora-tuning-peft.ipynb)

---

## What is LoRA?

LoRA (Low-Rank Adaptation) freezes the original model weights and injects two small trainable matrices into each attention layer. Instead of updating hundreds of millions of parameters, only the adapters are trained — typically less than 1% of the total parameter count.

The result matches or approximates full fine-tuning quality at a fraction of the compute cost. In language models like GPT-3 or BLOOM, this can mean training as little as 0.02% of parameters with comparable results.

---

## Experiment

| | |
|---|---|
| **Base model** | `bigscience/bloom-560m` |
| **Dataset** | `fka/awesome-chatgpt-prompts` (role-based instruction prompts) |
| **LoRA rank (r)** | 16 (primary) — also tested r=64 |
| **LoRA alpha** | 32 (r=16) / 128 (r=64) |
| **Target modules** | `query_key_value` |
| **Trainable params** | ~1.57M / 560.8M total (0.28%) at r=16 |
| **Epochs** | 2 |

`bloom-560m` was chosen for fast iteration; the dataset was chosen for its clear prompt-style structure, making behavioral shifts easy to observe.

---

## Before vs. After

Same prompt — before and after fine-tuning:

> **Prompt:** `"I want you to act as a motivational coach."`

| | Output |
|---|---|
| **Base model** | *"Don't be afraid of being challenged."* |
| **Fine-tuned (r=16)** | *"I will provide some information about someone's motivation and goals, but it should be your job... I need someone who can help me find the best way for myself stay motivated when competing against others."* |

The fine-tuned model produces responses aligned with the chatgpt-prompts style — describing the role and expected behavior rather than continuing the sentence.

---

## Rank Comparison: r=16 vs r=64

A second experiment compared adapter ranks:

| Config | Trainable params | % of total |
|---|---|---|
| r=16, alpha=32 | 1,572,864 | 0.28% |
| r=64, alpha=128 | 6,291,456 | 1.11% |

Higher rank gives the adapter more expressive capacity, but the qualitative difference in outputs was not proportional to the 4x parameter increase — validating one of the key takeaways below.

---

## What I Observed

**Adapter capacity steers behavior, but more isn't always better.** r=64 adapters are more expressive, but the quality gain was not linear relative to the parameter cost.

**Validation loss is a weak proxy for output quality.** Differences in generation style and tone didn't track with loss values in any predictable way. Qualitative evaluation was necessary.

**Controlled experiments matter.** Isolating one variable at a time (rank, dataset size, epochs) was the only reliable way to attribute behavioral changes to a specific cause.

---

## Tradeoffs

| Tradeoff | Detail |
|---|---|
| Rank vs. compute | Higher r captures more complex patterns but increases training cost with diminishing returns |
| Behavior vs. knowledge | LoRA shifts how the model responds, not what it knows — world knowledge comes from pretraining |
| Adapter expressiveness | Low-rank matrices can miss subtle task-specific patterns that full fine-tuning would capture |
| Small model ceiling | bloom-560m has limited capacity; alignment shifts are visible but bounded by base model depth |

---

## Stack

- [Hugging Face PEFT](https://github.com/huggingface/peft)
- [Transformers](https://github.com/huggingface/transformers)
- [Datasets](https://github.com/huggingface/datasets)
- PyTorch
