---
title: Текстовый Классификатор - еда/не еда
emoji: 🍔
colorFrom: green
colorTo: orange
app_file: app.py
pinned: false
license: apache-2.0
---

# 🍗🚫🥑 Классификатор текста «Еда / Не еда»

Небольшой демо-проект, показывающий текстовый классификатор, который определяет, относится ли предложение к еде или к чему-то другому.

Модель **ruBERT-base-cased** от DeepPavlov, дообученная на собственном синтетическом датасете из 8261 сгенерированных [подписей «Еда / Не еда» (v2)](https://huggingface.co/datasets/alexneo68/for_text_classification_food_not_food_v2).

[Исходный код ноутбука](https://github.com/AlexNeo68/ml-practice/blob/main/text_classification_ru.ipynb).

## 📊 Модели на HuggingFace

* [`food_not_food_text_classifier-DeepPavlov_rubert-base-cased`](https://huggingface.co/alexneo68/food_not_food_text_classifier-DeepPavlov_rubert-base-cased) — accuracy 0.96
* [`food_not_food_text_classifier-ru_deep_pavlov_rubert-base-cased`](https://huggingface.co/alexneo68/food_not_food_text_classifier-ru_deep_pavlov_rubert-base-cased) — accuracy 0.9921
