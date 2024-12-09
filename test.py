import pytest
import torch
from transformers import AutoModelForCausalLM


MODELS_TO_TEST = [
    "hf-internal-testing/tiny-random-OPTForCausalLM",
    "hf-internal-testing/tiny-random-GPT2LMHeadModel",
    "hf-internal-testing/tiny-random-gpt_neo",
]


@pytest.mark.parametrize("model_id", MODELS_TO_TEST)
@pytest.mark.parametrize("useless", [False, True])
def test_inference(model_id, useless):
    if useless:
        # do nothing
        pass

    model = AutoModelForCausalLM.from_pretrained(model_id, useless):
    model.eval()
    inputs = torch.tensor([[0, 1, 2, 3, 4]])
    model.generate(inputs, do_sample=True, num_return_sequences=1)
