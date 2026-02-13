LoRA Tuning Experiment Report

Overview
In this exercise, I ran a series of experiments using LoRA fine-tuning with different generation parameters and LoRA configurations. The goal was to understand how sampling settings and adapter parameters affect model behavior, output quality, and training efficiency. The focus was on achieving better results with fewer epochs and reduced computational cost.

Experiments with Generation Parameters
One of the main variables tested was the decoding configuration during inference. Initially, both top_k and top_p sampling were used together. However, this led to inconsistent behavior and less stable outputs.

Decided not to use both top_p and top_k: it was correct.
Final configuration used:

top_p = 0.95
temperature = 0.1

This setup produced more stable and coherent outputs. When both top_k and top_p were enabled simultaneously, the sampling space became overly restricted, which sometimes caused the model to generate incoherent tokens.

Another important observation was related to output length. The model started malfunctioning (producing incoherent tokens) when generating more than 40 tokens. However, when the maximum tokens were increased gradually in steps of five—starting from 30—the model was able to reach around 55 tokens without significant degradation in quality. This suggests that generation limits interact with the model’s learned distribution and should be tuned progressively.

LoRA Fine-Tuning Results
The base model was then fine-tuned using LoRA with approximately 700 trainable parameters. The training ran for 30 epochs using the same learning rate as previous tests.

Once inferenced with the (trained; 3 epochs, same learning ratio, 700 parameters) fine-tuned model, output becomes much more satisfying. There are no hallucinations, and the generated responses follow the expected structure more closely.

Compared to the base model:

The fine-tuned version produced more consistent outputs.

SQL or structured responses followed the schema more accurately.

The need for aggressive sampling constraints was reduced.

Efficiency Considerations
One of the objectives of the exercise was to explore whether better LoRA configurations could reduce the number of required epochs, saving both time and computational cost.

Key observations:

Adjusting LoRA parameters can significantly impact training efficiency.

Even a small number of trainable parameters (around 700) was enough to produce noticeable improvements.

The main performance gains came from fine-tuning rather than from more complex sampling strategies.

This suggests that investing effort in adapter configuration and training setup is often more effective than increasing inference complexity or generation randomness.

Key Lessons Learned

Using both top_k and top_p simultaneously is unnecessary and can degrade output quality.

A conservative sampling setup (top_p=0.95, temperature=0.1) produces more stable and coherent results.

Output length has a strong effect on generation quality; gradual increases help identify safe limits.

LoRA fine-tuning, even with a small number of parameters, can greatly reduce hallucinations.

Proper adapter tuning can reduce the number of epochs required, saving time and computational resources.

Conclusion
The experiments showed that careful tuning of both LoRA parameters and generation settings leads to more reliable and efficient models. The fine-tuned model produced significantly better outputs than the base model, with fewer hallucinations and more consistent structure. Additionally, simplifying the sampling configuration and focusing on effective LoRA training proved to be a better strategy for improving performance while reducing cost.