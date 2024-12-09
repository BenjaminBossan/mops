import pytest
import torch
from transformers import AutoModelForCausalLM


MODELS_TO_TEST = [
    "hf-internal-testing/tiny-random-OPTForCausalLM",
    "hf-internal-testing/tiny-random-GPT2LMHeadModel",
    "hf-internal-testing/tiny-random-gpt_neo",
]


@pytest.mark.parametrize("model_id", MODELS_TO_TEST)
@pytest.mark.parametrize("use_cache", [False, True])
def test_inference(model_id, use_cache):
    model = AutoModelForCausalLM.from_pretrained(model_id, use_cache=use_cache)
    model.eval()
    inputs = torch.tensor([[0, 1, 2, 3, 4]])
    model.generate(inputs, do_sample=True, num_return_sequences=1)
