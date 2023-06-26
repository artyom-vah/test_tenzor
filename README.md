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



### **Стек:**
![python version](https://img.shields.io/badge/Python-3.10.2-green) 


### **Дополнительные библиотеки:**
![pytest](https://img.shields.io/badge/Pytest-7.4.0-blue?style=flat-square) ![selenium version](https://img.shields.io/badge/Selenium-4.10.0-blue)

### **Запуск проекта в dev-режиме**
Инструкция ориентирована на операционную систему Windows и утилиту git bash.<br/>
##### Для прочих инструментов используйте аналоги команд для вашего окружения.

1. Клонируйте репозиторий и перейдите в него в командной строке:
```
git clone https://github.com/artyom-vah/test_tenzor.git
```

2. Установите и активируйте виртуальное окружение
```
python -m venv venv
```
```
source venv/Scripts/activate
```
или сразу так:
```
python -m venv venv && . venv/Scripts/activate
```
3. Обновите pip 
```
python -m pip install --upgrade pip
```
4. Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
```
Автор проекта: Артем Вахрушев.