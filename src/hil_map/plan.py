from openai import OpenAI
from instructor import patch, Mode
from hil_map.response_models.plan_model import HighLevelPlan, TaskPlan


# prompt_text = f"Given a task: '{task}', provide a step-by-step plan to perform it. Be short and clear in your instructions."
# response = model(mode=HighLevelPlan, prompt=prompt_text)

# for step in response.plan:
#     print(f"- Step: {step}")
#     prompt_text = f"Given the step: '{step}', provide concise plan. Be short and clear in your instructions. Your options are : Move, Hold, Rotate, Peel, Cut. Your objects are : Potato, Knife, Peeler."
#     actions = model(mode=TaskPlan, prompt=prompt_text)
#     for action in actions.plan:
#         print(f"   - {action.action}, Description: {action.description}")


def main():
    client = patch(OpenAI(base_url="https://inference.rcp.epfl.ch/v1"), mode=Mode.JSON)

    task = "Peel the potato and cut it into slices."
    prompt_text = f"Given a task: '{task}', provide a step-by-step plan to perform it. Be short and clear in your instructions."

    # Create structured output
    response = client.chat.completions.create(
        model="deepseek-ai/DeepSeek-V3.2",
        response_model=HighLevelPlan,
        messages=[
            {"role": "user", "content": prompt_text},
        ],
    )

    for step in response.plan:
        print(f"- Step: {step}")
        prompt_text = f"Given the step: '{step}', provide concise plan. Be short and clear in your instructions. Your options are : Move, Hold, Rotate, Peel, Cut. Your objects are : Potato, Knife, Peeler."
        actions = client.chat.completions.create(
            model="deepseek-ai/DeepSeek-V3.2",
            response_model=TaskPlan,
            messages=[
                {"role": "user", "content": prompt_text},
            ],
        )
        for action in actions.plan:
            print(f"   - {action.action}, Description: {action.description}")


if __name__ == "__main__":
    main()
