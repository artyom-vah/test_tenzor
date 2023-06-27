[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT)
# **Тестовое задание на позицию QA-разработчика в тестировании.**

### Необходимо автоматизировать проверку следующих сценариев:

#### 1й сценарий:
1)	Зайти на https://ya.ru/
2)	Проверить наличия поля поиска
3)	Ввести в поиск Тензор
4)	Проверить, что появилась таблица с подсказками (suggest)

![img_1.png](screens_for_README/img_1.png)
5)	Нажать enter

6)	Проверить, что появилась страница результатов поиска

7)	Проверить 1 ссылка ведет на сайт tensor.ru

![img_2.png](screens_for_README/img_2.png)


<br>

#### 2й сценарий:
1)	Зайти на ya.ru
2)	Проверить, что кнопка меню присутствует на странице

![img_3.png](screens_for_README/img_3.png)

<br>

3)	Открыть меню, выбрать “Картинки”

![img_4.png](screens_for_README/img_4.png)

4)	Проверить, что перешли на url https://yandex.ru/images/

5)	Открыть первую категорию

![img_5.png](screens_for_README/img_5.png)

<br>


6)	Проверить, что название категории отображается в поле поиска

![img_6.png](screens_for_README/img_6.png)

<br>

7)	Открыть 1 картинку

![img_7.png](screens_for_README/img_7.png)

<br>

8)	Проверить, что картинка открылась
9)	Нажать кнопку вперед

![img_8.png](screens_for_README/img_8.png)

<br>

10.	Проверить, что картинка сменилась
11.	Нажать назад
12.	Проверить, что картинка осталась из шага 8

<br><br>

### Правила выполнения задания:
1)	Автотесты реализованы на Python 3 и Selenium Webdriver
2)	В качестве тестового framework используется pytest
3)	Реализован паттерн PageObject
4)	Приветствуются любые сторонние библиотеки для логирования, отчетов, selenium wrapper
5)	Готовый проект залит на github / gitlab без кешей, драйверов и виртуальных окружений.
[search_page.py](pages%2Fsearch_page.py)
<br>

### Описание паттерна Page Object:
Паттерн Page Object - помогает разделить логику тестов от логики взаимодействия (автоматизации) 
с элементами на страницах. Это делает тесты более модульными, понятными и поддерживаемыми.

В моем случае я реализовал данный паттерн таким способом:
```bash
- locators/
  |-- yandex_locators.py
- pages/
  |-- images_page.py
  |-- search_page.py
- tests/
  |-- conftest.py
  |-- test_images_yandex.py
  |-- test_search_yandex.py
 ```
- `locators/yandex_locators.py`: В этом файле определены локаторы элементов на странице.

- `pages/`: В данной папке находятся файлы `images_page.py` и `search_page.py`. Они содержат методы для выполнения операций на определенных страницах, таких как ввод текста в поле поиска, нажатие на кнопку и другие операции.

- `tests/`: В данной папке находятся файлы `conftest.py`, `test_images_yandex.py` и `test_search_yandex.py`.
    - `conftest.py`: Файл конфигурации pytest, где можно определить фикстуры и настройки, используемые в тестах.
    - `test_images_yandex.py` и `test_search_yandex.py`: Файлы, содержащие сами тесты. В них вы можете описывать проверки и использовать методы из классов `ImagesPage` и `SearchPage` для выполнения операций на соответствующих страницах.

<br>




### **Стек:**
![python version](https://img.shields.io/badge/Python-3.10.2-green) 


### **Дополнительные библиотеки:**
![pytest](https://img.shields.io/badge/Pytest-7.4.0-blue?style=flat-square) ![selenium version](https://img.shields.io/badge/Selenium-4.10.0-blue)
[![pytest-html](https://img.shields.io/badge/Pytest--html-3.2.0-blue.svg)](https://pypi.org/project/pytest-html/3.2.0/)

### **Запуск проекта в dev-режиме**
Инструкция ориентирована на операционную систему Windows и утилиту git bash.<br/>
##### Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:
```bash
git clone https://github.com/artyom-vah/test_tenzor.git
```

2. Установите и активируйте виртуальное окружение
```bash
python -m venv venv
```
```bash
source venv/Scripts/activate
```
или сразу так:
```bash
python -m venv venv && . venv/Scripts/activate
```
3. Обновите pip 
```bash
python -m pip install --upgrade pip
```
4. Установите зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
```
5. Запуск всех тестов с использованием pytest
```bash
python -m pytest
```
6. Запуск тестов 1го / 2го сценариев - Поиск в яндексе / Картинки на яндексе
```bash
python -m pytest tests/test_search_yandex.py
```
```bash
python -m pytest tests/test_images_yandex.py
```
```bash
# просто нажатием на зеленый треугольник или же комбинацией клавиш Shift+f10
```
7. Чтобы сгенерировать HTML-отчет
```bash
python -m pytest --html=report.html
```
```bash
# после чего будет сгенерирован файл report.html в корне проекта, 
# а также папка с файлом assets/style.css
```
**Пример готового отчета:**
![img_9.png](screens_for_README/img_9.png)


Автор проекта: Артем Вахрушев.