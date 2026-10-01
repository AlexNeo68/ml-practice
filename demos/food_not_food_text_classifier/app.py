
import torch
import gradio as gr

from typing import Dict
from transformers import pipeline

def classifier_food_not_food(sentence: str) -> Dict[str, float]:

    food_not_food_classifier = pipeline(
        task="text-classification",
        model=model_save_dir,
        device=torch.device("mps") if torch.backends.mps.is_available() else "cpu",
        batch_size=32, 
        top_k=None
    )

    outputs = food_not_food_classifier(sentence)[0]

    output_dict = {}

    for o in outputs:
        output_dict[o['label']] = o['score']

    return output_dict


description = """
Это текстовый классификатор позволяющий относить введенное предложение к одному из двух типов, идет ли в нем речь о еде или не о еде
Используется зафайнтьюненая модель - https://huggingface.co/alexneo68/food_not_food_text_classifier-ru_deep_pavlov_rubert-base-cased
Исходный код - https://github.com/AlexNeo68/ml-practice/blob/main/text_classification_ru.ipynb
"""

demo = gr.Interface(
    fn=classifier_food_not_food,
    inputs="text",
    outputs=gr.Label(num_top_classes=2),
    title="Текстовый Классификатор - еда/не еда",
    description=description,
    examples=[
        ["Это арбуз довольно зрелый"],
        ["На тарелке лежали два апельсина"],
    ]
)


if __name__ == "__main__":
    demo.launch()

