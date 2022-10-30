# analysis_of_parallel_algorithms
**Counting the number of repeated characters in a string.** From the string passed to the input, you need to get a dictionary of the form "key-value", where the key is a unique character, and the value is the number of repetitions of this character in the source string.
To solve this problem, I found a text file with the number of characters ~ 1,000,000,000, but 10,000,000 characters will be used for tests, among which 2102 are unique. In this paper, we will consider: sequential (sync), asynchronous (async) and multiprocessor (smp) methods.

![image](https://user-images.githubusercontent.com/82733942/198885294-823cd002-f725-492a-ba79-358ae1ca52c4.png)
![image](https://user-images.githubusercontent.com/82733942/198885412-523555ef-bf16-4f5b-b861-ed3ca5718563.png)
![image](https://user-images.githubusercontent.com/82733942/198885403-14db85ed-0095-4a56-b419-ed8d7ef0afb2.png)
![parallelism](https://user-images.githubusercontent.com/82733942/198885346-793e9e62-c4aa-499a-8318-0cf5a626bf0a.gif)
![Видео без названия — сделано в Clipchamp](https://user-images.githubusercontent.com/82733942/198885358-3e11e283-7beb-45e2-b7a7-c71aa48abba7.gif)
