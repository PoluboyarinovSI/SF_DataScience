# Проект 3. Создание модели для предсказания рейтинга отеля

## Оглавление
[1. Описание проекта](https://github.com/PoluboyarinovSI/SF_DataScience/tree/main/project_1/README.md#Описание-проекта)   
[2. Какой кейс решаем?](https://github.com/PoluboyarinovSI/SF_DataScience/tree/main/project_1/README.md#Какой-кейс-решаем)   
[3. Краткая информация о данных](https://github.com/PoluboyarinovSI/SF_DataScience/tree/main/project_1/README.md#Краткая-информация-о-данных)   
[4. Этапы работы над проектом](https://github.com/PoluboyarinovSI/SF_DataScience/tree/main/project_1/README.md#Этапы-работы-над-проектом)   
[5. Результат](https://github.com/PoluboyarinovSI/SF_DataScience/tree/main/project_1/README.md#Результат)  
[6. Выводы](https://github.com/PoluboyarinovSI/SF_DataScience/tree/main/project_1/README.md#Выводы)   

## Описание проекта
Построить модель на основе алгоритмов машинного обучения, которая предсказывает рейтинг отеля.

:arrow_up[к оглавлению](https://github.com/PoluboyarinovSI/SF_DataScience/tree/main/project_1/README.md#Оглавление)


### Какой кейс решаем?
Создание модели предсказания рейтингра отеля для компании Booking. Одна из проблем компании — это нечестные отели, которые накручивают себе рейтинг. Одним из способов обнаружения таких отелей является построение модели, которая предсказывает рейтинг отеля. Если предсказания модели сильно отличаются от фактического результата, то, возможно, отель ведёт себя нечестно, и его стоит проверить.

**Метрика качества**   
Для оценки качества модели — точности прогнозов, сделанных моделью, — используется метрика MAPE (mean absolute percentage error), средняя абсолютная процентная ошибка. Для расчета MAPE сравниваются значения предсказанний созданной моделью с реальными значениями рейтинга отелей.

**Что практикуем**   
- Изученные приемы анализа данных
- Изученные приемы визуализации данных
- Изученные приему преобразования и очистки данных


### Краткая информация о данных
В распоряжении имеется база данных, в которой содержатся сведения отзывов на отели Европы, которая содержит 386803 записей и 17 признаков. Общий объем: 50.2+ MB.

:arrow_up[к оглавлению](https://github.com/PoluboyarinovSI/SF_DataScience/tree/main/project_1/README.md#Оглавление)


### Этапы работы над проектом
- Подготовка
- Анализ и очистка данных
- Генерация и преобразование признаков
- Кодирование признаков
- Преобразование признаков
- Отбор признаков
- Создание и обучение модели

:arrow_up[к оглавлению](https://github.com/PoluboyarinovSI/SF_DataScience/tree/main/project_1/README.md#Оглавление)


### Результат   
Отчет о проделанной работе в Jupyter NoteBook, в котором содержится подробное описание по каждому из выполненных этапов работы над проектом. 

:arrow_up[к оглавлению](https://github.com/PoluboyarinovSI/SF_DataScience/tree/main/project_1/README.md#Оглавление)


### Выводы
В рамках выполнения данного проекта разработана модель, которая предсказывает рейтинг отеля на основе отзывов посетителей. В процессе работы над проектом выполнен анализ и очистка исходных данных, сгенерированные новые признаки, произведено кодирование новых признаков и их нормализация, выполнен отбор признаков, создана и обучена модель. Метрика качества МАРЕ показывает результат порядка 0.147. Наиболее весомыми признаками для моедли являются: review_diff, p_compound, n_compound, review_total_positive_word_counts.

:arrow_up[к оглавлению](https://github.com/PoluboyarinovSI/SF_DataScience/tree/main/project_1/README.md#Оглавление)


Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами