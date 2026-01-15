# Report on Experiment with GPT-2 Model for Coaching Prompts

## Objective
The aim of this experiment was to evaluate the GPT-2 model's ability to generate coherent and relevant responses to various coaching-related prompts, utilizing text generation techniques. The focus was on life coaching, career coaching, and motivational coaching, using different prompts to see how well the model could adhere to the context and provide useful outputs.

## Methodology
The experiment utilized the GPT-2 language model along with the PEFT (Parameter Efficient Fine-Tuning) library to fine-tune the model, if necessary, using LoRA (Low-Rank Adaptation). Three distinct prompts were tested:

- "I want you to act as a life coach and guide me through making better decisions."
- "I want you to act as a career coach and help me find the best job opportunities."
- "I want you to act as a motivational coach and help me stay focused on achieving my goals."

Each input was tokenized and passed to the model for text generation. Parameters such as `max_new_tokens`, `top_k`, `top_p`, and `temperature` were adjusted to control the diversity and coherence of the output.

## Results

### Life Coaching Prompt
The response generated was a mix of motivational advice and personal anecdotes, but it veered off-topic, including an irrelevant mention of "The Spurs have been in training since the loss." This showed that while the model can generate relevant content, it also tends to drift into unrelated topics.

### Career Coaching Prompt
The output began with relevant career guidance but shifted toward personal praise ("You're a great person"), which was somewhat disconnected from the context. Although the response was positive, it lacked the practical advice expected from a career coaching prompt.

### Motivational Coaching Prompt
The generated text was largely motivational, with phrases like "Don't let anybody tell you you're useless." However, the response also became narrative-driven, moving away from a straightforward coaching tone and into storytelling.

## Analysis
The experiment revealed that while GPT-2 can generate responses related to coaching, it often deviates from the context. The model's tendency to produce irrelevant or off-topic content may be due to its sampling strategy (e.g., `top_p`, `temperature`) and its exposure to large, diverse datasets. The use of LoRA or further fine-tuning could help improve the model's focus and coherence.

## Conclusion
The experiment demonstrated the potential of GPT-2 for generating coaching-related responses but also highlighted the need for more refined control over the generated content. Fine-tuning the model using techniques like LoRA could help reduce the model's tendency to diverge from the intended context. The next steps include refining the model further and experimenting with more targeted datasets to achieve better results in specialized domains like coaching.
