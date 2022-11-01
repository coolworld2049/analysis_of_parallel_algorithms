# analysis_of_parallel_algorithms
**Подсчет количества повторяющихся символов в строке.** Из строки, переданной на вход, нужно получить словарь вида "ключ-значение", где ключ - это уникальный символ, а значение - количество повторений этого символа в исходной строке. Чтобы решить эту проблему, я нашел текстовый файл с количеством символов ~ 1 000 000 000, бут 10 000 000 символов будут использоваться для тестов, среди которых 2102 являются уникальными. В этой статье мы рассмотрим: последовательный (sync), асинхронный (async) и многопроцессорный (mpp) методы.

![image](https://user-images.githubusercontent.com/82733942/198885294-823cd002-f725-492a-ba79-358ae1ca52c4.png)
![image](https://user-images.githubusercontent.com/82733942/198885403-14db85ed-0095-4a56-b419-ed8d7ef0afb2.png)
![image](https://user-images.githubusercontent.com/82733942/198885412-523555ef-bf16-4f5b-b861-ed3ca5718563.png)
![parallelism](https://user-images.githubusercontent.com/82733942/198885346-793e9e62-c4aa-499a-8318-0cf5a626bf0a.gif)
![image](https://user-images.githubusercontent.com/82733942/198892560-3705c606-e459-45b6-bf90-0f80000a34a3.png)
![Видео без названия — сделано в Clipchamp](https://user-images.githubusercontent.com/82733942/198885358-3e11e283-7beb-45e2-b7a7-c71aa48abba7.gif)
