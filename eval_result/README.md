---
base_model: new_qwen
library_name: peft
license: other
metrics:
- accuracy
tags:
- llama-factory
- lora
- generated_from_trainer
model-index:
- name: qwen_accuracy
  results: []
---

<!-- This model card has been generated automatically according to the information the Trainer had access to. You
should probably proofread and complete it, then remove this comment. -->

# qwen_accuracy

This model is a fine-tuned version of [new_qwen](https://huggingface.co/new_qwen) on the shuimotang dataset.
It achieves the following results on the evaluation set:
- Loss: 0.4092
- Accuracy: 0.9073

## Model description

More information needed

## Intended uses & limitations

More information needed

## Training and evaluation data

More information needed

## Training procedure

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 1
- eval_batch_size: 1
- seed: 42
- gradient_accumulation_steps: 8
- total_train_batch_size: 8
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: cosine
- lr_scheduler_warmup_ratio: 0.1
- num_epochs: 3.0

### Training results



### Framework versions

- PEFT 0.11.1
- Transformers 4.41.2
- Pytorch 2.3.0+cu121
- Datasets 2.20.0
- Tokenizers 0.19.1