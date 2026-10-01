# 🍗🚫🥑 Классификатор текста «Еда / Не еда»

Небольшой демо-проект, показывающий текстовый классификатор, который определяет, относится ли предложение к еде или к чему-то другому.

Модель **ruBERT-base-cased** от DeepPavlov, дообученная на собственном синтетическом датасете из 8261 сгенерированных [подписей «Еда / Не еда» (v2)](https://huggingface.co/datasets/alexneo68/for_text_classification_food_not_food_v2).

[Исходный код ноутбука](https://github.com/AlexNeo68/ml-practice/blob/main/text_classification.ipynb).

## 📊 Модели на HuggingFace

* [`food_not_food_text_classifier-DeepPavlov_rubert-base-cased`](https://huggingface.co/alexneo68/food_not_food_text_classifier-DeepPavlov_rubert-base-cased) — accuracy 0.96
* [`food_not_food_text_classifier-ru_deep_pavlov_rubert-base-cased`](https://huggingface.co/alexneo68/food_not_food_text_classifier-ru_deep_pavlov_rubert-base-cased) — accuracy 0.9921

## 🚀 Демо на Gradio

```bash
pip install -r demos/food_not_food_text_classifier/requirements.txt
python demos/food_not_food_text_classifier/app.py
```

## 📁 Что внутри

| Путь | Описание |
|---|---|
| `create_dataset.ipynb` | Генерация и валидация датасета v2: лексика, фреймы, хард-пакет, сплит по группам |
| `data/food_not_food_v2/` | Датасет: 8261 строка, 580 групп, сплиты `train` / `validation` / `test` / `hard_test` |
| `text_classification.ipynb` | Обучение и оценка модели, замеры скорости инференса |
| `text_classification_ru.ipynb` | Обучение русскоязычной модели и запуск Gradio-демо |
| `demos/food_not_food_text_classifier/` | Gradio-приложение |
| `bench_models.py` | Сравнение distilBERT, ruBERT, ruRoberta-large и XLM-R через кросс-валидацию |

## ⚠️ Ограничения

* Датасет русскоязычный: латиница, code-switching и английский текст не представлены, на них модель ошибается.
* Классы сбалансированы 50/50, поэтому в реальном потоке модель завышает `food` — лечится подбором порога.
