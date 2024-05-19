Алгоритм фрактальной графики Diamond-Square, реализованный на языке Python. 

Использованы следующие стандартные бибдиотеки Python:
1. Tkinter для создания GUI
2. Random для генерации случайных чисел

Использованы следующие сторонние библиотеки, необходимые для работы программы:
1. MayaVi для качественного отображения карт высот, полученных с помощью алгоритма Diamond-Square
2. Visualization Toolkit (VTK) для закрытия всех окон по завершению работы с программой

Обязательные входные данные:
1. Степень двумерного массива (n) - размер матрицы карты высот (2n+1). Вводится положительное целое число, иначе выводится ошибка
2. Фактор неровности ландшафта (roughness) - насколько плоской будет земля. Чем выше этот критерий, тем неровнее земля (очень высокие и частые горы, глубокие водные впадины). Вводится положительное десятичное число (поддерживает как точку, так и запятую), иначе вывод ошибки
3. Размерность разультата (d) - в каком виде будет результат: 2d, 3d. Вводится число 2 или 3 (поддерживает вводы 2d, 3d, 2D, 3D), иначе ошибка

Необязательные входные данные:
1. Водная гладь - если флаг не активирован, то будет показываться водный ландшафт. Если активирован, то будет отображаться только земной ландшафт 

Год написания 2023

Примеры ландшафтов:

![тест1_2](https://github.com/ApsilonXi/Portfolio/assets/90376907/2ce894bb-9e7a-4ced-922e-eeb90505e27b)
![тест2_2](https://github.com/ApsilonXi/Portfolio/assets/90376907/631237d0-4d77-4e13-a73d-6bc5ecd5b451)
![тест1_4](https://github.com/ApsilonXi/Portfolio/assets/90376907/559160f4-291b-4ea1-a710-08d606ad0ce5)
![тест2_4](https://github.com/ApsilonXi/Portfolio/assets/90376907/85677d56-f07c-44ee-a688-eb5d5c85ae6f)
![тест2_5](https://github.com/ApsilonXi/Portfolio/assets/90376907/f395b19f-8014-41fe-893e-12ba2f09ac20)
![тест4_5](https://github.com/ApsilonXi/Portfolio/assets/90376907/f55971dd-b1c4-4bdf-8728-1fed20c69700)
![тест3_5](https://github.com/ApsilonXi/Portfolio/assets/90376907/485aa4ff-83ea-4104-ae45-dbb27186a407)
