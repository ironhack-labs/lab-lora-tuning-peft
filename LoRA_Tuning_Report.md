# LoRA Tuning with PEFT -- Experiment Report

## Objective

The objective of this lab was to fine-tune the **BLOOM-560M** language
model using **LoRA (Low-Rank Adaptation)** with the Hugging Face PEFT
library and evaluate how changing the LoRA rank (`r`) affects the
quality of the generated responses.

## Methodology

The pre-trained **BLOOM-560M** model was fine-tuned using a subset
(2,000 samples) of the **Databricks Dolly-15k** instruction-following
dataset. Two LoRA configurations were tested while keeping all other
training parameters constant:

  Parameter                      Experiment 1                Experiment 2
  --------------- --------------------------- ---------------------------
  LoRA Rank (r)                             8                          16
  LoRA Alpha                               16                          16
  Epochs                                    3                           3
  Learning Rate                          3e-4                        3e-4
  Dataset           Dolly-15k (2,000 samples)   Dolly-15k (2,000 samples)

The same prompt was used to evaluate both models:

> **"Create a beginner workout plan for someone who wants to improve
> fitness."**

## Results

The model trained with **r = 8** generated a workout plan including
weight training, cycling, squats, jumping rope, and general
strength-building advice. While not perfect, the response followed the
requested instruction.

The model trained with **r = 16** produced fluent English text, but
focused on describing a fitness application and progress tracking
instead of providing a workout plan. The response was coherent but less
relevant to the prompt.

The number of trainable parameters increased from **786,432 (≈0.14%)**
for **r = 8** to **1,572,864 (≈0.28%)** for **r = 16**.

## Findings

The experiment shows that increasing the LoRA rank does **not**
automatically improve performance. Although the **r = 16** model had
twice as many trainable parameters, it generated a response that was
less aligned with the requested task than the **r = 8** model.

This suggests that model quality depends not only on the LoRA rank but
also on factors such as dataset size, number of epochs, learning rate,
and overall hyperparameter tuning. With only 2,000 training examples and
three epochs, the additional capacity provided by **r = 16** did not
produce better instruction-following behavior.

## Conclusion

This lab demonstrated how PEFT and LoRA enable efficient fine-tuning by
updating only a small percentage of a large language model's parameters.
In this experiment, the **r = 8** configuration provided the best
balance between parameter efficiency and response quality. Future
improvements could include training on the full Dolly-15k dataset,
increasing the number of epochs, evaluating multiple prompts, and
testing additional LoRA ranks to determine the optimal configuration.
